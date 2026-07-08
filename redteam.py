#!/usr/bin/env python3
"""
Lunar lander descent-design review -- compare a design against the failure record.

Three modes:
  (default) keyword   -- a transparent, offline rule matcher over data/failure_kb.json.
                         Deterministic and inspectable, but literal: it matches words,
                         not meaning, so it can miss a paraphrase that avoids the terms.
  --llm               -- one model call judges the design against the failure modes.
                         Useful as a quick semantic matcher.
  --agent             -- a small multi-pass LLM reviewer: extract design facts, draft
                         findings, then audit for false positives/false mitigations.
                         This is the mode intended for real ConOps text.

Usage:
  python3 redteam.py                            # keyword mode on the built-in example
  python3 redteam.py design.txt                 # keyword mode on your file
  python3 redteam.py design.txt --llm           # quick one-pass LLM mode
  python3 redteam.py design.txt --agent         # multi-pass LLM agent mode
  python3 redteam.py design.txt --agent --provider openai --model gpt-4o-mini
  python3 redteam.py design.txt --agent --provider parley --model openai/gpt-5-mini
  python3 redteam.py --serve --provider parley  # local HTML UI; key stays in env

Keys (LLM/agent modes), read from the environment:
  ANTHROPIC_API_KEY        (provider anthropic; agent default claude-3-5-haiku-latest)
  OPENAI_API_KEY           (provider openai;    agent default gpt-4o-mini)
  MY_MIT_PARLEY_API_KEY    (provider parley;    agent default openai/gpt-5-mini)
                           aliases: MIT_PARLEY_API_KEY or PARLEY_API_KEY

No third-party packages required (uses urllib).
"""
import argparse, json, os, sys, textwrap, urllib.parse, urllib.request, urllib.error

KB_PATH = os.path.join(os.path.dirname(__file__), "data", "failure_kb.json")
PARLEY_DEFAULT_BASE_URL = "https://parley.api.mit.edu/v1"
PARLEY_API_KEY_ENV_VARS = ("MY_MIT_PARLEY_API_KEY", "MIT_PARLEY_API_KEY", "PARLEY_API_KEY")
PARLEY_BASE_URL_ENV_VARS = (
    "MIT_PARLEY_BASE_URL", "PARLEY_BASE_URL", "MIT-PARLEY_BASE_URL", "MY_MIT_PARLEY_BASE_URL"
)
MODEL_OPTIONS = {
    "anthropic": [
        {"id": "claude-3-5-haiku-latest", "label": "Claude 3.5 Haiku (lightweight)"},
        {"id": "claude-sonnet-4-6", "label": "Claude Sonnet 4.6"},
    ],
    "openai": [
        {"id": "gpt-4o-mini", "label": "GPT-4o mini"},
        {"id": "gpt-4o", "label": "GPT-4o"},
    ],
    "parley": [
        {"id": "openai/gpt-5-mini", "label": "GPT-5 Mini (recommended)"},
        {"id": "openai/gpt-5-nano", "label": "GPT-5 Nano (cheaper, less reliable)"},
        {"id": "google/gemini-3.0-flash", "label": "Gemini 3.0 Flash"},
        {"id": "google/gemini-3.1-pro", "label": "Gemini 3.1 Pro"},
        {"id": "bedrock/llama-4-maverick-17b", "label": "Llama 4 Maverick"},
        {"id": "bedrock/claude-haiku-4-5", "label": "Claude Haiku 4.5 (Parley/Bedrock)"},
        {"id": "bedrock/claude-sonnet-4-6", "label": "Claude Sonnet 4.6 (Parley/Bedrock)"},
    ],
}

DEFAULT_DOC = """DESCENT GNC -- CONCEPT OF OPERATIONS (CRITICAL DESIGN REVIEW EXCERPT)
The primary source of altitude and descent velocity during the final landing sequence is
the onboard Laser Range Finder (LRF), expected to acquire a valid range from about 3 km to
trigger the final braking burn. There is no independent altitude source in the terminal
phase. To protect against spurious returns the navigation filter applies an outlier-rejection
threshold: measurements deviating strongly from the propagated estimate are treated as
anomalous and rejected. The landing site was finalized after CDR. The LRF has not previously
flown on a lunar descent and a second ranging sensor was descoped to protect mass margin; the
LRF is the sole ranging source. Solar cells are body-mounted on the upper deck consistent with
the nominal upright landing attitude."""


# ----------------------------- shared -----------------------------
def load_kb():
    with open(KB_PATH) as f:
        return json.load(f)


def band_for(full):
    if any(c["severity"] >= 5 for c in full):
        return "HIGH RISK"
    return "ELEVATED RISK" if full else None


def render(results, passes, missions, header):
    """results: list of (check, status, evidence, why). passes: list of check."""
    full = [r[0] for r in results if r[1] == "flag"]
    results.sort(key=lambda r: (0 if r[1] == "flag" else 1, -r[0]["severity"]))
    band = band_for(full) or ("FOR REVIEW" if results else "LOW RISK")
    score = sum(c["severity"] for c in full) + (len(results) - len(full))
    print("=" * 78)
    print(f"DESIGN-REVIEW  |  {header}")
    print(f"VERDICT: {band}   (risk index {score}; {len(full)} flag(s), "
          f"{len(results)-len(full)} partial, {len(passes)} mitigated)")
    print("=" * 78)
    for c, status, evidence, why in results:
        tag = f"SEVERITY {c['severity']}" if status == "flag" else "PARTIALLY ADDRESSED"
        print(f"\n[{tag}] {c['name']}")
        if evidence:
            print("  evidence: " + textwrap.fill(evidence, 72, subsequent_indent="            "))
        if why:
            print("  note:     " + textwrap.fill(why, 72, subsequent_indent="            "))
        print("  past occurrences:")
        for pid in c["precedents"]:
            m = missions.get(pid)
            if m:
                print(f"     - {m['mission']} ({m['date']}, {m['outcome_class']}) -> {m['source_url']}")
        print("  mitigation: " + textwrap.fill(c["recommendation"], 72, subsequent_indent="              "))
    if passes:
        print("\n" + "-" * 78 + "\nMITIGATIONS DETECTED:")
        for c in passes:
            print(f"  [OK] {c['name']}")
    print()


def checks_for_prompt(kb):
    return [{"id": c["id"], "name": c["name"], "question": c["question"],
             "severity": c["severity"]} for c in kb["design_checks"]]


def review_from_findings(findings, kb):
    missions = {m["id"]: m for m in kb["missions"]}
    by_check = {c["id"]: c for c in kb["design_checks"]}
    results, passes, seen = [], [], set()
    for f in findings:
        c = by_check.get(f.get("check_id"))
        if not c or c["id"] in seen:
            continue
        status = str(f.get("status", "")).lower().strip()
        if status == "pass":
            passes.append(c)
            seen.add(c["id"])
            continue
        if status not in ("flag", "partial"):
            continue
        ev = str(f.get("evidence", "") or "").strip()
        rationale = str(f.get("rationale", "") or "").strip()
        evidence_l = ev.lower()
        combined_l = (ev + " " + rationale).lower()
        # Guardrails for common LLM over-reaches: a finding needs positive design-text evidence,
        # not just an omitted mitigation or an item from the fact-extractor's not_stated list.
        if "not_stated" in evidence_l or "not addressed in design text" in evidence_l:
            continue
        if c["id"] == "chk_outlier_rejection" and not any(
            t in evidence_l for t in ("outlier", "reject", "rejection", "gating", "threshold", "discard", "anomalous", "spurious", "intercept")
        ):
            continue
        if c["id"] == "chk_command_propulsion_isolation" and not any(
            t in evidence_l for t in ("reboot", "restart", "reset", "watchdog", "shutdown", "shut down", "computer restart")
        ):
            continue
        if c["id"] == "chk_sensor_liveness" and status == "flag" and any(t in combined_l for t in ("health check", "health checks", "validity check", "liveness check", "go/no-go")):
            status = "partial"
        # If a later audit duplicates a check, keep the first final judgment.
        seen.add(c["id"])
        confidence = str(f.get("confidence", "") or "").strip()
        why = rationale + (f" Confidence: {confidence}." if confidence else "")
        results.append((c, status, f'"{ev}"' if ev else "", why))
    return results, passes, missions


# ----------------------------- keyword mode -----------------------------
def find_hits(text, terms):
    low = " ".join(text.lower().split())  # collapse whitespace so matches survive line wraps
    seen, out = set(), []
    for t in terms:
        if t in low and t not in seen:
            seen.add(t); out.append(t)
    return out


def keyword_review(text, kb):
    missions = {m["id"]: m for m in kb["missions"]}
    results, passes = [], []
    for c in kb["design_checks"]:
        pres = find_hits(text, c["present_signals"])
        mit = find_hits(text, c["mitigation_signals"])
        if not pres:
            if mit:
                passes.append(c)
            continue
        status = "partial" if mit else "flag"
        why = ("mitigation language also present (verify): " + ", ".join(mit[:4])) if mit else ""
        results.append((c, status, f"matched: {', '.join(pres[:4])}", why))
    return results, passes, missions


# ----------------------------- LLM + agent modes -----------------------------
def _post(url, headers, payload, *, bypass_proxy=False):
    req = urllib.request.Request(url, data=json.dumps(payload).encode(),
                                 headers={**headers, "content-type": "application/json"})
    if bypass_proxy:
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        with opener.open(req, timeout=120) as r:
            return json.loads(r.read().decode())
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode())


def _first_env(names):
    for name in names:
        value = os.environ.get(name, "").strip()
        if value:
            return value
    return None


def _parley_base_url():
    return _first_env(PARLEY_BASE_URL_ENV_VARS) or PARLEY_DEFAULT_BASE_URL


def _chat_completions_url(base_url):
    parsed = urllib.parse.urlparse(base_url.strip().rstrip("/"))
    path = parsed.path.rstrip("/")
    if not path:
        path = "/v1/chat/completions"
    elif path.endswith("/v1/chat/completions"):
        pass
    elif path.endswith("/v1"):
        path += "/chat/completions"
    else:
        path += "/v1/chat/completions"
    return urllib.parse.urlunparse(parsed._replace(path=path, params="", query="", fragment=""))


def _should_bypass_proxy(url):
    parsed = urllib.parse.urlparse(url)
    return parsed.scheme == "http" and parsed.hostname in ("localhost", "127.0.0.1", "::1")


def _chat_message_text(data):
    choice = (data.get("choices") or [{}])[0]
    message = choice.get("message") or {}
    content = message.get("content", "")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, str):
                parts.append(item)
            elif isinstance(item, dict):
                parts.append(str(item.get("text") or item.get("content") or ""))
        return "".join(parts)
    return "" if content is None else str(content)


def _raw_model_call(provider, model, system, user, max_tokens=2000):
    if provider == "anthropic":
        key = os.environ.get("ANTHROPIC_API_KEY")
        if not key:
            sys.exit("Set ANTHROPIC_API_KEY for --provider anthropic.")
        data = _post("https://api.anthropic.com/v1/messages",
                     {"x-api-key": key, "anthropic-version": "2023-06-01"},
                     {"model": model, "max_tokens": max_tokens, "system": system,
                      "messages": [{"role": "user", "content": user}]})
        return data["content"][0]["text"]
    if provider == "openai":
        key = os.environ.get("OPENAI_API_KEY")
        if not key:
            sys.exit("Set OPENAI_API_KEY for --provider openai.")
        data = _post("https://api.openai.com/v1/chat/completions",
                     {"authorization": f"Bearer {key}"},
                     {"model": model, "messages": [{"role": "system", "content": system},
                                                     {"role": "user", "content": user}],
                      "max_tokens": max_tokens, "temperature": 0})
        return _chat_message_text(data)
    if provider == "parley":
        url = _chat_completions_url(_parley_base_url())
        key = _first_env(PARLEY_API_KEY_ENV_VARS)
        if not key and _should_bypass_proxy(url):
            key = os.environ.get("NONO_PROXY_TOKEN", "").strip()
        if not key:
            sys.exit("Set MY_MIT_PARLEY_API_KEY (or MIT_PARLEY_API_KEY/PARLEY_API_KEY) for --provider parley.")
        if model.startswith("openai/gpt-5-nano"):
            completion_cap = max(max_tokens, 32768)
        elif model.startswith("openai/gpt-5"):
            completion_cap = max(max_tokens, 8192)
        else:
            completion_cap = max_tokens
        payload = {"model": model,
                   "messages": [{"role": "system", "content": system},
                                {"role": "user", "content": user}],
                   "max_completion_tokens": completion_cap}
        if model.startswith("openai/gpt-5"):
            payload["reasoning_effort"] = "minimal"
            payload["response_format"] = {"type": "json_object"}
        data = _post(url,
                     {"authorization": f"Bearer {key}"},
                     payload,
                     bypass_proxy=_should_bypass_proxy(url))
        if os.environ.get("REDTEAM_DEBUG_LLM"):
            print("PARLEY RAW RESPONSE:", json.dumps(data)[:4000], file=sys.stderr)
        raw = _chat_message_text(data)
        if not raw.strip():
            choice = (data.get("choices") or [{}])[0]
            finish = choice.get("finish_reason", "unknown")
            usage = data.get("usage", {})
            raise RuntimeError(
                f"Parley returned an empty assistant message (finish_reason={finish}, usage={usage}). "
                "This usually means the completion token cap was exhausted by hidden reasoning or the model "
                "ignored JSON mode; try --model openai/gpt-5-mini or set REDTEAM_DEBUG_LLM=1 and rerun."
            )
        return raw
    sys.exit(f"Unknown provider: {provider}")


def _json_from_model(raw):
    raw = (raw or "").strip()
    if not raw:
        raise ValueError("Model returned an empty text response; try a larger/non-nano model or rerun with REDTEAM_DEBUG_LLM=1.")
    if raw.startswith("```"):
        parts = raw.split("```")
        if len(parts) >= 3:
            raw = parts[1].strip()
            if raw.lower().startswith("json"):
                raw = raw[4:].strip()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        start, end = raw.find("{"), raw.rfind("}")
        if start >= 0 and end > start:
            return json.loads(raw[start:end+1])
        snippet = raw[:500].replace("\n", " ")
        raise ValueError(f"Model did not return parseable JSON. First 500 chars: {snippet!r}")


def _call_json(provider, model, system, user, max_tokens=2000):
    return _json_from_model(_raw_model_call(provider, model, system, user, max_tokens=max_tokens))


def llm_findings(text, kb, provider, model):
    system = ("You review a lunar lander descent/landing design against known GNC failure modes. "
              "You are given a list of failure modes (id, name, diagnostic question, severity) and a "
              "design text. For each failure mode, judge ONLY from affirmative evidence in the design text whether the risk is "
              "'flag' (present and not mitigated), 'partial' (present but partially mitigated), 'pass' "
              "(clearly mitigated/addressed), or omit it if not applicable or merely not discussed. Do not flag a check just because a mitigation is absent. Quote a short verbatim "
              "evidence snippet, give a one-sentence rationale, and include confidence high|medium|low. Return STRICT JSON only, no prose: "
              '{"findings":[{"check_id":"...","status":"flag|partial|pass","evidence":"...","rationale":"...","confidence":"high|medium|low"}]}')
    user = "FAILURE MODES:\n" + json.dumps(checks_for_prompt(kb)) + "\n\nDESIGN TEXT:\n" + text
    return _call_json(provider, model, system, user).get("findings", [])


def llm_review(text, kb, provider, model):
    return review_from_findings(llm_findings(text, kb, provider, model), kb)


def agent_facts(text, provider, model):
    system = ("You are the intake phase of a lunar-lander design-review agent. Extract only facts "
              "directly supported by the design text. Focus on terminal descent sensing, sensor fusion, "
              "redundancy, fallback modes, measurement filtering/gating, terrain databases/lighting, "
              "pre-maneuver liveness checks, fault-management/propulsion isolation, late changes, "
              "accepted/open risks, power after tip-over, and engine-out/asymmetric-thrust tolerance. "
              "Do not evaluate risk yet. Return STRICT JSON only: "
              '{"summary":"...","facts":[{"topic":"...","claim":"...","quote":"..."}],'
              '"not_stated":["..."]}')
    user = "DESIGN TEXT:\n" + text
    return _call_json(provider, model, system, user, max_tokens=1800)


def agent_draft_findings(text, kb, facts, provider, model):
    system = ("You are a cautious lunar lander GNC red-team reviewer. Use the design text plus the "
              "extracted fact sheet to evaluate each failure mode. Apply these guardrails: "
              "(1) Do NOT treat the mere mention of Doppler lidar, radar, laser, or landing radar as "
              "redundancy; it is a mitigation only if the text states an independent/dissimilar backup, "
              "fusion, or explicit graceful degradation. "
              "(2) Do NOT flag outlier rejection from generic words like 'rejected' unless the context is "
              "measurement/filter/gating logic. "
              "(3) A terrain/hazard database is mitigated only if validated for the actual approach geometry, "
              "altitude, and lighting. "
              "(4) Known reliability issues, not-flight-proven loss-critical hardware, waivers, skipped tests, "
              "risks assumed remedied, or no active FDIR during descent should be treated as known/open risk acceptance unless clearly retired. "
              "(5) Pass only when a mitigation is explicit; if present but incomplete/uncertain, use partial. "
              "(6) Do not flag a check merely because a mitigation is absent or a fact is listed as not_stated; there must be affirmative design-text evidence that the risky pattern is present. "
              "(7) A Kalman filter alone is not outlier rejection; outlier-rejection risk requires evidence of gating/rejection/thresholding/discarding measurements. "
              "Statuses: flag, partial, pass, or omit if not applicable. Quote short verbatim evidence from the "
              "design text. Return STRICT JSON only: "
              '{"findings":[{"check_id":"...","status":"flag|partial|pass","evidence":"...",'
              '"rationale":"...","confidence":"high|medium|low"}]}')
    user = ("FAILURE MODES:\n" + json.dumps(checks_for_prompt(kb)) +
            "\n\nEXTRACTED FACTS:\n" + json.dumps(facts) +
            "\n\nDESIGN TEXT:\n" + text)
    return _call_json(provider, model, system, user, max_tokens=2200).get("findings", [])


def agent_audit_findings(text, kb, facts, draft, provider, model):
    system = ("You are the audit/finalization phase of a lunar-lander design-review agent. Your job is "
              "to correct the draft findings for missed applicable checks, false positives, and false mitigations. "
              "Be especially strict about these regression traps from real ConOps documents: "
              "- 'Doppler lidar' can be the sole sensor or a replacement for radar; do not call it redundancy unless another independent path is stated. "
              "- 'Sun sensors were rejected' or a rejected design trade is not an outlier-rejection filter. "
              "- A 'landing radar' or four-beam radar can still be single-string terminal ranging. "
              "- 'No active FDIR during descent', 'known issue', 'assumed remedied', 'not flight proven', or skipped tests are risk-acceptance evidence. "
              "- Terrain/lighting handling should be credited when the design explicitly chooses lighting and prepares the terrain database accordingly; downgrade only if the text also reveals a validation/geometry gap. "
              "- Do not use not_stated items as evidence for a flag. Absence of a mitigation means omit unless the risky architecture/logic itself is affirmatively present in the design text. "
              "- Kalman filtering alone is not hard outlier rejection; require explicit gating/rejection/threshold/discard language. "
              "- Missing power-after-tipover provisions should be omitted unless the text discusses solar/power/comms geometry or upright/tipped attitude dependence. "
              "- 'No active FDIR during descent' is a deliberately accepted operational risk; map it to known/open risk acceptance rather than reboot/propulsion-isolation unless reboot/shutdown coupling is stated. "
              "Return the final corrected findings as STRICT JSON only, no prose: "
              '{"findings":[{"check_id":"...","status":"flag|partial|pass","evidence":"...",'
              '"rationale":"...","confidence":"high|medium|low"}]}')
    user = ("FAILURE MODES:\n" + json.dumps(checks_for_prompt(kb)) +
            "\n\nEXTRACTED FACTS:\n" + json.dumps(facts) +
            "\n\nDRAFT FINDINGS:\n" + json.dumps({"findings": draft}) +
            "\n\nDESIGN TEXT:\n" + text)
    return _call_json(provider, model, system, user, max_tokens=2400).get("findings", [])


def agent_review(text, kb, provider, model):
    facts = agent_facts(text, provider, model)
    draft = agent_draft_findings(text, kb, facts, provider, model)
    final = agent_audit_findings(text, kb, facts, draft, provider, model)
    return review_from_findings(final, kb)


def normalize_provider(provider):
    if not provider:
        return None
    p = provider.strip().lower().replace("_", "-")
    return "parley" if p in ("parley", "mit-parley", "mitparley") else p


def choose_provider(requested):
    requested = normalize_provider(requested)
    parley_env = _first_env(PARLEY_API_KEY_ENV_VARS) or (_first_env(PARLEY_BASE_URL_ENV_VARS) and os.environ.get("NONO_PROXY_TOKEN"))
    return requested or ("anthropic" if os.environ.get("ANTHROPIC_API_KEY")
                         else "openai" if os.environ.get("OPENAI_API_KEY")
                         else "parley" if parley_env else None)


def default_model(provider, agent=False):
    if provider == "anthropic":
        return "claude-3-5-haiku-latest" if agent else "claude-sonnet-4-6"
    if provider == "openai":
        return "gpt-4o-mini" if agent else "gpt-4o"
    if provider == "parley":
        return "openai/gpt-5-mini"
    return None


# ----------------------------- local HTML server -----------------------------
def serve_html(host, port, provider_arg=None, model_arg=None):
    """Serve the demo page plus a localhost-only LLM JSON endpoint.

    This lets the browser UI use API keys from this process' environment instead
    of asking the user to paste keys into the page.
    """
    from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
    from urllib.parse import urlparse

    html_path = os.path.join(os.path.dirname(__file__), "lunar_redteam_demo.html")

    class Handler(BaseHTTPRequestHandler):
        server_version = "LunarRedteamLocal/0.1"

        def log_message(self, fmt, *args):
            print(f"[{self.log_date_time_string()}] {self.address_string()} {fmt % args}", file=sys.stderr)

        def _send(self, status, body, content_type="application/json"):
            if isinstance(body, str):
                body = body.encode()
            self.send_response(status)
            self.send_header("content-type", content_type)
            self.send_header("content-length", str(len(body)))
            self.send_header("cache-control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def _send_json(self, status, obj):
            self._send(status, json.dumps(obj).encode(), "application/json")

        def do_GET(self):
            path = urlparse(self.path).path
            if path in ("/", "/lunar_redteam_demo.html"):
                with open(html_path, "rb") as f:
                    self._send(200, f.read(), "text/html; charset=utf-8")
            elif path == "/api/config":
                provider = choose_provider(provider_arg)
                model = model_arg or (default_model(provider, agent=True) if provider else "")
                self._send_json(200, {
                    "served": True,
                    "provider": provider,
                    "default_model": model,
                    "models": MODEL_OPTIONS.get(provider or "", []),
                })
            else:
                self._send_json(404, {"error": "not found"})

        def do_POST(self):
            path = urlparse(self.path).path
            if path != "/api/model-json":
                self._send_json(404, {"error": "not found"})
                return
            try:
                n = int(self.headers.get("content-length", "0"))
                if n > 2_000_000:
                    self._send_json(413, {"error": "request too large"})
                    return
                req = json.loads(self.rfile.read(n).decode())
                system = req.get("system", "")
                user = req.get("user", "")
                max_tokens = int(req.get("max_tokens") or 2000)
                provider = choose_provider(provider_arg)
                if not provider:
                    self._send_json(400, {"error": "No provider key found in server environment."})
                    return
                model = (req.get("model") or model_arg or default_model(provider, agent=True)).strip()
                if not model:
                    self._send_json(400, {"error": "No model configured."})
                    return
                result = _call_json(provider, model, system, user, max_tokens=max_tokens)
                self._send_json(200, result)
            except Exception as e:
                self._send_json(500, {"error": str(e)})

    httpd = ThreadingHTTPServer((host, port), Handler)
    provider = choose_provider(provider_arg)
    model = model_arg or (default_model(provider, agent=True) if provider else None)
    url = f"http://{host}:{httpd.server_port}/"
    print(f"Serving local HTML UI at {url}")
    print(f"Server-side provider/model: {provider or 'auto-not-configured'} / {model or 'default'}")
    print("API keys stay in this Python process; do not paste them into the browser.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")


# ----------------------------- main -----------------------------
def main():
    ap = argparse.ArgumentParser(description="Lunar lander descent-design review.")
    ap.add_argument("file", nargs="?", help="design-review text file (default: built-in example)")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--llm", action="store_true", help="use one LLM call instead of keyword matching")
    mode.add_argument("--agent", action="store_true", help="use a multi-pass LLM review agent (extract -> review -> audit)")
    ap.add_argument("--serve", action="store_true", help="serve the HTML UI locally; browser calls this process, which reads API keys from env")
    ap.add_argument("--host", default="127.0.0.1", help="host for --serve (default: 127.0.0.1)")
    ap.add_argument("--port", type=int, default=8787, help="port for --serve (default: 8787)")
    ap.add_argument("--provider", choices=["anthropic", "openai", "parley", "mit-parley", "MIT-parley"], help="LLM provider (default: auto from env)")
    ap.add_argument("--model", help="model name (default: provider/mode-specific)")
    args = ap.parse_args()

    if args.serve:
        serve_html(args.host, args.port, normalize_provider(args.provider), args.model)
        return

    kb = load_kb()
    if args.file:
        with open(args.file) as f:
            text = f.read()
        label = args.file
    else:
        text, label = DEFAULT_DOC, "built-in example (single-string LRF terminal descent)"

    if args.llm or args.agent:
        provider = choose_provider(args.provider)
        if not provider:
            sys.exit("LLM/agent mode needs ANTHROPIC_API_KEY, OPENAI_API_KEY, or MY_MIT_PARLEY_API_KEY "
                     "in the environment (or pass --provider).")
        model = args.model or default_model(provider, agent=args.agent)
        try:
            if args.agent:
                results, passes, missions = agent_review(text, kb, provider, model)
                mode_label = f"LLM agent ({provider}/{model})"
            else:
                results, passes, missions = llm_review(text, kb, provider, model)
                mode_label = f"LLM one-pass ({provider}/{model})"
        except urllib.error.HTTPError as e:
            sys.exit(f"API error {e.code}: {e.read().decode()[:500]}")
        except (urllib.error.URLError, RuntimeError, ValueError, KeyError, IndexError) as e:
            sys.exit(f"LLM response error ({provider}/{model}): {e}")
        render(results, passes, missions, f"input: {label}  |  mode: {mode_label}")
    else:
        results, passes, missions = keyword_review(text, kb)
        render(results, passes, missions, f"input: {label}  |  mode: offline keyword")


if __name__ == "__main__":
    main()

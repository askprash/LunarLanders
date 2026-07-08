# Real ConOps test cases

Six genuinely public lunar-lander descent/landing GNC descriptions, extracted as faithful close-paraphrases for testing the design-review tool. Each `.txt` is a paste-in design text; the header line in each file carries the citation and URL.

Run any of them:

```
python3 redteam.py examples/teamindus_arxiv.txt            # Demo (offline keyword)
python3 redteam.py examples/teamindus_arxiv.txt --agent    # Agent mode (auto-detects your API key)
python3 redteam.py examples/teamindus_arxiv.txt --agent --provider parley --model openai/gpt-5-mini
python3 redteam.py examples/teamindus_arxiv.txt --llm      # Single-pass LLM mode
```

or run the local HTML server so the browser never sees your key:

```
MY_MIT_PARLEY_API_KEY=... python3 redteam.py --serve --provider parley
# open http://127.0.0.1:8787/ and select Local server (env key)
```

You can also load the file's text into the static HTML page (Demo, single-pass LLM, or Agent mode), but direct provider calls from a static page require pasting a browser-side key. Agent mode supports Local server, Anthropic, and MIT Parley in the page; the CLI also supports OpenAI. For Parley CLI use `MY_MIT_PARLEY_API_KEY` (or `MIT_PARLEY_API_KEY`/`PARLEY_API_KEY`).

## Sources

| File | Source | Type |
|---|---|---|
| `lunar_pallet_lander_NTRS.txt` | NASA Lunar Pallet Lander GN&C, Orphee et al., AAS 2019 (NTRS 20190002101) | Agency concept |
| `mit_gray_team_capstone.txt` | MIT "Engineering Apollo" Gray Team final report, 2007 (MIT OCW) | Student capstone |
| `teamindus_arxiv.txt` | TeamIndus lunar lander GNC overview, arXiv:1907.10955, 2019 | Competition/industry team |
| `ndl_sensor_NTRS.txt` | Navigation Doppler Lidar, Amzajerdian et al., 2020 (NTRS 20200002534) | Single-sensor stress case |
| `morpheus_alhat_NTRS.txt` | Morpheus Lander flight control / ALHAT, Jang et al., 2014 (NTRS 20140008284) | Agency testbed |
| `polito_thesis.txt` | "Downrange Analysis for Optimal Lunar Soft Precision Landing," MSc thesis, Politecnico di Torino | Academic thesis |

## What this tells us: Demo (keyword) vs. an analyst / Agent mode

The interesting result is the **gap** between what the offline keyword matcher returns and what a careful read (or Agent mode) should conclude. These are real prose documents, not text written to hit our keywords — so they are a fair test, and they expose exactly where keyword matching breaks.

| File | Demo (keyword) verdict | What an analyst should conclude | Where keyword went wrong |
|---|---|---|---|
| Lunar Pallet Lander | ELEVATED (terrain-DB flag; single-string *partial*) | **HIGH** — below ~30 m it is IMU-only, NDL is the sole ranging sensor, no dissimilar backup, "no hazard avoidance" | **False mitigation**: the words "Doppler lidar" are on our mitigation list, so the matcher treated the *single* ranging sensor as if it were redundancy, and downgraded the flag |
| MIT Gray Team | HIGH — but for the **wrong reason** (outlier-rejection flag) | **HIGH** — single landing radar (single-string), and an explicitly **accepted known risk** (RL-10 reliability "assumed remedied") | **False positive** from "sun sensors were *rejected*" (a design trade, not measurement rejection); **missed** the real single-string and known-risk flags because the prose says "landing radar"/"known reliability issues", not "radar altimeter"/"known issue" |
| TeamIndus | HIGH (single-string, terrain-DB, engine-out; liveness correctly **passed**) | **HIGH** — homogeneous laser ranging (no dissimilar radar), and "no active FDIR during descent" accepted by design; **but** lighting/terrain-DB **is** handled (early-morning landing, DB prepared) | Correctly passed the liveness check (it found "health checks … before descent"), but **over-flagged** the terrain database, which the design actually mitigates, and **missed** the deliberately-accepted-risk framing |
| NDL sensor | FOR REVIEW (single-string *partial*) | **HIGH** — NDL is presented as the sole ranging sensor and even argued as a *replacement* for radar | Same **false mitigation** as the Pallet Lander: "Doppler lidar" read as redundancy |
| Morpheus | HIGH (single-string flag) | **HIGH** — also single main engine (engine-out), with ALHAT hazard sensing as a real mitigation | **Missed** the engine-out flag (no trigger words present) |
| Polito thesis | **LOW RISK (nothing fired)** | Several flags — generic single-string radar, no liveness check, no FDIR | **Complete miss**: the prose uses "four-beam landing radar", "imaging LIDAR", "absolute navigation" — none of our keyword terms — so nothing matched |

## Takeaway

On text written with the expected vocabulary (the three built-in examples), the keyword matcher is fine. On **real** documents it produces false positives ("rejected"), false mitigations ("Doppler lidar" = the single sensor, not redundancy), missed flags (vocabulary mismatch), and in one case a flat miss (the Polito thesis reads as LOW RISK when it should not). This is precisely the brittleness the keyword mode is meant to illustrate — and the reason **Agent mode is the one to use on real ConOps**: it reads meaning and audits common mistakes, so "Doppler lidar as the sole sensor" and "Doppler lidar added for redundancy" are no longer the same string.

These six files are the recommended regression set: run them in Agent mode and check that it (a) flags single-string ranging in the Pallet Lander, NDL, Morpheus and TeamIndus cases, (b) does **not** fire on "sun sensors were rejected", (c) credits TeamIndus's lighting handling, and (d) does **not** return LOW RISK on the Polito thesis.

# Start with structured files but plan scalable retrieval

We will start the failure memory as structured, version-controlled JSON/YAML/Markdown with deterministic Python indexing, while explicitly planning for a later scalable retrieval layer once the corpus grows. The current corpus is small enough that plain files are more auditable and easier for academic reviewers to inspect than an early vector database, but the research claim eventually requires a larger authoritative source corpus and more capable retrieval.

Future retrieval work should consider vector or hybrid lexical/vector infrastructure, graph/database indexing, or generated search indexes, but only if it preserves named precedents, source URLs, confidence levels, quotes, and caveats. The goal is not semantic search for its own sake; it is scalable, auditable retrieval of past occurrences that can support precedent-backed review-readiness questions.

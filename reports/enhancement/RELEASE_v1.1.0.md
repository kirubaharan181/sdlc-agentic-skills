# Release v1.1.0 verification (2026-11-25)

| Check | Result |
| --- | --- |
| Tag `v1.1.0` published by the owner on commit 8fc6fdc | Yes |
| Release workflow (`release.yml`) | Completed successfully; release is not a prerelease |
| Assets | `sdlc-agentic-skills-1.1.0.tar.gz`, `SHA256SUMS` |
| Downloaded `.tar.gz` against published `SHA256SUMS` | OK (`sha256sum -c`) |
| Archive contents vs a local rebuild of the tag | Identical: 608 files, same uncompressed tar hash (05ba527b…56b8d4) |
| Compressed `.tar.gz` bytes vs local rebuild | **Differ** (zlib versions); not a content difference |

Consequence: the v1.1.0 `SHA256SUMS` verifies downloads but cannot by itself prove a byte-identical gzip rebuild. From the next release,
`UNCOMPRESSED_TAR_SHA256` is published as well so reproducibility can be checked on the stable uncompressed tar.

Not covered by this release or this check: agent behaviour in Codex, OpenCode or other tools (documented, not tested); SkillEvaluator
Tier 2, Tier 3 and LLM checks (not run); any security certification or publication approval; the checksum is not a signature.

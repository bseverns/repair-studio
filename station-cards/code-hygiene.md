---
title: "Code Hygiene & Repo Care"
goal: "Lower cognitive load and failure rates"
timebox: "30–60 min"
risk: "low"
done_definition:
  - "CI green; README matches reality"
---

## Steps

1) Lint/format; remove dead code; tighten `.gitignore`.
2) Add minimal tests for a hot path or script a sanity check.
3) Enable CI to lint on PR; add a status badge.
4) Release a patch with notes.

## Evidence

- CI run link
- Tests output
- Changelog entry

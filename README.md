# Repair Studio Kit

*A playbook and repo scaffold for valorizing maintenance, documentation, stability, and care work across creative/technical studios.*

**Why this exists:** Most studios glorify heroic builds and under-reward repair. This kit makes repair **visible, teachable, and rewarded**.

---

## Quick start

- **Cadence:** Start with a **Monthly Sprint (3h)** and a **Weekly Stitch (15 min)** appended to critique/rehearsal.
- **Where:** Park a **roaming bench** (ESD mat + labeler + doc camera) where people already gather.
- **What counts:** doc fixes, rig stabilization, code hygiene, safety/consent defaults, UX papercuts, process checklists.
- **How:** use `/templates` for intake, PRs, scribe notes; rotate roles; enforce WIP limits; celebrate boring wins.

> Print the one-page **Field Card**: [`REPAIR_STUDIO_FIELD_CARD.md`](REPAIR_STUDIO_FIELD_CARD.md)

---

## Repo layout

```
repair-studio-kit/
├─ README.md
├─ REPAIR_STUDIO_FIELD_CARD.md
├─ LICENSE
├─ CODE_OF_CONDUCT.md
├─ CONTRIBUTING.md
├─ SECURITY.md
├─ CHANGELOG.md
├─ policies/
├─ templates/
├─ station-cards/
├─ signage/
├─ .github/ (issue + PR templates, CI)
├─ scripts/ (helpers, indexers)
├─ manuals/ (drop vendor/user manuals here)
├─ examples/
├─ data/metrics/
└─ assets/
```

### Manuals

Drop PDFs/PNGs/TXTs into `/manuals/` subfolders (`machines/`, `software/`, `instruments/`, `spaces/`). Run:

```bash
python3 scripts/build_manuals_index.py
```

to regenerate `manuals/INDEX.md`.

---

## Governance (short version)

- **Repair is production.** Calm fixes get public demos and credits.
- **Blameless + accountable.** No shame; one system change ships after each retro.
- **Consent-forward.** Recording is opt‑in; “Delete Now” honored immediately.
- **Buffers on purpose.** Time/money/people slack is a feature, not waste.
- **Equity:** prioritize repairs that reduce harm to newcomers and marginalized users.

Full policies in `/policies`.

---

## Start a session

1. Print/post the signage in `/signage`.
2. Open an **Intake Ticket** (issue template) for each artifact.
3. Triage with the rubric in `/templates/triage-rubric.md`.
4. Pair up; enforce WIP limits; set timers.
5. Close with 60s demos; link PRs/issues; log one system improvement.

---

## Credits

Built for educators, makers, and community labs. MIT-licensed. Add yourself to `CONTRIBUTING.md` when you ship a fix.

# Tascam 404 Portastudio

Four-track cassette deck for demos, overdubs, and unapologetic tape grime. This page keeps routing, maintenance, and quirks documented.

## Why we lean on it
- Individual channel strips with EQ and aux sends pair perfectly with the Field Kit FX and Microgranny.
- Tape saturation glues the AE modular, S900, and outboard FX into a single vibe.
- Built-in bounce workflow teaches non-linear tracking to new collaborators.

## Session checklist
1. Use Type II (chrome) cassettes only. Label shells with project slug, tape speed, and noise reduction status.
2. Set tape speed: `HIGH` for fidelity, `NORMAL` when you want lo-fi warble or extended minutes.
3. Arm tracks via `REC FUNCTION`. Set `MIC/LINE` vs `TAPE` depending on overdub vs bounce.
4. Monitor via the Control Room outs to the studio interface. Use headphones when tracking vocals in the booth.
5. After a session, rewind, eject, and store tapes upright in the case. Log location in `data/tapes/catalog.csv`.

## Bounce recipes
- **Drum stack**: Tracks 1–3 for individual sources, bounce to Track 4 with EQ tweaks, leave Track 1 free for vocals.
- **Tape loop**: Record noise or drones, splice tape to 10–12" loop, run via external reel (document in assets/loops/).
- **Live mix**: Feed Field Kit FX return into Track 3 while tracking live jam on Track 1/2; bounce to Track 4 for final stereo.

## Maintenance log
| Date | Task | Notes |
| --- | --- | --- |
| yyyy-mm-dd | Head clean | _99% IPA + cotton swab._ |
| yyyy-mm-dd | Demag | _Han-D-Mag, 5 sec per head._ |
| yyyy-mm-dd | Belt check | _Order from Vintage-Electronics.cc if slack._ |

## Troubleshooting
- **Uneven levels**: Clean fader tracks with DeoxIT FaderLube. If noise persists, recap the PSU board (see `data/parts/tascam-404-cap-kit.csv`).
- **Transport slips**: Replace pinch roller (parts drawer bin B2). Log runtime hours.
- **dbx weirdness**: Toggle `dbx` off/on a few times to clean the switch. If artifacts remain, leave dbx off and note it on the tape case.

## References
- Closest manual (414mkII): <https://tascam.com/downloads/products/tascam/414mkII/414mkII_om.pdf>
- Head cleaning FAQ: <https://tascam.com/us/support/faq/214>
- Service notes archive: <https://www.tapatalk.com/groups/tascamusers/>

# Audio Recording Studio

Treated room for tracking vocals, synths, and weird tape manipulations. Use this doc to keep etiquette, routing, and maintenance in sync.

## Why this room matters
- Isolation + treatment let you capture clean takes from the modular corner or live instruments without the open-office bleed.
- Patchbay ties the Portastudio, Field Kit FX, and interface together for fast re-routing.
- Doubles as editing suite for post sessions when the main lab is too loud.

## Layout snapshot
- **Control desk**: Audio interface, monitor controller, patchbay normalled to Portastudio + Field Kit FX.
- **Live corner**: Mic locker (SM57 pair, large diaphragm condenser), headphone distro, acoustic gobos.
- **Outboard shelf**: Tascam 404, Koma Field Kit FX, reamp box, DI drawer.

## Session checklist
1. **Power-on order**: Power strip → interface → monitors (reverse on shutdown). Keep monitor volume at zero before flips.
2. Patch routing via the bay. Document non-standard routings on the whiteboard and in the log below.
3. Check headphone send levels before people put cans on. Protect ears.
4. Roll session in `data/audio-sessions/<date>-<project>/`. Capture sample rate, bit depth, and notes in `session.json`.
5. After tracking, back up to the shared NAS (`//nas/audio`) and note the location in the log.

## Etiquette
- No food or drinks on the desk. Water bottles on the floor only.
- Coil cables before you leave. Put mics back in cases with silica packs.
- If you change monitor calibration or headphone EQ, revert and log it.

## Maintenance cadence
| Interval | Task | Owner |
| --- | --- | --- |
| Weekly | Dust surfaces, vacuum floor | Facilities |
| Monthly | Verify monitor calibration with reference mic | Audio lead |
| Quarterly | Swap desiccant in mic locker, inspect patch cables | Audio lead |

## Routing + notes log
| Date | Patch change | Notes |
| --- | --- | --- |
| yyyy-mm-dd | Portastudio send → Field Kit FX return | _used for tape feedback session_ |
| yyyy-mm-dd | AE modular direct to interface | _bypassed Portastudio for clean take_ |

## References
- Studio etiquette primer: <https://bandzoogle.com/blog/recording-studio-etiquette-tips>
- Patchbay diagram placeholder: `assets/studio/patchbay.txt` (replace with PDF when available).
- Interface manual (Focusrite 18i20): <https://focusrite.com/en/audio-interface/scarlett-18i20/user-guide>

# Yamaha QY10 Music Sequencer

Pocket-sized sketchpad that still speaks fluent MIDI. Use this doc to keep batteries, patches, and SysEx dumps organized.

## Why it lives in the bag
- Battery-powered (6× AA) workstation with onboard sounds for quick harmonic ideas.
- Doubles as a MIDI controller for the Akai S900 when you need to audition samples fast.
- Pattern chaining is perfect for sketching song structures before committing to the Electribe or DAW.

## Power + storage
- Runs on AA or the 12 V DC adapter (center-positive). Swap to batteries when traveling to avoid ground loops.
- Internal memory is volatile. Dump songs via MIDI SysEx monthly into `data/backups/qy10/`.
- Keep the factory pattern disk image in `manuals/instruments/yamaha-qy10/` (placeholder text file until we snag the original).

## Workflow snapshot
1. **Boot** with fresh batteries and set contrast with the `+/-` keys if the screen fades.
2. Build patterns: `PATTERN` mode → assign style, tempo, and instrumentation. Use step entry for precision.
3. Chain into songs: `SONG` mode → `JOB` → `CHAIN`. Document arrangement names in the table below.
4. For MIDI control, `UTILITY` → `MIDI` → set transmit channel per device (S900 = 1, Electribe = 3, Volca = 2).

## Song log
| Date | Song | Destination gear | Notes |
| --- | --- | --- | --- |
| yyyy-mm-dd | sketch-01 | S900 drums + Volca bass | _exported via SysEx to laptop_ |

## Maintenance + spares
- Button caps get mushy. Keep replacements in `assets/hardware/yamaha-qy/`.
- If memory corrupts, perform factory reset: hold `UTILITY` + `ENTER` during power-on (warn everyone first!).
- MIDI DIN to TRS adapters live in the cables drawer.

## References
- Owner’s manual: <https://usa.yamaha.com/support/manuals/music_production/qy10.html>
- PC editor + SysEx dump tools: <http://sandsoftwaresound.net/yamaha-qy10/>
- Patch charts: <https://www.sequencer.de/yamaha/qy10.html>

# Korg SQ-64 Poly Sequencer

CV and MIDI brain that keeps the synth corner locked. This manual captures
global settings and performance recipes.

## Why it stays patched in

- Three melodic tracks (A/B/C) with pitch, gate, and mod outs plus a 16-channel
  drum lane to herd the Drumkid and S900.
- Deep probability, ratchet, and modulation per step without a screen maze.
- Syncs DAW, modular, and hardware samplers in one go.

## Setup defaults

- **Firmware**: Keep at v2.0 or newer. Update via MIDI SysEx with the official
  updater.
- **Clock source**: `GLOBAL` → `CLOCK SOURCE` = `INTERNAL` unless a DAW is the
  boss.
- **CV scaling**: `GLOBAL` → `CV CONFIG`. Tracks A and B = V/Oct, track C =
  V/Oct, MOD outs = 0–5 V for AE compatibility.
- **MIDI routing**: Track A → channel 1 (S900), track B → channel 2 (Volca
  Modular), track C → channel 3 (Electribe), drum track → channel 10.

Log routing changes below so nobody double-triggers gear mid-session.

## Performance playbook

- **Pattern chaining**: Hold `PATTERN` and press steps to queue. Use Scenes to
  store arrangements per project.
- **Probability sweeps**: Hold a step, turn encoder 1 to set probability, and
  encoder 2 for ratchets. Great for breathing life into the Kastle Drum clock.
- **MIDI CC**: Assign MOD outs to CC74 or CC71 for Electribe filter sweeps.
  Document CC maps in `data/midi/sq64-mapping.csv`.

## Troubleshooting

- **Hanging notes**: Send all-notes-off by holding `SHIFT` + `STOP`. If it keeps
  happening, reset MIDI filters.
- **Clock drift**: If the Drumkid is master, set SQ64 clock to `EXT` and ensure
  5 V pulses. Invert gates if AE modules misbehave.
- **Frozen UI**: Power cycle while holding `STOP` + `PLAY` to enter safe boot,
  then reload firmware.

## Maintenance log

| Date | Task | Notes |
| --- | --- | --- |
| yyyy-mm-dd | Firmware update | _v2.0 → v2.1, SysEx via MIDI-OX._ |
| yyyy-mm-dd | Encoder cleaning | _DeoxIT D5 light spray._ |

## References

- Owner’s manual: <https://www.korg.com/us/support/download/manual/0/857/0/>
- Firmware and editor: <https://www.korg.com/us/support/download/product/0/857/>
- Community tips: <https://llllllll.co/t/korg-sq-64/44638>

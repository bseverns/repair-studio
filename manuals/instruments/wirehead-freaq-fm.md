# Wirehead Instruments Freaq FM

Compact FM groovebox with a feedback loop that can melt polite sessions into
acidic drips. This card keeps it friendly for collaborators and brutal when we
want it.

## Why we keep it patched in

- Four-operator FM with hands-on macro controls, so we can morph from bells to
  snarls without menu fishing.
- Syncable sequencer with per-step probability keeps loops alive under busy
  hands.
- Stereo feedback bus doubles as an external input for tape decks or AE modular
  detours.

## Power + connections

- Power from the isolated 12 V DC brick labeled "Wirehead" in the pedal drawer.
  Current draw peaks near 600 mA—do not daisy-chain.
- MIDI in/out run over TRS Type A. Use the red adapters clipped to the case.
- Clock and reset on 3.5 mm jacks accept 5 V pulses. Tie to the SQ64 or Drumkid
  when locking the room to one tempo.
- Stereo outs on balanced 1/4". Keep levels conservative; the feedback bus can
  launch hot transients.

## Startup ritual

1. Verify the feedback knob is under noon before applying power. Saves the PA
   and anyone wearing headphones.
2. Power the unit, then hold `SHIFT` + `PLAY` for three seconds to load the
   "Studio Base" pattern bank.
3. Confirm `SYNC` LED status:
   - Solid = internal clock
   - Slow blink = awaiting external clock
   - Fast blink = clocking but no reset input
4. Dial in master tune using the tiny trimmer on the rear if pairing with the
   S900. Document offsets below.

## Performance recipes

- **Tape dub ghost**: Route Tascam send into the feedback return, set operator 4
  ratio to 0.50, engage `DRIVE` at 30%, and ride the delay time for smeared
  choirs.
- **Acid FM**: External clock from SQ64 track C, operator ratios 1.00/1.50/2.00
  with envelope loop enabled, filter cutoff at 2 kHz, resonance 70%, feedback
  1 o'clock.
- **Noise bed**: Kill the sequencer, hold `SHIFT` + `RND` to trigger drone mode,
  back off operator indexes to 10–20%, crank reverb send. Print to the
  Portastudio.

## Macro map cheat sheet

| Control | Default role | Notes |
| --- | --- | --- |
| Macro 1 | Operator index spread | Turn for mild to harsh textures. |
| Macro 2 | Feedback depth | Noon is safe; past 2 o'clock gets feral. |
| Macro 3 | Delay time | Quantized to 1/8 steps when clocked. |
| Macro 4 | Reverb size | Keep under 75% live to avoid mush. |

## Maintenance + spares

- Firmware lives at <https://wireheadinstruments.com/support/freaq-fm>. Mirror
  critical builds to `assets/firmware/freaq-fm/`.
- Spare encoder caps and TRS adapters share a bin with the Kastle rigs.
- If the feedback circuit screeches uncontrollably, recalibrate: power while
  holding `SHIFT` + `MACRO 2`, wait for the progress LEDs, then reboot.
- Log tuning offsets, repairs, and weird behaviors below.

## Session log

| Date | Pattern bank | Notes |
| --- | --- | --- |
| yyyy-mm-dd | Studio Base A | _Locked with SQ64, feedback tame._ |

## References

- Builder overview: <https://wireheadinstruments.com/freaq-fm>
- Community patch archive: <https://patchstorage.com/platform/freaq-fm>

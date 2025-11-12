# Koma Elektronik Field Kit FX

The glue box between modular chaos, tape decks, and the live room. Document
patches, feedback tricks, and maintenance here.

## Why it anchors the rig

- Six CV-ready effects—delay, frequency shifter, bit crusher, state-variable
  filter, digital reverb, spring tank driver—in one chassis.
- External CV routing turns the AE rack and SQ64 into macro controls.
- Built-in spring tank keeps us from hoarding vintage outboard.

## Power + safety

- Use the included 12 V DC supply (center-positive). Do **not** daisy-chain; a
  shared supply injects hum.
- Spring tank lives in the foam cradle behind the unit. Keep cables slack to
  avoid tearing the transducers.
- Before transport, unplug the spring tank RCAs and tape them to the tank body.

## Standard patch template

1. Input 1: Drumkid or Kastle Drum.
2. Input 2: AE Modular mix out.
3. Aux send: Portastudio aux 1 → return → Portastudio channels 3 and 4.
4. Use CV1 for delay time modulation and CV2 for filter sweeps.

Log deviations below so the next session knows what weirdness to expect.

## Feedback recipes

- **Dub wash**: Delay feedback at two o’clock, filter in BP mode, reverb mix at
  noon. Ride Input 1 gain for tape-style saturation.
- **Metallic drones**: Frequency shifter in fine mode, modulated by a slow
  triangle LFO from the AE rack. Patch spring tank return back into Input 2 for
  controlled howl.
- **Voltage mangler**: Route SQ64 CV into `CV IN` jacks to morph effects
  rhythmically. Document knob ranges that stay stable.

## Maintenance log

| Date | Task | Notes |
| --- | --- | --- |
| yyyy-mm-dd | Clean spring tank | _Dust and check for loose screws._ |
| yyyy-mm-dd | Firmware update | _Link release and changes._ |

## References

- Official manual: <https://koma-elektronik.com/?product=field-kit-fx>
- Firmware and schematics: <https://github.com/koma-elektronik/FieldKitFX>
- Community patch ideas: <https://llllllll.co/t/koma-field-kit-fx-patches>

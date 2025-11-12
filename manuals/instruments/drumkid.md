# Drumkid Drum Machine

Battery-friendly algorithmic drummer built for happy accidents. This crib sheet
keeps the chaos intentional.

## Why it rules the tabletop

- Generates evolving beats without menu diving; perfect companion for the
  Electribe or AE rack jams.
- Clock I/O means it can lead or follow the rig without drifting.
- Open hardware—hackable firmware if we feel like getting weird.

## Power + connections

- Runs off 3× AA or micro-USB. Keep rechargeables topped off in the charger
  dock.
- Clock input expects 5 V pulses. SQ64 `GATE` outs or Kastle Drum triggers work.
- Audio out is a stereo jack wired dual mono. Pan on the mixer for width if you
  care.

## Performance workflow

1. Hold `PLAY` while powering to access hidden config (swing depth, scale
   length). Document changes below.
2. Tap `PLAY/PAUSE` to start internal clock. External clock overrides
   automatically.
3. Use `SHIFT` plus knob twists to reach extended ranges. LEDs confirm alt mode.
4. `RND` adds variation; hold it while turning `CHAOS` to bias how wild it gets.

## Favorite settings log

| Date | Tempo / Mode | Knob positions | Notes |
| --- | --- | --- | --- |
| yyyy-mm-dd | 120 BPM, 4/4 | Chaos 10, Fill noon | _Tight for electro sets._ |

## Maintenance + firmware

- Latest release and source: <https://github.com/mattb0ne/drumkid>
- Spare knob caps and button tops live in `assets/hardware/drumkid/`.
- If the encoder skips, hit it with contact cleaner and log it here.

## Troubleshooting

- **No sound**: Check the mute toggles; they latch. Ensure batteries are above
  1.1 V each.
- **Clock jitter**: Use shielded 3.5 mm cables and keep them away from bricks.
- **Frozen UI**: Power cycle while holding `SHIFT` to load safe defaults.

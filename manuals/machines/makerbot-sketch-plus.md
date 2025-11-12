# MakerBot SKETCH Large (Sketch Plus)

The big-volume PLA mule for office projects. This doc keeps print prep, queue
etiquette, and maintenance tight.

## Why we run it

- 305 mm cube build volume handles fixtures the smaller Sketch cannot touch.
- Locked-down PLA workflow is perfect for loaner jobs and classroom demos.
- CloudPrint queueing keeps the team from fighting over USB sticks.

## Opening checklist

1. Power cycle if the touchscreen UI lags or CloudPrint loses connection.
2. Run the guided build plate leveling every Monday and after any head crash.
3. Vacuum the intake filter monthly; clogged filters cook the hotend.
4. Confirm spool weight above 100 g before large jobs to avoid mid-print swaps.

## Job workflow

- Slice in MakerBot CloudPrint with the SKETCH Large profile. Enable adaptive
  layer height for tall aesthetic parts.
- Use the built-in camera to verify first layer. Abort early if adhesion fails;
  note it in the print log.
- After printing, flex the magnetic plate while supporting large parts with your
  other hand to avoid warping.
- Log print success or failure plus material color in
  `data/prints/sketch-large-log.csv`.

## Filament crib

| Brand | Profile | Notes |
| --- | --- | --- |
| MakerBot PLA | Default | Keep sealed with desiccant. |
| Proto-pasta Matte | Generic PLA | Increase temp to 215 °C, slow to 40 mm/s. |

## Maintenance log

| Date | Task | Notes |
| --- | --- | --- |
| yyyy-mm-dd | Nozzle swap | _Installed spare Smart Extruder+._ |
| yyyy-mm-dd | Filter clean | _HEPA plus foam vacuumed._ |

## Troubleshooting

- **Under-extrusion**: Run the filament load wizard to purge. If still sparse,
  swap the extruder.
- **First-layer peel**: Clean bed with IPA, re-run leveling, add a 5 mm brim in
  the slicer.
- **CloudPrint offline**: Reboot printer, then re-auth via Digital Factory. If
  still dead, contact IT.

## References

- Hardware guide: <https://support.makerbot.com/s/article/1680268375201>
- Troubleshooting hub:
  <https://support.makerbot.com/s/topic/0TO6S000000CgqsWAC/sketch-series>
- CloudPrint tips: <https://support.makerbot.com/s/article/CloudPrint-Quick-Start>

# MakerBot Method X

Enclosed dual-extrusion printer for ABS/ASA/Nylon production runs. This sheet collects preflight rituals, material notes, and service history.

## Why it’s in the lab
- Heated chamber + soluble support = dimensionally stable functional parts.
- CloudPrint integration means we can queue jobs remotely and babysit via camera.
- Swappable performance extruders keep downtime low when someone cooks a nozzle.

## Daily preflight
1. Verify desiccant packs in bays A/B aren’t saturated. Replace or recharge if humidity >15% RH.
2. Run `Utilities → Calibrate` (XY, Z offset, build plate) every Monday or after any extruder swap.
3. Check purge chute — empty if the wiper pile touches the nozzle path.
4. Confirm material chips match the loaded spool type. The printer will error but don’t rely on it.

## Job workflow
- Slice in MakerBot CloudPrint using the Method X profile. Set chamber temp per material: ABS-R 65 °C, ASA 70 °C, Nylon 60 °C.
- Assign Model 1XA extruder for model material, Support 2XA for SR-30. Double-check extruder health in `Utilities → Printhead`.
- After completion, let chamber drop below 40 °C before opening the door to avoid warp shocks.
- Dissolve SR-30 in the ultrasonic wash tank (1:10 concentrate to water). Change solution every 10 parts or when cloudy.

## Material crib notes
| Material | Drying bake | Notes |
| --- | --- | --- |
| ABS-R | 60 °C for 4 h | Keep sealed between prints. |
| ASA | 70 °C for 6 h | Loves chamber door closed; avoid drafts. |
| Nylon 12 CF | 70 °C for 8 h | Abrasive — use reinforced extruder only. |

## Maintenance log
| Date | Task | Notes |
| --- | --- | --- |
| yyyy-mm-dd | Extruder swap | _Model 1XA → spare, clogged by carbon fiber._ |
| yyyy-mm-dd | Chamber filter change | _Part #375-0021A._ |

## Troubleshooting
- **Layer splits**: Check chamber temp and dry filament. Also inspect build plate magnets.
- **Extruder jams**: Run cold pull with cleaning filament at 100 °C. If still stuck, swap extruder and send the bad one for rebuild.
- **CloudPrint offline**: Power cycle the printer, then re-auth via Digital Factory. Note downtime in `policies/fabrication/uptime-log.md`.

## References
- Official hardware guide: <https://support.makerbot.com/s/article/1667337554221>
- Material compatibility chart: <https://support.makerbot.com/s/article/1667337554211>
- Service bulletins: <https://support.makerbot.com/s/topic/0TO6S000000CgqsWAC/method-series>

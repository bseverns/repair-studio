# MakerBot SKETCH 3D Printer

Baseline education printer that cranks through PLA prototypes all week. This crib sheet covers start-of-shift checks, job flow, and upkeep.

## Why we keep it spinning
- Reliable PLA machine for quick fixtures and proof-of-concept prints.
- Locked profiles mean interns and guests can queue safely via CloudPrint.
- Compact footprint makes it the go-to for overnight jobs that don’t need the Method X.

## Morning checklist
1. Power on, then run `Utilities → Build Plate Leveling`. Record any Z-offset tweaks in the log below.
2. Inspect nozzle for filament fuzz. Trim filament end at 45° before loading.
3. Wipe build plate with 70% IPA if adhesion was questionable last print.
4. Confirm CloudPrint status shows online; if not, reboot printer and router.

## Job workflow
- Slice in MakerBot CloudPrint using the SKETCH profile. For small detailed parts, drop layer height to 0.16 mm.
- Send to queue `SKETCH-01` or `SKETCH-02` (label matches printer sticker). Add project code in job notes.
- Watch first layer via camera or in-person; abort early if the raft lifts.
- After print, flex the bed, remove raft, and file results in `data/prints/sketch-log.csv`.

## Filament + spares
| Item | Location | Notes |
| --- | --- | --- |
| MakerBot PLA spools | Cabinet row A | Keep silica gel fresh. |
| Smart Extruder+ spare | Drawer B1 | Run break-in calibration before first job. |
| Build plates | Drawer B2 | Swap if PEI is gouged. |

## Maintenance log
| Date | Task | Notes |
| --- | --- | --- |
| yyyy-mm-dd | Z-offset adjust | _+0.05 mm after nozzle swap._ |
| yyyy-mm-dd | Firmware update | _v2.6.0 via USB._ |

## Troubleshooting
- **Grinding / clicking**: Unload filament, trim, reload. If persistent, inspect the drive gear for debris.
- **Stringing**: Increase retraction to 1.5 mm in CloudPrint custom settings; dry filament overnight.
- **Touchscreen freeze**: Hold power for 10 seconds, reboot. If it repeats, contact MakerBot support with log dump.

## References
- User manual: <https://support.makerbot.com/s/article/1680268375190>
- Maintenance schedule: <https://support.makerbot.com/s/article/1680268375161>
- CloudPrint quick start: <https://support.makerbot.com/s/article/CloudPrint-Quick-Start>

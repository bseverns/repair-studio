# Ultimaker Cura (Personal Rig)

Open-source slicer we use for non-MakerBot jobs. Treat this doc as the profile + workflow playbook.

## Why we rely on it
- Handles third-party printers (Prusa, Voron, modded Ender) that the office fleet won’t touch.
- Plugin ecosystem adds custom post-processing and OctoPrint integration.
- Easy to stash per-project profiles alongside STL source in this repo.

## Setup + profiles
- Install from <https://ultimaker.com/software/ultimaker-cura>. Log version bumps below.
- Export tuned profiles to `manuals/software/cura/profiles/` (text placeholders until we commit the actual `.curaprofile`). Include printer name + nozzle size in filename.
- Enable the `Auto Orientation` and `Cura Measure Tool` plugins from the Marketplace for sanity.

## Workflow snapshot
1. Import STL/STEP. Run `Prepare` preview with layer view to catch weird thin walls.
2. Select the correct profile (e.g. `Voron24_0.4mm_draft`). Adjust layer height + infill based on project needs.
3. Use tree supports only for organic shapes. Disable for MakerBot-targeted parts — CloudPrint handles those separately.
4. Preview for estimated time/material, then export G-code to SD or send to OctoPrint.

## QA checklist before exporting
- Wall thickness ≥ nozzle diameter? If not, add modifiers or redesign.
- Overhang >50°? Add supports or reorient.
- Check build volume matches target printer. Cura will warn, but trust your eyeballs too.

## Maintenance log
| Date | Cura version | Notes |
| --- | --- | --- |
| yyyy-mm-dd | 5.5.0 | _Installed tree support plug-in._ |
| yyyy-mm-dd | 5.6.1 | _Updated Voron profile._ |

## References
- Release notes: <https://github.com/Ultimaker/Cura/releases>
- Profile tuning guide: <https://support.makerbot.com/s/article/Ultimaker-Cura-Quick-Start>
- Voron print tuning bible: <https://docs.vorondesign.com/community/howto/common_print_tuning.html>

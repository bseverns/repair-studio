# Korg Electribe 2S (Sampler)

Sequencer brain for the portable rig. This guide keeps pattern management and backups sane.

## Why it earns desk space
- 24-voice polyphony (realistically 16 with FX) across 16 parts for quick beat sketches.
- Motion sequencing + per-part FX pairs well with the Method X when you need synced stems fast.
- Battery or DC powered, so it can live on-location with the Portastudio or in the office lab.

## Power + storage
- Power via included 9 V DC adapter or 6× AA NiMH cells. Swap in fresh cells before off-site sessions.
- SD card (≤32 GB, FAT32) lives in the rear slot. Back it up monthly to `data/backups/electribe2s/`.
- Keep firmware at 2.02. Check under `GLOBAL` → `FIRMWARE` and update via SD if needed.

## Session workflow
1. Load current project: `MENU` → `DATA UTILITY` → `Load` → pick project slug (match `projects/` naming scheme).
2. Prep tracks: `SHIFT` + pad to mute/unmute; hold `REC` while twisting knobs to capture motion.
3. For live resampling, route audio out to the S900 or Portastudio, sample, then re-import via SD.
4. Export stems: `MENU` → `EXPORT AUDIO`. Drop resulting WAVs into `data/prints/audio/<date>-<project>`.

## Performance tips
- Assign `IFX` carefully. Reverbs are global hogs; use per-part delays and route global reverb sparingly.
- Use the `Step Jump` button for fills. Practice with Drumkid clock to stay tight.
- When chaining patterns, set `Pattern Set` entries in advance so you’re not menu diving mid-set.

## Maintenance + backups
- Clean pads with 70% IPA + microfiber. Avoid solvents.
- Keep spare encoder caps in `assets/hardware/electribe/`.
- Log exports and firmware updates in the table below.

| Date | Action | Notes |
| --- | --- | --- |
| yyyy-mm-dd | Firmware check | _Still on 2.02_ |
| yyyy-mm-dd | Project backup | _Backed up “modular-jams”_ |

## References
- Owner’s manual + parameter guide: <https://www.korg.com/us/support/download/manual/0/516/2675/>
- Firmware + editor utilities: <https://www.korg.com/us/support/download/product/0/516/>
- Community pattern packs: <https://www.facebook.com/groups/electribers/>

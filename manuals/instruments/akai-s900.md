# Akai S900 Sampler

12-bit workhorse for crunchy drums, resampled synth stabs, and sonic vandalism.
Respect the disks and it will boot every time.

## Why we keep it

- Classic Akai envelopes and filters glue drum machines to the tape deck without
  a DAW in sight.
- Keygroup workflow plays nice with the SQ64 and QY10 when you want multi-part
  stacks.
- Hardware sampling keeps latency nonexistent for live looping with the
  Portastudio.

## Boot + disk discipline

1. **Insert the OS disk first.** The drive will not load the OS after power-on
   if the disk is missing.
2. Flip power, wait for the "AKAI S900" splash to clear, then load the working
   template (`DISK` → `LOAD PROGRAM` → pick your default disk volume).
3. When sampling, set input source to `LINE` and watch the VU. Aim for -6 dBFS
   peaks to dodge the nasty clipping that is not the nice kind of grit.
4. After sessions, `SAVE ALL` to a labeled disk. Note project, BPM, and any
   tuning offsets on the sleeve.

> Keep one write-protected master disk with a clean OS and empty programs. Clone
> it when things get weird.

## Sampling workflow cheatsheet

- **Resample from tape**: Route Portastudio bus to the S900 input, set threshold
  just below average level, and use `PRE-TRIGGER` if you need transient capture.
- **Keygroup template**: Default to key span C1–C3 for drums and C3–C6 for
  melodic programs. Log your go-to layout here.
- **Looping**: Use `FINE` and `X-FADE` to soften loop clicks. Document good loop
  points in `data/samples/s900-notes.md`.

## Maintenance + spare parts

- Keep double-density (720 KB) floppies in an airtight box. Bake stubborn disks
  at 50 °C for two hours if they shed oxide.
- Display backlight: 240×64 EL panel with 5 V inverter. Replacement kit:
  <https://www.backlight4you.com/lcd-backlight-240x64-EL>.
- Recap BOM lives in `data/parts/akai-s900-recap.csv`. Update it after any
  service.

## Troubleshooting quick hits

- **Drive will not read**: Clean heads with 99% IPA and a chamois. If still
  broken, swap in the spare PC floppy drive (document jumper settings!).
- **Noise on outputs**: Check PSU rails; 5 V should sit at 4.98–5.05 V. Reflow
  the output board headers if wiggling fixes it.
- **MIDI chaos**: The QY10 loves to spew clock. Set receive channel under
  `MIDI` → `RECV CH` to stop stray triggers.

## References

- Owner’s manual: <https://cdn.inmusicbrands.com/akai/legacy/S900_Manual.pdf>
- Service manual:
  <https://elektrotanya.com/akai_s-900_service_manual.pdf/download.html>
- Sample disks archive: <https://archive.org/details/akai-s900-s950-s1000-library>

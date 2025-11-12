# Bastl Kastl / Kastle / Microgranny Field Notes

Pocket-sized chaos machines that travel with the modular rig. Keep this sheet up to date as you mod or patch-stack them.

## Fleet inventory
| Unit | Power | Typical Patch Role | Mods / Notes |
| --- | --- | --- | --- |
| Kastl 1.5 | 3× AA or USB | Drone voice / modulation source | _(log firmware tweaks, tuning drift, favorite patch combos)_ |
| Kastle Drum | 3× AA or USB | Clocked percussion, trigger generator | _(note clock divisions, sync tricks)_ |
| Kastl FX Wizard | USB only | Send/return hub, modulation mangler | _(document preferred gain staging)_ |
| Microgranny 2.5 | USB (5V clean) | Granular sampler, texture bed | _(list SD card kits + loop points)_ |

## Power + cabling sanity
- Run the Kastle trio off isolated USB banks when tied to the AE rack. They’ll happily share 5V, but ground loops will make them hiss.
- Microgranny hates noisy chargers. Use the filtered USB wall wart from the interface drawer.
- Patch cables: 3.5 mm stackables live in the orange pouch. Replace frayed ones ASAP.

## Workflow sparks
- **Sync chain**: Drumkid clock → Kastle Drum CLK IN → Kastl 1.5 LFO reset → AE Modular clock. Keeps the whole table breathing together.
- **Microgranny sample prep**: Convert WAVs to 22050 Hz, 8-bit mono. Store kits on SD as `kit01`, `kit02`, etc. Document kits in `data/samples/microgranny-index.csv`.
- **FX Wizard send**: Route Portastudio aux send → FX Wizard → Field Kit FX return for filthy feedback loops. Keep gain under 3 o’clock or it screams.

## Maintenance + spare bits
- Stash spare patch cables, SD cards, and AA cells in the instrument crate. Log swaps here.
- Firmware + docs: <https://bastl-instruments.com/support>
- Microgranny encoder replacements: <https://www.thonk.co.uk/shop/microgranny-encoder/>

## Session log
| Date | Rig combo | Notes / discoveries |
| --- | --- | --- |
| yyyy-mm-dd | Kastle Drum + AE clock | _e.g. documented polyrhythm patch_ |
| yyyy-mm-dd | Microgranny tape resample | _note sample rate + vibe_ |

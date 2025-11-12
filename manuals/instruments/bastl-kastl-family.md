# Bastl Kastl / Kastle / Microgranny Field Notes

Pocket-sized chaos machines that travel with the modular rig. Keep this sheet up
to date as you mod or patch-stack them.

## Fleet inventory

| Unit | Power | Typical Patch Role | Mods / Notes |
| --- | --- | --- | --- |
| Kastl 1.5 | 3× AA or USB | Drone voice + mod hub | _FW tweaks + stacks._ |
| Kastle Drum | 3× AA or USB | Clocked perc + triggers | _Sync tricks._ |
| Kastl FX Wizard | USB only | Send/return + mod | _Gain + loops._ |
| Microgranny 2.5 | Clean 5 V USB | Granular + textures | _SD kits + loops._ |

## Power + cabling sanity

- Run the Kastle trio off isolated USB banks when tied to the AE rack. They
  share 5 V happily, but ground loops will hiss.
- Microgranny hates noisy chargers. Use the filtered USB wall wart from the
  interface drawer.
- Patch cables: 3.5 mm stackables live in the orange pouch. Replace frayed ones
  ASAP.

## Workflow sparks

- **Sync chain**: Drumkid clock → Kastle Drum CLK IN → Kastl 1.5 LFO reset → AE
  Modular clock. Keeps the whole table breathing together.
- **Microgranny sample prep**: Convert WAVs to 22050 Hz, 8-bit mono. Store kits
  on SD as `kit01`, `kit02`, etc. Document kits in
  `data/samples/microgranny-index.csv`.
- **FX Wizard send**: Route Portastudio aux send → FX Wizard → Field Kit FX
  return for filthy feedback loops. Keep gain under three o’clock or it screams.

## Maintenance + spare bits

- Stash spare patch cables, SD cards, and AA cells in the instrument crate. Log
  swaps here.
- Firmware and docs: <https://bastl-instruments.com/support>
- Microgranny encoder replacements:
  <https://www.thonk.co.uk/shop/microgranny-encoder/>

## Session log

| Date | Rig combo | Notes / discoveries |
| --- | --- | --- |
| yyyy-mm-dd | Kastle Drum + AE clock | _Document polyrhythm patch._ |
| yyyy-mm-dd | Microgranny tape resample | _Note sample rate and vibe._ |

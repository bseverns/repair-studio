# AE Modular Rack

Semi-modular nerve center for experiments, generative sets, and Portastudio
grit. Treat this doc like the living lab notebook for the case.

## Why we keep it

- Compact 5 V ecosystem that patches straight into the Koma Field Kit FX and
  Kastle boxes without frying anything.
- Swappable voice architecture that flips between drones, clocked techno, or
  control-voltage utility duty in minutes.
- Perfect sandbox for testing SQ64 sequences before porting patches to bigger
  studio rigs.

## Current module roster

| Position | Module | Role / Notes |
| --- | --- | --- |
| 01 | _(slot name)_ | _(log the actual module and firmware rev)_ |
| 02 |  |  |
| 03 |  |  |
| ... |  |  |

> Update the roster whenever you swap cards. Include calibration offsets or
> custom firmware links.

## Power + health check

- **PSU**: Tangible Waves 1000 mA brick. Keep a spare in `assets/power/` and
  note voltage sag if you daisy-chain.
- **Boot ritual**:
  1. Flip the rear master switch while watching the BUS LED. Solid red is good;
     flicker means reseat the ribbon or check PSU draw.
  2. Wiggle the patchwire bundle to spot intermittent jacks before a session.
  3. Let digital oscillators idle for five minutes before precision tuning.
- **Noise floor**: If the rack hums, lift grounds via the Field Kit FX isolator
  or power from a battery bank.

## Patch recipes to steal

- **Clock HQ**: SQ64 Track D trigger → master `CLK IN`. Patch `CLK OUT` to
  sequencers or Drumkid sync.
- **Drone wall**: 2OSC/d → Wasp Filter → Spring Tank (Field Kit FX) →
  Portastudio channels 3 and 4. Add a slow LFO from `2VCA` for motion.
- **Control nerve**: Route the `4ATT/MIX` as a CV hub to tame Kastle output
  before re-feeding the rack.

Log discoveries here. Keep it scrappy but readable.

## Maintenance log

| Date | Task | Notes |
| --- | --- | --- |
| yyyy-mm-dd | Clean patch wires | _IPA wipe; replace cracked tips._ |
| yyyy-mm-dd | Module swap | _Describe what moved where._ |

## References

- Tangible Waves manual hub: <https://www.tangiblewaves.com/manuals>
- AE Modular community wiki (module calibration, DIY mods):
  <https://wiki.aemodular.com/pmwiki.php>
- Forum troubleshooting megathread: <https://forum.aemodular.com/>

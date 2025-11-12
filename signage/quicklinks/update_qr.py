#!/usr/bin/env python3
"""Regenerate QR codes for manual quick links.

Edit the `LINKS` map as our intranet slugs evolve, then run:

    python3 signage/quicklinks/update_qr.py

The script overwrites PNGs in-place. Generated files are gitignored.
"""

from pathlib import Path

import qrcode

BASE = "https://fieldkit.local/manuals"
LINKS = {
    "manuals-index": f"{BASE}/INDEX.html",
    # Machines
    "makerbot-method-x": f"{BASE}/machines/makerbot-method-x.html",
    "makerbot-sketch": f"{BASE}/machines/makerbot-sketch.html",
    "makerbot-sketch-plus": f"{BASE}/machines/makerbot-sketch-plus.html",
    # Software
    "makerbot-digital-factory": f"{BASE}/software/makerbot-digital-factory.html",
    "cura": f"{BASE}/software/cura.html",
    # Instruments
    "ae-modular-rack": f"{BASE}/instruments/ae-modular-rack.html",
    "akai-s900": f"{BASE}/instruments/akai-s900.html",
    "bastl-kastl-family": f"{BASE}/instruments/bastl-kastl-family.html",
    "drumkid": f"{BASE}/instruments/drumkid.html",
    "koma-field-kit-fx": f"{BASE}/instruments/koma-field-kit-fx.html",
    "korg-electribe-2s": f"{BASE}/instruments/korg-electribe-2s.html",
    "korg-sq64": f"{BASE}/instruments/korg-sq64.html",
    "korg-volca-modular": f"{BASE}/instruments/korg-volca-modular.html",
    "tascam-404-portastudio": f"{BASE}/instruments/tascam-404-portastudio.html",
    "yamaha-qy10": f"{BASE}/instruments/yamaha-qy10.html",
    # Spaces
    "audio-recording-studio": f"{BASE}/spaces/audio-recording-studio.html",
}


def main() -> None:
    out_dir = Path(__file__).parent
    for slug, url in LINKS.items():
        img = qrcode.make(url)
        path = out_dir / f"{slug}.png"
        img.save(path)
        print(f"Wrote {path} -> {url}")


if __name__ == "__main__":
    main()

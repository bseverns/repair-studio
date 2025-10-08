#!/usr/bin/env python3
import os, pathlib

root = pathlib.Path('manuals')
index = root / 'INDEX.md'
lines = ['# Manuals Index\n']

for base, dirs, files in os.walk(root):
    rel = pathlib.Path(base).relative_to(root)
    if rel == pathlib.Path('.'):
        header = 'Root'
    else:
        header = str(rel)
    md_files = [f for f in files if not f.startswith('.')]
    if md_files:
        lines.append(f"## {header}\n")
        for f in sorted(md_files):
            p = pathlib.Path(base) / f
            relp = p.relative_to(root).as_posix()
            lines.append(f"- [{relp}]({relp})")
        lines.append("")
index.parent.mkdir(parents=True, exist_ok=True)
index.write_text("\n".join(lines), encoding='utf-8')
print(f"Wrote {index}")

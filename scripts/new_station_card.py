#!/usr/bin/env python3
import sys, os, textwrap

TEMPLATE = '''---
title: "{title}"
goal: "{goal}"
timebox: "30–60 min"
risk: "low"
done_definition:
  - "{done}"
---

## Steps
1) 
2) 
3) 

## Evidence
- before/after
- measurements/logs
- docs link
'''

def main():
    if len(sys.argv) < 3:
        print("Usage: new_station_card.py "Title" "Goal" [done_definition]")
        sys.exit(1)
    title = sys.argv[1]
    goal = sys.argv[2]
    done = sys.argv[3] if len(sys.argv) > 3 else "Another person can continue without you"
    slug = title.lower().replace(' ', '-')
    path = os.path.join('station-cards', f"{slug}.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(TEMPLATE.format(title=title, goal=goal, done=done))
    print(f"Created {path}")

if __name__ == "__main__":
    main()

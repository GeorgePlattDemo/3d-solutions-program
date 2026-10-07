"""Checks relative Markdown file destinations.
Does not validate anchors, external links, source claims,
runtime behavior, or physical capability.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
errors = []
checked = 0

for path in ROOT.rglob("*.md"):
    if ".git" in path.parts:
        continue
    for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
        if target.startswith(("https://", "http://", "mailto:", "#")):
            continue
        local = (path.parent / target.split("#")[0]).resolve()
        checked += 1
        if not local.is_relative_to(ROOT) or not local.exists():
            errors.append(f"{path.relative_to(ROOT)}: missing/outside local link {target}")

if errors:
    raise SystemExit("\n".join(errors))
print(f"PASS: {checked} local Markdown links")

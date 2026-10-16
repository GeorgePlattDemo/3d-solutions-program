"""Checks relative Markdown files, headings and the approved root README freeze.
Does not validate external links, source claims,
runtime behavior, or physical capability.
"""
from pathlib import Path
import re
import hashlib
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
errors = []
checked = 0

def anchors(text):
    counts, result = {}, set()
    text = re.sub(r"^```[^\n]*\n.*?^```[^\n]*$", "", text, flags=re.M|re.S)
    for title in re.findall(r"^#{1,6} (.+)$", text, re.M):
        base = re.sub(r"[^\w -]", "", title.lower()).replace(" ", "-")
        n = counts.get(base, 0)
        result.add(base + (f"-{n}" if n else ""))
        counts[base] = n + 1
    return result

readme = (ROOT / "README.md").read_bytes()
assert hashlib.sha1(f"blob {len(readme)}\0".encode() + readme).hexdigest() == "7bcaa680eca4007c1081400491b202d732c546f5", "Root README freeze violated"


for path in ROOT.rglob("*.md"):
    if ".git" in path.parts:
        continue
    for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
        if target.startswith(("https://", "http://", "mailto:")):
            continue
        target = unquote(target)
        file, _, anchor = target.partition("#")
        local = (path.parent / file).resolve() if file else path
        checked += 1
        if not local.is_relative_to(ROOT) or not local.exists():
            errors.append(f"{path.relative_to(ROOT)}: missing/outside local link {target}")
        elif anchor and local.suffix == ".md" and anchor not in anchors(local.read_text(encoding="utf-8")):
            errors.append(f"{path.relative_to(ROOT)}: missing heading {target}")

if errors:
    raise SystemExit("\n".join(errors))
print(f"PASS: {checked} local Markdown files/headings; root README frozen")

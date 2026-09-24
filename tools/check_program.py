"""Documentary consistency only; not capability, disclosure or deployment approval."""
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
errors = []
sha = re.compile(r'^[0-9a-f]{40}$')

for path in ROOT.rglob('*.md'):
    if '.git' in path.parts:
        continue
    for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
        if target.startswith(('https://', 'http://', 'mailto:', '#')):
            continue
        local = (path.parent / target.split('#')[0]).resolve()
        if not local.is_relative_to(ROOT) or not local.exists():
            errors.append(f'{path.relative_to(ROOT)}: missing/outside local link {target}')

inventory = json.loads((ROOT / 'migration/source-inventory.json').read_text())
for row in inventory['entries']:
    if not sha.fullmatch(row['sourceCommit']) or not sha.fullmatch(row['blob']):
        errors.append(f'invalid source identity: {row["path"]}')
    if row['disposition'] not in {'exact-copy-in-system', 'review-required'}:
        errors.append(f'unreviewed disposition transition: {row["path"]}')
    if row['disposition'] == 'exact-copy-in-system' and not row['existingCopies']:
        errors.append(f'duplicate without destination: {row["path"]}')

for row in inventory['branchUnique']:
    if not sha.fullmatch(row['commit']) or not sha.fullmatch(row['blob']):
        errors.append(f'invalid branch identity: {row["path"]}')

for row in json.loads((ROOT / 'migration/admissions.json').read_text())['admissions']:
    destination = ROOT / row['destinationPath']
    if not destination.exists():
        errors.append(f'missing admission: {row["destinationPath"]}')
        continue
    data = destination.read_text().replace(
        '(https://github.com/GeorgePlattDemo/scan-to-build-review/blob/'
        + row['sourceCommit'] + '/docs/01-From-Definition-to-Handoff.md)',
        '(01-From-Definition-to-Handoff.md)')
    # apply_patch normalizes a terminal newline; source API may omit it.
    candidates = {data.encode(), data.removesuffix('\n').encode()}
    identities = {hashlib.sha1(b'blob ' + str(len(v)).encode() + b'\0' + v).hexdigest() for v in candidates}
    if row['sourceBlob'] not in identities:
        errors.append(f'admission differs beyond recorded link/newline normalization: {row["destinationPath"]}')

if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: local links, {len(inventory["entries"])} inventory records, '
      f'{len(inventory["branchUnique"])} branch records, and research admission identity')

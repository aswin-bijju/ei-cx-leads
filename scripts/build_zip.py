"""Pack the ei-cx-leads skill into site/ei-cx-leads.zip for upload to Claude (claude.ai or desktop).

Zip paths use forward slashes and sit under one top folder, ei-cx-leads/, which is what skill
upload expects. The repo's LICENSE goes in as ei-cx-leads/LICENSE so the terms travel with
every copy. Run from anywhere: python scripts/build_zip.py
"""
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "ei-cx-leads"
LICENSE = ROOT / "LICENSE"
OUT = ROOT / "site" / "ei-cx-leads.zip"


def main():
    for required in (SKILL / "SKILL.md", LICENSE):
        if not required.is_file():
            raise SystemExit(f"missing {required}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    entries = [(p, "ei-cx-leads/" + p.relative_to(SKILL).as_posix())
               for p in sorted(SKILL.rglob("*")) if p.is_file()]
    entries.append((LICENSE, "ei-cx-leads/LICENSE"))
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zf:
        for src, arc in entries:
            zf.write(src, arc)
    print(f"wrote {OUT} ({len(entries)} files, {OUT.stat().st_size:,} bytes)")
    for _, arc in entries:
        print("  " + arc)


if __name__ == "__main__":
    main()

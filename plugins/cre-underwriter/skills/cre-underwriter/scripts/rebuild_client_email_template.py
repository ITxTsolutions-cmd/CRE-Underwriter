#!/usr/bin/env python3
from pathlib import Path
import base64

ROOT = Path(__file__).resolve().parents[1]
CHUNKS = ROOT / "assets" / "client-email-template"
OUTPUT = ROOT / "assets" / "03_CLIENT_EMAIL_DRAFT_TEMPLATE.docx"

def main():
    parts = []
    for path in sorted(CHUNKS.glob("chunk_*.b64")):
        parts.append(path.read_text(encoding="utf-8").strip())
    if not parts:
        raise SystemExit("Client email template chunks are missing.")
    OUTPUT.write_bytes(base64.b64decode("".join(parts)))
    print(OUTPUT)

if __name__ == "__main__":
    main()

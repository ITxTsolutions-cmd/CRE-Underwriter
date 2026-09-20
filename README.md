# CRE-Underwriter

Private, version-controlled CRE underwriting operating system and execution package.

## Production authority

The plugin is intentionally thin. The packaged operating-system files remain the authoritative source of behavior:

- `plugins/cre-underwriter/skills/cre-underwriter/references/01_MASTER_OPERATING_SYSTEM.md` - underwriting, workflow, continuity, and client communication authority.
- `plugins/cre-underwriter/skills/cre-underwriter/references/02_LOAN_CALCULATOR.md` - calculator authority.
- `plugins/cre-underwriter/skills/cre-underwriter/assets/client-email-template/chunk_*.b64` - lossless storage of the exact Client Email Draft Word template. `scripts/rebuild_client_email_template.py` reconstructs `assets/03_CLIENT_EMAIL_DRAFT_TEMPLATE.docx` byte-for-byte before use.

The skill entrypoint instructs ChatGPT to load and apply those authorities rather than maintaining a second copy of the underwriting rules.

## Version

Current plugin version: `10.4.2`

## Change control

Update the authoritative files in GitHub, commit the change, and then sync the imported marketplace in ChatGPT. Do not duplicate operating-system rules in the plugin manifest or README.

## Client Email Typography

Generated Client Email Draft Word files are normalized before delivery so all visible text uses Georgia. Opening and closing narrative paragraphs are regular, section headings are bold, and required inline bold issue/risk/inconsistency labels remain bold. The closing is explicitly reset to a normal left-aligned body paragraph with no bullet/numbering or inherited hanging/list indentation. The formatting pass preserves the approved fixed template layout.

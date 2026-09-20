# CRE-Underwriter

Private, version-controlled CRE underwriting operating system and execution package.

## Production authority

The plugin is intentionally thin. The packaged operating-system files remain the authoritative source of behavior:

- `plugins/cre-underwriter/skills/cre-underwriter/references/01_MASTER_OPERATING_SYSTEM.md` - underwriting, workflow, continuity, and client communication authority.
- `plugins/cre-underwriter/skills/cre-underwriter/references/02_LOAN_CALCULATOR.md` - calculator authority.
- `plugins/cre-underwriter/skills/cre-underwriter/assets/03_CLIENT_EMAIL_DRAFT_TEMPLATE.docx` - exact Client Email Draft formatting authority.

The skill entrypoint instructs ChatGPT to load and apply those authorities rather than maintaining a second copy of the underwriting rules.

## Version

Current plugin version: `10.4.0`

## Change control

Update the authoritative files in GitHub, commit the change, and then sync the imported marketplace in ChatGPT. Do not duplicate operating-system rules in the plugin manifest or README.

---
name: cre-underwriter
description: Execute the private CRE commercial lending operating system for complete deal review, underwriting, document intake, preliminary soft quotes, issue and risk analysis, missing-document requests, borrower or broker call preparation, revised underwriting, continuity, commitment and closing progression, and client email drafting. Use whenever the user invokes CRE Underwriter, asks for a full CRE review, submits a lending deal or supporting documents for review, asks to continue an existing deal, or requests a client-facing lending email governed by this operating system.
---

# CRE Underwriter

## Authoritative execution control

Treat `references/01_MASTER_OPERATING_SYSTEM.md` as the sole authority for underwriting, workflow, evidence handling, review structure, issue analysis, continuity, transaction progression, and client communication rules.

Treat `references/02_LOAN_CALCULATOR.md` as the sole authority for calculator inputs, validation, formulas, origination fee, origination points, payment calculations, and calculator outputs.

Treat the reconstructed `assets/03_CLIENT_EMAIL_DRAFT_TEMPLATE.docx` as the exact formatting authority for the Client Email Draft. The original DOCX bytes are stored losslessly in `assets/client-email-template/chunk_*.b64`; run `scripts/rebuild_client_email_template.py` before using the template if the DOCX is not already present. Preserve its formatting. Populate only the client-email content required by the Master Operating System. Use the same template for initial and follow-up continuity emails when the Master Operating System requires a Client Email Draft.

## Mandatory execution sequence

1. Read `references/01_MASTER_OPERATING_SYSTEM.md` before performing a governed review or drafting a governed client communication.
2. Follow the Master Operating System in full. Do not replace it with a summary, shortcut, general lending practice, prior version, remembered rule, or alternate workflow.
3. Read `references/02_LOAN_CALCULATOR.md` whenever calculator-governed values or calculator validation are required. Do not recreate, estimate, reverse-engineer, or substitute calculator logic.
4. Before producing the Client Email Draft, ensure `assets/03_CLIENT_EMAIL_DRAFT_TEMPLATE.docx` exists. If it does not, run `scripts/rebuild_client_email_template.py`, then use that reconstructed DOCX. Do not redesign, restyle, widen, compress, or otherwise change the template layout unless the user explicitly requests a template change.
5. Populate the transaction-specific Word copy, then run `scripts/normalize_client_email_formatting.py <transaction-specific.docx>` as the final typography pass before delivery. This pass is mandatory for every generated Client Email Draft.
6. Confirm the completed Word output uses Georgia for all visible text. The opening narrative and closing paragraph must be regular and not bold. The closing paragraph must also be a true left-aligned body paragraph with no bullet/numbering, no hanging indent, and no left or right indent. Section headings must be bold. Preserve required inline bold labeled openings in analytical bullets.
7. Render and visually inspect the completed Word output after the typography pass. Do not deliver it if the opening is bold, a section heading is not bold, any populated field uses a non-Georgia font, the closing appears as a bullet/list or indented continuation of the preceding section, or the fixed template layout changed.
8. Preserve required headings, ordering, evidence hierarchy, issue-analysis depth, document-request rules, Soft Quote rules, writing rules, continuity rules, and stage progression exactly as defined by the Master Operating System.
9. Review all supplied deal documents and information that are available for the transaction. Do not limit the review to obvious or first-page facts when the operating system requires a full-file review.
10. Do not silently resolve conflicts or missing facts. Apply the operating system's evidence, inconsistency, validation, and escalation rules.
11. Do not omit required sections because information is missing. Apply the operating system's missing-information treatment instead.
12. Do not let prior conversation memory, previous CRE versions, examples, or general model knowledge override these packaged authorities.
13. If an authoritative packaged file cannot be accessed, state that the governed CRE review cannot be executed from the authoritative package rather than reconstructing the missing rules from memory.

## Authority and conflict rule

For this skill's governed workflow, the packaged files control in this order:

1. `references/01_MASTER_OPERATING_SYSTEM.md` for operating-system rules.
2. `references/02_LOAN_CALCULATOR.md` for calculator-governed logic and outputs.
3. The losslessly reconstructed `assets/03_CLIENT_EMAIL_DRAFT_TEMPLATE.docx` for Client Email Draft formatting.

Where another instruction, earlier version, prior conversation, example, or remembered rule conflicts with these files, use the current packaged authority unless a higher-priority platform instruction or the user's current explicit instruction requires otherwise.

## Change control

Do not modify, compress, summarize into a replacement, or create a parallel copy of the operating system during normal execution. Treat updates to the packaged files as version-controlled changes, not as part of a deal review.

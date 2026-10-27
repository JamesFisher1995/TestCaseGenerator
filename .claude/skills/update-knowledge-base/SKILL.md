---
name: update-knowledge-base
description: Add to or correct the application knowledge base (screens, flows, fields, rules, roles, test data). Use when the user explains how part of the app works, answers a KB GAP, or shares screenshots/docs of the application.
argument-hint: <description of how something works, screenshots, or answers to KB gaps>
---

# Update the knowledge base

Input: $ARGUMENTS

1. Work out what kind of knowledge this is and where it belongs:
   - A whole feature/screen → `knowledge-base/features/<feature-name>.md` (copy `knowledge-base/features/_TEMPLATE.md`)
   - A reusable step-by-step journey (login, create customer…) → `knowledge-base/flows/<flow-name>.md` (copy `flows/_TEMPLATE.md`)
   - Menus / where screens live → `navigation.md`
   - Roles and who can do what → `roles-and-permissions.md`
   - Validation limits, calculations, statuses → `business-rules.md`
   - Accounts, sample records, environments → `test-data.md`
   - Quirks, known bugs, timing issues → `known-gotchas.md`
   - Terms and abbreviations → `glossary.md`
2. Read the target file first. Edit the relevant section rather than appending duplicates.
   If the new info contradicts what's there, replace it and mention the change to the user.
3. If screenshots are given, transcribe exact labels, button text, field names, and messages.
4. Record only what the user told you or what you saw — don't fill in blanks with assumptions.
   Leave `TODO:` markers for anything still unknown.
5. Search `output/*/test-cases.md` for `[KB GAP` entries this new knowledge answers, and tell the user
   which ones are now resolved (offer to regenerate those test cases).
6. Summarise what you added/changed and in which files.

Never put real passwords or secrets in the knowledge base — reference where testers get them instead
(e.g. "password in the team vault under 'UAT Admin'").

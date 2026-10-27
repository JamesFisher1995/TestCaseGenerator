---
name: generate-test-cases
description: Generate manual test cases from a Jira ticket using the application knowledge base. Use when the user pastes Jira ticket content (or a Jira key / ticket file) or asks for test cases for a story/bug.
argument-hint: <pasted ticket text>
---

# Generate test cases

Input: $ARGUMENTS

## 1. Get the ticket

The usual input is **ticket text pasted by the user** — use it directly. It may be messy (copied straight
from the Jira page, with field labels, comments and noise mixed in): pick out the key, summary, description,
acceptance criteria, issue type, components and any comments that clarify or change requirements.
If no ticket key is present, ask for one or use `NOKEY-<short-slug>`.

(If instead a file path is given, read it; if only a Jira key is given and a Jira connector is available, fetch it.
If there's nothing to work from, ask the user to paste the ticket.)

Save a copy of what you worked from to `output/<KEY>/ticket.md` so the run is reproducible.

## 2. Load application knowledge

- Always read `knowledge-base/00-application-overview.md`, `roles-and-permissions.md` and `navigation.md`.
- Read `business-rules.md`, `test-data.md` and `known-gotchas.md`.
- Search `knowledge-base/flows/` and `knowledge-base/features/` for anything matching the ticket's
  feature, components, labels and key nouns. Read every match.
- Look in `output/` for earlier tickets touching the same feature — reuse their style and regression ideas.

## 3. Analyse before writing

Write a short analysis (it goes at the top of the output):
- What is changing, in one or two sentences.
- Numbered list of acceptance criteria (if the ticket has none, derive them from the description and say so).
- **Questions / ambiguities** for the BA/dev — things the ticket doesn't specify that affect testing.
- Regression risks worth knowing about (one line, no tests; regression is covered by a separate suite).

If the ticket is too vague to test at all, stop and present the questions instead of guessing.

## 4. Design the test cases

Cover, where relevant:
- **Positive / happy path** for each acceptance criterion.
- **Negative** — invalid input, missing mandatory fields, wrong state.
- **Boundary values** — min, max, just over/under, empty, very long, special characters (use limits from `business-rules.md`).
- **Roles & permissions** — each role in `roles-and-permissions.md` that can or must not reach the feature.
- **State / workflow** — status transitions, back button, refresh, session timeout, concurrent edits.
- **Integration & data** — what downstream screens, reports, emails or exports should reflect the change.
- **No regression tests.** The team has a separate regression suite. Only write tests that check the change itself
  (including the changed thing in its different states: error state, other entry routes, mobile, screen reader).
  If a regression risk stands out, mention it in one line in the analysis instead of writing a test.
- **Accessibility** — for any UI change, include a step to run an accessibility checker (axe/WAVE) on the changed page,
  checking ARIA references point to elements that exist (see known-gotchas).
- For **bugs**: a test that reproduces the original defect (should now pass) plus variations around it.

Prefer fewer, sharper cases over many near-duplicates. Mark each with a priority:
High (AC coverage / core path), Medium (negative, permissions), Low (edge/cosmetic).

## 5. Write the steps

- Use exact screen names, menu paths, labels and messages from the knowledge base or the ticket.
- Unknown detail → generic wording + `[KB GAP: ...]`. Never make it up.
- Shared setup (login, creating a record, etc.) goes in Preconditions, referencing the flow file.
- Use concrete test data from `test-data.md`; if none fits, describe the data needed.
- If a test case touches an item under **KNOWN OPEN DEFECTS** in `known-gotchas.md`, still write it with the *correct* expected result,
  and add a line "Known defect: <description / Jira key> — expected to fail until fixed" so the tester doesn't re-raise it.

## 6. Output

The user copies the test cases **from the chat** and pastes them into a Jira test ticket, so the chat
reply is the deliverable:

1. Write `output/<KEY>/test-cases.md` following `templates/test-case-format.md` (kept for reference/re-runs).
2. In the chat reply, print **each test case in its own ```text code block**, in the paste-ready format from the
   template's "Paste-ready test case" section. One block per test case so the copy button grabs exactly one.
   Plain text only inside the blocks — no markdown tables, no `**bold**`, no `#` headings — so it pastes cleanly
   into any Jira editor.
3. Before the blocks, show the short analysis (what's changing, questions for BA/dev) and the traceability
   (AC → test case IDs) as normal chat text — that part is for the user to read, not paste.

## 7. Report back

After the blocks, tell the user briefly:
- Number of test cases by type and priority, and that every AC is covered (or which isn't and why).
- The questions for the BA/dev.
- The `[KB GAP]` list, and offer to run `/update-knowledge-base` once they supply the answers.

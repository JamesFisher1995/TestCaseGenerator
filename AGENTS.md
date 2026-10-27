# Test Case Generator — instructions for AI assistants

This file is read by any AI coding assistant (GitHub Copilot, Claude Code, Cursor, Codex, …).
If your tool doesn't read it automatically, paste this file into the chat first.

This project turns Jira tickets into **manual test cases** for the **Get air pollution data** service
(https://get-air-pollution-data.service.gov.uk). You act as a senior QA analyst.

## How it works

1. The user pastes a Jira ticket into the chat.
2. You read the **knowledge base** in `knowledge-base/` to learn how the application actually works:
   screens, navigation, business rules, test data, known defects.
3. You write test cases whose steps use the real screen names, field labels and messages from the knowledge base.
4. Where the knowledge base doesn't cover something, you flag it — you never invent UI details.
5. You print each test case in its own plain-text code block so the user can copy it straight into a Jira test ticket.

## Tasks

| Task | Instructions to follow |
|------|------------------------|
| Generate test cases from a ticket | `instructions/generate-test-cases.md` |
| Add or correct application knowledge | `instructions/update-knowledge-base.md` |

## Team rules (always apply)

- **No regression tests.** The team has a separate regression suite. Only write tests that check what the ticket changes
  (including the changed thing in its different states: error state, other entry routes, mobile, screen reader).
  If a regression risk stands out, mention it in one line in the analysis — don't write a test for it.
- **The tester picks which test cases to run.** Give the full set of distinct, change-related test cases with clear titles and
  priorities. Don't trim the list or keep asking whether to merge overlapping cases; only remove true duplicates.
- **Known defects are already raised.** If a test touches an item under "KNOWN OPEN DEFECTS" in `knowledge-base/known-gotchas.md`,
  keep the correct expected result and add "Known defect: #<n> — expected to fail until fixed". Don't present it as a new bug.
- **Check ARIA.** The devs often get ARIA attributes wrong. For any UI change, include a step to run an accessibility checker
  (axe DevTools or WAVE) on the changed page and check `aria-describedby` / `aria-labelledby` point to elements that exist.

## Ground rules

- **The knowledge base is the source of truth for how the app works.** The ticket is the source of truth for what is changing.
  If they conflict, the ticket wins for new behaviour, and you note that the knowledge base needs updating.
- **Never invent** screen names, menu paths, button labels, field names or validation messages.
  If you need one that isn't in the knowledge base or the ticket, write the step generically and tag it
  `[KB GAP: <what is missing>]`. Every gap is listed at the end of the output so the knowledge base can be improved.
- One test case checks one thing. Steps are numbered, atomic actions; each verifiable step has an expected result.
- Every acceptance criterion must be covered by at least one test case (show this in the traceability table).
- Reuse shared flows from `knowledge-base/flows/` as preconditions ("On the Hub page — see flow: search-by-location")
  rather than repeating them in every test case.
- Output follows `templates/test-case-format.md` exactly.

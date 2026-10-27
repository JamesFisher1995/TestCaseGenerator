# Test Case Generator

An AI assistant setup that turns Jira tickets into manual test cases for the
**Get air pollution data** service (https://get-air-pollution-data.service.gov.uk).

You paste a ticket; it reads the application knowledge base and gives you test cases you can copy straight
into a Jira test ticket, one per box.

## Team rules

- **No regression tests.** We have a separate regression suite, so it only writes tests for what the ticket changes.
- **You pick which test cases to run.** It gives you the full set of change-related cases with priorities; review them and choose.
- **Known defects are flagged**, not reported as new bugs (see `knowledge-base/known-gotchas.md`).
- **Every UI change gets an accessibility check step** (axe or WAVE), because ARIA attributes are often wrong.

These rules live in [AGENTS.md](AGENTS.md), so every tool below follows them.

## How to use it

### GitHub Copilot (VS Code)
1. Open this folder in VS Code. Copilot reads `.github/copilot-instructions.md` and `AGENTS.md` automatically.
2. Open Copilot Chat in **Agent** mode so it can read the knowledge base files.
3. Type `/generate-test-cases`, then paste the ticket. (To add app knowledge: `/update-knowledge-base`.)
   If the `/` commands don't appear, just paste the ticket and say "generate test cases for this ticket".

### Claude Code
1. Open this folder in Claude Code.
2. Type `/generate-test-cases`, then paste the ticket — or just paste it and ask for test cases.

### Cursor, Codex or other AI coding tools
Open the folder and paste the ticket. Most of these read `AGENTS.md` automatically; if yours doesn't,
paste `AGENTS.md` into the chat first.

### A chat tool with no access to the folder (e.g. Copilot in the browser or Teams)
Upload or paste these files first, then paste the ticket:
`AGENTS.md`, `instructions/generate-test-cases.md`, `templates/test-case-format.md`, and the
`knowledge-base/` files for the area the ticket touches (always include `known-gotchas.md` and `business-rules.md`).

## What's in the folder

| Path | What it is |
|------|-----------|
| `AGENTS.md` | Rules every AI tool follows — **edit team rules here** |
| `instructions/` | Step-by-step for generating test cases and updating the knowledge base |
| `templates/test-case-format.md` | The test case format (change it to change every future output) |
| `knowledge-base/` | How the app works: screens, flows, rules, test data, known defects |
| `output/<ticket>/` | Saved test cases for each ticket |
| `.github/` | Copilot hooks (point at the files above) |
| `.claude/`, `CLAUDE.md` | Claude Code hooks (point at the files above) |

## Keeping it useful

When the agent flags a `[KB GAP]`, or a bug is fixed, update the knowledge base
(`/update-knowledge-base`, or edit the files directly) and commit it, so everyone benefits.

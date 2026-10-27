---
name: generate-test-cases
description: Generate manual test cases from a Jira ticket using the application knowledge base. Use when the user pastes Jira ticket content (or a Jira key / ticket file) or asks for test cases for a story/bug.
argument-hint: <pasted ticket text>
---

Ticket: $ARGUMENTS

Follow `instructions/generate-test-cases.md` exactly, applying the team rules in `AGENTS.md`.

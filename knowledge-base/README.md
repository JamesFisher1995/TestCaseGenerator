# Application knowledge base

This is what the agent knows about the application. The better this is, the better the test steps.

**Start small:** fill in the overview, navigation and roles, plus one flow (login) and the feature you test most.
Then let it grow — every generated test suite ends with a list of `[KB GAP]`s. Answer them with
`/update-knowledge-base` and the next run will be sharper.

| File | What goes in it |
|------|-----------------|
| `00-application-overview.md` | What the app is, who uses it, environments, main modules |
| `navigation.md` | Menus, screens, how to get to each one |
| `roles-and-permissions.md` | User roles and what each can see/do |
| `business-rules.md` | Validation rules, field limits, statuses, calculations |
| `test-data.md` | Test accounts (no passwords!), sample records |
| `known-gotchas.md` | Quirks, caching, slow jobs, known bugs |
| `glossary.md` | Domain terms and abbreviations |
| `flows/` | Reusable step-by-step journeys (login, create X…) |
| `features/` | One file per feature/screen: fields, buttons, messages |

**Fastest ways to populate it:** paste existing docs/user guides/Confluence pages, or give screenshots of
each screen to `/update-knowledge-base` and it will transcribe the exact labels.

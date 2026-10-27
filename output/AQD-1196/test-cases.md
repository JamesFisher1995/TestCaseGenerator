# AQD-1196: Remove 'Choose how you want to add years' text on Add time period page

**Generated:** 27 October 2026 · **Ticket type:** Content change · **Components:** Create a custom dataset > Add time period

## Analysis

**What's changing:** The line "Choose how you want to add years", shown under the "Add time period" heading and above the options, is removed. Nothing else on the page should change.

**Acceptance criteria** (derived from the ticket, which has none)
1. AC1: "Choose how you want to add years" is not displayed on the Add time period page.
2. AC2: The rest of the page (heading, the four options, their hints and fields, Continue, Back) is unchanged and still works.

**Questions for BA / Dev**
- Answered: the text was a hint and its removal is already live (ticket likely a leftover).
- The fieldset's `aria-describedby="time-hint"` points to an id that isn't on the page — to be fixed under this ticket (agreed with QA 27 Oct 2026).

**Regression:** not included — covered by the existing regression suite.

## Traceability

| AC  | Test cases |
|-----|------------|
| AC1 | TC-001, TC-002, TC-003, TC-004, TC-005 |
| AC2 | TC-001, TC-004 |

## Test cases

### TC-001: Add time period page no longer shows "Choose how you want to add years"
| Field | Value |
|---|---|
| Priority | High |
| Type | Positive |
| AC ref | AC1, AC2 |
| Preconditions | - On "Create a custom dataset" with a pollutant selected (flow: create-custom-dataset steps 1–4) |
| Test data | Pollutant group: Daily Air Quality Index (DAQI) pollutants |

| # | Step | Expected result |
|---|------|-----------------|
| 1 | In the Time period row, click Add | "Add time period" page is displayed |
| 2 | Check the area between the "Add time period" heading and the first option | "Choose how you want to add years" is not displayed; no empty gap is left |
| 3 | Check the options | Last 7 days, Year to date (1 January to <today's date>), Any year, Range of years are shown in that order |

### TC-002: Text not shown when the page is redisplayed with an error
| Field | Value |
|---|---|
| Priority | Medium |
| Type | Negative |
| AC ref | AC1 |
| Preconditions | - On "Add time period" (TC-001 steps 1) |
| Test data | None |

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Without choosing an option, click Continue | Error summary "There is a problem" with "Select an option before continuing" |
| 2 | Check the area between the heading and the options | "Choose how you want to add years" is not displayed |

### TC-003: Text not shown when reached through Change time period
| Field | Value |
|---|---|
| Priority | Medium |
| Type | Positive |
| AC ref | AC1 |
| Preconditions | - On "Create a custom dataset" with a pollutant and Time period "1 January to 31 December 2024" set (flow: create-custom-dataset steps 1–5) |
| Test data | Any year: 2024 |

| # | Step | Expected result |
|---|------|-----------------|
| 1 | In the Time period row, click Change | "Add time period" page is displayed |
| 2 | Check the area between the heading and the options | "Choose how you want to add years" is not displayed |

### TC-004: Screen reader still announces the time period options as one group
| Field | Value |
|---|---|
| Priority | Medium |
| Type | Accessibility |
| AC ref | AC1, AC2 |
| Preconditions | - On "Add time period" (TC-001 step 1); screen reader running (e.g. VoiceOver or NVDA) |
| Test data | None |

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Tab to the first option | Group is announced as "Add time period", then "Last 7 days, radio button" [KB GAP: exact announcement] |
| 2 | Read through the page | "Choose how you want to add years" is not announced |
| 3 | Run an accessibility checker (e.g. axe DevTools or WAVE) on the page | No broken ARIA reference errors (the fieldset doesn't reference a missing id such as `time-hint`). Found 27 Oct 2026 — currently fails (known-gotchas #24) |

### TC-005: Text not shown on a mobile screen
| Field | Value |
|---|---|
| Priority | Low |
| Type | Positive |
| AC ref | AC1 |
| Preconditions | - Phone or browser at 375px wide; on "Add time period" (TC-001 step 1) |
| Test data | None |

| # | Step | Expected result |
|---|------|-----------------|
| 1 | View the top of the page | Heading "Add time period" followed directly by the options; "Choose how you want to add years" not shown; no sideways scroll |

---

## Knowledge base gaps

| # | Test case(s) | Missing information |
|---|--------------|---------------------|
| 1 | TC-004 | Exact screen reader announcement for the time period radios |

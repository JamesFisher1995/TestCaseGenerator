# <TICKET-KEY>: <Ticket summary>

**Generated:** <date> · **Ticket type:** <Story/Bug/...> · **Components:** <...>

## Analysis

**What's changing:** <1–2 sentences>

**Acceptance criteria**
1. AC1 — <...>
2. AC2 — <...>

**Questions for BA / Dev**
- <question>

**Regression areas:** <areas>

## Traceability

| AC  | Test cases           |
|-----|----------------------|
| AC1 | TC-001, TC-002       |
| AC2 | TC-003               |

## Test cases

### TC-001: <Verb-led title, e.g. "Save customer with valid postcode">

| Field         | Value |
|---------------|-------|
| Priority      | High / Medium / Low |
| Type          | Positive / Negative / Boundary / Permission / Regression / Bug-retest |
| AC ref        | AC1 |
| Preconditions | - <starting state, referencing a flow, e.g. On the Hub page (flow: search-by-location steps 1–3)><br>- <data that must exist> |
| Test data     | <specific values> |

| # | Step | Expected result |
|---|------|-----------------|
| 1 | <action> | <observable result, or "—" if none> |
| 2 | <action> | <observable result> |

---

## Knowledge base gaps

| # | Test case(s) | Missing information |
|---|--------------|---------------------|
| 1 | TC-002 | <e.g. exact error message for invalid postcode> |

---

## Paste-ready test case (format for the chat reply)

Each test case goes in its own ```text block, exactly like this:

```text
TC-001: Search by unique town returns stations sorted by distance

Priority: High
Type: Positive
Covers: AC1

Preconditions:
- On the "Find monitoring stations by location" page (flow: search-by-location steps 1-4)

Test data:
- Town: Leeds

Steps:
1. Clear the "Enter a town or postcode" field and enter "Leeds"
   Expected: Text is shown in the field
2. Leave "50 miles" selected and click Continue
   Expected: Page heading "Monitoring stations within 50 miles of Leeds" is displayed
3. Check the first row of the results table
   Expected: "Leeds Centre" with "0.2 miles away", site type "Urban Background"
4. Check the distances down the list
   Expected: Stations are sorted from nearest to furthest
```

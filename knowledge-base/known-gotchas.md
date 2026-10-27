# Known gotchas & observed defects

Observed 14 Oct 2026 on the live service. All defects below were confirmed by QA and raised with the devs on 22 Oct 2026.

## Tester gotchas
- **ARIA attributes are often wrong** (QA, 27 Oct 2026). On any page a ticket changes, run an accessibility checker (axe DevTools or WAVE) and check `aria-describedby` / `aria-labelledby` point to elements that exist.
- **Direct URLs 404.** Typing an inner page URL (e.g. `/customdataset`, `/location-aurn/change`) into the address bar shows "Page not found". Always navigate via links/buttons from the start page.
- **Search field is pre-filled** with your previous search. Clear it before typing, or your text is appended.
- **Entering Create a custom dataset from the Hub resets selections**; Back links keep them.
- Station details **year tabs load asynchronously** (~3 s) — the table briefly shows the previous year's numbers. Wait before checking values.
- Time period and Location **Add** links only appear after a pollutant is chosen.
- Autocomplete pickers: after picking an option the page layout shifts; re-locate buttons before clicking.

## KNOWN OPEN DEFECTS
All of these are **confirmed and raised — do not re-raise.** Test cases that touch them should keep the *correct* expected
result and add "Known defect: #<n> — expected to fail until fixed". When a fix is released, retest and move the item to "Fixed".
Jira keys: TODO — add each key next to its item.

1. **Disambiguation choice is ignored; results always use the first match.** Search "Newport" (50 miles), choose "Newport, Isle of Wight" or "Newport, Cornwall" → results show stations around Newport, Wales (first item in the list, shown as "Casnewydd, Casnewydd - Newport"): Newport 1.2 miles, Cwmbran 4.6 miles, Cardiff Newport Road 9.5 miles. Newport IoW is ~96 miles from Newport Wales, so these are outside the 50-mile radius. Heading still reads "Monitoring stations within 50 miles of Newport". Also reproduced with "Richmond" — so it affects all ambiguous place names, not just Newport.
2. **Unmatched search text sometimes causes a service error** — "zzqqxx", "xyzzy", "12345", any 50+ character string → "Sorry, there is a problem with the service", while "qwerty" correctly gives "We could not find 'qwerty'". Expected: always the "could not find" page.
3. **Northern Ireland postcode search fails** (raised before this review). Valid NI postcodes (e.g. "BT1 5GS", "BT1") return "We could not find…" instead of stations. Expected: NI postcodes return stations (NI town names are not supported by design).
   - Related (not yet confirmed as a separate bug): searching an NI town name ("Belfast") gives the service error page rather than a friendly message.
4. **HTML entity shown on station page** — Region shows "Yorkshire &amp; Humberside" instead of "Yorkshire & Humberside" (Leeds Centre).
5. **Data capture over 100%** — Leeds Centre Sulphur dioxide "Data capture: 382%" (2026) / "370%" (2024).
6. **Typo** — summary error "Select a timeperiod to continue" (should be "time period").
7. **Inconsistent year error wording** — Any year: "Enter a 4-digit year, for example 2009." vs Range: "Start year must be 4 digits, for example 2009."
8. **Duplicate error in summary** — Range > 5 years shows "Choose up to 5 whole years at a time" twice in the error summary.
9. **Missing/odd page titles** — Not-found results page title is "| Get air pollution data - GOV.UK" (empty); disambiguation page title "Multiplelocations".
10. **Back link on search error page** goes to `/` instead of `/hubpage`.
11. **Problem-with-service page** — "UK AIR" link points to a mailto: address rather than the UK AIR website.
12. **GOV.UK style** — local authority message "Please select a local authority from the list" uses "Please" (GOV.UK style avoids it).
13. **Screen reader text** — download button contains hidden "(Visual only)" text; "Year to date" radio's accessible name drops the date on error re-render.
14. Custom dataset pages all have the generic title "Get air pollution data" — titles don't reflect the page/error state.
15. **Server doesn't enforce the 10-pollutant limit** — the page blocks an 11th, but the server accepts 11 if the form is submitted directly.
16. **Stale error after Remove** — "You can add up to 10 pollutants" stays on screen after removing a pollutant.
17. **"1 stations available"** — wrong plural on the Download your data page (Non-Automatic Hydrocarbon Network).
18. **Same download link for all "Other" networks** — UKEAP and Non-Automatic Hydrocarbon both link to `/download_aurn_nojs/<year>/NON-AURN`.
19. **Error messages handled inconsistently on Add location(s)** — "Select an option before continuing" only in the summary (not beside the radios); duplicate local authority message only inline (not in the summary).
20. **Inconsistent limit wording** — "You can add up to 10 pollutants" vs "Add up to 10 local authorities" (which is also just the hint text).
21. **Inconsistent date format on summary** — Any year 2024 shows "1 January to 31 December 2024" but range 2024–2024 shows "1 January 2024 to 31 December 2024".
22. **Cookies page** — the Google Analytics cookies `_ga` and `_ga_PQP5766L23` are listed in the "Essential cookies we use" table, but they're optional analytics cookies.
23. **Unstyled 403 page** — input like "<script>" returns a plain "403 Forbidden" page (firewall) instead of a GOV.UK error page.
24. **Broken ARIA reference on Add time period** (found 27 Oct 2026 — to be fixed under AQD-1196 when devs pick it up) — the options fieldset has `aria-describedby="time-hint"`, but no element with id `time-hint` exists on the page. Accessibility checkers (axe/WAVE) flag it; no visible effect.

## Fixed
- **AQD-1196** — "Choose how you want to add years" hint removed from Add time period (live by 14 Oct 2026). Broken `aria-describedby="time-hint"` on the fieldset still open (#24), same ticket.

## Notes (not defects)
- Footer pages (`/cookies`, `/privacy`, `/accessibility`) can be opened directly by URL, unlike the journey pages.
- Typing "York" in the local authority box shows "East Riding of Yorkshire" first; check you pick the intended council.


# Application overview

- **Name:** Get air pollution data (GOV.UK service, run by Defra) — **Beta**
- **URL (live):** https://get-air-pollution-data.service.gov.uk
- **What it does:** Lets the public view and download air pollution data from UK monitoring networks.
- **Who uses it:** Members of the public, researchers, local authorities. **No login / no accounts** — everyone is anonymous.
- **Platform:** Web, GOV.UK Design System (govuk-frontend styling, error summaries, back links).
- **Contact shown in service:** getairpollutiondata@defra.gov.uk

## Main journeys
1. **Find monitoring stations by location** — search by town or postcode → list of stations → station details page
   with yearly pollution levels and CSV downloads. See `features/find-stations-by-location.md`, `features/station-details.md`.
2. **Create a custom dataset** — choose pollutant(s), time period and location(s) → download page with CSV per network.
   See `features/create-custom-dataset.md`.

## Common page furniture (every page)
- Cookie banner (first visit): "Cookies on Get air pollution data" with **Accept analytics cookies**, **Reject analytics cookies**, **View cookies**.
- Header: GOV.UK logo, service name "Get air pollution data" (links to `/`).
- Phase banner: "Beta — This is a new service. Help us improve it and give your feedback." (feedback link → Qualtrics survey)
- Footer: Privacy, Cookies, Accessibility statement, Open Government Licence v3.0, © Crown copyright.

## Footer pages
- **Cookies** (`/cookies`): essential cookies table (cookies_policy 1 year, session_cookie 4 hours, plus _ga entries), Google Analytics explanation,
  radios "Do you want to accept analytics cookies?" **Yes** / **No** (reflects banner choice), button **Save cookie settings**.
- **Privacy** (`/privacy`): "Privacy notice" — who collects data, lawful basis, sharing, retention, rights, complaints, personal information charter.
- **Accessibility statement** (`/accessibility`): claims WCAG 2.2 AA compliance; last tested 5 June 2025 by the Digital Accessibility Centre; reviewed 26 August 2026; contact accessibility@defra.gov.uk.

## Session behaviour
- State (last search term, custom dataset selections) is held in the server session (`session_cookie`, expires after 4 hours).
- See `known-gotchas.md` — direct URL entry to inner pages returns "Page not found".

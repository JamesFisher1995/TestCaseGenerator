# Flow: search by location

**Used for:** Precondition for station results / station details tests.
**Starting point:** Browser on https://get-air-pollution-data.service.gov.uk
**Roles:** Any (no login)

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Open https://get-air-pollution-data.service.gov.uk | Start page "Get air pollution data" with **Start now** button |
| 2 | If the cookie banner shows, click **Reject analytics cookies** (or Accept) and then **Hide cookie message** | Banner confirms choice / disappears |
| 3 | Click **Start now** | Hub page with links "Find monitoring stations by location" and "Create a custom dataset" |
| 4 | Click **Find monitoring stations by location** | "Find monitoring stations by location" form; 50 miles selected |
| 5 | Clear the "Enter a town or postcode" field and enter the location (e.g. Leeds) | |
| 6 | Select the search area (5 / 25 / 50 miles) | |
| 7 | Click **Continue** | "Monitoring stations within <N> miles of <place>" results table (or disambiguation list if ambiguous) |
| 8 | (Optional) Click a station name, e.g. **Leeds Centre** | Station details page for that station |

**End state:** On results (or station details) page.
**Variations:** ambiguous term → choose from "Locations matching '<term>'" list first.

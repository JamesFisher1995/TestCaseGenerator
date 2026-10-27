# Feature: Create a custom dataset

**Where:** Start page > Start now > Create a custom dataset (`/customdataset`)
**Purpose:** Build a dataset by pollutant, time period and location, then download CSVs per monitoring network.

## Summary screen — H1 "Create a custom dataset"
- Link **Clear selections** (resets all rows to "None selected")
- Summary list rows:
| Row | Initial value | Action link | Notes |
|-----|---------------|-------------|-------|
| Pollutant | None selected | **Add** → `/airpollutant` (becomes **Change** once set) | |
| Data sources | Any | **View network information** (gov.uk collection page) once a pollutant is chosen | Auto-derived from pollutants, grouped "Near real-time data from Defra" / "Other data from Defra" |
| Time period | None selected | **Add** → `/year-aurn` — **only shown once a pollutant is set** | Shows e.g. "1 January to 31 December 2024" |
| Location | None selected | **Add** → `/location-aurn/change` — **only shown once a pollutant is set** | Lists chosen locations, e.g. "Leeds City Council" |
- **Continue** button. Validation in order:
  - No pollutant → "Select a pollutant to continue" (summary link "Add pollutant")
  - No time period → "Select a timeperiod to continue" (summary link "Add time period") — note typo, see gotchas
  - No location → "Select a location to continue" (summary link "Add location")
- Entering from the Hub resets selections; the Back link from later pages keeps them.

## Add pollutant(s) — `/airpollutant`
- Radios (hint "Select one option"):
  1. **Add pollutant(s)** — hint "Add up to 10 pollutants"
     - Autocomplete text field (type to filter, choose from list; arrow keys + Enter work)
     - Button **Add pollutant** (becomes **Add another pollutant** after first add)
     - Table "Added pollutants": "Pollutant 1 | <name> | Remove", "Pollutant 2 …"
  2. **Add a group of pollutants** — sub-radios:
     - **Daily Air Quality Index (DAQI) pollutants** — PM2.5, PM10, NO2, O3, SO2
     - **Pollutants in the Air Quality Standards Regulations 2010** — PM2.5, PM10, NO2, O3, SO2, NO, NOx as NO2, CO
- **Continue**
- Messages (exact):
  - No radio chosen: "Select an option before continuing"
  - Add clicked with empty field: "Enter a pollutant"
  - Free text not from list: "Select a pollutant from the list"
  - Duplicate: "This pollutant has already been added"
  - 11th pollutant: "You can add up to 10 pollutants"
  - Group radio with no group chosen: "Select a pollutant group"
- **Remove** deletes the row and renumbers the rest (Pollutant 2 becomes Pollutant 1). The "You can add up to 10 pollutants" error stays visible after removing (defect).
- Server-side messages (seen when the hidden list is submitted directly): "Please add at least one pollutant", "Invalid pollutant(s): <name>. Select from the allowed list.", "Duplicate pollutant(s): <name> have already been added." The server does **not** enforce the 10 limit (11 accepted).
- **Data sources** change with the pollutants, e.g. NO2+O3 → AURN + UKEAP - Rural NO2 Network; adding Benzene adds "Non-Automatic Hydrocarbon Network".
- 82 pollutants available — see `business-rules.md` § Pollutant list.

## Add time period — `/year-aurn` (legend "Add time period")
- No hint under the legend. A hint "Choose how you want to add years" used to be there and was removed (AQD-1196, already live by 14 Oct 2026).
  The radios' fieldset has `aria-describedby="time-hint"`, but no element with that id exists (see known-gotchas #24).
- Hint IDs on this page: time-last7days-hint, time-any-hint, any-year-input-hint, time-range-hint, range-start-hint, range-end-hint.
| Option | Extra fields | Hint |
|--------|--------------|------|
| **Last 7 days** | — | "Only near real-time data from Defra is available" |
| **Year to date (1 January to <today>)** | — | |
| **Any year** | "Year" (hint "For example: 2009") | "Choose a single whole year" |
| **Range of years** | "Enter start year" (e.g. 2021), "Enter end year" (e.g. 2025) | "Choose up to 5 whole years at a time" |
- **Continue**. Validation messages — see `business-rules.md` § Time period.
- Summary display: Any year 2024 → "1 January to 31 December 2024"; Range 2024–2024 → "1 January 2024 to 31 December 2024";
  Range 2022–2026 → "1 January 2022 to 14 October 2026"; Year to date → "1 January to 14 October 2026";
  Last 7 days → "7 October 2026 to 13 October 2026" (the 7 days before today, today excluded); Any year 2026 → "1 January to 14 October 2026".

## Add location(s) — `/location-aurn/change` (H1 "Add location(s)")
1. **Countries** — hint "Choose one or more: England, Scotland, Wales or Northern Ireland"; checkboxes England, Scotland, Wales, Northern Ireland
2. **Local authority** — hint "Add up to 10 local authorities"; autocomplete (e.g. "Leeds" → "Leeds City Council"); button **Add local authority** → **Add another local authority**; table "Added local authorities": "Local authority 1 | <name> | Remove"
- **Continue**
- Messages (all confirmed):
  - No option chosen → "Select an option before continuing" (shown in the error summary only, not beside the radios)
  - Countries with none ticked → "Select at least one country"
  - Add local authority with empty field → "Enter a local authority"
  - Free text not in list (e.g. "Nowhere Council") → "Please select a local authority from the list"
  - Duplicate → "This local authority has already been added" (inline only — not added to the error summary)
  - Continue with Local authority chosen but none added → "Add at least one local authority"
  - 11th local authority → "Add up to 10 local authorities"
  - "No local authorities available" (from code; not seen)
- Autocomplete names are council names, e.g. Leeds City Council, Bradford City Council, Cardiff County Council, Glasgow City Council,
  Wakefield Metropolitan District Council, Kirklees Metropolitan Council. Typing "York" lists **East Riding of Yorkshire** first.
- Summary Location row lists every chosen local authority (10 shown), or the country name(s) e.g. "Northern Ireland".

## Download your data — `/download_dataselector`
- H1 "Download your data"
- Expandable **File format and metadata**: "This data will download in a long format (CSV). Data in a long format is stacked vertically." Metadata may include: name of monitoring station, site type, site ID, map coordinates, local authority, region, instrument type, inlet height.
- Tabs: **Near real-time data from Defra** | **Other data from Defra**
  - Near real-time: "This data is automatically measured and published every hour." → **Automatic Urban and Rural Network (AURN)** description, green panel "<n> stations available", button **Download hourly data**
  - Other: "Data is measured hourly, weekly or monthly depending on the network." → per network (e.g. UKEAP - Rural NO2 Network, UKEAP - Acid Gas & Aerosol Network) "<n> stations available" or "No data available for the selected range."
- Example: DAQI group + 2024 + Leeds City Council → AURN "5 stations available"; UKEAP networks 0 stations.
- Network panels show "<n> stations available"; singular is wrong — "1 stations available" (defect).
- Example: 9 pollutants (O3, SO2, PM10, PM2.5, CO, Benzene, NO, NOx, 1,3-butadiene) + Year to date + Northern Ireland → AURN 7 stations; UKEAP - Acid Gas & Aerosol Network 3; Non-Automatic Hydrocarbon Network 1.
- Download links: AURN `/download_aurn_nojs/<year>/AURN`; every "Other" network uses the same `/download_aurn_nojs/<year>/NON-AURN` link (check each network downloads its own data).
- TODO: CSV file name / columns of the download.

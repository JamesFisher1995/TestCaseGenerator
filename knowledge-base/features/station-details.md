# Feature: Station details

**Where:** Location search results > click a station name (`/stationdetails`)
**Purpose:** Show a station's metadata, yearly pollution summary, and CSV downloads.

## Header area
- H1: station name (e.g. "Leeds Centre")
- Status tag (e.g. **Active**) + "Latest at <h:mm am/pm> on <d Month yyyy>"
- **Monitoring network** (e.g. "Automatic Urban and Rural Network (AURN)")
- **Region** (e.g. "Yorkshire & Humberside")
- **Site type** (e.g. "Urban Background") with an info toggletip (i) — text: "This monitoring area is in a city or town. It is located so pollutant measurements do not come from one specific source."
- Link **View on Google Maps (opens in new tab)** → google.co.uk/maps?q=<lat>,<long>

## Yearly levels — H2 "Air pollution levels in <year>"
- Sub-text: date range — current year "1 January to <today>", past years "1 January to 31 December"
- Year tabs: **2018 … 2026** (current year selected by default). Content loads asynchronously (~3 s).
- Verification note: current year "Data has been verified until 30 June"; past years "Data has been verified"
- Table columns: **Pollutant** | **Annual average** | **Daily exceedances** | **Hourly exceedances**
  - Each pollutant row shows "Data capture: <n>%" under the pollutant name
  - Values in µg/m3; "n/a" where a limit doesn't apply
  - Info toggletips (i) explain each limit — see `business-rules.md` § Limit values

## Downloads — H2 "Download data for <year>"
- "Approximate file sizes (CSV)": hourly data - usually less than 1MB; daily average data - usually less than 500KB; annual average data - usually less than 100KB
- Section **All pollutants** then one section per pollutant, each with three buttons:
  **Download hourly data**, **Download daily average data**, **Download annual average data**
- Download year follows the selected year tab.
- Mobile (375px): pollutant table stacks (pollutant name + data capture above the values row); file sizes collapse into an expandable "Approximate file sizes (CSV)"; no horizontal page scroll.
- TODO: CSV file name and column layout (not yet downloaded).

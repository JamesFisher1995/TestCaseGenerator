# Navigation

All paths relative to https://get-air-pollution-data.service.gov.uk

| Screen (H1 / title) | Path | How to get there | Back link goes to |
|---------------------|------|------------------|-------------------|
| Start page — "Get air pollution data" | `/` | Enter the URL | — |
| Hub — "Get air pollution data" (two option links) | `/hubpage` | Start page > **Start now** | — |
| "Find monitoring stations by location" | `/search-location` | Hub > **Find monitoring stations by location** | `/hubpage` |
| "Locations matching '<term>'" (disambiguation) | `/multiplelocations` (POST) | Search with an ambiguous term (e.g. Newport) | — |
| "Monitoring stations within <N> miles of <place>" | `/multiplelocations` or `/location/<slug>` | Search with an exact match, or pick a location from disambiguation | — |
| "We could not find '<term>'" | `/multiplelocations` | Search a term with no match | — |
| Search again (same form, field cleared) | `/search-location/searchagain` | Results > **Change search area**, or "try searching again" / "Go back to search a location" | `/hubpage` |
| Station details — "<Station name>" | `/stationdetails` (POST) | Results > click a station name | results |
| "Create a custom dataset" (summary page) | `/customdataset` | Hub > **Create a custom dataset** | `/hubpage` |
| "Add pollutant(s)" | `/airpollutant` | Custom dataset > Pollutant row **Add** / **Change** | `/customdataset` |
| "Add time period" | `/year-aurn` | Custom dataset > Time period row **Add** / **Change** | `/customdataset` |
| "Add location(s)" | `/location-aurn/change` (posts to `/location-aurn`) | Custom dataset > Location row **Add** / **Change** | `/customdataset` |
| "Download your data" | `/download_dataselector` (POST) | Custom dataset > **Continue** (all rows complete) | `/customdataset` |
| Clear selections | `/customdataset/clear` | Custom dataset > **Clear selections** | — |
| "Sorry, there is a problem with the service" | `/problem-with-service` | Server error | — |
| "Page not found" | any | Unknown URL, or inner page typed directly into address bar | — |

Footer pages: `/privacy`, `/cookies`, `/accessibility`.

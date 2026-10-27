# Business rules

## Location search
| Field | Mandatory | Rule | Error message (exact) |
|-------|-----------|------|-----------------------|
| Enter a town or postcode | Yes | Town/place name or postcode in England, Scotland or Wales. **Northern Ireland: postcode only** (town names not supported). NI postcode search is currently broken — known open defect, see known-gotchas | "Enter a town or postcode" |
| Approximate search area | Yes (defaulted) | 5 / 25 / 50 miles; default 50 | — |
- Results sorted by distance ascending, distance shown to 1 decimal place ("0.2 miles away").
- Allowed characters: letters, numbers, spaces, ' - , . — others (e.g. & !) → "Enter a town or postcode using only numbers and letters".
- Postcodes are case/space insensitive.
- No stations in radius → "There are no monitoring stations within <N> miles of '<place>'".
- Ambiguous names show a disambiguation list; choosing one shows stations for that place.

## Custom dataset — pollutants
- Choose **either** individual pollutants (max **10**, enforced in the browser only) **or** one pollutant group.
- Pollutant must be picked from the autocomplete list; no duplicates.
- Messages: "Select an option before continuing", "Enter a pollutant", "Select a pollutant from the list",
  "This pollutant has already been added", "You can add up to 10 pollutants", "Select a pollutant group".
- At summary: "Select a pollutant to continue" if none.
- Data sources are derived automatically from the pollutants chosen.

## Custom dataset — time period
Valid year range: **1973 to current year (2026)**.
| Option | Input | Error message (exact) |
|--------|-------|-----------------------|
| (none chosen) | — | "Select an option before continuing" |
| Any year | empty | "Enter a year." |
| Any year | not 4 digits (e.g. 20) | "Enter a 4-digit year, for example 2009." |
| Any year | outside range (1950, 2030) | "Year must be between 1973 and 2026." |
| Range | start empty | "Enter a start year." |
| Range | start non-numeric (abcd) | "Start year must be 4 digits, for example 2009." |
| Range | outside range | "Start year must be between 1973 and 2026." / "End year must be between 1973 and 2026." |
| Range | start > end | "Start year must be the same as or before the end year." + "End year must be the same as or after the start year." |
| Range | more than 5 years (2015–2025) | "Choose up to 5 whole years at a time" |
| Range | end empty | "Enter an end year." |
| Range | both empty | "Enter a start year." + "Enter an end year." |
| Any year | 1972 | "Year must be between 1973 and 2026." |
| Any year | 2024.5 | "Enter a 4-digit year, for example 2009." |
| Range | 2020–2025 (6 years) | "Choose up to 5 whole years at a time" |
- Boundaries confirmed valid: Any year 1973 and 2026; Range 2021–2025, 2022–2026, 2024–2024 (same year allowed). Leading/trailing spaces are trimmed (" 2024 " accepted).
- Boundaries confirmed invalid: 1972 (any/range start), 2027+.
- Last 7 days: only near real-time (AURN) data available.
- At summary: "Select a timeperiod to continue" if none.

## Custom dataset — location
- **Countries**: one or more of England, Scotland, Wales, Northern Ireland ("Select at least one country"). Northern Ireland is supported here.
- **Local authority**: up to **10**, picked from list, no duplicates.
- At summary: "Select a location to continue" if none.

## Limit values (station details toggletips, exact text)
| Pollutant | Annual average | Daily exceedances | Hourly exceedances |
|-----------|----------------|-------------------|--------------------|
| PM2.5 | must not go above 20 µg/m³ | n/a | n/a |
| PM10 | must not go above 40 µg/m³ | daily average must not go above 50 µg/m³ more than 35 times a year | n/a |
| Nitrogen dioxide | must not go above 40 µg/m³ | n/a | hourly must not go above 200 µg/m³ more than 18 times a year |
| Ozone | "There is no annual average limit value for ozone." | n/a | n/a |
| Sulphur dioxide | "There is no annual average limit value for sulphur dioxide." | daily average must not go above 125 µg/m³ more than 3 times a year | hourly must not go above 350 µg/m³ more than 24 times a year |
All "in a calendar year (when rounded to a whole number)".

## Data rules
- "Data capture" is a percentage of expected measurements and should be **0–100%**.
- Current-year data verified until 30 June; earlier years fully verified.
- Station details year tabs: 2018 to current year.

## Pollutant list (82 in autocomplete)
Key ones: Fine particulate matter (PM2.5), Particulate matter (PM10), Nitrogen dioxide (NO2), Nitrogen oxides as nitrogen dioxide (NOx as NO2),
Nitric oxide (NO), Ozone (O3), Sulphur dioxide (SO2), Carbon monoxide (CO), Benzene (C6H6), 1,3-butadiene (C4H6), Benzo(a)pyrene (BaP).
Also many particulates (Particulate calcium (Ca), Particulate nitrate (NO3)…), gaseous acids (Gaseous nitric acid (HNO3)…), PAHs (Anthracene (ANT), Pyrene (PYR)…),
precipitation chemistry (Nitrate as N in precipitation (NO3-N), pH in precipitation (pH), Rainfall (RF (or PPT))), ammonia (Gaseous ammonia (active) (NH3)…).
Typing "nit" returns 8 matches: Particulate nitrite (NO2-), Particulate nitrate (NO3), Gaseous nitric acid (HNO3), Gaseous nitrous acid (HNO2),
Nitrogen dioxide (NO2), Nitrogen oxides as nitrogen dioxide (NOx as NO2), Nitric oxide (NO), Nitrate as N in precipitation (NO3-N).

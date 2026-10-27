# Test data

No accounts needed — the service is public and anonymous.

## Locations (location search)
| Input | Radius | Behaviour seen (14 Oct 2026) | Use for |
|-------|--------|------------------------------|---------|
| Leeds | 50 | Unique match, 28 stations, nearest "Leeds Centre" 0.2 miles | Happy path |
| Newport | 50 | Disambiguation list of 14 places | Multiple matches |
| Newport, Isle of Wight / Newport, Cornwall (from list) | 50 | **Confirmed bug:** shows Welsh Newport stations (first match). Expected: stations near the chosen place (e.g. IoW → Southampton/Portsmouth area) | Disambiguation regression |
| Richmond (non-first option from list) | 50 | **Confirmed bug:** same — first match used | Disambiguation regression |
| LS1 1UR / ls11ur | 5 | Leeds Centre 0.1 miles, 2 stations | Postcode search, case/space insensitivity |
| SW1A 1AA | 5 | Disambiguation: "SW1A 1AA, City of Westminster" / "W1A 1AA, City of Westminster" | Postcode with near-duplicate match |
| Lerwick | 5 | 1 station (Lerwick 1.8 miles, Rural Background, Ozone) | Single result |
| Durness | 25 | "There are no monitoring stations within 25 miles of 'Durness'" | No stations in radius |
| Tongue, Highland | 50 | No stations within 50 miles | No stations at max radius |
| King's Lynn / Bath, Somerset / Stoke-on-Trent | 50 | Accepted (apostrophe, comma, hyphen) | Allowed characters |
| Brighton & Hove / Leeds! | — | "Enter a town or postcode using only numbers and letters" | Disallowed characters |
| qwerty | — | "We could not find 'qwerty'" | Not found |
| xyzzy / 12345 / 50+ chars | — | Service error page | Unmatched input (inconsistent) |
| <script> | — | 403 Forbidden | Security / WAF |
| BT1 5GS / BT1 | — | "We could not find…" — **known open defect** (should return stations) | NI postcode search / bug retest |
| Belfast | — | Service error page | Out-of-scope location (error page is questionable) |
| (empty) | — | "Enter a town or postcode" | Mandatory validation |
| zzqqxx | — | Service error page (**Bug**) | Invalid input |

## Stations
| Station | Network | Region | Site type | Pollutants |
|---------|---------|--------|-----------|------------|
| Leeds Centre | AURN | Yorkshire & Humberside | Urban Background | PM2.5, PM10, NO2, Ozone, SO2 |
| Leeds Headingley Kerbside | — | — | Urban Traffic | PM2.5, PM10, NO2 |
| Ladybower | — | — | Rural Background | PM2.5, PM10, NO2, Ozone, SO2 |
| Scunthorpe Town | — | — | Urban Industrial | PM2.5, PM10, NO2, SO2 |

## Custom dataset combinations
| Pollutant | Time period | Location | Result |
|-----------|-------------|----------|--------|
| DAQI group | Any year 2024 | Leeds City Council | AURN 5 stations; UKEAP networks 0 ("No data available for the selected range.") |
| Nitrogen dioxide (NO2) + Ozone (O3) | — | — | Data sources: AURN, UKEAP - Rural NO2 Network |
| 9 pollutants incl. Benzene (C6H6) | Year to date | Countries: Northern Ireland | AURN 7, UKEAP Acid Gas & Aerosol 3, Non-Automatic Hydrocarbon 1 ("1 stations available") |
| DAQI group | Year to date | 10 local authorities: Leeds, Bradford, Manchester, Sheffield, Cardiff, Glasgow, Bristol, East Riding of Yorkshire, Wakefield, Kirklees | Max local authorities; Calderdale (11th) rejected |

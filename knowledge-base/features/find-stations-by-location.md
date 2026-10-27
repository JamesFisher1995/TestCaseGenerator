# Feature: Find monitoring stations by location

**Where:** Start page > Start now > Find monitoring stations by location (`/search-location`)
**Who:** Anyone (no login)
**Purpose:** Find air quality monitoring stations near a town or postcode.

## Search screen — H1 "Find monitoring stations by location"
| Element | Type | Mandatory | Rules / notes |
|---------|------|-----------|---------------|
| Hint: "For locations in Northern Ireland, you can only search by postcode." | text | — | By design NI is postcode-only. NI postcode search currently fails — known open defect, see known-gotchas |
| "Enter a town or postcode" | text field (`fullSearchQuery`) | Yes | No maxlength. **Pre-filled with the previous search term** from the session (except via "searchagain" route, which is empty) |
| "Approximate search area" | radios: **5 miles**, **25 miles**, **50 miles** | Yes | **50 miles selected by default** |
| **Continue** | button | | Pressing Enter in the field also submits |

## Outcomes after Continue
| Input | Result page | Exact text |
|-------|-------------|------------|
| Empty | Same form with error | Error summary "There is a problem" + link "Enter a town or postcode"; field error "Enter a town or postcode" |
| Unique town (e.g. Leeds) | Results | H1 "Monitoring stations within 50 miles of Leeds" |
| Ambiguous town (e.g. Newport) — choosing one should show stations near **that** place (currently broken, see known-gotchas #1) | Disambiguation | H1 "Locations matching 'Newport'", text "More than one match was found for your location. Choose the correct location from the following options:", list of links "<Place>, <Area>" (e.g. "Newport, Isle of Wight"), then "Alternatively, try searching again" |
| No match (e.g. BT1) | Not found | H1 "We could not find '<term>'", bullets "check the spelling / enter a broader location / enter a correct postcode", "If you searched for a place in Northern Ireland, check that you have entered the correct postcode.", link "Go back to search a location" |
| Place with no stations in radius (e.g. Durness at 25 miles, "Tongue, Highland" at 50) | No stations | H1 "There are no monitoring stations within <N> miles of '<place>'", "You should either:" bullets "choose a different search area" / "choose a different location", link "Go back to search a location" |
| Disallowed characters (e.g. "Brighton & Hove", "Leeds!") | Same form with error | "Enter a town or postcode using only numbers and letters" |
| Some unmatched strings (e.g. zzqqxx, xyzzy, 12345, 50+ chars, Belfast) | Error page | "Sorry, there is a problem with the service" / "Try again later." — inconsistent with "qwerty" which gives "We could not find…" — see known-gotchas |
| HTML/script-like input (e.g. "<script>") | Plain "403 Forbidden" page (firewall), not GOV.UK styled | |

## Results screen — H1 "Monitoring stations within <N> miles of <place>"
- Link **Change search area** → `/search-location/searchagain` (empty search field, 50 miles default)
- Table columns: **Monitoring station** | **Site type** | **Pollutants**
  - Station name is a link (opens station details) with "<x.x> miles away" beneath
  - Site types seen: Urban Background, Urban Traffic, Rural Background, Urban Industrial
  - Pollutants listed as: PM2.5, PM10, Nitrogen dioxide, Ozone, Sulphur dioxide
- Sorted by distance ascending.
- Example (Leeds, 50 miles): Leeds Centre 0.2 miles (Urban Background; PM2.5, PM10, NO2, Ozone, SO2), Leeds Headingley Kerbside 1.8 miles (Urban Traffic) … Scunthorpe Town 40.2 miles. 28 stations.

## Related
- Flows: `flows/search-by-location.md`
- Next screen: `features/station-details.md`
- Postcodes: case and spacing don't matter ("LS1 1UR" = "ls11ur" → Leeds Centre 0.1 miles, 2 stations at 5 miles).
  A full postcode can still show the disambiguation list (e.g. "SW1A 1AA" → "SW1A 1AA, City of Westminster" and "W1A 1AA, City of Westminster").
- Accepted characters: letters, numbers, spaces, apostrophe (King's Lynn), hyphen (Stoke-on-Trent), comma (Bath, Somerset), full stop. Rejected: & ! (and likely other symbols).
- Lenient matching: "Leeds1" and "Leeds." both return Leeds results.
- Hyphenated names may show disambiguation (Stoke-on-Trent → list incl. "Stoke, Medway", "Trent, Dorset").
- Mobile (375px): results table fits the screen, no horizontal scroll.

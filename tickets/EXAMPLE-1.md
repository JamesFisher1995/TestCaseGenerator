# EXAMPLE-1: Add a 10 miles option to the location search area

**Type:** Story · **Components:** Find monitoring stations by location

## Description
As a user searching for monitoring stations, I want a 10 mile search area so that I can see stations close to me without the long list that 25 miles gives.

## Acceptance criteria
1. The "Approximate search area" options are 5 miles, 10 miles, 25 miles and 50 miles, in that order.
2. 50 miles remains the default selection.
3. Selecting 10 miles and searching shows only stations within 10 miles, and the heading reads "Monitoring stations within 10 miles of <place>".
4. If there are no stations within 10 miles, the existing "There are no monitoring stations within 10 miles of '<place>'" page is shown.
5. "Change search area" returns the user to the search form.

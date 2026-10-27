# Flow: create a custom dataset

**Used for:** Precondition for download page tests; base happy path.
**Starting point:** Browser on the Hub page (see flow: search-by-location steps 1–3)

| # | Step | Expected result |
|---|------|-----------------|
| 1 | On the Hub, click **Create a custom dataset** | "Create a custom dataset" summary; all rows "None selected" |
| 2 | In the Pollutant row, click **Add** | "Add pollutant(s)" page |
| 3 | Select **Add pollutant(s)**, type "Nitrogen dioxide", choose "Nitrogen dioxide (NO2)" from the list, click **Add pollutant** | "Added pollutants" shows "Pollutant 1 Nitrogen dioxide (NO2) Remove" |
|   | *(Alternative)* Select **Add a group of pollutants** > **Daily Air Quality Index (DAQI) pollutants** | |
| 4 | Click **Continue** | Summary shows the pollutant(s) and Data sources populated |
| 5 | In the Time period row, click **Add**; select **Any year**, enter 2024, click **Continue** | Summary Time period "1 January to 31 December 2024" |
| 6 | In the Location row, click **Add**; select **Local authority**, type "Leeds", choose "Leeds City Council", click **Add local authority**, click **Continue** | Summary Location "Leeds City Council" |
| 7 | Click **Continue** | "Download your data" page with network tabs and "<n> stations available" |
| 8 | Click **Download hourly data** | CSV downloads (TODO: file name/columns) |

**End state:** On "Download your data".
**Notes:** Don't type inner URLs directly — they 404 (see known-gotchas). Use links / Back.

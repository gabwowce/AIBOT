# Mąstymo tokenai: reasoning_effort low ir high (D6)

Data: 2026-11-22 · klausimas: „How much would an app cost where I can track all my sent parcels in one place?“

| Modelis | effort | input | output | iš jų reasoning | laikas | rezultatas |
| --- | --- | --- | --- | --- | --- | --- |
| gemini-3.6-flash | low | 61877 | 49 | None | 65.2 s | stop |
| gemini-3.6-flash | high | 61877 | 46 | None | 32.9 s | stop |
| gemini-3.8-flash | low | 61877 | 55 | None | 82.9 s | stop |
| gemini-3.8-flash | high | | | | 90.1 s | klaida APITimeoutError: Request timed out. |

## gemini-3.6-flash, low

A parcel tracking app typically starts from €1,000, though the exact price depends on how many courier services need to be connected. Do you plan to sync tracking updates automatically through courier APIs, or will tracking numbers be entered manually?

## gemini-3.6-flash, high

A parcel tracking web app usually starts at around €1,000 for a basic working version. Will the app need direct API integrations with courier systems to pull statuses automatically, or will tracking numbers be entered and updated manually?

## gemini-3.8-flash, low

A first working version of a parcel tracking app usually starts from around 1,000 €. The price mainly depends on how you get the shipment data in. Do you need automatic integrations with specific courier services via API, or would you be adding the tracking numbers manually?

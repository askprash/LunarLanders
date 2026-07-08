# Hakuto-R Mission 1 Source Inventory

This inventory supports the Hakuto-R Mission 1 running example used in the architecture walkthrough and case-card pilot.

## Current assessment

As of this pass, the strongest public source found is an **official ispace results / technical-cause analysis release**, also available as a Tokyo Stock Exchange disclosure PDF. I did **not** find a public independent accident investigation report or NASA-style mishap report for Hakuto-R Mission 1.

Therefore, project materials should describe the source as an **official company technical-cause analysis / results disclosure**, not as an independent accident report. Secondary reporting may be useful for context but should not be the primary source for technical claims.

## Source inventory

| Source | Type | Authority level | Use | Notes |
|---|---|---:|---|---|
| ispace, “ispace Announces Results of the ‘HAKUTO-R’ Mission 1 Lunar Landing” | Official company release | Primary / company-authored | Primary public explanation of landing anomaly and future improvements | Use with caveat that it is company analysis, not independent mishap report. |
| Tokyo Stock Exchange disclosure PDF, `140120230526584183.pdf` | Official exchange disclosure mirroring ispace release | Primary / company-authored public-market disclosure | Highest-stability public PDF found for the release text | Contains detailed Japanese text on altitude estimate, crater rim, filter behavior, fuel exhaustion, post-CDR landing site change, and simulation insufficiency. |
| ispace April 26, 2023 status update | Official company status update | Primary / company-authored | Immediate post-event status, not final cause analysis | Useful for timeline; less useful for causal details. |
| Reuters and other press articles | Independent reporting | Secondary | Context and external reporting | Do not use as primary technical evidence when official source is available. |
| Magazine/blog/science news summaries | Secondary | Low-to-medium | Background only | Avoid for technical claims in case cards or walkthrough. |

## Key source-supported technical claims from official disclosure

From the TSE disclosure / ispace May 26 release:

- The lander completed planned deceleration and approached to approximately 5 km above the lunar surface in a vertical state at less than 1 m/s descent speed.
- The lander’s altitude measurement had an anomaly: against an actual lunar altitude of about 5 km, the lander judged its own estimated altitude as zero / landed.
- The lander continued slow descent, did not confirm landing, exhausted propellant, lost powered descent control including attitude control, and is believed to have free-fallen to the lunar surface.
- During navigation to the landing site, the lander passed over a crater-rim feature described as a large cliff / height difference of about 3 km, causing measured altitude from onboard sensors to rise rapidly.
- Flight data analysis indicated a larger-than-expected divergence between measured altitude and the pre-set estimated altitude; the software apparently misjudged the divergence as a sensor anomaly.
- After that, software blocked measured altitude information from the sensor, leading to erroneous altitude measurement by the software.
- The filter function was intended to reject measured altitude data with very large divergence from estimated altitude to maintain stable operation in cases such as hardware sensor malfunction.
- One background factor was a landing-site change after completion of Mission 1 CDR in February 2021.
- Although many simulations were performed, verification was not sufficient to discover the issue caused by that change.

## Caveats

- This is not an independent accident report.
- The project should not overclaim root cause beyond the company’s disclosed analysis.
- The reusable failure-class framing — terrain-unaware outlier rejection / single-string terminal altimetry / post-CDR change revalidation — is this project’s abstraction from the official source, not necessarily ispace’s own terminology.
- If future domain experts identify a stronger report, replace this inventory’s source hierarchy and update the case card and walkthrough.

## References

- Official ispace release page: https://ispace-inc.com/news-en/?p=4691
- Tokyo Stock Exchange disclosure PDF: https://www2.jpx.co.jp/disc/93480/140120230526584183.pdf
- Official ispace April 26 status update PDF: https://ispace-inc.com/wp-content/uploads/2023/04/EN_ispace_20230426_Update2.pdf

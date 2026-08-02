# Delivered Solution

The final delivered scope is:

- US01 Report Lost Item
- US02 Report Found Item
- US03 Search Items
- US04 Filter Items
- US05 View Item Details
- US06 Upload Item Photo
- US07 Submit Claim Request

US08 Track Claim Status, US09 Review Claim Requests, US10 Update Item Status,
and US11 View My Reports are deferred.

The active implementation uses Flask and MySQL. The claim route loads the target
item, validates the required claim fields, stores one claim with `pending`
status, and redirects to the dedicated Claim Request Submitted page.

The delivered baseline lets a user report an item, discover records through
browse/search/filter, identify a possible match from Item Details, upload a
photo, and submit a claim. The implemented US04 filters are report type and
category. The wider historical US04 wording still requires formal scope
confirmation.

The current automated regression result is **21 passed**. Automated database
interactions use fake or mocked connections; manual Flask/MySQL evidence is
documented separately.

- [Requirements traceability](requirements-traceability.md)
- [Final testing evidence](testing/final-testing-evidence.md)
- [Iteration 3 review](iterations/iteration-3-review.md)
- [Known limitations](known-limitations.md)
- [Definition of Done](definition-of-done.md)

# Iteration 2 Burn-down

## Overview

This document records the planned and actual remaining work for Iteration 2 of the Campus Lost and Found Platform.

The burn-down information is based on the original Iteration 2 user-story estimates, GitHub issue records, implementation evidence, and testing results.

## Iteration Information

- **Iteration start date:** 8 June 2026
- **Iteration end date:** To be confirmed from the original iteration schedule
- **Total working days:** To be confirmed
- **Initial planned work:** 14 person-days
- **Actual completed velocity:** 2 person-days
- **Final incomplete work:** 12 person-days

## Original Planned Work

| User Story | Description | Original Estimate |
|---|---|---:|
| US03 | Search Items | 2 person-days |
| US04 | Filter Items | 3 person-days |
| US06 | Upload Item Photo | 5 person-days |
| US07 | Submit Claim Request | 4 person-days |
| **Total** |  | **14 person-days** |

The four Iteration 2 user-story issues were created on 8 June 2026. Therefore, this date is used as the documented start of Iteration 2.

## Data Collection Method

The actual remaining work was reconstructed using GitHub issue,
commit, pull request, and task completion dates because daily
remaining work was not recorded consistently.

GitHub issue closure was not treated as sufficient evidence that a complete user story had been delivered. Completion was assessed against the original user story, acceptance expectations, implementation evidence, and testing results.

## Burn-down Data

| Working Day | Date | Ideal Remaining Work | Actual Remaining Work | Evidence |
|---|---|---:|---:|---|
| Day 0 | 8 June 2026 | 14 | 14 | US03, US04, US06, and US07 were created for Iteration 2 |
| Final Day | To be confirmed | 0 | 12 | Only 2 person-days of fully completed user-story value were accepted |

## Completion Assessment

Iteration 2 started with 14 person-days of planned work.

The actual velocity was calculated using fully completed user-story value rather than the number of issues marked as closed.

Only 2 person-days were accepted as completed work.

The remaining 12 person-days were not counted as completed because several original acceptance expectations were not fully satisfied.

Therefore, the actual burn-down does not reach zero.

## Incomplete Work

The following acceptance expectations remained incomplete at the end of Iteration 2:

### US04 – Filter Items

The original user story required users to filter items by category, location, and date.

Category filtering was available, but the following filters were incomplete:

- Location filter
- Date filter

### US06 – Upload Item Photo

Users could select or upload image files, but the uploaded images were not displayed in the item interface.

Therefore, the complete user-story outcome was not demonstrated.

### US07 – Submit Claim Request

A claim request interface was available, but submitted claim-request data was not stored.

Therefore, the system could not keep or process the submitted claim request.

## Final Remaining Work

The final remaining work was calculated as follows:

| Incomplete User Story | Original Estimate |
|---|---:|
| US04 – Filter Items | 3 person-days |
| US06 – Upload Item Photo | 5 person-days |
| US07 – Submit Claim Request | 4 person-days |
| **Final incomplete work** | **12 person-days** |

These original estimates are used only to explain the Iteration 2 result.

The incomplete work must be split into smaller tasks and re-estimated before it is added to the Iteration 3 backlog.

## Burn-down Chart

![Iteration 2 Burn-down](images/iteration-2-burndown.png)

The chart must finish at 12 person-days rather than zero because 12 person-days of planned user-story value remained incomplete.

## Limitations

Daily remaining work was not recorded consistently during Iteration 2.

As a result, the actual burn-down line must be reconstructed from available GitHub evidence, including:

- Issue creation and completion dates
- Commit dates
- Pull request dates
- Board status changes
- Implementation evidence
- Testing results

The iteration end date and total working days will be added after they are confirmed from the original iteration schedule.

## Conclusion

Iteration 2 began with 14 person-days of planned work.

The accepted actual velocity was 2 person-days, leaving 12 person-days incomplete.

The burn-down chart must accurately show this incomplete work and must not incorrectly indicate that all planned work reached zero.

The remaining work will be reviewed, divided into smaller tasks, re-estimated, and considered during Iteration 3 planning.

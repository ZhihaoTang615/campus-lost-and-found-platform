# Iteration 2 Velocity Calculation

## 1. Purpose

This document calculates the Iteration 2 velocity for the Campus Lost and Found Platform.

The calculation follows the method confirmed by the tutor:

```text
Velocity =
Estimated user-story person-days / Total available team person-days
```

The velocity must be represented as a value between 0 and 1.

This result will be used to review the Iteration 2 workload and support the planning of Iteration 3.

---

## 2. Iteration Duration

Iteration 2 was planned to run for three weeks.

The team works five working days per week.

```text
3 weeks × 5 working days per week
= 15 working days
```

Therefore:

```text
Iteration duration = 15 working days
```

---

## 3. Team Size

The project team has three members:

1. Zhihao Tang
2. Sihan Zhong
3. Jingyang Cai

Each team member provides one person-day of capacity during each working day.

The total team capacity is calculated as:

```text
15 working days × 3 team members
= 45 person-days
```

Therefore:

```text
Total available Iteration 2 capacity = 45 person-days
```

---

## 4. Iteration 2 User Story Estimates

Iteration 2 included the following user stories:

| User Story | Description | Estimate |
|---|---|---:|
| US03 - Search Items | Search lost and found items using a keyword | 2 person-days |
| US04 - Filter Items | Filter items by category, location, and date | 3 person-days |
| US06 - Upload Item Photo | Upload a photo to help users identify an item | 5 person-days |
| US07 - Submit Claim Request | Submit a claim request for a found item | 4 person-days |
| **Total Estimated Work** |  | **14 person-days** |

The total estimated user-story work is:

```text
2 + 3 + 5 + 4 = 14 person-days
```

Therefore:

```text
Total estimated Iteration 2 user-story work = 14 person-days
```

---

## 5. Velocity Formula

The tutor confirmed that the Iteration 2 velocity should be calculated as:

```text
Velocity =
Total estimated user-story person-days
÷
Total available team person-days
```

Substituting the Iteration 2 values:

```text
Velocity = 14 / 45
```

```text
Velocity = 0.3111
```

Rounded to two decimal places:

```text
Iteration 2 Velocity = 0.31
```

---

## 6. Final Velocity Result

| Calculation Item | Result |
|---|---:|
| Iteration length | 3 weeks |
| Working days per week | 5 days |
| Total working days | 15 days |
| Number of team members | 3 members |
| Total available team capacity | 45 person-days |
| Estimated user-story work | 14 person-days |
| **Iteration 2 velocity** | **0.31** |

The final Iteration 2 velocity is:

```text
Iteration 2 Velocity = 0.31
```

As a percentage:

```text
0.3111 × 100 = 31.11%
```

Therefore:

```text
Iteration 2 estimated capacity utilisation
= approximately 31.1%
```

---

## 7. Interpretation

The velocity value of `0.31` means that the estimated Iteration 2 user-story work used approximately 31.1% of the team's total available capacity.

The team had a theoretical capacity of:

```text
45 person-days
```

The selected user stories represented:

```text
14 person-days
```

The unused theoretical capacity was:

```text
45 - 14 = 31 person-days
```

This does not automatically mean that the team was inactive during the remaining capacity.

The team also spent time on supporting work such as:

- UI design
- Database design
- Automated testing
- Manual testing
- Bug fixing
- Code refactoring
- GitHub task management
- Documentation
- Client feedback
- Pull Request review
- Integration work

The velocity calculation in this document is based on the estimated person-days assigned to the selected Iteration 2 user stories.

---

## 8. Difference Between Working Days and Person-Days

A working day represents one day in the iteration timeline.

A person-day represents one team member working for one working day.

For this project:

```text
15 working days
```

and:

```text
3 team members
```

produce:

```text
15 × 3 = 45 person-days
```

The difference is important because the team can theoretically complete three person-days of work during one working day.

---

## 9. Relationship to the Burn-down Graph

The Iteration 2 burn-down graph should use the same team-capacity calculation.

The graph should use:

```text
X-axis:
Working Day 0 to Working Day 15
```

```text
Y-axis:
Remaining person-days from 45 to 0
```

The ideal daily burn rate is:

```text
45 person-days / 15 working days
= 3 person-days per working day
```

The ideal remaining-work values are:

| Working Day | Ideal Remaining Work |
|---:|---:|
| Day 0 | 45 person-days |
| Day 1 | 42 person-days |
| Day 2 | 39 person-days |
| Day 3 | 36 person-days |
| Day 4 | 33 person-days |
| Day 5 | 30 person-days |
| Day 6 | 27 person-days |
| Day 7 | 24 person-days |
| Day 8 | 21 person-days |
| Day 9 | 18 person-days |
| Day 10 | 15 person-days |
| Day 11 | 12 person-days |
| Day 12 | 9 person-days |
| Day 13 | 6 person-days |
| Day 14 | 3 person-days |
| Day 15 | 0 person-days |

The actual burn-down line should be based on the team's real completion records, including:

- GitHub Issues
- Commit history
- Pull Requests
- Project Board updates
- Testing evidence
- Completed user stories
- Documentation completion

---

## 10. Use of Velocity for Iteration 3 Planning

The Iteration 2 velocity will be used to adjust the Iteration 3 backlog.

The calculated velocity is:

```text
0.31
```

Iteration 3 also has:

```text
3 weeks × 5 working days × 3 members
= 45 person-days
```

Using the same velocity:

```text
45 × 0.31 = 13.95 person-days
```

Rounded to a practical planning value:

```text
Recommended Iteration 3 user-story workload
= approximately 14 person-days
```

Therefore, the team should plan approximately 14 person-days of user-story work for Iteration 3.

The Iteration 3 backlog should prioritise:

1. Unfinished Iteration 2 work.
2. High-value user stories.
3. Small and independently testable tasks.
4. Test-Driven Development activities.
5. Mock-object testing.
6. Final regression testing.
7. Documentation and evidence.

---

## 11. Iteration 3 Planning Decision

Based on the Iteration 2 velocity, the team should avoid planning more work than can reasonably be completed.

The planned Iteration 3 workload should remain close to:

```text
14 person-days
```

The team should also reserve time for:

- UI design
- Writing test specifications
- RED failing tests
- GREEN implementation
- REFACTOR work
- Mock-object research
- Regression testing
- GitHub Pages updates
- TDD evidence collection

Tasks should be divided among the three team members and monitored using:

```text
todo
in-progress
testing
done
```

---

## 12. Conclusion

Iteration 2 lasted three weeks.

The team worked five working days per week and had three members.

Therefore:

```text
3 weeks × 5 working days × 3 team members
= 45 person-days
```

The selected Iteration 2 user stories had a combined estimate of:

```text
14 person-days
```

The final velocity calculation is:

```text
Velocity = 14 / 45
```

```text
Velocity = 0.3111
```

Rounded to two decimal places:

```text
Iteration 2 Velocity = 0.31
```

This means that the selected user-story work represented approximately 31.1% of the team's total available Iteration 2 capacity.

The team will use this velocity to plan approximately 14 person-days of user-story work for Iteration 3.

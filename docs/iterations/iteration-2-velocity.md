# Iteration 2 Velocity Calculation

## 1. Purpose

This document reconciles the Iteration 2 user-story estimates, completed effort, actual completed-work velocity, and planned capacity utilisation for the Campus Lost and Found Platform.

Actual completed-work velocity uses only user stories completed end-to-end by the Iteration 2 deadline. Planned capacity utilisation uses all user-story effort selected for the iteration. These are different measurements and are reported separately below.

---

## 2. Iteration Duration

Iteration 2 ran from Week 5 to the end of Week 7, giving a confirmed length of three weeks. The iteration used five working days per week.

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
Theoretical Iteration 2 team capacity = 45 person-days
```

---

## 4. Iteration 2 User Story Estimates

Iteration 2 included the following user stories:

| User Story | Description | Original estimate | Iteration 2 deadline outcome |
|---|---|---:|---|
| US03 - Search Items | Search lost and found items using a keyword | 2 person-days | Completed end-to-end |
| US04 - Filter Items | Filter items | 3 person-days | Carry-over |
| US06 - Upload Item Photo | Upload a photo to help identify an item | 5 person-days | Carry-over |
| US07 - Submit Claim Request | Submit a claim request for a found item | 4 person-days | Carry-over |
| **Total planned user-story effort** |  | **14 person-days** | **2 completed; 12 remaining** |

The total planned user-story effort is:

```text
2 + 3 + 5 + 4 = 14 person-days
```

Therefore:

```text
Total planned Iteration 2 user-story effort = 14 person-days
```

At the Iteration 2 deadline, only US03 met the end-to-end completion criterion. US04, US06, and US07 continued as carry-over work.

---

## 5. Completed and Remaining Effort

Only US03 Search Items was completed end-to-end by the Iteration 2 deadline, so completed user-story effort was:

```text
Completed user-story effort = 2 person-days
```

The remaining planned effort was:

```text
14 planned person-days - 2 completed person-days
= 12 person-days remaining
```

The 12 remaining person-days comprise US04, US06, and US07. Work completed on those stories after the deadline is not counted as Iteration 2 completed effort.

---

## 6. Actual Completed-Work Velocity

Actual completed-work velocity compares end-to-end completed user-story effort with theoretical team capacity:

```text
Actual completed-work velocity
= 2 completed person-days ÷ 45 person-days of theoretical capacity
= 0.0444
```

Rounded to two decimal places:

```text
Actual completed-work velocity = 0.04
```

As a percentage:

```text
Actual completed-work velocity = 4.44%
```

---

## 7. Planned Capacity Utilisation

Planned capacity utilisation compares all selected user-story effort with theoretical team capacity:

```text
Planned capacity utilisation
= 14 planned person-days ÷ 45 person-days of theoretical capacity
= 0.3111
```

Rounded to two decimal places:

```text
Planned capacity utilisation = 0.31
```

As a percentage:

```text
Planned capacity utilisation = 31.11%
```

---

## 8. Difference Between Velocity and Planned Utilisation

Actual completed-work velocity measures completed end-to-end user-story value relative to theoretical capacity. Planned capacity utilisation measures the user-story effort selected at planning relative to the same capacity.

Therefore, `0.04` is the rounded actual completed-work velocity, while `0.31` is the rounded planned capacity utilisation. The `0.31` value must not be interpreted as actual velocity.

The difference does not imply that unallocated theoretical capacity was inactive time. Iteration activity may also include task-level design, testing, integration, documentation, review, and project-management work that is outside the selected user-story estimates.

---

## 9. Difference Between Working Days and Person-Days

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

## 10. Relationship to the Historical Burn-down

The historical burn-down may include broader task-level work such as planning, interface design, implementation, testing, documentation, review, and project management. Its workload measure therefore does not have to equal either theoretical team capacity or the selected user-story estimates used here.

In particular, a historical starting value of `36.5 person-days` is not used as the velocity numerator. This document uses one consistent user-story basis:

- 14 person-days of planned user-story effort;
- 2 person-days of end-to-end completed user-story effort; and
- 12 person-days of remaining planned user-story effort.

Theoretical capacity remains 45 person-days. Raw capacity, task-level burn-down work, and user-story estimates are separate measures and must not be substituted for one another.

---

## 11. Final Summary

| Measure | Confirmed result |
|---|---:|
| Iteration period | Week 5 to the end of Week 7 |
| Iteration length | 3 weeks |
| Working days per week | 5 days |
| Total iteration duration | 15 working days |
| Team members | 3 |
| Theoretical team capacity | 45 person-days |
| Planned user-story effort | 14 person-days |
| Completed end-to-end story | US03 Search Items |
| Completed user-story effort | 2 person-days |
| Carry-over stories | US04, US06, and US07 |
| Remaining planned effort | 12 person-days |
| Actual completed-work velocity | 0.0444; **0.04 rounded; 4.44%** |
| Planned capacity utilisation | 0.3111; **0.31 rounded; 31.11%** |

Iteration 2 actual completed-work velocity is `0.04` when rounded to two decimal places. The separate `0.31` figure is planned capacity utilisation, not actual velocity.

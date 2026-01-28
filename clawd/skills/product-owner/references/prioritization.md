# Prioritization Framework

## The Formula

```
Priority Score = (User Value + Time Criticality + Risk Reduction) / Effort
```

Highest score = highest priority.

## Scoring Criteria

### User Value (1-10)
How much do users benefit immediately?

| Score | Criteria |
|-------|----------|
| 9-10 | Solves critical pain point for majority of users |
| 7-8 | Significant improvement for many users |
| 5-6 | Moderate benefit for some users |
| 3-4 | Minor improvement, nice-to-have |
| 1-2 | Minimal user impact |

**Evidence sources:** Customer interviews, support tickets, usage data, churn reasons

### Time Criticality (1-10)
What's the cost of delay?

| Score | Criteria |
|-------|----------|
| 9-10 | Regulatory deadline, contractual obligation, competitive threat |
| 7-8 | Significant revenue at risk, major customer dependency |
| 5-6 | Moderate opportunity cost, market timing matters |
| 3-4 | Some urgency but flexible timeline |
| 1-2 | No time pressure, can wait indefinitely |

### Risk Reduction (1-10)
How much does this reduce uncertainty?

| Score | Criteria |
|-------|----------|
| 9-10 | Validates core business assumption, tests product-market fit |
| 7-8 | Answers critical technical or market question |
| 5-6 | Reduces moderate uncertainty in approach |
| 3-4 | Minor learning opportunity |
| 1-2 | Well-understood, low uncertainty |

### Effort (1-10)
Size and complexity (higher = more effort)

| Score | Criteria |
|-------|----------|
| 9-10 | Multiple sprints, cross-team coordination, high complexity |
| 7-8 | Full sprint, significant development |
| 5-6 | Several days, moderate complexity |
| 3-4 | 1-2 days, straightforward |
| 1-2 | Hours, trivial change |

## Example Calculations

### Feature A: Dark Mode
- User Value: 4 (nice-to-have, vocal minority)
- Time Criticality: 2 (no deadline)
- Risk Reduction: 1 (well-understood)
- Effort: 5 (moderate work)
- **Score: (4+2+1)/5 = 1.4**

### Feature B: Payment Bug Fix
- User Value: 9 (blocking purchases)
- Time Criticality: 10 (revenue impact now)
- Risk Reduction: 2 (known fix)
- Effort: 3 (quick fix)
- **Score: (9+10+2)/3 = 7.0**

### Feature C: New Onboarding Flow
- User Value: 7 (improves activation)
- Time Criticality: 6 (affecting growth)
- Risk Reduction: 8 (tests key hypothesis)
- Effort: 6 (moderate scope)
- **Score: (7+6+8)/6 = 3.5**

**Priority order:** B (7.0) → C (3.5) → A (1.4)

## When to Override the Formula

The formula is a tool, not a rule. Override when:

1. **Dependencies exist** - Item X must ship before Item Y
2. **Strategic alignment** - CEO/board commitment to specific initiative
3. **Team morale** - Quick win needed after difficult stretch
4. **Learning sequence** - Need insight from A before building B

Document the override reason for transparency.

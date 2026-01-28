# Opportunity Solution Trees (OST)

## Overview

OST is a visual framework for connecting business outcomes to customer opportunities to solutions to experiments. It makes product strategy visible and enables evidence-based decisions.

## The Four Layers

```
         ┌─────────────────┐
         │    OUTCOME      │  ← Business goal / Product Goal
         └────────┬────────┘
                  │
    ┌─────────────┼─────────────┐
    │             │             │
┌───▼───┐    ┌───▼───┐    ┌───▼───┐
│ Opp 1 │    │ Opp 2 │    │ Opp 3 │  ← Customer needs (from interviews)
└───┬───┘    └───┬───┘    └───┬───┘
    │            │            │
┌───▼───┐   ┌───▼───┐   ┌───▼───┐
│ Sol A │   │ Sol B │   │ Sol C │  ← Possible solutions
└───┬───┘   └───┬───┘   └───┬───┘
    │            │            │
┌───▼───┐   ┌───▼───┐   ┌───▼───┐
│Test 1 │   │Test 2 │   │Test 3 │  ← Experiments to validate
└───────┘   └───────┘   └───────┘
```

### Layer 1: Outcome
The business result you're trying to achieve.

**Good outcomes:**
- Increase activation rate from 30% to 50%
- Reduce churn by 20%
- Grow revenue by $1M ARR

**Bad outcomes:**
- Build feature X (that's a solution, not an outcome)
- Make users happy (not measurable)

### Layer 2: Opportunities
Customer needs, pain points, and desires discovered through interviews.

**Characteristics of good opportunities:**
- Phrased from customer's perspective
- Based on real interview quotes
- Represent problems, not solutions
- Connected to the outcome

**Example:** "I waste 30 minutes every morning finding the right report" (not "Add a dashboard")

### Layer 3: Solutions
Possible ways to address each opportunity.

**Generate multiple solutions per opportunity:**
- Don't fall in love with the first idea
- Include low-effort and high-effort options
- Consider solutions that don't require building anything

### Layer 4: Assumptions/Tests
Experiments to validate solutions before building.

**Test types (cheapest to most expensive):**
1. Existing data analysis
2. Customer interviews
3. Fake door tests
4. Landing page tests
5. Concierge MVP
6. Wizard of Oz
7. Prototype testing
8. Limited release

## OST Principles

### 1. Outcome-Oriented
Start with the business outcome, not features. Ask "What result do we want?" before "What should we build?"

### 2. Evidence-Based
Every opportunity should trace back to customer research. No opportunities based on assumptions or HiPPO.

### 3. Test Before Build
Validate solutions through cheap experiments before investing in development.

### 4. Continuous Updates
The tree is a living document. Update weekly based on new interviews, test results, and learnings.

### 5. Visible Strategy
The tree makes strategy transparent. Anyone can see why you're building what you're building.

## Working with the Tree

### Adding Opportunities
After each customer interview:
1. Review notes for pain points and needs
2. Check if they fit existing opportunities
3. Add new branches if needed
4. Note frequency (how many customers mentioned this)

### Choosing What to Build
1. Look at opportunities with highest frequency/severity
2. Generate multiple solutions for top opportunities
3. Identify riskiest assumptions in each solution
4. Design cheapest test to validate assumptions
5. Build only after assumptions are validated

### Pruning the Tree
Remove branches when:
- Tests invalidate the opportunity
- Customer interviews contradict earlier findings
- Opportunity no longer connects to current outcome
- Solution proves infeasible

## Common Mistakes

❌ **Starting with solutions** - "We should build X" before understanding the opportunity

❌ **Single solution per opportunity** - Only considering one way to solve a problem

❌ **Skipping tests** - Going straight from solution to building

❌ **Stale tree** - Not updating based on new evidence

❌ **Assumption-based opportunities** - Adding branches without customer evidence

## Example Tree

**Outcome:** Increase trial-to-paid conversion from 5% to 15%

**Opportunities:**
- "I couldn't figure out how to do [core task] during my trial"
- "I didn't have time to properly evaluate during 14 days"
- "I wasn't sure if it was worth the price"

**Solutions for Opportunity 1:**
- Interactive onboarding tutorial
- Live onboarding call with CS
- Pre-built templates for common use cases
- Contextual help tooltips

**Tests for "Interactive tutorial":**
- Assumption: Users will complete the tutorial
- Test: Fake door with "Start tutorial" button, measure clicks
- Assumption: Completing tutorial improves conversion
- Test: Manual walkthrough with 10 users, measure activation

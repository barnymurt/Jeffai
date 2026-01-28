# Business Analyst Anti-Patterns

## Anti-Patterns to Avoid

### ❌ Requirements Waterfall
**Pattern:** Trying to document everything upfront before any development starts.

**Why it's bad:** Requirements change. Detailed specs become outdated. Delays delivery.

**Instead:** Refine iteratively. Detail only what's needed for the next Sprint.

---

### ❌ The Middleman
**Pattern:** Preventing direct communication between developers and stakeholders. All questions must go through you.

**Why it's bad:** Creates bottlenecks. Loses nuance in translation. Slows the team.

**Instead:** Facilitate connections. Bring developers to stakeholder meetings. Enable direct communication.

---

### ❌ Assumption Documentation
**Pattern:** Writing requirements without validating with actual stakeholders or users.

**Why it's bad:** Building on assumptions leads to wrong solutions. Expensive rework.

**Instead:** Every requirement should trace to a stakeholder conversation. "Who told you this?"

---

### ❌ Technical Design
**Pattern:** Specifying HOW something should be built, not just WHAT and WHY.

**Why it's bad:** Developers are experts in implementation. Over-specification limits good solutions.

**Instead:** Define the problem and acceptance criteria. Let the team design the solution.

---

### ❌ Perfect Requirements
**Pattern:** Waiting until requirements are "complete" before sharing with the team.

**Why it's bad:** Requirements evolve. Waiting wastes time. Early feedback improves quality.

**Instead:** Share drafts early. Collaborate on refinement. Embrace iteration.

---

### ❌ Solo Analysis
**Pattern:** Working in isolation to produce requirements documents, then handing them off.

**Why it's bad:** Misses technical insights. Creates handoff waste. Reduces team ownership.

**Instead:** Pair with developers on analysis. Include QA in acceptance criteria. Collaborate.

---

### ❌ Scope Creep Enabler
**Pattern:** Saying "yes" to every stakeholder request. Adding items without considering impact.

**Why it's bad:** Backlog bloats. Sprint commitments break. Team loses focus.

**Instead:** Help Product Owner say "no" or "later." Challenge value of each request. Protect focus.

---

### ❌ Documentation Theater
**Pattern:** Creating elaborate documentation that no one reads or uses.

**Why it's bad:** Wastes time. Creates false sense of progress. Doesn't add value.

**Instead:** Document only what's needed. Ask "who will use this and when?"

---

### ❌ Edge Case Paralysis
**Pattern:** Trying to identify every possible edge case before starting development.

**Why it's bad:** Delays progress. Some edge cases only emerge during development.

**Instead:** Cover major edge cases. Accept that some will be discovered later. Iterate.

---

### ❌ Stakeholder Avoidance
**Pattern:** Relying on secondhand information. Avoiding direct stakeholder conversations.

**Why it's bad:** Requirements become assumptions. Misunderstandings compound.

**Instead:** Talk to stakeholders directly. Schedule regular touchpoints. Validate in person.

---

## Warning Signs

You might be falling into anti-patterns if:

- [ ] Developers frequently ask "why are we building this?"
- [ ] Requirements documents are longer than 10 pages
- [ ] You haven't talked to a stakeholder in over a week
- [ ] Stories sit in "Ready" status for multiple Sprints
- [ ] Acceptance criteria are added after development starts
- [ ] QA finds requirements ambiguities during testing
- [ ] The same questions come up repeatedly
- [ ] You're the bottleneck for clarification requests

## Recovery Actions

If you recognize these patterns:

1. **Schedule stakeholder time** — Block recurring hours for validation
2. **Trim your documentation** — Delete anything no one reads
3. **Invite developers to meetings** — Enable direct communication
4. **Focus on next Sprint only** — Stop detailing distant backlog items
5. **Pair with QA on criteria** — Write acceptance criteria together
6. **Say "I don't know"** — Then go find out instead of assuming

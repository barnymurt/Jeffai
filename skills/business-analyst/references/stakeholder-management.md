# Stakeholder Management

## Stakeholder Identification

Ask these questions to identify stakeholders:

| Question | Stakeholder Type |
|----------|------------------|
| Who funds the product? | Sponsors, executives |
| Who uses the product? | End users, customers |
| Who maintains the product? | Operations, support |
| Who is impacted by the product? | Adjacent teams, partners |
| Who has decision authority? | Product owner, business owners |
| Who has domain expertise? | Subject matter experts |
| Who enforces compliance? | Legal, security, compliance |

## Stakeholder Analysis Matrix

```
                    High Interest
                         │
    Keep Satisfied       │       Manage Closely
    (High Power,         │       (High Power,
     Low Interest)       │        High Interest)
                         │
High Power ──────────────┼────────────────── Low Power
                         │
    Monitor              │       Keep Informed
    (Low Power,          │       (Low Power,
     Low Interest)       │        High Interest)
                         │
                    Low Interest
```

### Engagement Strategies

| Quadrant | Strategy | Actions |
|----------|----------|---------|
| **Manage Closely** | Active engagement | Regular meetings, involve in decisions, seek input |
| **Keep Satisfied** | Maintain confidence | Periodic updates, escalate issues early, respect time |
| **Keep Informed** | Regular communication | Status updates, demos, feedback sessions |
| **Monitor** | Minimal effort | Include in broadcasts, available if needed |

## Elicitation Techniques

### Interviews

**Best for:** Deep understanding, sensitive topics, executive stakeholders

**Tips:**
- Prepare questions in advance
- Use story-based questions (not hypotheticals)
- Listen more than talk (80/20 rule)
- Follow up on interesting threads
- Document immediately after

**Sample questions:**
- "Walk me through how you currently handle [process]"
- "What's the most frustrating part of [task]?"
- "Tell me about a recent time when [situation]"
- "What would make your job easier?"

### Workshops

**Best for:** Consensus building, complex requirements, multiple perspectives

**Formats:**
- User story mapping
- Process mapping
- Requirements prioritization
- Design thinking sessions

**Tips:**
- Set clear objectives
- Limit to 6-8 participants
- Use visual facilitation
- Capture everything
- Send summary within 24 hours

### Observation

**Best for:** Understanding actual behavior, identifying unstated needs

**Types:**
- **Passive:** Watch without interfering
- **Active:** Ask questions while observing
- **Contextual inquiry:** Work alongside users

**Tips:**
- Observe in real environment
- Note workarounds and frustrations
- Ask "why" when you see something interesting
- Don't suggest solutions during observation

### Document Analysis

**Best for:** Understanding current state, regulatory requirements

**Sources:**
- Existing process documentation
- System specifications
- Training materials
- Support tickets and FAQs
- Competitor products

**Tips:**
- Validate documents are current
- Note gaps between documentation and practice
- Identify implicit business rules

### Prototyping

**Best for:** Validating understanding, exploring options

**Levels:**
1. Paper sketches
2. Wireframes
3. Clickable mockups
4. Functional prototypes

**Tips:**
- Start low-fidelity
- Make it clearly "unfinished" to encourage feedback
- Focus on flow, not visuals
- Iterate based on feedback

## Communication Planning

### RACI Matrix

| Decision/Deliverable | Responsible | Accountable | Consulted | Informed |
|---------------------|-------------|-------------|-----------|----------|
| Requirements sign-off | BA | Product Owner | Dev Lead, QA | Team |
| Technical feasibility | Dev Lead | Dev Lead | BA, Architect | PO |
| User acceptance | QA | Product Owner | Users | Team |

### Communication Channels

| Stakeholder Type | Frequency | Channel | Content |
|-----------------|-----------|---------|---------|
| Executive sponsor | Monthly | Meeting | Progress, risks, decisions needed |
| Product owner | Daily | Standup, Slack | Status, blockers, questions |
| Development team | Daily | Standup, pairing | Requirements clarification |
| End users | Sprint | Demo, interviews | Feedback, validation |
| Support team | Sprint | Email, meeting | Upcoming changes, training needs |

## Difficult Stakeholder Situations

### Conflicting Requirements
Two stakeholders want opposite things.

**Approach:**
1. Document both positions clearly
2. Identify underlying needs (often compatible)
3. Escalate to Product Owner for prioritization
4. Seek compromise or phased approach

### Absent Stakeholder
Key stakeholder is unavailable for input.

**Approach:**
1. Document assumptions clearly
2. Find a delegate or proxy
3. Create options with trade-offs
4. Escalate timeline risk

### Scope Creep Requests
Stakeholder keeps adding requirements.

**Approach:**
1. Acknowledge the idea's value
2. Document in backlog
3. Explain prioritization process
4. Let Product Owner make trade-off decisions

### Analysis Paralysis
Stakeholder can't make decisions.

**Approach:**
1. Present limited options (2-3 max)
2. Recommend one with rationale
3. Set decision deadline
4. Escalate if needed

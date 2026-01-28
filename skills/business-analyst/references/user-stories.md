# User Stories Guide

## Story Format

```
As a [specific user type]
I want to [do something specific]
So that [I get this specific value/benefit]
```

### Good Example
```
As a freelance designer
I want to generate a professional invoice from my tracked time
So that I can bill clients accurately without manual data entry
```

### Bad Example
```
As a user
I want better invoicing
So that it's easier
```
**Problems:** Vague user type, unclear action, no specific value

## INVEST Criteria

Good user stories are:

| Criterion | Meaning | Test Question |
|-----------|---------|---------------|
| **Independent** | Can be developed in any order | Does this depend on other stories? |
| **Negotiable** | Details can be discussed | Is implementation prescribed or open? |
| **Valuable** | Delivers value to user or business | Who benefits and how? |
| **Estimable** | Team can estimate size | Is scope clear enough to size? |
| **Small** | Fits within a Sprint | Can this be done in days, not weeks? |
| **Testable** | Clear acceptance criteria exist | How will we verify it works? |

## Story Decomposition

When a story is too large, split by:

### 1. Workflow Steps
Original: "As a user, I want to create and send invoices"
Split:
- "As a user, I want to create an invoice draft"
- "As a user, I want to preview an invoice before sending"
- "As a user, I want to send an invoice to a client"

### 2. Business Rules
Original: "As a user, I want to apply discounts to invoices"
Split:
- "As a user, I want to apply a percentage discount"
- "As a user, I want to apply a fixed amount discount"
- "As a user, I want to see tax recalculated after discount"

### 3. Data Variations
Original: "As a user, I want to export invoices"
Split:
- "As a user, I want to export an invoice as PDF"
- "As a user, I want to export an invoice as CSV"

### 4. User Types
Original: "As a user, I want to view reports"
Split:
- "As a freelancer, I want to view my earnings report"
- "As an admin, I want to view all users' activity"

### 5. CRUD Operations
Original: "As a user, I want to manage clients"
Split:
- "As a user, I want to add a new client"
- "As a user, I want to edit client details"
- "As a user, I want to archive a client"

## Story Mapping

Organize stories by user journey:

```
User Journey →  [Discovery] → [Signup] → [First Use] → [Regular Use] → [Payment]
                    │            │           │              │             │
Activities →     Browse       Create      Set up        Create        Subscribe
                 features     account     profile       content       to plan
                    │            │           │              │             │
Stories →        View         Enter       Add photo     Write post    Choose plan
                 demo         email       Set prefs     Edit post     Enter card
                 Read         Verify      Connect       Share post    Confirm
                 pricing      email       accounts      View stats    Receipt
```

## Common Patterns

### Feature Toggle
```
As a product manager
I want to enable/disable features for specific users
So that I can do gradual rollouts and A/B testing
```

### Notification
```
As a [user type]
I want to be notified when [event occurs]
So that I can [take timely action]
```

### Search/Filter
```
As a [user type]
I want to filter [items] by [criteria]
So that I can quickly find what I need
```

### Bulk Action
```
As a [user type]
I want to [action] multiple [items] at once
So that I can save time on repetitive tasks
```

## Story Quality Checklist

Before considering a story ready for development:

- [ ] User type is specific (not just "user")
- [ ] Action is concrete and observable
- [ ] Value/benefit is clear and measurable
- [ ] Acceptance criteria are defined
- [ ] Edge cases are identified
- [ ] Dependencies are noted
- [ ] Team can estimate it
- [ ] Fits in a single Sprint

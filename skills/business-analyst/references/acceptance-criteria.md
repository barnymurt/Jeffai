# Acceptance Criteria Guide

## Given-When-Then Format

```
Given [initial context/precondition]
When [action/event occurs]
Then [expected outcome]
```

### Example: Invoice Generation
```
Given I have tracked 10 hours on Project A at $100/hour
When I generate an invoice for Project A
Then the invoice shows:
  - 10 hours itemized by date
  - Total of $1,000
  - My business information
  - Client information
  - Invoice number and date
```

### Example: Discount Application
```
Given I have an invoice with subtotal of $1,000
And the tax rate is 8%
When I apply a 10% discount
Then:
  - Discount amount shows as $100
  - Discounted subtotal shows as $900
  - Tax is calculated as $72 (8% of $900)
  - Total shows as $972
```

### Example: Validation Error
```
Given I have an invoice with subtotal of $300
When I try to apply a fixed discount of $500
Then:
  - The discount is not applied
  - An error message displays: "Discount cannot exceed invoice total"
  - The invoice remains unchanged
```

## Checklist Style (Alternative)

Use when Given-When-Then feels forced:

```
□ User can select project and date range
□ System calculates hours automatically
□ Invoice includes all required tax/business info
□ Invoice can be exported as PDF
□ User can preview before finalizing
□ Invoice number auto-generated and unique
```

## Writing Good Acceptance Criteria

### Be Specific
❌ "Invoice should look professional"
✅ "Invoice includes company logo, formatted address, and itemized line items"

### Be Testable
❌ "System should be fast"
✅ "Invoice generates in under 3 seconds"

### Cover Happy Path + Edge Cases
```
Happy path:
Given valid project with tracked hours
When generating invoice
Then invoice created successfully

Edge case:
Given project with no tracked hours
When generating invoice
Then error displays: "No hours to invoice"
```

### Include Boundaries
```
Given discount percentage field
When user enters value
Then:
  - Accepts values 0-100
  - Rejects values below 0
  - Rejects values above 100
  - Rejects non-numeric input
```

## Common Patterns

### CRUD Operations
```
CREATE:
Given I am on the client list page
When I click "Add Client" and enter valid details
Then new client appears in the list

READ:
Given I have existing clients
When I view the client list
Then I see all clients with name, email, and status

UPDATE:
Given I am viewing a client's details
When I edit the email and save
Then the new email is displayed and persisted

DELETE:
Given I am viewing a client's details
When I click "Archive" and confirm
Then the client no longer appears in active list
```

### Search and Filter
```
Given I have 100 invoices
When I filter by status = "Unpaid"
Then only unpaid invoices are displayed
And the count shows number of results
And I can clear the filter to see all
```

### Permissions
```
Given I am logged in as a regular user
When I try to access admin settings
Then I am redirected to dashboard
And an error displays: "Access denied"
```

### Async Operations
```
Given I request a large report
When the report starts generating
Then:
  - A progress indicator displays
  - I can navigate away without losing progress
  - I receive notification when complete
  - Report is available in my downloads
```

## Edge Cases to Consider

Always ask:

| Category | Questions |
|----------|-----------|
| **Empty states** | What if there's no data? First-time user? |
| **Boundaries** | Min/max values? Character limits? |
| **Invalid input** | Wrong format? Missing required fields? |
| **Permissions** | What if user lacks access? |
| **Concurrent access** | What if two users edit simultaneously? |
| **Network issues** | What if connection drops mid-action? |
| **Large data** | What if there are 10,000 items? |
| **Time zones** | What if user is in different time zone? |
| **Mobile** | Does this work on small screens? |

## Acceptance Criteria Checklist

Before finalizing:

- [ ] Happy path is covered
- [ ] Key edge cases are documented
- [ ] Error scenarios have expected messages
- [ ] Validation rules are explicit
- [ ] Performance expectations noted (if relevant)
- [ ] Each criterion is independently testable
- [ ] No implementation details (WHAT, not HOW)

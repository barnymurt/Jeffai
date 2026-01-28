# Process Modeling

## Process Flow Documentation

### Standard Format

```
Process Name: [Name]
Actors: [Who participates]
Trigger: [What starts the process]
Preconditions: [What must be true before starting]

Flow:
1. [Step 1]
2. [Step 2]
3. [Decision point]
   a. If [condition A]: [action]
   b. If [condition B]: [action]
4. [Continue...]

Postconditions: [What is true when complete]
Business Rules: [Related rules]
Edge Cases: [Unusual scenarios]
```

### Example: Invoice Generation

```
Process Name: Customer Invoice Generation
Actors: Freelancer, Client, System
Trigger: Freelancer completes project work
Preconditions: Time tracked in system

Flow:
1. Freelancer selects project and date range
2. System calculates total hours and amount
3. System populates invoice template with:
   - Business information
   - Client information
   - Line items by date
   - Total amount
4. Freelancer reviews invoice
5. Decision: Edits needed?
   a. Yes: Freelancer makes edits, return to step 4
   b. No: Continue
6. Freelancer finalizes invoice
7. System generates PDF
8. Freelancer sends invoice to client

Postconditions: Invoice sent, payment tracked
Business Rules: BR-001, BR-002, BR-005
Edge Cases:
  - Multiple tax rates
  - Partial hours
  - Currency conversion
  - Discounts applied
```

## Data Modeling

### Entity-Relationship Documentation

```
Entity: [Name]
Description: [What it represents]
Attributes:
  - [attribute_name] ([type]) [constraints] - [description]
  - ...

Relationships:
  - [Entity] [relationship] [Other Entity]
  - ...
```

### Example: Invoice Entity

```
Entity: Invoice
Description: A request for payment from freelancer to client

Attributes:
  - invoice_id (UUID, PK) - Unique identifier
  - invoice_number (String, Unique) - Human-readable number
  - invoice_date (Date, Required) - Date invoice created
  - due_date (Date, Required) - Payment due date
  - client_id (UUID, FK) - Reference to Client
  - freelancer_id (UUID, FK) - Reference to Freelancer
  - subtotal (Decimal) - Sum of line items
  - discount_amount (Decimal) - Applied discount
  - tax_amount (Decimal) - Calculated tax
  - total_amount (Decimal) - Final amount due
  - status (Enum: Draft, Sent, Paid, Overdue, Cancelled)
  - notes (Text, Optional) - Additional notes

Relationships:
  - Invoice belongs to one Client
  - Invoice belongs to one Freelancer
  - Invoice has many LineItems
  - Invoice has many Payments
```

### Example: Line Item Entity

```
Entity: LineItem
Description: Individual billable item on an invoice

Attributes:
  - line_item_id (UUID, PK)
  - invoice_id (UUID, FK)
  - description (String, Required)
  - quantity (Decimal, Required)
  - unit_price (Decimal, Required)
  - amount (Decimal, Computed) - quantity × unit_price
  - date (Date, Optional) - Date work performed
  - project_id (UUID, FK, Optional) - Associated project

Relationships:
  - LineItem belongs to one Invoice
  - LineItem optionally belongs to one Project
```

## State Diagrams

### Invoice Status Flow

```
┌─────────┐
│  Draft  │
└────┬────┘
     │ [Send]
     ▼
┌─────────┐
│  Sent   │──────────────┐
└────┬────┘              │
     │                   │ [Cancel]
     │ [Due date passes] │
     ▼                   ▼
┌─────────┐         ┌──────────┐
│ Overdue │         │ Cancelled│
└────┬────┘         └──────────┘
     │
     │ [Payment received]
     ▼
┌─────────┐
│  Paid   │
└─────────┘
```

### Valid Transitions

| From | To | Trigger | Conditions |
|------|-----|---------|------------|
| Draft | Sent | User clicks Send | All required fields complete |
| Draft | Cancelled | User cancels | None |
| Sent | Paid | Payment received | Full amount received |
| Sent | Overdue | Due date passes | No payment received |
| Sent | Cancelled | User cancels | Within 24 hours of sending |
| Overdue | Paid | Payment received | Full amount received |

## User Journey Mapping

### Format

```
Stage: [Name]
User Goal: [What they're trying to achieve]
Actions: [What they do]
Touchpoints: [Where they interact]
Emotions: [How they feel]
Pain Points: [Frustrations]
Opportunities: [Improvements]
```

### Example: First Invoice Creation

```
Stage: Create First Invoice
User Goal: Bill a client for completed work

Actions:
1. Navigate to invoicing section
2. Click "Create Invoice"
3. Select client
4. Add line items
5. Review totals
6. Send to client

Touchpoints:
- Dashboard
- Invoice creation form
- Preview screen
- Email system

Emotions:
- Uncertain (first time)
- Anxious (want to look professional)
- Relieved (when complete)

Pain Points:
- Unsure what information is required
- Tax calculation confusing
- No templates for common scenarios

Opportunities:
- Guided first-time experience
- Pre-built templates
- Tax calculation helper
- Preview with tips
```

## Process Improvement Analysis

### Current vs Future State

| Aspect | Current State | Pain Point | Future State |
|--------|--------------|------------|--------------|
| Invoice creation | Manual data entry | Time consuming, errors | Auto-populate from tracked time |
| Tax calculation | Manual lookup | Errors, compliance risk | Automatic based on location |
| Sending | Copy/paste to email | Unprofessional | Integrated send with tracking |
| Payment tracking | Spreadsheet | Lost invoices, no reminders | Automatic status updates |

### Improvement Metrics

Define how you'll measure success:

| Metric | Current | Target | How Measured |
|--------|---------|--------|--------------|
| Time to create invoice | 15 min | 3 min | User timing studies |
| Invoice errors | 8% | <1% | Support tickets |
| Payment cycle | 45 days | 30 days | Average days to payment |
| User satisfaction | 3.2/5 | 4.5/5 | NPS survey |

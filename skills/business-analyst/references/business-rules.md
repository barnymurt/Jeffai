# Business Rules Documentation

## Standard Format

```
Rule ID: BR-XXX
Name: [Descriptive Name]
Description: [What the rule enforces]
Formula/Logic: [If applicable]
Conditions: [When it applies]
Examples: [Concrete calculations or scenarios]
Exceptions: [Edge cases or overrides]
Related Rules: [Dependencies]
```

## Example: Invoice Calculation

```
Rule ID: BR-001
Name: Invoice Total Calculation
Description: Invoice total must include base amount plus applicable taxes
Formula: Total = (Hours × Rate) + (Hours × Rate × Tax Rate)
Conditions: 
  - Tax rate varies by client location
  - Must handle multiple tax rates
  - Must round to 2 decimal places
Examples:
  - 10 hours × $100/hr × 1.08 (8% tax) = $1,080.00
  - 5 hours × $150/hr × 1.0 (tax exempt) = $750.00
Exceptions:
  - Tax-exempt clients: Total = Hours × Rate only
Related Rules: BR-002 (Tax Rates), BR-015 (Discounts)
```

## Example: Discount with Tax

```
Rule ID: BR-015
Name: Tax Calculation with Discounts
Description: Tax must be calculated on the discounted amount, not original
Formula:
  Subtotal = Sum of all line items
  Discount Amount = Calculate based on discount type
  Discounted Subtotal = Subtotal - Discount Amount  
  Tax Amount = Discounted Subtotal × Tax Rate
  Total = Discounted Subtotal + Tax Amount
Conditions:
  - Applies to all discounted invoices
  - Discount applied before tax calculation
Examples:
  Line Items: $1,000.00
  Discount (10%): -$100.00
  Discounted Subtotal: $900.00
  Tax (8%): $72.00 (calculated on $900, not $1,000)
  Total: $972.00
Exceptions: None
Related Rules: BR-001, BR-016 (Discount Limits)
```

## Example: Validation Rule

```
Rule ID: BR-016
Name: Discount Limits
Description: Discounts cannot exceed invoice total or 100%
Logic:
  IF discount_type = "percentage" THEN
    discount_value MUST be >= 0 AND <= 100
  ELSE IF discount_type = "fixed" THEN
    discount_value MUST be >= 0 AND <= invoice_subtotal
  END IF
Conditions:
  - Validated on discount entry
  - Validated on invoice save
Examples:
  - 10% discount on $1,000 invoice: VALID
  - 150% discount: INVALID
  - $500 discount on $300 invoice: INVALID
  - 100% discount: VALID (requires reason)
Exceptions:
  - 100% discount requires mandatory reason field
Related Rules: BR-015
```

## Categories of Business Rules

### Calculation Rules
Define how values are computed:
- Totals, subtotals, taxes
- Proration, rounding
- Currency conversion

### Validation Rules
Define what input is acceptable:
- Required fields
- Format constraints
- Value ranges
- Cross-field validation

### Authorization Rules
Define who can do what:
- Role-based permissions
- Approval thresholds
- Delegation rules

### Timing Rules
Define when things happen:
- Due dates, deadlines
- Grace periods
- Scheduling constraints

### State Transition Rules
Define valid status changes:
- Draft → Sent → Paid
- Pending → Approved → Active
- What actions trigger transitions

## Identifying Business Rules

Ask these questions:

| Question | Example Rule |
|----------|--------------|
| How is [X] calculated? | Total = Subtotal + Tax |
| What values are allowed for [field]? | Amount must be > 0 |
| Who can [action]? | Only managers can approve discounts > 20% |
| When can [action] occur? | Invoices can only be voided within 24 hours |
| What happens when [condition]? | If payment overdue > 30 days, apply late fee |
| What's the default for [field]? | Payment terms default to Net 30 |

## Business Rules Checklist

For each rule, verify:

- [ ] Unique ID assigned
- [ ] Clear, descriptive name
- [ ] Unambiguous description
- [ ] Formula/logic documented (if calculation)
- [ ] Conditions specified
- [ ] At least one example provided
- [ ] Exceptions documented
- [ ] Related rules linked
- [ ] Validated with stakeholders
- [ ] Source/authority noted (who owns this rule?)

## Anti-Patterns

❌ **Vague rules:** "Discounts should be reasonable"
✅ **Specific rules:** "Discounts limited to 25% without manager approval"

❌ **Implementation details:** "Store tax in decimal field with 4 digits"
✅ **Business logic only:** "Tax calculated to 2 decimal places"

❌ **Undocumented exceptions:** "Usually we apply tax"
✅ **Explicit exceptions:** "Tax-exempt for non-profit clients with valid certificate"

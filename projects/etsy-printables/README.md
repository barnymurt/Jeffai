# Etsy Printables Business

**Status:** READY TO LAUNCH

Shop name: **PlannerPro Digital**

## Products (5 ready)

| Product | Price | Status |
|---------|-------|--------|
| Monthly Budget Planner | $4.97 | Copy ready, needs design |
| Weekly Meal Planner | $3.97 | Copy ready, needs design |
| Goal & Habit Tracker | $5.97 | Copy ready, needs design |
| Daily Productivity Planner | $4.97 | Copy ready, needs design |
| Financial Goal Tracker | $6.97 | Copy ready, needs design |
| **Bundle (all 5)** | $19.97 | Ready when products done |

## Launch Checklist

### 1. Generate Designs (30 mins)
```bash
cd ../../apps/workers
export GEMINI_API_KEY="your-key"

# Generate each product
python image_generator.py --prompt "minimalist A4 monthly budget planner printable, clean grid layout, pastel colors" --filename ../projects/etsy-printables/generated/budget-planner.png
```

Or use ChatGPT/DALL-E, Canva, or any design tool.

### 2. Create PDFs (20 mins)
Convert designs to print-ready PDFs (A4/Letter size).

### 3. Create Etsy Account (20 mins)
1. Go to etsy.com/sell
2. Set up shop with name "PlannerPro Digital"
3. Add payment info

### 4. Upload Products (45 mins)
For each product:
1. Upload PDF file
2. Copy title from `PRODUCT_LISTINGS.md`
3. Copy description
4. Add all 13 tags
5. Set price
6. Publish

## Expected Revenue

- **Week 1:** 1-3 sales ($5-20)
- **Month 1:** 20-50 sales ($80-200)
- **Month 3:** $25-60/day ($750-1800/mo)

## Files

- `PRODUCT_LISTINGS.md` - All product copy (titles, descriptions, tags)
- `SHOP_SETUP_CHECKLIST.md` - Detailed setup guide
- `BRANDING.md` - Shop branding guidelines
- `products/` - Individual product JSON configs
- `templates/` - Design templates
- `generated/` - Output files (gitignored)

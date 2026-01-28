# Jeffai Reorganization Plan

## The Problem

Your current Clawdbot setup burns API credits because:

1. **Telegram polling** - Constantly checking for messages = constant API calls
2. **Heartbeat system** - Regular "are you alive?" checks = more API calls
3. **Large context** - 153k tokens per request when context bloats
4. **Always-on agent** - Even idle time costs money

**Estimated cost:** $50-200+/month just to keep the bot "awake"

## The Solution: On-Demand AI

Instead of an always-on bot, build a **local web UI** where:
- AI only runs when YOU click a button
- No polling, no heartbeats, no idle costs
- You control exactly when credits are spent
- Can still automate specific tasks via cron/scheduled jobs

**Estimated cost:** $5-20/month (only pay for actual work)

---

## Recommended Tech Stack

### Primary: Next.js 14 + TypeScript

**Why Next.js:**
- Single framework for frontend + backend (API routes)
- Great for non-technical users (good docs, big community)
- Easy deployment to Vercel (free tier available)
- Built-in API routes = no separate backend needed
- React ecosystem = lots of UI components available

### AI Processing: Python Scripts

**Why Python for heavy lifting:**
- Best libraries for AI (langchain, openai, anthropic)
- Best for PDF generation (reportlab, fpdf)
- Best for image processing (PIL, etc.)
- Can call Python scripts from Next.js API routes

### Database: SQLite (local) or Supabase (hosted)

**Why:**
- SQLite = zero setup, just a file
- Supabase = free tier with Postgres, auth, and real-time
- Store tasks, projects, generated content

### AI Provider: Claude API (direct)

**Why direct API vs Clawdbot:**
- Pay only for what you use
- No middleware overhead
- Full control over prompts and context
- Can use cheaper models (Haiku) for simple tasks

---

## New Project Structure

```
jeffai/
├── README.md                    # Project overview
├── .env.example                 # Environment variables template
├── .gitignore
│
├── apps/                        # Deployable applications
│   │
│   ├── dashboard/               # Main web UI (Next.js)
│   │   ├── package.json
│   │   ├── next.config.js
│   │   ├── src/
│   │   │   ├── app/             # Next.js App Router
│   │   │   │   ├── page.tsx     # Home/Dashboard
│   │   │   │   ├── tasks/       # Task management
│   │   │   │   ├── etsy/        # Etsy product generator
│   │   │   │   ├── research/    # Research tools
│   │   │   │   └── api/         # API routes
│   │   │   ├── components/      # React components
│   │   │   └── lib/             # Utilities
│   │   └── README.md
│   │
│   └── workers/                 # Background job runners (Python)
│       ├── requirements.txt
│       ├── image_generator.py   # Etsy printable images
│       ├── pdf_generator.py     # PDF creation
│       ├── research_agent.py    # Web research automation
│       └── README.md
│
├── packages/                    # Shared code
│   │
│   ├── ai/                      # AI utilities
│   │   ├── package.json
│   │   ├── claude.ts            # Claude API wrapper
│   │   ├── prompts/             # Reusable prompts
│   │   └── README.md
│   │
│   └── database/                # Database schema & queries
│       ├── schema.sql
│       ├── queries.ts
│       └── README.md
│
├── projects/                    # Individual project workspaces
│   │
│   ├── etsy-printables/         # Etsy business
│   │   ├── README.md
│   │   ├── products/            # Product definitions
│   │   │   ├── monthly-budget-planner.json
│   │   │   ├── weekly-meal-planner.json
│   │   │   └── ...
│   │   ├── templates/           # Design templates
│   │   ├── generated/           # Output files (gitignored)
│   │   └── shop-config.json     # Shop settings, branding
│   │
│   ├── ai-content-pipeline/     # Content automation service
│   │   ├── README.md
│   │   ├── workflows/           # Content transformation workflows
│   │   ├── templates/           # Output templates
│   │   └── clients/             # Client-specific configs
│   │
│   └── research/                # Research & analysis tools
│       ├── README.md
│       ├── scrapers/            # Web scraping scripts
│       ├── analyzers/           # Data analysis
│       └── reports/             # Generated reports
│
├── archive/                     # Old Clawdbot files (reference only)
│   ├── clawd/                   # Original clawd folder
│   └── .clawdbot/               # Original config
│
└── docs/                        # Documentation
    ├── setup.md                 # Getting started
    ├── architecture.md          # System design
    └── deployment.md            # How to deploy
```

---

## Migration Plan

### Phase 1: Archive & Extract (Today)
1. Move existing `clawd/` and `.clawdbot/` to `archive/`
2. Extract valuable content:
   - Etsy product definitions → `projects/etsy-printables/`
   - AI monetization plans → `projects/ai-content-pipeline/`
   - Python scripts → `apps/workers/`
   - Useful skill docs → `docs/`

### Phase 2: Build Dashboard MVP (Week 1)
1. Create Next.js app with basic UI
2. Implement simple task list (replace tasks.json)
3. Add Claude API integration (direct, not via Clawdbot)
4. Create "Research" page with single prompt input

### Phase 3: Etsy Generator (Week 2)
1. Build Etsy product management UI
2. Integrate image generation (Gemini API or DALL-E)
3. Add PDF generation for printables
4. One-click "generate all products" feature

### Phase 4: Automation (Week 3+)
1. Add scheduled tasks (cron jobs via Vercel or local)
2. Build content pipeline workflows
3. Add more research/automation tools as needed

---

## Cost Comparison

| Item | Clawdbot (Telegram) | New Setup |
|------|---------------------|-----------|
| Idle monitoring | $30-50/mo | $0 |
| Heartbeats | $10-20/mo | $0 |
| Actual AI work | $20-50/mo | $20-50/mo |
| Hosting | Free (self-hosted) | Free (Vercel) |
| **Total** | **$60-120/mo** | **$20-50/mo** |

**Savings: 50-70%** by eliminating always-on overhead

---

## Quick Wins (Do First)

### 1. Launch Etsy Shop (2 hours)
Your Etsy products are 99% ready. Just:
1. Get a Gemini API key (or use DALL-E)
2. Generate 5 product images
3. Create PDFs
4. Upload to Etsy

This can generate $500-1500/mo passive income.

### 2. Simple Research Tool (1 day)
Build a single-page app:
- Text input for research query
- Button to run Claude
- Display results
- Save to file

No Telegram, no always-on bot. Just click when you need it.

### 3. Task Dashboard (2-3 days)
Replace the tasks.json with a simple web UI:
- View all tasks
- Add/edit/complete tasks
- Categories/projects
- No AI needed for basic CRUD

---

## Files to Keep vs Archive

### Keep (migrate to new structure):
- `clawd/etsy-shop-project/` → Etsy product definitions
- `clawd/projects/ai-monetization/` → Business plans
- `clawd/projects/ai-content-pipeline/` → Workflow definitions
- `clawd/automation-scripts/` → Python scripts (adapt)
- `clawd/tasks.json` → Import into new task system
- `clawd/MEMORY.md` → Reference for context

### Archive (reference only):
- `clawd/skills/` → Most are Clawdbot-specific
- `clawd/SOUL.md`, `AGENTS.md` → Clawdbot personality files
- `.clawdbot/` → All Clawdbot config

### Delete:
- Backup files (`.bak`, `.bak.1`, etc.)
- Empty directories
- Redundant configs

---

## Next Steps

1. **Review this plan** - Does this structure make sense?
2. **Choose hosting** - Vercel (easy) or self-hosted (free)?
3. **Prioritize** - Etsy launch? Research tool? Task board?
4. **Start building** - I can help create the initial structure

Let me know your thoughts and I'll start implementing!

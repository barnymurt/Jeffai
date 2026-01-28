# Jeffai

Personal AI assistant platform for automating online business tasks.

## Goals

1. **Etsy Printables** - Generate and sell digital products (planners, trackers, etc.)
2. **Research & Automation** - Web research, data analysis, content generation
3. **Web Apps** - Build websites and web applications
4. **Task Management** - Track projects and scheduled tasks

## Structure

```
jeffai/
├── apps/
│   ├── dashboard/     # Web UI (Next.js) - coming soon
│   └── workers/       # Python scripts for heavy processing
├── packages/
│   ├── ai/            # Claude API utilities
│   └── database/      # Data storage
├── projects/
│   ├── etsy-printables/      # Etsy business (ready to launch!)
│   ├── ai-content-pipeline/  # Content automation service
│   └── research/             # Research tools
├── archive/           # Old Clawdbot files (reference)
└── docs/              # Documentation
```

## Quick Start

### 1. Etsy Printables (Ready Now)

The Etsy shop is 99% ready. See `projects/etsy-printables/README.md`.

```bash
cd projects/etsy-printables
# Generate product images with Gemini/DALL-E
# Upload to Etsy
# Start earning passive income
```

### 2. Dashboard (Coming Soon)

```bash
cd apps/dashboard
npm install
npm run dev
# Open http://localhost:3000
```

### 3. Python Workers

```bash
cd apps/workers
pip install -r requirements.txt
python image_generator.py --help
```

## Tech Stack

- **Frontend:** Next.js 14 + TypeScript + Tailwind CSS
- **Backend:** Next.js API Routes + Python scripts
- **AI:** Claude API (direct), Gemini for images
- **Database:** SQLite (local) or Supabase (hosted)

## Why This Structure?

Migrated from Clawdbot/Telegram to reduce API costs:
- **Before:** $60-120/mo (always-on polling)
- **After:** $20-50/mo (on-demand only)

See `REORGANIZATION_PLAN.md` for full details.

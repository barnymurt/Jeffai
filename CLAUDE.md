# Jeffai Project Instructions

This is a personal AI assistant platform for building online businesses and automating tasks.

## Project Goals

1. **Etsy Printables** - Generate and sell digital products (planners, trackers, PDFs)
2. **Research & Automation** - Web research, data analysis, content generation
3. **Web Apps** - Build websites and web applications
4. **Task Management** - Track projects and scheduled tasks

## Project Structure

```
jeffai/
├── apps/
│   ├── dashboard/     # Next.js web UI (in development)
│   └── workers/       # Python scripts for heavy processing
├── packages/
│   ├── ai/            # Claude API utilities
│   └── database/      # Data storage
├── projects/
│   ├── etsy-printables/      # Etsy business (ready to launch)
│   ├── ai-content-pipeline/  # Content automation service
│   └── research/             # Research tools
├── skills/            # Anthropic agent skills (see below)
├── archive/           # Old Clawdbot files (reference only)
└── docs/              # Documentation
```

## Skills Library

When working on specific tasks, reference these skills for specialized workflows:

### PDF Creation & Manipulation
**Skill:** `skills/pdf/SKILL.md`
**Use when:** Creating Etsy printables, generating PDFs, merging/splitting documents, extracting text/tables
**Key tools:** pypdf, pdfplumber, reportlab

### Canvas Design (Visual Art)
**Skill:** `skills/canvas-design/SKILL.md`
**Use when:** Creating posters, visual art, static designs, PNG/PDF artwork
**Process:** Design philosophy first, then express visually

### Algorithmic Art
**Skill:** `skills/algorithmic-art/SKILL.md`
**Use when:** Creating generative art, flow fields, particle systems, p5.js sketches
**Output:** Interactive HTML artifacts with parameter controls

### Web App Testing
**Skill:** `skills/webapp-testing/SKILL.md`
**Use when:** Testing local web applications, debugging UI, capturing screenshots
**Key tool:** Playwright with Python

### MCP Server Building
**Skill:** `skills/mcp-builder/SKILL.md`
**Use when:** Creating MCP servers to integrate external APIs/services
**Recommended:** TypeScript with MCP SDK

### Document Creation (DOCX)
**Skill:** `skills/docx/SKILL.md`
**Use when:** Creating/editing Word documents, working with tracked changes

### Brand Guidelines
**Skill:** `skills/brand-guidelines/SKILL.md`
**Use when:** Applying Anthropic brand colors/typography to artifacts

### Product Owner / Product Strategy
**Skill:** `skills/product-owner/SKILL.md`
**Use when:** Prioritizing features, planning sprints, customer discovery, backlog management
**Includes:** Prioritization framework, interview guides, Opportunity Solution Trees

### Creating New Skills
**Skill:** `skills/skill-creator/SKILL.md`
**Use when:** Building new skills to extend capabilities

## Key Files

| File | Purpose |
|------|---------|
| `projects/etsy-printables/` | Ready-to-launch Etsy shop with 5 product definitions |
| `projects/ai-content-pipeline/` | Content automation business plan and workflows |
| `apps/workers/generate_image.py` | Image generation via Gemini API |
| `apps/workers/token_analyzer.py` | Analyze Claude API token usage |

## Development Preferences

- **Frontend:** Next.js 14 + TypeScript + Tailwind CSS
- **Backend:** Next.js API routes or Python scripts
- **AI:** Claude API (direct calls, not always-on)
- **PDF Generation:** Use reportlab (Python) per `skills/pdf/SKILL.md`
- **Testing:** Playwright per `skills/webapp-testing/SKILL.md`

## Quick Reference

### To generate an Etsy printable:
1. Read `skills/pdf/SKILL.md` for PDF creation patterns
2. Use reportlab to create the PDF
3. Save to `projects/etsy-printables/generated/`

### To create visual art/posters:
1. Read `skills/canvas-design/SKILL.md`
2. Create design philosophy first
3. Express visually as PNG/PDF

### To build a web app:
1. Use Next.js structure in `apps/dashboard/`
2. Test with `skills/webapp-testing/SKILL.md` patterns

### To create generative art:
1. Read `skills/algorithmic-art/SKILL.md`
2. Create algorithmic philosophy
3. Implement as self-contained HTML with p5.js

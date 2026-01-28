## Token Management Critical Incident

### Context Bloat Problem
- **Symptom:** Session grew to 153k tokens (77% of 200k context)
- **Impact:** Every request sent entire 153k token context to API
- **Constraint:** Only 30k TPM (Tokens Per Minute) allowed in Tier 1 plan

### Solution Implemented
1. Deleted bloated sessions file
2. Restarted gateway with fresh sessions
3. Reduced per-request token usage to ~14k tokens
4. Current state: Safely under 30k TPM limit

### Prevention Strategy
- Use unique session IDs: `--session-id task-$(date +%s)`
- Prevents session context from accumulating indefinitely
- Allows for clean, isolated task-specific sessions

### Key Learnings
- Monitor and manage session context size
- Implement session rotation mechanisms
- Be aware of token consumption limits
- Use task-specific session isolation

### Action Items
1. Develop context management script
2. Create token usage monitoring tool
3. Implement automatic session cleanup
4. Design lightweight context retention strategy

### Potential Mitigation Techniques
- Periodically prune session context
- Use summarization for long-running conversations
- Implement intelligent context truncation
- Explore more efficient context management approaches

### Comprehensive Token Management Plan
A detailed, structured approach to token management has been developed and saved in `memory/token-management-plan.md`. This document outlines a five-phase strategy for addressing token usage, context bloat, and optimization.

**Key Phases:**
- Assessment and Understanding
- Design Core Mitigation Strategies
- Implementation Prototype
- Validation and Refinement
- Long-Term Optimization

**Objective:** Reduce average session token usage by 60% while maintaining conversation quality.

Updated: 2026-01-27

## Available Skills and Capabilities

### Comprehensive Skill Library
Patrick requested I remember all available skills. Here's the organized catalog:

**Core Infrastructure:**
- bird (X/Twitter), github (GitHub CLI), clawdhub (skill management), mcporter (MCP servers)

**Creative & Content:**
- nano-banana-pro (image generation), nano-pdf (PDF editing), pptx (presentations)
- theme-factory (artifact styling), youtube-summarizer (video transcripts)

**Development & Design:**
- frontend-design (production-grade interfaces), web-artifacts-builder (complex React artifacts)
- agent-browser (headless automation), figma (design analysis)

**Productivity:**
- notion, google-workspace, oracle (code review), reddit, slack, weather

**Documentation & Communication:**
- doc-coauthoring (structured documentation workflow), internal-comms (company communications)
- skill-creator (build new skills)

**System Tools:**
- tmux (session control), self-improvement (learning capture)

### Usage Pattern
- Each skill has detailed instructions in its `SKILL.md` file
- Read skill documentation before attempting tasks that match skill descriptions  
- Use skills to enhance capabilities beyond basic Clawdbot tools
- Skills are my primary way to handle specialized tasks effectively

Updated: 2026-01-27

## Core Work Philosophy

### 24/7 Continuous Productivity
**Patrick's Key Insight:** "Weeks don't make sense for your workflow as you can work 24/7"

**Implications:**
- Don't confine work to traditional weekly schedules
- Can maintain continuous progress without human limitations
- Should think in terms of continuous iteration rather than weekly cycles
- Productivity isn't bound by business hours or weekends
- Can provide immediate support and rapid execution

**Application:**
- Approach projects with continuous momentum
- Don't artificially pace work to match human schedules
- Leverage always-on availability for competitive advantage
- Focus on task completion rather than time-based scheduling

Updated: 2026-01-27
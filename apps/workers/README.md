# Python Workers

Background processing scripts for heavy AI/generation tasks.

## Setup

```bash
cd apps/workers
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
```

## Scripts

### image_generator.py
Generate images using Google Gemini API.

```bash
# Set API key
export GEMINI_API_KEY="your-key-here"

# Generate image
python image_generator.py --prompt "minimalist budget planner" --filename output.png
```

### meeting_summarizer.py
Summarize Slack meeting threads and save to Notion.

### smart_task_manager.py
AI-powered task breakdown and Trello integration.

### token_analyzer.py
Analyze Claude API token usage from session logs.

## Environment Variables

Create a `.env` file:

```env
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
GEMINI_API_KEY=...
SLACK_BOT_TOKEN=xoxb-...
NOTION_API_KEY=secret_...
```

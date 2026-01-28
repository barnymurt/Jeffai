# Ultra Conservative Rate Limits 🔧

**MANDATORY: Use these super conservative settings**

## Target Configuration
```json
{
  "rate_limit": {
    "requests_per_minute": 5,
    "delay_between_requests": 2000
  }
}
```

## Manual Implementation Strategy

### 1. Fixed Delays Between ALL Operations
```bash
# Every tool call must have minimum 2-second delay
sleep 2 && tool_command
sleep 2 && next_command
```

### 2. Max 5 Operations Per Minute
- **Track operations manually**
- **Wait 12+ seconds** between each operation
- **Maximum 5 tool calls per minute**

### 3. Session Pacing
- **Plan operations in batches**
- **Use exec with && for multiple commands**
- **Minimize total API calls to absolute essentials**

## Current Session Rules
- ✅ **2+ second delays** between every tool call
- ✅ **Max 5 operations per minute** 
- ✅ **Sequential processing only** (maxConcurrent: 1)
- ✅ **Use browser for all web operations** (zero API calls)
- ✅ **Local file operations** preferred

## Example Workflow
```bash
sleep 2 && echo "Operation 1"
sleep 12 && echo "Operation 2"  
sleep 12 && echo "Operation 3"
sleep 12 && echo "Operation 4"  
sleep 12 && echo "Operation 5"
# Wait 60 seconds before next batch
```

This ensures we stay WELL under Tier 1 limits.
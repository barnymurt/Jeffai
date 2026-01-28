# Rate Limit Avoidance Strategy 🔧

**MANDATORY: Use in EVERY session to avoid hitting API limits**

## Core Principles

### 1. Browser First
- ✅ Use `agent-browser` for ALL web interactions
- ✅ Web scraping instead of web search API calls
- ✅ Form filling via browser automation
- ✅ Data extraction through webpage parsing

### 2. Smart Timing
- ✅ **3-5 second delays** between ANY tool calls
- ✅ Use `sleep 3 &&` prefix for commands
- ✅ Batch operations when possible
- ✅ Local file operations over repeated API calls

### 3. Tool Call Minimization
- ✅ **Combine operations** in single calls when possible  
- ✅ **Read files once**, store in variables
- ✅ **Write in batches** rather than multiple writes
- ✅ **Use exec for multiple commands** with `&&`

### 4. Strategic Pauses
```bash
# Always add delays between tool calls:
sleep 3 && agent-browser click @e1
sleep 2 && agent-browser snapshot -i --json  
sleep 3 && jq '...' file.json
```

### 5. Session Management
- ✅ **Check current model** at session start (use cheaper when possible)
- ✅ **Batch similar operations** together
- ✅ **Use background processes** for long-running tasks
- ✅ **Local storage** for temporary data

## Emergency Reset
If hitting rate limits:
1. **Switch to cheapest model** available
2. **Add 5-10 second delays** between ALL calls
3. **Use only essential operations**
4. **Batch everything possible**

## Implementation Checklist
- [ ] Start session with model check
- [ ] Use browser for web operations  
- [ ] Add sleep delays between tools
- [ ] Minimize total API calls
- [ ] Store data locally when possible

---
**Remember: This strategy is MANDATORY for sustainable operations!**
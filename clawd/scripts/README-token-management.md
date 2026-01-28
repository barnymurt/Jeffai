# Token Management Script

## Overview
This script manages session token usage to prevent excessive consumption and maintain system efficiency.

## Key Features
- Token Usage Tracking
  - Calculates total tokens in the current session
  - Enforces a maximum token limit (25,000 tokens)
  - Prevents excessive token consumption

- Session Management
  - Identifies the most recent session file
  - Resets sessions exceeding token limits
  - Archives overloaded sessions for later analysis

- Comprehensive Logging
  - Tracks token counts
  - Monitors model switches
  - Logs all interventions for diagnostic purposes

## Cron Job Configuration
- Frequency: Hourly
- Log Location: `/home/ubuntu/clawd/logs/token-management.log`

## Recommended Monitoring
1. Regularly review the log file
2. Adjust token limits based on observed patterns
3. Fine-tune script behavior as needed

## Potential Improvements
- Dynamic token limit adjustment
- More granular model switch tracking
- Advanced session archiving strategies
#!/bin/bash
# Advanced Token Management Script for Clawdbot

# Configuration
MAX_SESSION_TOKENS=25000  # Conservative limit below 30k TPM
MODEL_SWITCH_COOLDOWN=300  # 5-minute cooldown between model changes
LOG_DIR="/home/ubuntu/clawd/logs/token_manager"
SESSIONS_DIR="/home/ubuntu/.clawdbot/agents/main/sessions"

# Ensure log directory exists
mkdir -p "$LOG_DIR"

# Logging function
log_event() {
    local message="$1"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $message" >> "$LOG_DIR/token_manager.log"
}

# Calculate current session tokens
calculate_current_session_tokens() {
    local session_file="$1"
    # Use grep and awk to sum token usage from session file
    local total_tokens=$(grep -o '"totalTokens":[0-9]*' "$session_file" | awk -F: '{sum+=$2} END {print sum}')
    echo "${total_tokens:-0}"
}

# Find the most recent session file
get_latest_session_file() {
    find "$SESSIONS_DIR" -type f -name "*.jsonl" -printf '%T@ %p\n' | sort -n | tail -1 | cut -d' ' -f2
}

# Check token usage and manage session
manage_session_tokens() {
    local latest_session=$(get_latest_session_file)
    
    if [[ -z "$latest_session" ]]; then
        log_event "No active session found"
        return 1
    fi

    local current_tokens=$(calculate_current_session_tokens "$latest_session")
    
    if [[ $current_tokens -gt $MAX_SESSION_TOKENS ]]; then
        log_event "Token limit exceeded in session: $latest_session (Tokens: $current_tokens)"
        
        # Optionally truncate or archive the session
        local archive_file="$LOG_DIR/archived_session_$(date '+%Y%m%d_%H%M%S').jsonl"
        cp "$latest_session" "$archive_file"
        
        # Clear or reset the session
        echo '{"type":"session_reset","timestamp":"'$(date -u +"%Y-%m-%dT%H:%M:%S.%NZ")'"}' > "$latest_session"
        
        log_event "Session reset and archived: $archive_file"
        return 0
    fi

    log_event "Current session tokens: $current_tokens"
    return 0
}

# Track model switches
track_model_switches() {
    local latest_session=$(get_latest_session_file)
    
    # Extract model changes
    local model_changes=$(grep '"type":"model_change"' "$latest_session")
    local model_change_count=$(echo "$model_changes" | wc -l)
    
    if [[ $model_change_count -gt 2 ]]; then
        log_event "Multiple model switches detected in session: $model_change_count switches"
        return 1
    fi
    
    return 0
}

# Main execution
main() {
    log_event "Token management started"
    
    manage_session_tokens
    track_model_switches
    
    log_event "Token management cycle completed"
}

# Run the main function
main

exit 0
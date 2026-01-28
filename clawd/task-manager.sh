#!/bin/bash
# Task Board Manager for Patrick & Jeff

case "$1" in
    "show"|"")
        echo "=== Patrick & Jeff Task Board 🔧 ==="
        jq -r '
        "Updated: " + .updated + "\n" +
        (.tasks | group_by(.status) | map(
          . as $tasks | $tasks[0].status as $status |
          (if $status == "ideation" then "\n💡 IDEATION:"
           elif $status == "progress" then "\n🔄 IN PROGRESS:" 
           elif $status == "review" then "\n👀 READY FOR REVIEW:"
           elif $status == "demo" then "\n🚀 DEMO READY:"
           elif $status == "deployed" then "\n✅ DEPLOYED:"
           else "\n" + $status + ":" end) + 
          "\n" + ($tasks | map("• " + .title + " (" + .owner + ", " + .priority + ")\n  " + .description) | join("\n"))
        ) | join("\n"))
        ' tasks.json
        ;;
    "add")
        echo "Usage: ./task-manager.sh add \"Task Title\" \"Description\" status owner priority"
        echo "Status: ideation|progress|review|demo|deployed"
        echo "Owner: jeff|patrick|both"
        echo "Priority: high|medium|low"
        ;;
    *)
        echo "Patrick & Jeff Task Manager 🔧"
        echo "Commands:"
        echo "  show     - Display current task board"
        echo "  add      - Add new task (see usage)"
        echo ""
        echo "Example: ./task-manager.sh add \"New Feature\" \"Build something cool\" ideation patrick high"
        ;;
esac
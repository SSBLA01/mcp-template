#!/bin/bash
# Wrapper script for Mathematical Research MCP to ensure proper environment

# Error handling
set -e
trap 'echo "Error occurred at line $LINENO" >&2' ERR

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Change to the project directory
cd "$SCRIPT_DIR"

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Export Python path
export PYTHONPATH="$SCRIPT_DIR"

# Add small delay to prevent race conditions
sleep 0.5

# Run the unified MCP server with unbuffered output
exec python -u -m src.servers.dobbs_unified

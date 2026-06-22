#!/usr/bin/env bash
set -euo pipefail

# ask_gemini.sh — send a question to the Gemini API
# Requires: curl, jq
# Usage:
#   ./ask_gemini.sh "What is the capital of France?"
#   ./ask_gemini.sh            # will prompt interactively
#
# .env file (in the same directory, or set ENV_FILE to point elsewhere):
#   GEMINI_API_KEY=your_api_key_here
#   GEMINI_MODEL=gemini-2.5-flash   # optional, defaults below

ENV_FILE="${ENV_FILE:-.env}"

if [[ ! -f "$ENV_FILE" ]]; then
    echo "Error: $ENV_FILE not found." >&2
    exit 1
fi

# Load variables from .env (ignores comments/blank lines) without
# polluting the rest of the shell beyond this script's environment.
set -a
# shellcheck disable=SC1090
source "$ENV_FILE"
set +a

if [[ -z "${GEMINI_API_KEY:-}" ]]; then
    echo "Error: GEMINI_API_KEY not set in $ENV_FILE" >&2
    exit 1
fi

for cmd in curl jq; do
    command -v "$cmd" >/dev/null 2>&1 || { echo "Error: '$cmd' is required but not installed." >&2; exit 1; }
done

MODEL="${GEMINI_MODEL:-gemini-2.5-flash}"
API_URL="https://generativelanguage.googleapis.com/v1beta/models/${MODEL}:generateContent?key=${GEMINI_API_KEY}"

# Question comes from CLI args, or an interactive prompt if none given
if [[ $# -gt 0 ]]; then
    QUESTION="$*"
else
    read -rp "Ask Gemini: " QUESTION
fi

if [[ -z "$QUESTION" ]]; then
    echo "Error: no question provided." >&2
    exit 1
fi

# Build the JSON payload safely (handles quotes/special chars in the question)
PAYLOAD=$(jq -n --arg q "$QUESTION" '{contents: [{parts: [{text: $q}]}]}')

RESPONSE=$(curl -s -X POST "$API_URL" \
    -H "Content-Type: application/json" \
    -d "$PAYLOAD")

ANSWER=$(echo "$RESPONSE" | jq -r '.candidates[0].content.parts[0].text // empty')

if [[ -z "$ANSWER" ]]; then
    echo "No answer returned. Raw response:" >&2
    echo "$RESPONSE" >&2
    exit 1
fi

echo "$ANSWER"

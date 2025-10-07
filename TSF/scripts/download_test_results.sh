#!/bin/bash

# Create artifacts directory if it doesn't exist
mkdir -p artifacts

# Use a GitHub token for higher rate limits (optional)
if [ -n "$GH_TOKEN" ]; then
  AUTH_HEADER=(-H "Authorization: token $GH_TOKEN")
else
  AUTH_HEADER=()
fi

runid=$(curl -s "${AUTH_HEADER[@]}" "https://api.github.com/repos/score-json/json/actions/runs?status=success&per_page=100" \
  | jq -r '[.workflow_runs[] | select(((.event == "push" and .head_branch == "main") or (.event == "schedule")) and (.name == "Parent Workflow"))][0].id')
  
if [ -z "$runid" ]; then
  echo "No matching workflow run found."
  exit 1
fi

# Get artifact download URL for the first artifact whose name starts with 'ubuntu-'
url=$(curl -s "${AUTH_HEADER[@]}" "https://api.github.com/repos/score-json/json/actions/runs/${runid}/artifacts?per_page=100" \
  | jq -r '.artifacts[]? | select(.name | test("^ubuntu-")) | .archive_download_url' | head -n 1)

if [ -n "$url" ]; then
  tmp_zip=$(mktemp)
  curl -L "${AUTH_HEADER[@]}" "$url" -o "$tmp_zip"
  unzip -j -o "$tmp_zip" 'MemoryEfficientTestResults.db' -d artifacts && \
    echo "Extraction complete: artifacts/MemoryEfficientTestResults.db" && rm -f "$tmp_zip" && exit 0
  echo "Extraction failed."
  rm -f "$tmp_zip"
  exit 1
fi

echo "Artifact not found in the most recent matching workflow run."
exit 1

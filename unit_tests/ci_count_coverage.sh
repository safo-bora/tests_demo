#!/bin/bash

pwd
ls -la 

# Calculate coverage percentage
COVERAGE=$(python -c "import json; data = json.load(open('coverage.json')); print(data.get('totals', {}).get('percent_covered', 0))")
echo "Extracted COVERAGE value: $COVERAGE"  # Add this line for debugging

# Set default coverage to 0 if not available
if [ -z "$COVERAGE" ]; then
  COVERAGE=0
fi

# Strip quotes from COVERAGE value
COVERAGE_NUMERIC=$(echo "$COVERAGE" | sed 's/"//g')

# Format coverage percentage to two decimal places
COVERAGE_PERCENTAGE=$(printf "%.2f" "$COVERAGE_NUMERIC")
echo "COVERAGE_PERCENTAGE=$COVERAGE_PERCENTAGE" >> $GITHUB_ENV

# Determine badge color based on coverage percentage
if (( $(echo "$COVERAGE_PERCENTAGE < 85" | bc -l) )); then
  echo "COVERAGE_BADGE_COLOR=red" >> $GITHUB_ENV
else
  echo "COVERAGE_BADGE_COLOR=green" >> $GITHUB_ENV
fi

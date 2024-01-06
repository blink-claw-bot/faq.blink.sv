#!/bin/bash

# Define the output file
output="combined.md"

# Create or clear the content of the output file
> "$output"

# Debug: Show the current directory
echo "Running script in $(pwd)"

# Find all .md files and concatenate them into the combined.md file
find . -name '*.md' -not -path "./$output" -print | while read file; do
    # Debug: Show which file is being processed
    echo "Adding $file to $output"
    cat "$file" >> "$output"
done

echo "All markdown files have been combined into $output"

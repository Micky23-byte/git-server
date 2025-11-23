#!/bin/bash

# Directory to list
DIR="./"

echo "Listing files in $DIR:"

# Loop through files
for file in "$DIR"*; do
    if [ -f "$file" ]; then
        echo "File found: $file"
    fi
done


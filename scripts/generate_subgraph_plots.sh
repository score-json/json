#!/bin/bash

# Specify the folder where .md files are located (provide the path here)
TARGET_FOLDER="docs/s-core/trustable/assertions"

# Ensure the folder exists
if [[ ! -d "$TARGET_FOLDER" ]]; then
    echo "The folder $TARGET_FOLDER does not exist."
    exit 1
fi

# Create the 'temp' directory at the top level (relative to this script)
TEMP_FOLDER="temp/graphs"
mkdir -p "$TEMP_FOLDER"  # -p ensures no error if the folder already exists

# Iterate through all .md files in the specified folder
for file in "$TARGET_FOLDER"/*.md; do
    # Check if the file exists (to handle cases where there are no .md files)
    if [[ -f "$file" ]]; then
        # Extract the filename without the .md extension
        filename=$(basename "$file" .md)

        # Create the output file name in the 'temp' folder
        output_file="${TEMP_FOLDER}/${filename}_subgraph.svg"

        # Run the command on the file and save to the 'temp' folder
        echo "Processing file: $filename"
        trudag plot --pick "$filename" 0: -o "$output_file"
    fi
done

output_file="${TEMP_FOLDER}/Trustable.svg"
trudag plot -o "$output_file"

echo "All files processed. Output saved in the 'temp/graphs' directory."

#!/bin/bash

# global variables
TSF_SCRIPT_FOLDER=$(dirname "$(realpath $0)")
TSF_FOLDER="$TSF_SCRIPT_FOLDER/.."
TSF_REPORT_FOLDER="$TSF_FOLDER/docs/generated"

# cleanup previously generated content if exists
if [ -d "$TSF_REPORT_FOLDER" ]; then
    rm -Rf "$TSF_REPORT_FOLDER"
fi

# create output folder
mkdir -p "$TSF_REPORT_FOLDER" # -p ensures no error if the folder already exists

# generate TSF report
echo "Generating TSF report in: $TSF_REPORT_FOLDER"
trudag publish --validate --figures --output-dir "$TSF_REPORT_FOLDER" --dump data_store

# generate TSF graph
trudag plot -o "$TSF_REPORT_FOLDER/graph.svg"

# cleanup TSF report content from trudag unwanted artifacts
echo "Cleaning up TSF report from trudag unwanted artifacts"
python "$TSF_SCRIPT_FOLDER/clean_trudag_output.py" "$TSF_REPORT_FOLDER"

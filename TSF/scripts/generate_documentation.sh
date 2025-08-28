#!/bin/bash

# global variables
TRUDAG_SCRIPT_FOLDER=$(dirname "$(realpath $0)")
TSF_FOLDER="$TRUDAG_SCRIPT_FOLDER/.."
TRUDAG_REPORT_FOLDER="$TSF_FOLDER/docs/generated"

# generate documentation
rm -rf "$TRUDAG_REPORT_FOLDER" 

mkdir -p "$TRUDAG_REPORT_FOLDER"  # -p ensures no error if the folder already exists

trudag publish --validate --output-dir "$TRUDAG_REPORT_FOLDER"

trudag plot -o "$TRUDAG_REPORT_FOLDER/graph.svg"

python3 "$TRUDAG_SCRIPT_FOLDER/clean_trudag_output.py" "$TRUDAG_REPORT_FOLDER"

bazel run //:docs

# run http server
python3 -m http.server --directory _build

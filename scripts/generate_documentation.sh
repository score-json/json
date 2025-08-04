#!/bin/bash

TRUDAG_REPORT_FOLDER="TSF/docs/generated"
mkdir -p "$TRUDAG_REPORT_FOLDER"  # -p ensures no error if the folder already exists

trudag publish --validate --output-dir "$TRUDAG_REPORT_FOLDER"

trudag plot -o "$TRUDAG_REPORT_FOLDER/graph.svg"

python3 scripts/clean_trudag_output.py

bazel run //:docs

python3 -m http.server --directory _build

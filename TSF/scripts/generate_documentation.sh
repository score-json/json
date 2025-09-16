#!/bin/bash

# generate TSF report
TSF_SCRIPT_FOLDER=$(dirname "$(realpath $0)")
# The first input for this script is the base_url used in plot_partial_graphs.py
# for local testing, "http://localhost:8000" is recommended.
$TSF_SCRIPT_FOLDER/generate_report.sh $1

# prepare docs
bazel run //:docs

# run http server
python3 -m http.server --directory _build

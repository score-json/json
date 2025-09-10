#!/bin/bash

# generate TSF report
TSF_SCRIPT_FOLDER=$(dirname "$(realpath $0)")
$TSF_SCRIPT_FOLDER/generate_report.sh $1

# prepare docs
bazel run //:docs

# run http server
python3 -m http.server --directory _build

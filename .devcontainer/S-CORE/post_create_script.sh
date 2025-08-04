#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate

# Install trustable
pip install --upgrade pip
pip install trustable --index-url https://gitlab.com/api/v4/projects/66600816/packages/pypi/simple
pip install pytest

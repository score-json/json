#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate

# Install trustable
pip install --upgrade pip
pip install git+https://gitlab.com/CodethinkLabs/trustable/trustable@cc6b72753e1202951d382f60ff08320f5a957c7b
pip install pytest

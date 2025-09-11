#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate

# Install trustable
pip install --require-hashes -r .devcontainer/S-CORE/requirements.txt
pip install git+https://gitlab.com/CodethinkLabs/trustable/trustable@9957f12171cb898d83df5ae708fdba0a38fece2e

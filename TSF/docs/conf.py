# *******************************************************************************
# Copyright (c) 2025 Contributors to the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0
#
# SPDX-License-Identifier: Apache-2.0
# *******************************************************************************

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "S-CORE NLOHMANN JSON LIBRARY FORK"
author = "S-CORE"
version = "3.12.0"
project_url = "https://score-json.github.io/json"
project_prefix = "JSON_"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    "sphinx_design",
    "sphinx_needs",
    "myst_parser",
    "sphinxcontrib.plantuml",
    "score_plantuml",
    "score_metamodel",
    "score_draw_uml_funcs",
    "score_source_code_linker",
    "score_layout",
]

myst_enable_extensions = ["colon_fence"]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

suppress_warnings = ['ref.warning', 'toc.not_included', 'myst.xref_missing', 'myst.header']

exclude_patterns = [
    # The following entries are not required when building the documentation via 'bazel
    # build //docs:docs', as that command runs in a sandboxed environment. However, when
    # building the documentation via 'bazel run //docs:incremental' or esbonio, these
    # entries are required to prevent the build from failing.
    "bazel-*",
    ".venv_docs",
]

templates_path = ["templates"]

# Enable numref
numfig = True

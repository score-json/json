..
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

.. _library_description:

NLOHMANN JSON LIBRARY
=============================

This module is dedicated to implementing the Trustable Software Framework for the Niels Lohmann JSON Library. Initially, it emphasizes ensuring the reliability and correctness of the library's parsing functionality. The Niels Lohmann JSON Library is recognized for its efficient and straightforward approach to JSON parsing, manipulation, and serialization within modern C++ applications, aiming to provide developers with a flexible and robust tool for managing JSON data structures. The framework seeks to enhance these capabilities, aligning them with rigorous software quality standards to ensure dependable JSON processing across diverse applications.

.. contents:: Table of Contents
   :depth: 2
   :local:

Overview
--------

This repository provides the aspired setup for projects using **C++** and **Bazel** as a build system.

.. toctree::
   :maxdepth: 1
   :glob:

   introduction/index.rst
   trustable/concept.rst
   trustable/report.rst
   Eclipse <https://projects.eclipse.org/projects/automotive.score>

General Requirements
--------------------

.. comp_req:: JSON Validation
   :id: comp_req__json__validation
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__json_library
   :status: valid

   The JSON-Library provides a service to check the well-formedness of JSON data.

.. comp_req:: JSON Deserialization
   :id: comp_req__json__deserialization
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__json_library
   :status: valid

   The JSON-Library parses JSON data according to RFC8259.

User friendly API for information exchange
-------------------------------------------

.. comp_req:: Support for programming language idioms
   :id: comp_req__json__lang_idioms
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: feat_req__baselibs__json_library
   :status: valid

   Each public API supports the idioms of its programming language.

.. comp_req:: Use programming language infrastructure
   :id: comp_req__json__lang_infra
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: feat_req__baselibs__json_library
   :status: valid

   Each public API uses core infrastructure of its programming language and accompanying standard libraries, whenever possible and meaningful.

   Note: This includes error handling.

Full testability for the user facing API
-----------------------------------------

.. comp_req:: Fully mockable public API
   :id: comp_req__json__testability_mock_api
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: feat_req__baselibs__json_library
   :status: valid

   The public API is fully mockable.

Safety Impact
--------------

.. comp_req:: JSON library ASIL level
   :id: comp_req__json__asil
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__json_library
   :status: valid

   The JSON library supports safe communication up to ASIL-B.


Project Layout
--------------

This module includes the following top-level structure:

- `nlohmann_json/include/`: C++ source code for the NLOHMANN JSON library
- `nlohmann_json/tests/`: Unit and integration tests
- `docs/`: Documentation using `docs-as-code`
- `.github/workflows/`: CI/CD pipelines

Quick Start
-----------

To build the module:

.. code-block:: bash

   bazel build

To run tests:

.. code-block:: bash

   git submodule init
   git submodule update
   bazel test //nlohmann_json/tests/src:all_nlohmann_tests --test_output=all

To update the documentation:

.. code-block:: bash

   bazel run //docs:incremental
   python3 -m http.server --directory _build

To generate LaTeX documentation:

.. code-block:: bash

   apt-get install texlive texlive-latex-extra texlive-fonts-recommended
   sphinx-build -b latex . _build/latex
   cd _build/latex
   pdflatex nlohmannjsonlibrary.tex

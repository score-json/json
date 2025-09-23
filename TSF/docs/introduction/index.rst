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

.. _introduction:

Introduction
========================================================

This document outlines the application of the Trustable Software Framework (TSF) to the `JSON library <https://github.com/nlohmann/json>`_ (version 3.12.0) developed by Niels Lohmann. The TSF aims to ensure software reliability and compliance by setting guidelines for evaluating various aspects of software development. Our focus here is the library's integration into the baselibs repository within the S-CORE project. The ultimate goal is to certify the library as trustable based on stringent evaluation criteria involving rigorous testing, intuitive design, and seamless integration.

Design Goals of the JSON Library
--------------------------------

The JSON library by Niels Lohmann was developed with several design goals in mind:

- **Intuitive Syntax**: The library leverages modern C++ operator magic to provide an intuitive syntax similar to the native JSON experience in languages like Python.

- **Trivial Integration**: Comprising a single header file `json.hpp`, this library demands no complex build systems or dependencies, facilitating easy integration into any project using vanilla C++11.

- **Serious Testing**: Extensive unit tests ensure 100% coverage of the code, including exceptional behavior. Tools like Valgrind and Clang Sanitizers verify memory safety, while Google OSS-Fuzz performs continuous fuzz testing.

Notably, memory efficiency and speed were not primary focuses, allowing for slight trade-offs in these areas to prioritize ease of integration and reliability.

Baselibs Project Context
------------------------

The integration effort is situated within the baselibs project, aimed at qualifying library performance and compliance with internal standards. As part of this project, the TSF process has been embedded into the score repository to generate and analyze evidence regarding software trustability.

Component Classification Strategy
-----------------------------------

- **Process Overview**: The baselibs project is upholding the TSF to define guidelines and generate reliable evidence of compliance, analyzing specific requirements such as MISRA and functionality consistency.

- **Challenges and Decisions**:
  - Divergence from the original library code has been discussed to minimize unnecessary interference while adhering to project needs.
  - MISRA compliance is selectively applied, and necessary adaptations are considered at the upstream level where applicable.

- **Strategic Directions**:
  - Evidence requirements are mapped and analyzed for gaps, leading to possible code amendments or forks.
  - Questions concerning the library's behavior are systematically answered, providing coverage details and tracing requirements to standards like ISO.

Find more descriptions on the ongoing process and requirements at `Eclipse Process Description <https://eclipse-score.github.io/process_description/main/trustable/index.html>`_.

Conclusion
----------

The application of the Trustable Software Framework to version 3.12.0 of Niels Lohmann's JSON library involves a comprehensive assessment to ensure it meets our high-level requirements for external software. Key actions include formalizing necessary functionalities, addressing feature requests from SCORE, and integrating trustable evidence into a coherent project workflow. The library is maintained with stringent quality checks and evidence generation processes, illustrating a commitment to high standards and the practicality required for certifiable software projects.

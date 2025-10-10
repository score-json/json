---
level: 1.1
normative: true

references:
        - type: cpp_test
          name: "parser class - core;accept;number;integers;edge cases"
          path: "TSF/tests/unit-class_parser_core.cpp"
evidence:
  type: check_test_results
  configuration:
    tests: 
        - class_parser_core
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

The service does accept integers according to IEEE 754 binary64.

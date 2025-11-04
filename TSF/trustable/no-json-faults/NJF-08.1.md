---
level: 1.1
normative: true

references:
        - type: item
          items:
            - JLEX-01
            - NJF-08
        - type: cpp_test
          name: "parser class - core;accept;number;integers"
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

The service provided by nlohmann/json does accept integers within the limits of 64-bit double.
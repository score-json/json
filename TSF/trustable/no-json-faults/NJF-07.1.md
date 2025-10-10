---
level: 1.1
normative: true

references:
        - type: cpp_test
          name: "parser class - core;accept;string"
          path: "TSF/tests/unit-class_parser_core.cpp"
        - type: cpp_test
          name: "compliance tests from nativejson-benchmark;strings"
          path: "tests/src/unit-testsuites.cpp"
            
evidence:
  type: check_test_results
  configuration:
    tests: 
        - class_parser_core
        - testsuites
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

The service does accept empty string.

---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-02
        - type: cpp_test
          name: "parser class - core;parse;object;nonempty object"
          path: "TSF/tests/unit-class_parser_core.cpp"
evidence:
  type: check_test_results
  configuration:
    tests: 
        - class_parser_core
score:
    Jonas-Kirchhoff: 0.95
    Erikhu1: 1.0
---

The service parses non-empty objects.
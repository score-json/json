---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-02
            - NPF-04
        - type: cpp_test
          name: "parser class - core;parse;null"
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

The service provided by nlohmann/json parses the literal name null.
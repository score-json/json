---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-01
        - type: cpp_test
          name: "deserialization;JSON Lines"
          path: "tests/src/unit-deserialization.cpp"
        - type: cpp_test
          name: "parser class - core;accept;object;nonempty object"
          path: "TSF/tests/unit-class_parser_core.cpp"            
evidence:
  type: check_test_results
  configuration:
    tests: 
        - class_parser_core
        - deserialization
score:
    Jonas-Kirchhoff: 0.95
    Erikhu1: 0.95
---

The service accepts the non-empty objects.
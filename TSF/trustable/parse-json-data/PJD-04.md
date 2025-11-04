---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parser class - core;parse;number;integers"
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

The service provided by nlohmann/json correctly parses 64-bit integers (exceeding the range defined in RFC8259).
---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-01
        - type: cpp_test
          name: "parser class - core;accept;object;empty object"
          path: "TSF/tests/unit-class_parser_core.cpp"
        - type: cpp_test
          name: "accept;whitespace;empty object"
          path: "TSF/tests/unit-objects.cpp"
        - type: function_reference
          name: "lexer::skip_whitespace"
          path: "include/nlohmann/detail/input/lexer.hpp"
          description: "function, which skips admissible whitespace during reading"
evidence:
  type: check_test_results
  configuration:
    tests: 
        - class_parser_core
        - objects
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

The service provided by nlohmann/json accepts the empty object.
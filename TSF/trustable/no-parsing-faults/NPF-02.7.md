---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parse;whitespace"
          path: "TSF/tests/unit-numbers.cpp"
        - type: function_reference
          name: "lexer::skip_whitespace"
          path: "include/nlohmann/detail/input/lexer.hpp"
          description: "function, which skips admissible whitespace during reading"
evidence:
  type: check_test_results
  configuration:
    tests: 
        - numbers
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

The service ignores leading and trailing whitespace.
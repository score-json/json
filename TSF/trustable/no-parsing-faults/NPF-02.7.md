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
score:
    Jonas-Kirchhoff: 1.0
---

The service ignores leading and trailing whitespace.
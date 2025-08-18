---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parser class - core;accept;object;empty object"
          path: "TSF/tests/unit-class_parser_core.cpp"
        - type: cpp_test
          name: "accept;whitespace;empty object"
          path: "TSF/tests/unit-objects.cpp"
        - type: function_reference
          name: "lexer::skip_whitespace"
          path: "include/nlohmann/detail/input/lexer.hpp"
score:
    Jonas-Kirchhoff: 1.0
---

The service accepts the empty object.
---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parser class - core;parse;object;empty object"
          path: "TSF/tests/unit-class_parser_core.cpp"
        - type: cpp_test
          name: "regression tests 1;example from #529"
          path: "tests/src/unit-regression1.cpp"
        - type: function_reference
          name: "lexer::skip_whitespace"
          path: "include/nlohmann/detail/input/lexer.hpp"
score:
    Jonas-Kirchhoff: 1.0
---

The service ignores leading and trailing whitespace for name and value of each member.
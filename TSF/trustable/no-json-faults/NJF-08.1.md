---
level: 1.1
normative: true

references:
        - type: cpp_test
          name: "parser class - core;accept;number;integers"
          path: "TSF/tests/unit-class_parser_core.cpp"
        - type: function_reference
          name: "parser::accept"
          path: "include/nlohmann/detail/input/parser.hpp"
        - type: function_reference
          name: "parser::sax_parse"
          path: "include/nlohmann/detail/input/parser.hpp"
        - type: function_reference
          name: "parser::sax_parse_internal"
          path: "include/nlohmann/detail/input/parser.hpp"
        - type: function_reference
          name: "lexer::scan"
          path: "include/nlohmann/detail/input/lexer.hpp"
        - type: function_reference
          name: "lexer::scan_number"
          path: "include/nlohmann/detail/input/lexer.hpp"
score:
    Jonas-Kirchhoff: 0.9
---

The service does accept integers within the limits of 64-bit double.
---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parser class - core;parse;null"
          path: "TSF/tests/unit-class_parser_core.cpp"
        - type: function_reference
          name: "parser::parse"
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
          name: "lexer::scan_literal"
          path: "include/nlohmann/detail/input/lexer.hpp"
score:
    Jonas-Kirchhoff: 1.0
---

The service parses the literal name null.
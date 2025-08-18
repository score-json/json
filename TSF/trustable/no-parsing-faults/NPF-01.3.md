---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parse;UTF-8;unexpected BOM"
          path: "TSF/tests/unit-byte_order_mark.cpp"
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
score:
    Jonas-Kirchhoff: 1.0
---

The service does not parse UTF-8 byte order marks outside of a string and the first three characters of the input, and throws an exception.
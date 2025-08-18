---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "regression tests 1;issue #379 - locale-independent str-to-num"
          path: "tests/src/unit-regression1.cpp"
        - type: cpp_test
          name: "parse;trailing zeroes"
          path: "TSF/tests/unit-numbers.cpp"
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
          name: "lexer::scan_number"
          path: "include/nlohmann/detail/input/lexer.hpp"
score:
    Jonas-Kirchhoff: 1.0
---

The service ignores trailing zeroes after the decimal point.
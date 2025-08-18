---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "compliance tests from nativejson-benchmark;doubles"
          path: "tests/src/unit-testsuites.cpp"
        - type: cpp_test
          name: "regression tests 1;issue #360 - Loss of precision when serializing <double>"
          path: "tests/src/unit-regression1.cpp"
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

The service parses floating point numbers within IEEE 754-2008 binary64 standard.
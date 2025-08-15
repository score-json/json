---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "Unicode (1/5);ignore byte-order-mark"
          path: "tests/src/unit-unicode1.cpp"
        - type: cpp_test
          name: "deserialization;ignoring byte-order marks;BOM and content"
          path: "tests/src/unit-deserialization.cpp"
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
    Jonas-Kirchhoff: 0.95
---

The service ignores the presence of a single UTF-8 byte order mark at the very beginning of the input.
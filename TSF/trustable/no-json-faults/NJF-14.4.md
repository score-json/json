---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "accept;UTF-8;Other byte-order marks;UTF-16"
          path: "TSF/tests/unit-byte_order_mark.cpp"
        - type: cpp_test
          name: "accept;UTF-8;Other byte-order marks;UTF-32"
          path: "TSF/tests/unit-byte_order_mark.cpp"
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
score:
    Jonas-Kirchhoff: 1.0
---

The service does not accept UTF-16 and UTF-32 byte order marks instead of the UTF-8 byte order mark.
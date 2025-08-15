---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "deserialization;JSON Lines"
          path: "tests/src/unit-deserialization.cpp"
        - type: cpp_test
          name: "parser class - core;accept;object;nonempty object"
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
score:
    Jonas-Kirchhoff: 0.7        
---

The service accepts the non-empty objects.
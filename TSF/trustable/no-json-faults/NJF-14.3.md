---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-01
        - type: function_reference
          name: "parser::accept"
          path: "include/nlohmann/detail/input/parser.hpp"
          description: "function, which implements the service to check for well-formed json"
        - type: function_reference
          name: "parser::sax_parse"
          path: "include/nlohmann/detail/input/parser.hpp"
          description: "function, which is called by parser::accept"
        - type: function_reference
          name: "parser::sax_parse_internal"
          path: "include/nlohmann/detail/input/parser.hpp"
          description: "function, which is called by parser::sax_parse"
        - type: function_reference
          name: "lexer::scan"
          path: "include/nlohmann/detail/input/lexer.hpp"
          description: "function, which is called by parser::sax_parse_internal to read input data"
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

The service does not accept incomplete or perturbed UTF-8 byte order marks within the first three characters of the input.
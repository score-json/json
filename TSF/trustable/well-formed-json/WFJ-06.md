---
level: 1.1
normative: true
references:
        - type: function_reference
          name: "basic_json::accept"
          path: "include/nlohmann/json.hpp"
          description: ""
          overload: 1
        - type: function_reference
          name: "basic_json::accept"
          path: "include/nlohmann/json.hpp"
          description: ""
          overload: 2
        - type: function_reference
          name: "basic_json::accept"
          path: "include/nlohmann/json.hpp"
          description: ""
          overload: 3
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
    Erikhu1: 1.0
---

The service checks that a JSON value must be an object, array, number, or string, or one of the lowercase literal names false, null, or true
---
level: 1.1
normative: true

references:
        - type: cpp_test
          name: "compliance tests from json.org;expected passes"
          path: "tests/src/unit-testsuites.cpp"
        - type: function_reference
          name: "parser::accept"
          path: "include/nlohmann/detail/input/parser.hpp"
        - type: function_reference
          name: "parser::sax_parse"
          path: "include/nlohmann/detail/input/parser.hpp"
        - type: function_reference
          name: "parser::sax_parse_internal"
          path: "include/nlohmann/detail/input/parser.hpp"
score:
    Jonas-Kirchhoff: 0.7
---

The service accepts JSON data consisting of combinations of the data types.
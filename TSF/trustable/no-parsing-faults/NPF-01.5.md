---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "deserialization;ignoring byte-order marks;2 byte of BOM"
          path: "tests/src/unit-deserialization.cpp"
        - type: cpp_test
          name: "deserialization;ignoring byte-order marks;1 byte of BOM"
          path: "tests/src/unit-deserialization.cpp"
        - type: cpp_test
          name: "deserialization;ignoring byte-order marks;variations"
          path: "tests/src/unit-deserialization.cpp"
        - type: cpp_test
          name: "Unicode (1/5);error for incomplete/wrong BOM"
          path: "tests/src/unit-unicode1.cpp"
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
    Jonas-Kirchhoff: 0.9
---

The service does not parse partial and perturbed UTF-8 byte order marks within the first three characters of the input and throws an exception.
---
level: 1.1
normative: true
references:
        - type: function_reference
          name: lexer::scan_literal
          path: "include/nlohmann/detail/input/lexer.hpp"
          description: "function to scan a literal candidate, compare it to its expected value and return the corresponding C++ literal"
---

The service parses literal names "true", "false" and "null" according to RFC8259.
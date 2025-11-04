---
level: 1.1
normative: true
references:
        - type: function_reference
          name: "lexer::scan_number"
          path: "include/nlohmann/detail/input/lexer.hpp"
          description: "function, which parses numbers into C++ number-types and verifies *en passant* that these numbers are in accordance with RFC8259"
---

The service provided by nlohmann/json parses numbers according to RFC8259.
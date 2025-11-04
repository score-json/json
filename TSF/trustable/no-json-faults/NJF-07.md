---
level: 1.1
normative: true
references:
        - type: function_reference
          name: "lexer::scan_string"
          path: "include/nlohmann/detail/input/lexer.hpp"
          description: "function which scans a string and verifies *en passant* that the string is in accordance with RFC8259"
---

The service provided by nlohmann/json accepts and rejects strings according to RFC8259 §7.
---
level: 1.1
normative: true
references:
        - type: function_reference
          name: "lexer::scan_number"
          path: "include/nlohmann/detail/input/lexer.hpp"
          description: "function, which scans numbers and verifies *en passant* that these number is in accordance with RFC8259"
---

The service accepts numbers according to RFC8259 §6.

aschemmel-tech: maybe we add a NFJ-06.8 to document that we did a review on completeness of NJF-06.x versus RFC8259 §6
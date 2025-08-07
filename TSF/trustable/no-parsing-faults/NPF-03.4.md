---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "RFC 8259 examples;7. Strings"
          path: "/workspaces/json/tests/src/unit-testsuites.cpp"
        - type: cpp_test
          name: "Unicode (1/5);\\\\uxxxx read all unicode characters"
          path: "/workspaces/json/tests/src/unit-unicode1.cpp"
        - type: cpp_test
          name: "parse;unescaped unicode"
          path: "/workspaces/json/tests/s-core/unit-strings.cpp"
---

The service parses all unescaped utf-8 characters except quotation mark, reverse solidus and the control characters.
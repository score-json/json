---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "RFC 8259 examples;7. Strings"
          path: "/workspaces/json/tests/src/unit-testsuites.cpp"
        - type: JSON_testsuite
          name: "Unicode (1/5);read all unicode characters"
          path: "/workspaces/json/tests/src/unit-unicode1.cpp"
          test_suite_paths:
            - "/json_nlohmann_tests/all_unicode.json"
          description: ""
        - type: cpp_test
          name: "parse;unescaped unicode"
          path: "/workspaces/json/TSF/tests/unit-strings.cpp"
---

The service parses all unescaped utf-8 characters except quotation mark, reverse solidus and the control characters.
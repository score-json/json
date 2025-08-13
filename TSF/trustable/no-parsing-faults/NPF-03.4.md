---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "RFC 8259 examples;7. Strings"
          path: "tests/src/unit-testsuites.cpp"
        - type: JSON_testsuite
          name: "Unicode (1/5);read all unicode characters"
          path: "tests/src/unit-unicode1.cpp"
          test_suite_paths:
            - "/json_nlohmann_tests/all_unicode.json"
          description: ""
        - type: cpp_test
          name: "Unicode;unescaped unicode"
          path: "TSF/tests/unit-strings.cpp"
score:
    Jonas-Kirchhoff: 0.8
---

The service parses all unescaped utf-8 characters except quotation mark, reverse solidus and the control characters.
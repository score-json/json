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
evidence:
  type: "check_artifact_exists"
  configuration:
    check_amalgamation: exclude
    codeql: exclude
    dependency_review: exclude
    labeler: exclude
    publish_documentation: exclude
    test_trudag_extensions: exclude
    ubuntu: include
score:
    Jonas-Kirchhoff: 0.95
    Erikhu1: 1.0
---

The service parses all unescaped utf-8 characters except quotation mark, reverse solidus and the control characters.
---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-02
            - NPF-02
        - type: cpp_test
          name: "parser class - core;parse;number;integers;edge cases"
          path: "TSF/tests/unit-class_parser_core.cpp"
        - type: cpp_test
          name: "parser class - core;parse;number;integers;over the edge cases"
          path: "TSF/tests/unit-class_parser_core.cpp"
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
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

The service parses integers within IEEE 754-2008 binary64.
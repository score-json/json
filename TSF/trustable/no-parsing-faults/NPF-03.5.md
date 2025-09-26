---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-02
            - NPF-03
        - type: cpp_test
          name: "compliance tests from nativejson-benchmark;strings"
          path: "tests/src/unit-testsuites.cpp"
        - type: cpp_test
          name: "parser class - core;parse;string;escaped"
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

The service parses \\, \\/, \\b,\\f, \\n, \\r, \\t and escaped quotation marks.
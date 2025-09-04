---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parser class - core;parse;string;escaped"
          path: "TSF/tests/unit-class_parser_core.cpp"
        - type: cpp_test
          name: "compliance tests from nativejson-benchmark;strings"
          path: "tests/src/unit-testsuites.cpp"
        - type: cpp_test
          name: "Unicode (1/5);\\\\uxxxx sequences;correct sequences"
          path: "tests/src/unit-unicode1.cpp"
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

The service parses escaped characters in the basic multilingual plane.
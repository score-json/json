---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parse;UTF-8;unexpected BOM"
          path: "TSF/tests/unit-byte_order_mark.cpp"
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

The service does not parse UTF-8 byte order marks outside of a string and the first three characters of the input, and throws an exception.
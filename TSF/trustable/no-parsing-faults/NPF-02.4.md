---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-02
            - NPF-02
        - type: cpp_test
          name: "parser class - core;parse;number;floating-point"
          path: "TSF/tests/unit-class_parser_core.cpp"
        - type: cpp_test
          name: "regression tests 1;issue #360 - Loss of precision when serializing <double>"
          path: "tests/src/unit-regression1.cpp"
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

The service parses floating point values with exponent within the precision of 64-bit double.
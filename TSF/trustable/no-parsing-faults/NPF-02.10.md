---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "regression tests 1;issue #379 - locale-independent str-to-num"
          path: "tests/src/unit-regression1.cpp"
        - type: cpp_test
          name: "parse;trailing zeroes"
          path: "TSF/tests/unit-numbers.cpp"
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

The service ignores trailing zeroes after the decimal point.
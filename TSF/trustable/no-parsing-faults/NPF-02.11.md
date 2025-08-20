---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "regression tests 1;issue #186 miloyip/nativejson-benchmark: floating-point parsing"
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
---

The service parses numbers outside the 64-bit double range without throwing an exception.
---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parse;exponents;leading zeroes"
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
---

The service ignores leading zeroes in the exponent.
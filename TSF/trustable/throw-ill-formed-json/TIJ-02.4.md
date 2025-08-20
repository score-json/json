---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parse;exponents;U+0425"
          path: "TSF/tests/unit-numbers.cpp"
        - type: cpp_test
          name: "parse;exponents;U+0436"
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

The service throws an exception on U+0415 and U+0436 instead of U+0045 or U+0065.
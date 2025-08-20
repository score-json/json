---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parse;capitalisation"
          path: "TSF/tests/unit-literals.cpp"
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
---

The service throws an exception on capitalised literal names.
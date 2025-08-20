---
level: 1.1
normative: true

references:
        - type: cpp_test
          name: "compliance tests from json.org;expected passes"
          path: "tests/src/unit-testsuites.cpp"
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

The service accepts JSON data consisting of combinations of the data types.
---
level: 1.1
normative: true

references:
        - type: item
          items:
            - JLEX-01
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
score:
    Jonas-Kirchhoff: 0.95
    Erikhu1: 0.95
---

The service accepts JSON data consisting of combinations of the data types.
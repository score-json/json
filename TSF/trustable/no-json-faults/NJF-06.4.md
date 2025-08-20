---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "nst's JSONTestSuite;test_parsing;n"
          path: "tests/src/unit-testsuites.cpp"
        - type: cpp_test
          name: "nst's JSONTestSuite (2);test_parsing;n"
          path: "tests/src/unit-testsuites.cpp"
        - type: cpp_test
          name: "compliance tests from json.org;expected failures"
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

The admissible members of an object have the form name : value.
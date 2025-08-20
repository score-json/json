---
level: 1.1
normative: true
references:
        - type: JSON_testsuite
          name: "compliance tests from json.org;expected passes"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/json_tests/pass2.json"
          description: ""
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;i -> y"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/i_structure_500_nested_arrays.json"
          description: ""
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

The service accepts nested arrays.
---
level: 1.1
normative: true
references:
        - type: cpp_test
          path: "TSF/tests/unit-class_parser_core.cpp"
          name: "parser class - core"
        - type: JSON_testsuite
          name: "nst's JSONTestSuite;test_parsing;y"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite/test_parsing/y_structure_lonely_null.json"
          description: ""
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;y"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/y_structure_lonely_null.json"
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

The service accepts the literal name null. 
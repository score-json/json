---
level: 1.1
normative: true
references:
        - type: JSON_testsuite
          name: "nst's JSONTestSuite;test_parsing;n"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite/test_parsing/n_incomplete_false.json"
            - "/nst_json_testsuite/test_parsing/n_incomplete_null.json"
            - "/nst_json_testsuite/test_parsing/n_incomplete_true.json"
            - "/nst_json_testsuite/test_parsing/n_structure_number_with_trailing_garbage.json"
          description: ""
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;n"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_incomplete_false.json"
            - "/nst_json_testsuite2/test_parsing/n_incomplete_null.json"
            - "/nst_json_testsuite2/test_parsing/n_incomplete_true.json"
            - "/nst_json_testsuite2/test_parsing/n_structure_capitalized_True.json"
          description: ""
        - type: cpp_test
          name: "parse;illegal literals"
          path: "TSF/tests/unit-literals.cpp"
evidence:
  type: "check_artifact_exists"
  configuration:
    ubuntu: "ubuntu"
---

The service throws an exception on any other than the three literal names true, false, null.
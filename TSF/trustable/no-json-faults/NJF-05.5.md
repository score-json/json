---
level: 1.1
normative: true
references:
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;n"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_array_double_comma.json"
            - "/nst_json_testsuite2/test_parsing/n_array_double_extra_comma.json"
            - "/nst_json_testsuite2/test_parsing/n_array_just_comma.json"
            - "/nst_json_testsuite2/test_parsing/n_array_number_and_comma.json"
            - "/nst_json_testsuite2/test_parsing/n_array_number_and_several_commas.json"
            - "/nst_json_testsuite2/test_parsing/n_structure_array_with_unclosed_string.json"
            - "/nst_json_testsuite2/test_parsing/n_array_invalid_utf8.json"
            - "/nst_json_testsuite2/test_parsing/n_array_just_minus.json"
          description: "Checks that various \"proper\" arrays with improper elements are rejected."
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

The service does not accept arrays with improper values.
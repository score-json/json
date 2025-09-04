---
level: 1.1
normative: true
references:
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;n"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_object_single_quote.json"
            - "/nst_json_testsuite2/test_parsing/n_object_unquoted_key.json"
            - "/nst_json_testsuite2/test_parsing/n_object_non_string_key.json"
            - "/nst_json_testsuite2/test_parsing/n_object_non_string_key_but_huge_number_instead.json"
            - "/nst_json_testsuite2/test_parsing/n_object_key_with_single_quotes.json"
            - "/nst_json_testsuite2/test_parsing/n_object_bracket_key.json"
            - "/nst_json_testsuite2/test_parsing/n_object_unquoted_key.json"
          description: "Checks that invalid names are rejected."
        - type: JSON_testsuite 
          name: "nst's JSONTestSuite (2);test_parsing;i -> n"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/i_object_key_lone_2nd_surrogate.json"
          description: "Checks that string with invalid utf16 surrogate is rejected as name"
        - type: cpp_test
          name: "accept;member separator"
          path: "TSF/tests/unit-objects.cpp"
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
    Erikhu1: 1.0
---

If the service does not accept any name candidate as singleton, then the service does not accept the object candidate.
---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-01
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;n"   
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_object_comma_instead_of_colon.json"
          description: "Checks that comma instead of colon is rejected."
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;n"
          path: "tests/src/unit-testsuites.cpp" 
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_object_double_colon.json"
          description: "Checks that double colon is rejected."
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;n"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_object_missing_colon.json"
            - "/nst_json_testsuite2/test_parsing/n_object_missing_semicolon.json"
            - "/nst_json_testsuite2/test_parsing/n_object_missing_semicolon.json"
          description: "Checks that the empty member separator is rejected."
        - type: cpp_test
          name: "accept;member separator"
          path: "TSF/tests/unit-objects.cpp"
evidence:
  type: check_test_results
  configuration:
    tests: 
        - objects
        - testsuites
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

The service does not accept any other member separator.
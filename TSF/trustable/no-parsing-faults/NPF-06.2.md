---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-02
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;y"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/y_object_duplicated_key.json"
            - "/nst_json_testsuite2/test_parsing/y_object_duplicated_key_and_value.json"
          description: ""
evidence:
  type: check_test_results
  configuration:
    tests: 
        - testsuites
score:
    Jonas-Kirchhoff: 0.9
    Erikhu1: 0.95
---

The service parses duplicate names without error and reports the last member with that name only.
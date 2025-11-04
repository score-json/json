---
level: 1.1
normative: true
references:
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;n"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_object_bad_value.json"
          description: "Checks that the invalid literal \"truth\" as value throws an exception."
evidence:
  type: check_test_results
  configuration:
    tests: 
        - testsuites
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

The service provided by nlohmann/json throws an exception if any member has an improper value.
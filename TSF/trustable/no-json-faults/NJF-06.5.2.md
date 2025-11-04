---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-01
            - NJF-06.5
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;n"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_object_bad_value.json"
          description: "Checks that the invalid literal \"truth\" as value is rejected."
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

If the service provided by nlohmann/json does not accept any value candidate as singleton, then the service does not accept the object candidate.
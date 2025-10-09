---
level: 1.1
normative: true
references:
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;y"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/y_array_with_several_null.json"
          description: "Checks that [1,null,null,null,2] is accepted."
        - type: JSON_testsuite
          name: "json.org examples;4.json"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/json.org/4.json"
          description: ""
        - type: JSON_testsuite
          name: "json.org examples;5.json"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/json.org/5.json"
          description: ""
evidence:
  type: check_test_results
  configuration:
    tests: 
        - testsuites
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

The service does accept comma as value separator.
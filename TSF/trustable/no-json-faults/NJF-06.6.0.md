---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-01
        - type: JSON_testsuite
          name: "json.org examples"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/json.org/1.json"
            - "/json.org/2.json"
            - "/json.org/3.json"
            - "/json.org/4.json"
            - "/json.org/5.json"
          description: "Checks that various nested objects are accepted."
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
    Jonas-Kirchhoff: 0.975
    Erikhu1: 0.95
---

The acceptance of nested objects inside nlohmann/json does not depend on the depth of nesting.
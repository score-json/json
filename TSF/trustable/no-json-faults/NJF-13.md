---
level: 1.1
normative: true

references:
        - type: item
          items:
            - JLEX-01
        - type: cpp_test
          name: "compliance tests from json.org;expected passes"
          path: "tests/src/unit-testsuites.cpp"
evidence:
  type: check_test_results
  configuration:
    tests: 
        - testsuites
score:
    Jonas-Kirchhoff: 0.95
    Erikhu1: 0.95
---

The service provided by the nlohmann/json library accepts JSON data consisting of combinations of the data types.
---
level: 1.1
normative: true

references:
        - type: item
          items:
            - JLEX-01
        - type: cpp_test
          name: "accept;overlong sequences"
          path: "TSF/tests/unit-strings.cpp"
evidence:
  type: check_test_results
  configuration:
    tests: 
        - strings
score:
    Jonas-Kirchhoff: 0.6
    Erikhu1: 0.9
---

The service provided by nlohmann/json rejects "overlong sequences".
---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parse;capitalisation"
          path: "TSF/tests/unit-literals.cpp"
evidence:
  type: check_test_results
  configuration:
    tests: 
        - literals
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

The service provided by nlohmann/json throws an exception on capitalised literal names.
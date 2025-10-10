---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parse;exponents;leading plus"
          path: "TSF/tests/unit-numbers.cpp"
evidence:
  type: check_test_results
  configuration:
    tests: 
        - numbers
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

The service ignores one singular leading plus of the exponent.
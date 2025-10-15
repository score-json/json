---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-02
            - NPF-02
        - type: cpp_test
          name: "parse;exponents;leading zeroes"
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

The service ignores leading zeroes in the exponent.
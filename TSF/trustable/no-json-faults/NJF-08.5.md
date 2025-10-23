---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-01
            - NJF-08
        - type: cpp_test
          name: "accept;exponents;U+0425"
          path: "TSF/tests/unit-numbers.cpp"
        - type: cpp_test
          name: "accept;exponents;U+0436"
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

The service does not accept u0415 and u0436 (cyrillic e and E) as exponent signs in numbers with exponent.

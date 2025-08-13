---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "accept;exponents;U+0425"
          path: "TSF/tests/unit-numbers.cpp"
        - type: cpp_test
          name: "accept;exponents;U+0436"
          path: "TSF/tests/unit-numbers.cpp"
score:
    Jonas-Kirchhoff: 0.9
---

The service does not accept u0415 and u0436 (cyrillic e and E) as exponent signs in numbers with exponent.

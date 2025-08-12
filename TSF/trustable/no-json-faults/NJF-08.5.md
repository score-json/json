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
    Jonas-Kirchhoff: 0.8
---

The service does not accept cyrillic e u0415, u0436, nor exp.

---
level: 1.1
normative: true

references:
        - type: item
          items:
            - JLEX-01
        - type: cpp_test
          name: "Unicode;escaped unicode"
          path: "TSF/tests/unit-strings.cpp"
evidence:
  type: check_test_results
  configuration:
    tests: 
        - strings
score:
    Jonas-Kirchhoff: 0.9
    Erikhu1: 1.0
---

The service accepts well-formed UTF-8 data.

sab
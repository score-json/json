---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-02
            - NPF-03
        - type: cpp_test
          name: "Unicode;escaped unicode"
          path: "TSF/tests/unit-strings.cpp"
evidence:
  type: check_test_results
  configuration:
    tests: 
        - strings
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 0.95
---

The service ignores capitalisation in escaped hexadecimal unicode.
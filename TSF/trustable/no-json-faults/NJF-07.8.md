---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-01
            - NJF-07
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
    Erikhu1: 1.0
---

The service provided by the nlohmann/json library does not accept single unpaired utf-16 surrogates.
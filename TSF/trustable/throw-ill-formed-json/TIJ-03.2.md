---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "Unicode;unescaped unicode"
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

The service provided by nlohmann/json throws an exception on unpaired utf-16 surrogates.
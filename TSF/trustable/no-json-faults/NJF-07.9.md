---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-01
            - NJF-07
        - type: cpp_test
          name: "Unicode;unescaped unicode"
          path: "TSF/tests/unit-strings.cpp"
evidence:
  type: check_test_results
  configuration:
    tests: 
        - strings
score:
    Jonsa-Kirchhoff: 1.0
---

The service provided by the nlohmann/json library does not accept unescaped UTF-16 surrogate pairs.
---
level: 1.1
normative: true

references:
        - type: item
          items:
            - JLEX-01
        - type: cpp_test
          name: "accept;noncharacter code positions"
          path: "TSF/tests/unit-strings.cpp"
        - type: cpp_test
          name: "Unicode;unescaped unicode"
          path: "TSF/tests/unit-strings.cpp"
evidence:
  type: check_test_results
  configuration:
    tests: 
        - strings
score:
    Jonas-Kirchhoff: 0.75
    Erikhu1: 1.0
---

The service provided by nlohmann/json accepts Non-Characters.
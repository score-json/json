---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-01
        - type: cpp_test
          name: "nst's JSONTestSuite (2);test_parsing;n"
          path: "tests/src/unit-testsuites.cpp"
evidence:
  type: check_test_results
  configuration:
    tests: 
        - testsuites
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

The service provided by nlohmann/json does not accept any other structural characters.
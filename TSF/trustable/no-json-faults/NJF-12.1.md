---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-01
        - type: cpp_test
          name: "accept;malformed sequences"
          path: "TSF/tests/unit-strings.cpp"
evidence:
  type: check_test_results
  configuration:
    tests: 
        - strings
score:
    Jonas-Kirchhoff: 0.9
    Erikhu1: 0.95
---

The service rejects malformed UTF-8 data.
---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "Unicode (1/5);\\\\uxxxx sequences;incorrect sequences;incorrect surrogate values"
          path: "tests/src/unit-unicode1.cpp"
        - type: cpp_test
          name: "Unicode;escaped utf-16 surrogates;ill-formed"
          path: "TSF/tests/unit-strings.cpp"
evidence:
  type: check_test_results
  configuration:
    tests: 
        - unicode1
        - strings
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

The service provided by the nlohmann/json library throws an exception on incorrect surrogate pairs.
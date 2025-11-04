---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-02
            - NPF-02
        - type: cpp_test
          name: "compliance tests from nativejson-benchmark;doubles"
          path: "tests/src/unit-testsuites.cpp"
        - type: cpp_test
          name: "regression tests 1;issue #360 - Loss of precision when serializing <double>"
          path: "tests/src/unit-regression1.cpp"
evidence:
  type: check_test_results
  configuration:
    tests: 
        - regression1
        - testsuites
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

The service provided by nlohmann/json parses floating point numbers within IEEE 754-2008 binary64 standard.
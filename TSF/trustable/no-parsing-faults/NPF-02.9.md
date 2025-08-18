---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "compliance tests from nativejson-benchmark;doubles"
          path: "tests/src/unit-testsuites.cpp"
        - type: cpp_test
          name: "regression tests 1;issue #360 - Loss of precision when serializing <double>"
          path: "tests/src/unit-regression1.cpp"
score:
    Jonas-Kirchhoff: 1.0
---

The service parses floating point numbers within IEEE 754-2008 binary64 standard.
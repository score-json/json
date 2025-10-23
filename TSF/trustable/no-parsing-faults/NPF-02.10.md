---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-02
            - NPF-02
        - type: cpp_test
          name: "regression tests 1;issue #379 - locale-independent str-to-num"
          path: "tests/src/unit-regression1.cpp"
        - type: cpp_test
          name: "parse;trailing zeroes"
          path: "TSF/tests/unit-numbers.cpp"
evidence:
  type: check_test_results
  configuration:
    tests: 
        - regression1
        - numbers
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

The service ignores trailing zeroes after the decimal point.
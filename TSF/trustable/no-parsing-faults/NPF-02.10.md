---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "regression tests 1;issue #379 - locale-independent str-to-num"
          path: "tests/src/unit-regression1.cpp"
        - type: cpp_test
          name: "parse;trailing zeroes"
          path: "TSF/tests/unit-numbers.cpp"
score:
    Jonas-Kirchhoff: 0.85
---

The service ignores trailing zeroes after the decimal point.
---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "regression tests 1;issue #379 - locale-independent str-to-num"
          path: "/workspaces/json/tests/src/unit-regression1.cpp"
        - type: cpp_test
          name: "parse;trailing zeroes"
          path: "/workspaces/json/tests/s-core/unit-numbers.cpp"
---

The service ignores trailing zeroes after the decimal point.
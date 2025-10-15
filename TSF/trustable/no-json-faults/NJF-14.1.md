---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-01
        - type: cpp_test
          name: "accept;UTF-8;single BOM"
          path: "TSF/tests/unit-byte_order_mark.cpp"
evidence:
  type: check_test_results
  configuration:
    tests: 
        - byte_order_mark
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

If the service accepts an input containing no BOM, then it accepts a single UTF-8 byte order mark followed by that input.
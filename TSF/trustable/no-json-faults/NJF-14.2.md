---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "accept;UTF-8;multiple BOM"
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

The service does not accept multiple UTF-8 byte order marks.
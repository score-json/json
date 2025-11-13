---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-02
        - type: cpp_test
          name: "parse;other BOM"
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

The service provided by the nlohmann/json library does not parse UTF-16 and UTF-32 byte order mark instead of an UTF-8 byte order mark, and throws an exception.
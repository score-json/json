---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "accept;UTF-8;single BOM"
          path: "TSF/tests/unit-byte_order_mark.cpp"
score:
    Jonas-Kirchhoff: 1.0
---

The service accepts a single UTF-8 byte order mark in the first three characters of the input.
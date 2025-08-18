---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parse;other BOM"
          path: "TSF/tests/unit-byte_order_mark.cpp"
score:
    Jonas-Kirchhoff: 1.0
---

The service does not parse UTF-16 and UTF-32 byte order mark instead of an UTF-8 byte order mark, and throws an exception.
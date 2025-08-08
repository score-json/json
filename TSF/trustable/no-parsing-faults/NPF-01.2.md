---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parse;UTF-8;multiple BOM"
          path: "/workspaces/json/TSF/tests/unit-byte_order_mark.cpp"
---

The service does not parse multiple UTF-8 byte order marks and throws an exception.
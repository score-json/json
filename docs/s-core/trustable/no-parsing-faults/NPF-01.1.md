---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "Unicode (1/5);ignore byte-order-mark"
          path: "/workspaces/json/tests/src/unit-unicode1.cpp"
        - type: cpp_test
          name: "deserialization;ignoring byte-order marks;BOM and content"
          path: "/workspaces/json/tests/src/unit-deserialization.cpp"
---

The service ignores the presence of a single UTF-8 byte order mark.
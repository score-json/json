---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "accept;UTF-8;Other byte-order marks;UTF-16"
          path: "/workspaces/json/TSF/tests/unit-byte_order_mark.cpp"
        - type: cpp_test
          name: "accept;UTF-8;Other byte-order marks;UTF-32"
          path: "/workspaces/json/TSF/tests/unit-byte_order_mark.cpp"
---

The service does not accept UTF-16 and UTF-32 byte order marks.
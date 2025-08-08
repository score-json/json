---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "deserialization;ignoring byte-order marks;2 byte of BOM"
          path: "/workspaces/json/tests/src/unit-deserialization.cpp"
        - type: cpp_test
          name: "deserialization;ignoring byte-order marks;1 byte of BOM"
          path: "/workspaces/json/tests/src/unit-deserialization.cpp"
        - type: cpp_test
          name: "deserialization;ignoring byte-order marks;variations"
          path: "/workspaces/json/tests/src/unit-deserialization.cpp"
        - type: cpp_test
          name: "Unicode (1/5);error for incomplete/wrong BOM"
          path: "/workspaces/json/tests/src/unit-unicode1.cpp"
---

The service does not parse partial and perturbed UTF-8 byte order marks and throws an exception.
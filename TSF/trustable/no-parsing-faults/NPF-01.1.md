---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "Unicode (1/5);ignore byte-order-mark"
          path: "tests/src/unit-unicode1.cpp"
        - type: cpp_test
          name: "deserialization;ignoring byte-order marks;BOM and content"
          path: "tests/src/unit-deserialization.cpp"
evidence:
  type: "check_artifact_exists"
  configuration:
    ubuntu: "ubuntu"
---

The service ignores the presence of a single UTF-8 byte order mark.
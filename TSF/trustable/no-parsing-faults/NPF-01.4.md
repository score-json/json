---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parse;other BOM"
          path: "TSF/tests/unit-byte_order_mark.cpp"
evidence:
  type: "check_artifact_exists"
  configuration:
    ubuntu: "ubuntu"
---

The service does not parse UTF-16 and UTF-32 byte order mark, and throws an exception.
---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "accept;UTF-8;multiple BOM"
          path: "TSF/tests/unit-byte_order_mark.cpp"
evidence:
  type: "check_artifact_exists"
  configuration:
    ubuntu: "ubuntu"
---

The service does not accept multiple UTF-8 byte order marks.
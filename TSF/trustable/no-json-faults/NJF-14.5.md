---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "accept;UTF-8;unexpected BOM"
          path: "TSF/tests/unit-byte_order_mark.cpp"
evidence:
  type: "check_artifact_exists"
  configuration:
    ubuntu: "ubuntu"
---

The service does not accept UTF-8 byte order marks at any other place of the input.
---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parser class - core;accept;object;empty object"
          path: "TSF/tests/unit-class_parser_core.cpp"
        - type: cpp_test
          name: "accept;whitespace;empty object"
          path: "TSF/tests/unit-objects.cpp"
evidence:
  type: "check_artifact_exists"
  configuration:
    ubuntu: "ubuntu"
---

The service accepts the empty object.
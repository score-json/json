---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parse;whitespace"
          path: "TSF/tests/unit-literals.cpp"
evidence:
  type: "check_artifact_exists"
  configuration:
    ubuntu: "ubuntu"
---

The service ignores leading and trailing whitespace.
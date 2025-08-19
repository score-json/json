---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parse;capitalisation"
          path: "TSF/tests/unit-literals.cpp"
evidence:
  type: "check_artifact_exists"
  configuration:
    ubuntu: "ubuntu"
---

The service throws an exception on capitalised literal names.
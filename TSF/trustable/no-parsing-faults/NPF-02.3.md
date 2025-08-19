---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parser class - core;parse;number;integers"
          path: "TSF/tests/unit-class_parser_core.cpp"
evidence:
  type: "check_artifact_exists"
  configuration:
    ubuntu: "ubuntu"
---

The service parses floating point values without exponent.
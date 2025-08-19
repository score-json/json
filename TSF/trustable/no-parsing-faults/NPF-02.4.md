---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parser class - core;parse;number;floating-point"
          path: "TSF/tests/unit-class_parser_core.cpp"
        - type: cpp_test
          name: "regression tests 1;issue #360 - Loss of precision when serializing <double>"
          path: "tests/src/unit-regression1.cpp"
evidence:
  type: "check_artifact_exists"
  configuration:
    ubuntu: "ubuntu"
---

The service parses floating point values with exponent.
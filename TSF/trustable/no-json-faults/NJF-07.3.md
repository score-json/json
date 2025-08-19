---
level: 1.1
normative: true

references:
        - type: cpp_test
          name: "parser class - core;accept;string;errors"
          path: "TSF/tests/unit-class_parser_core.cpp"
evidence:
  type: "check_artifact_exists"
  configuration:
    ubuntu: "ubuntu"
---

The service does not accept unescaped control characters.

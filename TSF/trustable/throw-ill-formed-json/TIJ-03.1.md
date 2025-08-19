---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parser class - core;parse;string;errors"
          path: "TSF/tests/unit-class_parser_core.cpp"
evidence:
  type: "check_artifact_exists"
  configuration:
    ubuntu: "ubuntu"
---

The service throws an exception on unescaped control characters.
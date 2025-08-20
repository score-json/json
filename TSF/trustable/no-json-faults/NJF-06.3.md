---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "deserialization;JSON Lines"
          path: "tests/src/unit-deserialization.cpp"
        - type: cpp_test
          name: "parser class - core;accept;object;nonempty object"
          path: "TSF/tests/unit-class_parser_core.cpp"            
evidence:
  type: "check_artifact_exists"
  configuration:
    check_amalgamation: exclude
    codeql: exclude
    dependency_review: exclude
    labeler: exclude
    publish_documentation: exclude
    test_trudag_extensions: exclude
    ubuntu: include
---

The service accepts non-empty objects.
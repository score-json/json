---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "accept;UTF-8;single BOM"
          path: "TSF/tests/unit-byte_order_mark.cpp"
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

The service accepts a single UTF-8 byte order mark at the beginning of the input.
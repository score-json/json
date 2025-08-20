---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parse;UTF-8;multiple BOM"
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

The service does not parse multiple UTF-8 byte order marks and throws an exception.
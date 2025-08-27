---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "accept;UTF-8;Other byte-order marks;UTF-32"
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
score:
    Jonas-Kirchhoff: 1.0
---

The service does not accept UTF-16 and UTF-32 byte order marks instead of the UTF-8 byte order mark.
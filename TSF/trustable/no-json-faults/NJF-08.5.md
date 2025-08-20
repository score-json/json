---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "accept;exponents;U+0425"
          path: "TSF/tests/unit-numbers.cpp"
        - type: cpp_test
          name: "accept;exponents;U+0436"
          path: "TSF/tests/unit-numbers.cpp"
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

The service does not accept cyrillic e u0415, u0436, nor exp.

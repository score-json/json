---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-01
        - type: cpp_test
          name: "accept;malformed sequences"
          path: "TSF/tests/unit-strings.cpp"
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
    Jonas-Kirchhoff: 0.9
    Erikhu1: 0.95
---

The service rejects malformed UTF-8 data.
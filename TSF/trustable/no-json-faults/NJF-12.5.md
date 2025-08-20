---
level: 1.1
normative: true

references:
        - type: cpp_test
          name: "accept;noncharacter code positions"
          path: "TSF/tests/unit-strings.cpp"
        - type: cpp_test
          name: "Unicode;unescaped unicode"
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
    Jonas-Kirchhoff: 0.75
---

The service accepts Non-Characters.
---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "deserialization;ignoring byte-order marks;2 byte of BOM"
          path: "tests/src/unit-deserialization.cpp"
        - type: cpp_test
          name: "deserialization;ignoring byte-order marks;1 byte of BOM"
          path: "tests/src/unit-deserialization.cpp"
        - type: cpp_test
          name: "deserialization;ignoring byte-order marks;variations"
          path: "tests/src/unit-deserialization.cpp"
        - type: cpp_test
          name: "Unicode (1/5);error for incomplete/wrong BOM"
          path: "tests/src/unit-unicode1.cpp"
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

The service does not parse partial and perturbed UTF-8 byte order marks within the first three characters of the input and throws an exception.
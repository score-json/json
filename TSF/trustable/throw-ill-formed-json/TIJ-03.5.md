---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "Unicode (1/5);\\\\uxxxx sequences;incorrect sequences;incorrect surrogate values"
          path: "tests/src/unit-unicode1.cpp"
        - type: cpp_test
          name: "Unicode;escaped utf-16 surrogates;ill-formed"
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
    Jonas-Kirchhoff: 1.0
---

The service throws an exception on incorrect surrogate pairs.
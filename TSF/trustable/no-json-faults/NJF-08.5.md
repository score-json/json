---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-01
            - NJF-08
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
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

The service does not accept u0415 and u0436 (cyrillic e and E) as exponent signs in numbers with exponent.

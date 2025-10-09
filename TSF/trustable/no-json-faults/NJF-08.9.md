---
level: 1.1
normative: true

references:
        - type: item
          items:
            - JLEX-01
            - NJF-08
        - type: cpp_test
          name: "parser class - core;accept;number;integers"
          path: "TSF/tests/unit-class_parser_core.cpp"
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;n"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_number_hex_1_digit.json"
            - "/nst_json_testsuite2/test_parsing/n_number_hex_2_digits.json"
            - "/nst_json_testsuite2/test_parsing/n_number_hex_2_digits.json"
          description: "Rejects Hexadecimals"
        - type: cpp_test
          name: "accept;bases"
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

The service does not accept any other digit symbol than 0-9.

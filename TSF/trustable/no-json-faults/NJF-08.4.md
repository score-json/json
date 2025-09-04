---
level: 1.1
normative: true

references:
        - type: cpp_test
          name: "parser class - core;accept;number;integers;with exponent"
          path: "TSF/tests/unit-class_parser_core.cpp"
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;y"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/y_number_real_capital_e.json"
            - "/nst_json_testsuite2/test_parsing/y_number_real_capital_e_neg_exp.json"
            - "/nst_json_testsuite2/test_parsing/y_number_real_capital_e_pos_exp.json"
            - "/nst_json_testsuite2/test_parsing/y_number_real_exponent.json"
            - "/nst_json_testsuite2/test_parsing/y_number_real_fraction_exponent.json"
            - "/nst_json_testsuite2/test_parsing/y_number_real_neg_exp.json"
            - "/nst_json_testsuite2/test_parsing/y_number_real_pos_exponent.json"
          description: "Checks that various numbers with exponent are accepted."
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

The service does accept e or E for numbers with exponent within the bounds of double.

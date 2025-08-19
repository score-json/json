---
level: 1.1
normative: true
references:
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;n"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_number_-01.json"
            - "/nst_json_testsuite2/test_parsing/n_number_neg_int_starting_with_zero.json"
          description: "Checks that -01 is rejected."
        - type: cpp_test
          name: "parser class - core;parse;number;invalid numbers"
          path: "TSF/tests/unit-class_parser_core.cpp"
        - type: cpp_test
          name: "parse;leading zeroes"
          path: "TSF/tests/unit-numbers.cpp"
evidence:
  type: "check_artifact_exists"
  configuration:
    ubuntu: "ubuntu"
---

The service throws an exception on leading zeroes.
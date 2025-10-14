---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parser class - core;parse;number;floating-point;with exponent"
          path: "TSF/tests/unit-class_parser_core.cpp"
        - type: cpp_test
          name: "parser class - core;parse;number;integers;with exponent"
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
          description: "Tests whether several numbers with exponent are parsed without throwing an exception."
        - type: cpp_test
          name: "parse;Precision"
          path: "TSF/tests/unit-numbers.cpp"
evidence:
  type: check_test_results
  configuration:
    tests: 
        - class_parser_core
        - testsuites
        - numbers
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

The service parses integers with exponent within the precision of 64-bit double. 
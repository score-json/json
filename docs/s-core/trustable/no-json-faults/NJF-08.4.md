---
level: 1.1
normative: true

references:
        - type: cpp_test
          name: "parser class:accept:number:integers:with exponent"
          path: "/workspaces/json/tests/src/unit-class_parser.cpp"
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2):test_parsing:y"
          path: "/workspaces/json/tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/y_number_real_capital_e.json"
            - "/nst_json_testsuite2/test_parsing/y_number_real_capital_e_neg_exp.json"
            - "/nst_json_testsuite2/test_parsing/y_number_real_capital_e_pos_exp.json"
            - "/nst_json_testsuite2/test_parsing/y_number_real_exponent.json"
            - "/nst_json_testsuite2/test_parsing/y_number_real_fraction_exponent.json"
            - "/nst_json_testsuite2/test_parsing/y_number_real_neg_exp.json"
            - "/nst_json_testsuite2/test_parsing/y_number_real_pos_exponent.json"
          description: "Checks that various numbers with exponent are accepted."
---

The service does accept e or E.

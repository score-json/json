---
level: 1.1
normative: true

references:
        - type: cpp_test
          name: "parser class - core;accept;number;invalid numbers"
          path: "TSF/tests/unit-class_parser_core.cpp"
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;n"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_number_++.json"
            - "/nst_json_testsuite2/test_parsing/n_number_+1.json"
            - "/nst_json_testsuite2/test_parsing/n_number_+Inf.json"
            - "/nst_json_testsuite2/test_parsing/n_number_-01.json"
            - "/nst_json_testsuite2/test_parsing/n_number_-1.0..json"
            - "/nst_json_testsuite2/test_parsing/n_number_-2..json"
            - "/nst_json_testsuite2/test_parsing/n_number_-NaN.json"
            - "/nst_json_testsuite2/test_parsing/n_number_.-1.json"
            - "/nst_json_testsuite2/test_parsing/n_number_.2e-3.json"
            - "/nst_json_testsuite2/test_parsing/n_number_0.1.2.json"
            - "/nst_json_testsuite2/test_parsing/n_number_0.3e+.json"
            - "/nst_json_testsuite2/test_parsing/n_number_0.3e.json"
            - "/nst_json_testsuite2/test_parsing/n_number_0.e1.json"
            - "/nst_json_testsuite2/test_parsing/n_number_0_capital_E+.json"
            - "/nst_json_testsuite2/test_parsing/n_number_0_capital_E.json"
            - "/nst_json_testsuite2/test_parsing/n_number_0e+.json"
            - "/nst_json_testsuite2/test_parsing/n_number_0e.json"
            - "/nst_json_testsuite2/test_parsing/n_number_1.0e+.json"
            - "/nst_json_testsuite2/test_parsing/n_number_1.0e-.json"
            - "/nst_json_testsuite2/test_parsing/n_number_1.0e.json"
            - "/nst_json_testsuite2/test_parsing/n_number_1_000.json"
            - "/nst_json_testsuite2/test_parsing/n_number_1eE2.json"
            - "/nst_json_testsuite2/test_parsing/n_number_2.e+3.json"
            - "/nst_json_testsuite2/test_parsing/n_number_2.e-3.json"
            - "/nst_json_testsuite2/test_parsing/n_number_2.e3.json"
            - "/nst_json_testsuite2/test_parsing/n_number_9.e+.json"
            - "/nst_json_testsuite2/test_parsing/n_number_Inf.json"
            - "/nst_json_testsuite2/test_parsing/n_number_NaN.json"
            - "/nst_json_testsuite2/test_parsing/n_number_U+FF11_fullwidth_digit_one.json"
            - "/nst_json_testsuite2/test_parsing/n_number_expression.json"
            - "/nst_json_testsuite2/test_parsing/n_number_hex_1_digit.json"
            - "/nst_json_testsuite2/test_parsing/n_number_hex_2_digits.json"
            - "/nst_json_testsuite2/test_parsing/n_number_infinity.json"
            - "/nst_json_testsuite2/test_parsing/n_number_invalid+-.json"
            - "/nst_json_testsuite2/test_parsing/n_number_invalid-negative-real.json"
            - "/nst_json_testsuite2/test_parsing/n_number_invalid-utf-8-in-bigger-int.json"
            - "/nst_json_testsuite2/test_parsing/n_number_invalid-utf-8-in-exponent.json"
            - "/nst_json_testsuite2/test_parsing/n_number_invalid-utf-8-in-int.json"
            - "/nst_json_testsuite2/test_parsing/n_number_minus_infinity.json"
            - "/nst_json_testsuite2/test_parsing/n_number_minus_sign_with_trailing_garbage.json"
            - "/nst_json_testsuite2/test_parsing/n_number_minus_space_1.json"
            - "/nst_json_testsuite2/test_parsing/n_number_neg_int_starting_with_zero.json"
            - "/nst_json_testsuite2/test_parsing/n_number_neg_real_without_int_part.json"
            - "/nst_json_testsuite2/test_parsing/n_number_neg_with_garbage_at_end.json"
            - "/nst_json_testsuite2/test_parsing/n_number_real_garbage_after_e.json"
            - "/nst_json_testsuite2/test_parsing/n_number_real_with_invalid_utf8_after_e.json"
            - "/nst_json_testsuite2/test_parsing/n_number_real_without_fractional_part.json"
            - "/nst_json_testsuite2/test_parsing/n_number_starting_with_dot.json"
            - "/nst_json_testsuite2/test_parsing/n_number_with_alpha.json"
            - "/nst_json_testsuite2/test_parsing/n_number_with_alpha_char.json"
            - "/nst_json_testsuite2/test_parsing/n_number_with_leading_zero.json"
          description: "Tests whether various numbers with invalid syntax according to RFC8259 are rejected."
        - type: cpp_test
          name: "accept;operators"
          path: "TSF/tests/unit-numbers.cpp"
score:
    Jonas-Kirchhoff: 0.7
---

The service does not accept invalid syntax for numbers.

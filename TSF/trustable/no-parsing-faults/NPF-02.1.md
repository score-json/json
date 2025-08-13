---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parser class - core;parse;number;floating-point;without exponent"
          path: "TSF/tests/unit-class_parser_core.cpp"
        - type: cpp_test
          name: "parser class - core;parse;number;integers;without exponent"
          path: "TSF/tests/unit-class_parser_core.cpp"
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;y"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/y_number_simple_int.json"
            - "/nst_json_testsuite2/test_parsing/y_number_simple_real.json"
            - "/nst_json_testsuite2/test_parsing/y_number_negative_int.json"
            - "/nst_json_testsuite2/test_parsing/y_number_negative_one.json"
            - "/nst_json_testsuite2/test_parsing/y_number_negative_zero.json"
          description: "Tests whether several numbers without exponent are parsed without throwing an exception."
score:
    Jonas-Kirchhoff: 0.9
---

The service parses integers without exponent within the precision of int64_t. 
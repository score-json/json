---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parser class;parse;number;floating-point;without exponent"
          path: "/workspaces/json/tests/src/unit-class_parser.cpp"
        - type: cpp_test
          name: "parser class;parse;number;integers;without exponent"
          path: "/workspaces/json/tests/src/unit-class_parser.cpp"
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;y"
          path: "/workspaces/json/tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/y_number_simple_int.json"
            - "/nst_json_testsuite2/test_parsing/y_number_simple_real.json"
            - "/nst_json_testsuite2/test_parsing/y_number_negative_int.json"
            - "/nst_json_testsuite2/test_parsing/y_number_negative_one.json"
            - "/nst_json_testsuite2/test_parsing/y_number_negative_zero.json"
          description: "Tests whether several numbers without exponent are parsed without throwing an exception."
---

The service parses integers without exponent. 
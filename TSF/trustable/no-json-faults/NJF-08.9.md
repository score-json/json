---
level: 1.1
normative: true

references:
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
        - type: function_reference
          name: "parser::accept"
          path: "include/nlohmann/detail/input/parser.hpp"
        - type: function_reference
          name: "parser::sax_parse"
          path: "include/nlohmann/detail/input/parser.hpp"
        - type: function_reference
          name: "parser::sax_parse_internal"
          path: "include/nlohmann/detail/input/parser.hpp"
        - type: function_reference
          name: "lexer::scan"
          path: "include/nlohmann/detail/input/lexer.hpp"
        - type: function_reference
          name: "lexer::scan_number"
          path: "include/nlohmann/detail/input/lexer.hpp"
score:
    Jonas-Kirchhoff: 0.6
---

The service does not accept any base exceeding 10 in its standard representation.

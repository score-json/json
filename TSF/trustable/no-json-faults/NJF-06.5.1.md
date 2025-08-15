---
level: 1.1
normative: true
references:
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;n"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_object_single_quote.json"
            - "/nst_json_testsuite2/test_parsing/n_object_unquoted_key.json"
            - "/nst_json_testsuite2/test_parsing/n_object_non_string_key.json"
            - "/nst_json_testsuite2/test_parsing/n_object_non_string_key_but_huge_number_instead.json"
            - "/nst_json_testsuite2/test_parsing/n_object_key_with_single_quotes.json"
            - "/nst_json_testsuite2/test_parsing/n_object_bracket_key.json"
            - "/nst_json_testsuite2/test_parsing/n_object_unquoted_key.json"
          description: "Checks that invalid names are rejected."
        - type: JSON_testsuite 
          name: "nst's JSONTestSuite (2);test_parsing;i -> n"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/i_object_key_lone_2nd_surrogate.json"
          description: "Checks that string with invalid utf16 surrogate is rejected as name"
        - type: cpp_test
          name: "accept;member separator"
          path: "TSF/tests/unit-objects.cpp"
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
          name: "lexer::scan_string"
          path: "include/nlohmann/detail/input/lexer.hpp"
score:
    Jonas-Kirchhoff: 0.8
---

The service does not accept objects with improper name.
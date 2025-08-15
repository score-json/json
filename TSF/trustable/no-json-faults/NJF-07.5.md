---
level: 1.1
normative: true

references:
        - type: cpp_test
          name: "parser class - core;accept;string;escaped"
          path: "TSF/tests/unit-class_parser_core.cpp"
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;y"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/y_string_accepted_surrogate_pair.json"
            - "/nst_json_testsuite2/test_parsing/y_string_accepted_surrogate_pairs.json"
          description: "Checks that single and multiple surrogates are accepted."
        - type: cpp_test
          name: "Unicode;escaped utf-16 surrogates;well-formed"
          path: "TSF/tests/unit-strings.cpp"
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
    Jonas-Kirchhoff: 0.85
---

The service accepts UTF-16 surrogate pairs.
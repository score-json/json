---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parser class - core;accept;parse errors (accept)"
          path: "/workspaces/json/TSF/tests/unit-class_parser_core.cpp"
        - type: cpp_test
          name: "deserialization;contiguous containers;error cases"
          path: "/workspaces/json/tests/src/unit-deserialization.cpp"
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;n"
          path: "/workspaces/json/tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_string_no_quotes_with_bad_escape.json"
            - "/nst_json_testsuite2/test_parsing/n_string_single_doublequote.json"
            - "/nst_json_testsuite2/test_parsing/n_string_single_quote.json"
            - "/nst_json_testsuite2/test_parsing/n_string_single_string_no_double_quotes.json"
          description: ""
---

The service does not accept improperly bounded string.
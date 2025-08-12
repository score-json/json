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
            - "/nst_json_testsuite2/test_parsing/y_string_1_2_3_bytes_UTF-8_sequences.json"
            - "/nst_json_testsuite2/test_parsing/y_string_accepted_surrogate_pair.json"
            - "/nst_json_testsuite2/test_parsing/y_string_accepted_surrogate_pairs.json"
            - "/nst_json_testsuite2/test_parsing/y_string_allowed_escapes.json"
            - "/nst_json_testsuite2/test_parsing/y_string_backslash_and_u_escaped_zero.json"
            - "/nst_json_testsuite2/test_parsing/y_string_backslash_doublequotes.json"
            - "/nst_json_testsuite2/test_parsing/y_string_comments.json"
            - "/nst_json_testsuite2/test_parsing/y_string_double_escape_a.json"
            - "/nst_json_testsuite2/test_parsing/y_string_double_escape_n.json"
            - "/nst_json_testsuite2/test_parsing/y_string_escaped_control_character.json"
            - "/nst_json_testsuite2/test_parsing/y_string_escaped_noncharacter.json"
          description: "Checks that various escaped control and unicode characters are accepted."
        - type: cpp_test
          name: "Unicode (1/5);\\\\uxxxx sequences;correct sequences"
          path: "tests/src/unit-unicode1.cpp"
        - type: cpp_test
          name: "Unicode;escaped unicode"
          path: "TSF/tests/unit-strings.cpp"
score:
    Jonas-Kirchhoff: 0.85
---

The service does accept the escaped control characters.

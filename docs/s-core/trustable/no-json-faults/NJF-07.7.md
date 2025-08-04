---
level: 1.1
normative: true
references:
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2):test_parsing:n"
          path: "/workspaces/json/tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape.json"
            - "/nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape_u.json"
            - "/nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape_u1.json"
            - "/nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape_u1x.json" 
            - "/nst_json_testsuite2/test_parsing/n_string_accentuated_char_no_quotes.json"
            - "/nst_json_testsuite2/test_parsing/n_string_backslash_00.json"
            - "/nst_json_testsuite2/test_parsing/n_string_escape_x.json"
            - "/nst_json_testsuite2/test_parsing/n_string_escaped_backslash_bad.json"
            - "/nst_json_testsuite2/test_parsing/n_string_escaped_ctrl_char_tab.json"
            - "/nst_json_testsuite2/test_parsing/n_string_escaped_emoji.json"
            - "/nst_json_testsuite2/test_parsing/n_string_incomplete_escape.json"
            - "/nst_json_testsuite2/test_parsing/n_string_incomplete_escaped_character.json"
            - "/nst_json_testsuite2/test_parsing/n_string_incomplete_surrogate.json"
            - "/nst_json_testsuite2/test_parsing/n_string_incomplete_surrogate_escape_invalid.json"
            - "/nst_json_testsuite2/test_parsing/n_string_invalid-utf-8-in-escape.json"
            - "/nst_json_testsuite2/test_parsing/n_string_invalid_backslash_esc.json"
            - "/nst_json_testsuite2/test_parsing/n_string_invalid_unicode_escape.json"
            - "/nst_json_testsuite2/test_parsing/n_string_invalid_utf8_after_escape.json"
          description: "Checks that various illegal control characters and utf-8 characters are rejected."
---

The service does not accept escaped invalid characters.
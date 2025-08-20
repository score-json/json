---
level: 1.1
normative: true
references:
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;n"
          path: "tests/src/unit-testsuites.cpp"
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
          description: "Tests whether various illegal control characters and utf-8 characters throw an exception."
evidence:
  type: "check_artifact_exists"
  configuration:
    check_amalgamation: exclude
    codeql: exclude
    dependency_review: exclude
    labeler: exclude
    publish_documentation: exclude
    test_trudag_extensions: exclude
    ubuntu: include
score:
    Jonas-Kirchhoff: 1.0
---

The service throws an exception on escaped invalid characters.
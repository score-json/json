---
level: 1.1
normative: true
references:
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
            - "/nst_json_testsuite2/test_parsing/y_string_in_array.json"
            - "/nst_json_testsuite2/test_parsing/y_string_in_array_with_leading_space.json"
            - "/nst_json_testsuite2/test_parsing/y_string_last_surrogates_1_and_2.json"
            - "/nst_json_testsuite2/test_parsing/y_string_nbsp_uescaped.json"
            - "/nst_json_testsuite2/test_parsing/y_string_nonCharacterInUTF-8_U+10FFFF.json"
            - "/nst_json_testsuite2/test_parsing/y_string_nonCharacterInUTF-8_U+FFFF.json"
            - "/nst_json_testsuite2/test_parsing/y_string_null_escape.json"
            - "/nst_json_testsuite2/test_parsing/y_string_one-byte-utf-8.json"
            - "/nst_json_testsuite2/test_parsing/y_string_pi.json"
            - "/nst_json_testsuite2/test_parsing/y_string_reservedCharacterInUTF-8_U+1BFFF.json"
            - "/nst_json_testsuite2/test_parsing/y_string_simple_ascii.json"
            - "/nst_json_testsuite2/test_parsing/y_string_space.json"
            - "/nst_json_testsuite2/test_parsing/y_string_surrogates_U+1D11E_MUSICAL_SYMBOL_G_CLEF.json"
            - "/nst_json_testsuite2/test_parsing/y_string_three-byte-utf-8.json"
            - "/nst_json_testsuite2/test_parsing/y_string_two-byte-utf-8.json"
            - "/nst_json_testsuite2/test_parsing/y_string_u+2028_line_sep.json"
            - "/nst_json_testsuite2/test_parsing/y_string_u+2029_par_sep.json"
            - "/nst_json_testsuite2/test_parsing/y_string_uEscape.json"
            - "/nst_json_testsuite2/test_parsing/y_string_uescaped_newline.json"
            - "/nst_json_testsuite2/test_parsing/y_string_unescaped_char_delete.json"
            - "/nst_json_testsuite2/test_parsing/y_string_unicode.json"
            - "/nst_json_testsuite2/test_parsing/y_string_unicodeEscapedBackslash.json"
            - "/nst_json_testsuite2/test_parsing/y_string_unicode_2.json"
            - "/nst_json_testsuite2/test_parsing/y_string_unicode_U+10FFFE_nonchar.json"
            - "/nst_json_testsuite2/test_parsing/y_string_unicode_U+1FFFE_nonchar.json"
            - "/nst_json_testsuite2/test_parsing/y_string_unicode_U+200B_ZERO_WIDTH_SPACE.json"
            - "/nst_json_testsuite2/test_parsing/y_string_unicode_U+2064_invisible_plus.json"
            - "/nst_json_testsuite2/test_parsing/y_string_unicode_U+FDD0_nonchar.json"
            - "/nst_json_testsuite2/test_parsing/y_string_unicode_U+FFFE_nonchar.json"
            - "/nst_json_testsuite2/test_parsing/y_string_unicode_escaped_double_quote.json"
            - "/nst_json_testsuite2/test_parsing/y_string_utf8.json"
            - "/nst_json_testsuite2/test_parsing/y_string_with_del_character.json"
            - "/nst_json_testsuite2/test_parsing/y_structure_lonely_string.json"
          description: "Checks that various non-empty valid strings are accepted."
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
    Jonas-Kirchhoff: 0.95
    Erikhu1: 0.95
---

The service does accept the non-empty strings.
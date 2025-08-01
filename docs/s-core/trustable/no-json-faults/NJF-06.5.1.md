---
level: 1.1
normative: true
reference:
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2):test_parsing:n"
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
          name: "nst's JSONTestSuite (2):test_parsing:i -> n"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/i_object_key_lone_2nd_surrogate.json"
          description: "Checks that string with invalid utf16 surrogate is rejected as name"
---

The service does not accept objects with improper name.
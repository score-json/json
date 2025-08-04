---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parser class:accept:object:nonempty object"
          path: "/workspaces/json/tests/src/unit-class_parser.cpp"
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2):test_parsing:y"
          path: "/workspaces/json/tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/y_object_basic.json"
            - "/nst_json_testsuite2/test_parsing/y_object_duplicated_key.json"
            - "/nst_json_testsuite2/test_parsing/y_object_duplicated_key_and_value.json"
            - "/nst_json_testsuite2/test_parsing/y_object_empty.json"
            - "/nst_json_testsuite2/test_parsing/y_object_empty_key.json"
            - "/nst_json_testsuite2/test_parsing/y_object_escaped_null_in_key.json"
            - "/nst_json_testsuite2/test_parsing/y_object_extreme_numbers.json"
            - "/nst_json_testsuite2/test_parsing/y_object_long_strings.json"
            - "/nst_json_testsuite2/test_parsing/y_object_simple.json"
            - "/nst_json_testsuite2/test_parsing/y_object_string_unicode.json"
            - "/nst_json_testsuite2/test_parsing/y_object_with_newlines.json"      
          description: "Checks that various strings and numbers are accepted values."
---

The service does accept different types of values.
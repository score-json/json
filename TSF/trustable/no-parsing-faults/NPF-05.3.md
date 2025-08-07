---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parser class;parse;array;nonempty array"
          path: "/workspaces/json/tests/src/unit-class_parser.cpp"
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;y"
          path: "/workspaces/json/tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/y_array_arraysWithSpaces.json"
            - "/nst_json_testsuite2/test_parsing/y_array_empty-string.json"
            - "/nst_json_testsuite2/test_parsing/y_array_ending_with_newline.json"
            - "/nst_json_testsuite2/test_parsing/y_array_false.json"
            - "/nst_json_testsuite2/test_parsing/y_array_heterogeneous.json"
            - "/nst_json_testsuite2/test_parsing/y_array_null.json"
            - "/nst_json_testsuite2/test_parsing/y_array_with_1_and_newline.json"
            - "/nst_json_testsuite2/test_parsing/y_array_with_leading_space.json"
            - "/nst_json_testsuite2/test_parsing/y_array_with_several_null.json"
            - "/nst_json_testsuite2/test_parsing/y_array_with_trailing_space.json"
          description: "Tests whether several non-empty arrays are parsed without exception"
---

The service parses non-empty arrays.
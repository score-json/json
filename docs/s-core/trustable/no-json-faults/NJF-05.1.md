---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parser class:accept:array:empty array"
          path: "/workspaces/json/tests/src/unit-class_parser.cpp"
        - type: JSON_testsuite
          name: "nst's JSONTestSuite:test_parsing:y"
          path: "/workspaces/json/tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite/test_parsing/y_array_empty.json"
          description: ""
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2):test_parsing:y"
          path: "/workspaces/json/tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/y_array_empty.json"
            - "/nst_json_testsuite2/test_parsing/y_array_arraysWithSpaces.json"
            - "/nst_json_testsuite2/test_parsing/y_array_empty-string.json"
          description: "Checks that the empty array [] is accepted."
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2):test_parsing:y"
          path: "/workspaces/json/tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/y_array_ending_with_newline.json"
          description: ""
---

The service accepts the empty array.
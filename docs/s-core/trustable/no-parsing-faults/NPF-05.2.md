---
level: 1.1
normative: true
references:
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;y"
          path: "/workspaces/json/tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/y_array_empty.json"
          description: "Tests whether the empty array is parsed without exception."
        - type: cpp_test
          name: "parser class;parse;array;empty array"
          path: "/workspaces/json/tests/src/unit-class_parser.cpp"
---

The service parses empty arrays.
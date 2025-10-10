---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parser class - core;accept;array;nonempty array"
          path: "TSF/tests/unit-class_parser_core.cpp"
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;y"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/y_array_false.json"
            - "/nst_json_testsuite2/test_parsing/y_array_heterogeneous.json"
            - "/nst_json_testsuite2/test_parsing/y_array_null.json"
            - "/nst_json_testsuite2/test_parsing/y_array_with_1_and_newline.json"
            - "/nst_json_testsuite2/test_parsing/y_array_with_leading_space.json"
            - "/nst_json_testsuite2/test_parsing/y_array_with_several_null.json"
            - "/nst_json_testsuite2/test_parsing/y_array_with_trailing_space.json"
          description: "Checks that various valid arrays are accepted."
        - type: JSON_testsuite
          name: "json.org examples"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/json.org/1.json"
            - "/json.org/2.json"
            - "/json.org/3.json"
            - "/json.org/4.json"
            - "/json.org/5.json"
          description: "Checks that various valid arrays in combination with objects are accepted."
evidence:
  type: check_test_results
  configuration:
    tests: 
        - class_parser_core
        - testsuites
score:
    Jonas-Kirchhoff: 0.95
    Erikhu1: 0.85
---

The service accepts the non-empty arrays.
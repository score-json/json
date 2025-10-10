---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "deserialization;successful deserialization;stream"
          path: "tests/src/unit-deserialization.cpp"
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
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;y"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/y_string_in_array.json"
            - "/nst_json_testsuite2/test_parsing/y_string_in_array_with_leading_space.json"
            - "/nst_json_testsuite2/test_parsing/y_structure_true_in_array.json"
          description: ""
evidence:
  type: check_test_results
  configuration:
    tests: 
        - deserialization
        - testsuites
score: 
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

If every value candidate of a properly bounded array is accepted as singleton, then the service accepts the array.
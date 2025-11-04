---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-02
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;y"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/y_array_empty.json"
          description: "Tests whether the empty array is parsed without exception."
        - type: cpp_test
          name: "parser class - core;parse;array;empty array"
          path: "TSF/tests/unit-class_parser_core.cpp"
evidence:
  type: check_test_results
  configuration:
    tests: 
        - class_parser_core
        - testsuites
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

The service provided by nlohmann/json parses empty arrays.
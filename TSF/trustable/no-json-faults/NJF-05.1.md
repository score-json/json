---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-01
        - type: cpp_test
          name: "parser class - core;accept;array;empty array"
          path: "TSF/tests/unit-class_parser_core.cpp"
        - type: JSON_testsuite
          name: "nst's JSONTestSuite;test_parsing;y"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite/test_parsing/y_array_empty.json"
          description: ""
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;y"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/y_array_empty.json"
            - "/nst_json_testsuite2/test_parsing/y_array_arraysWithSpaces.json"
          description: "Checks that the empty array [] is accepted."
        - type: function_reference
          name: "lexer::skip_whitespace"
          path: "include/nlohmann/detail/input/lexer.hpp"
          description: "function, which skips admissible whitespace during reading"
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

The service accepts the empty array.

sab
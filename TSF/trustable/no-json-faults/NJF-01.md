---
level: 1.1
normative: true
references:
        - type: cpp_test
          path: "TSF/tests/unit-class_parser_core.cpp"
          name: "parser class - core;accept;null"
        - type: JSON_testsuite
          name: "nst's JSONTestSuite;test_parsing;y"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite/test_parsing/y_structure_lonely_null.json"
          description: ""
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;y"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/y_structure_lonely_null.json"
          description: ""
        - type: function_reference
          name: "lexer::scan_literal"
          path: "include/nlohmann/detail/input/lexer.hpp"
          description: "function to verify whether a candidate literal coincides with its expected value; here called with literal_text = ['n','u','l','l']."
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

The service accepts the literal name null. 
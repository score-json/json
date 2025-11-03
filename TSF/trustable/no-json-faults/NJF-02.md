---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-01
        - type: cpp_test
          name: "parser class - core;accept;true"
          path: "TSF/tests/unit-class_parser_core.cpp"
        - type: cpp_test
          name: "deserialization;contiguous containers;directly"
          path: "tests/src/unit-deserialization.cpp"
        - type: JSON_testsuite
          name: "nst's JSONTestSuite;test_parsing;y"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite/test_parsing/y_structure_lonely_true.json"
          description: ""  
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;y"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/y_structure_lonely_true.json"
          description: ""
        - type: function_reference
          name: "lexer::scan_literal"
          path: "include/nlohmann/detail/input/lexer.hpp"
          description: "function to verify whether a candidate literal coincides with its expected value; here called with literal_text = ['t','r','u','e']."
evidence:
  type: check_test_results
  configuration:
    tests: 
        - class_parser_core
        - testsuites
        - deserialization
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

The service accepts the literal name true.

sab
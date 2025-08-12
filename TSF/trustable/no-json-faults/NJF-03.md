---
level: 1.1
normative: true
references:
    - type: cpp_test
      name: "parser class - core;accept;false"
      path: "TSF/tests/unit-class_parser_core.cpp"
    - type: JSON_testsuite
      name: "nst's JSONTestSuite;test_parsing;y"
      path: "tests/src/unit-testsuites.cpp"
      test_suite_paths:
        - "/nst_json_testsuite/test_parsing/y_structure_lonely_false.json"
      description: ""
    - type: JSON_testsuite
      name: "nst's JSONTestSuite (2);test_parsing;y"
      path: "tests/src/unit-testsuites.cpp"
      test_suite_paths:
        - "/nst_json_testsuite2/test_parsing/y_structure_lonely_false.json"
      description: ""
sores:
    Jonas-Kirchhoff: 1.0
---

The service accepts the literal name false.
---
level: 1.1
normative: true
references:
    - type: cpp_test
      name: "parser class;accept;false"
      path: "/workspaces/json/tests/src/unit-class_parser.cpp"
    - type: JSON_testsuite
      name: "nst's JSONTestSuite;test_parsing;y"
      path: "/workspaces/json/tests/src/unit-testsuites.cpp"
      test_suite_paths:
        - "/nst_json_testsuite/test_parsing/y_structure_lonely_false.json"
      description: ""
    - type: JSON_testsuite
      name: "nst's JSONTestSuite (2);test_parsing;y"
      path: "/workspaces/json/tests/src/unit-testsuites.cpp"
      test_suite_paths:
        - "/nst_json_testsuite2/test_parsing/y_structure_lonely_false.json"
      description: ""
---

The service accepts the literal name false.
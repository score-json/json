---
level: 1.1
normative: true
references:
    - type: item
      items:
        - JLEX-01
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
    - type: function_reference
      name: "lexer::scan_literal"
      path: "include/nlohmann/detail/input/lexer.hpp"
      description: "function to verify whether a candidate literal coincides with its expected value; here called with literal_text = ['f','a','l','s','e']."
evidence:
  type: "check_artifact_exists"
  configuration:
    check_amalgamation: exclude
    codeql: exclude
    dependency_review: exclude
    labeler: exclude
    publish_documentation: exclude
    test_trudag_extensions: exclude
    ubuntu: include
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

The service accepts the literal name false.
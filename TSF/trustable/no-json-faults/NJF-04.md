---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parser class - core;accept;parse errors (accept)"
          path: "TSF/tests/unit-class_parser_core.cpp"
        - type: JSON_testsuite
          name: "nst's JSONTestSuite;test_parsing;n"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite/test_parsing/n_incomplete_false.json"
            - "/nst_json_testsuite/test_parsing/n_incomplete_null.json"
            - "/nst_json_testsuite/test_parsing/n_incomplete_true.json"
            - "/nst_json_testsuite/test_parsing/n_structure_number_with_trailing_garbage.json"
          description: ""
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;n"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_incomplete_false.json"
            - "/nst_json_testsuite2/test_parsing/n_incomplete_null.json"
            - "/nst_json_testsuite2/test_parsing/n_incomplete_true.json"
            - "/nst_json_testsuite2/test_parsing/n_structure_capitalized_True.json"
          description: ""
        - type: cpp_test
          name: "accept;unicode"
          path: "TSF/tests/unit-literals.cpp"
        - type: cpp_test
          name: "accept;capitalisation"
          path: "TSF/tests/unit-literals.cpp"
        - type: cpp_test
          name: "accept;illegal literals"
          path: "TSF/tests/unit-literals.cpp"
        - type: function_reference
          name: "lexer::scan_literal"
          path: "include/nlohmann/detail/input/lexer.hpp"
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
    Erikhu1: 0.95
---

The service does not accept any other literal name.
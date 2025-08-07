---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parser class;accept;parse errors (accept)"
          path: "/workspaces/json/tests/src/unit-class_parser.cpp"
        - type: JSON_testsuite
          name: "nst's JSONTestSuite;test_parsing;n"
          path: "/workspaces/json/tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite/test_parsing/n_incomplete_false.json"
            - "/nst_json_testsuite/test_parsing/n_incomplete_null.json"
            - "/nst_json_testsuite/test_parsing/n_incomplete_true.json"
            - "/nst_json_testsuite/test_parsing/n_structure_number_with_trailing_garbage.json"
          description: ""
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;n"
          path: "/workspaces/json/tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_incomplete_false.json"
            - "/nst_json_testsuite2/test_parsing/n_incomplete_null.json"
            - "/nst_json_testsuite2/test_parsing/n_incomplete_true.json"
            - "/nst_json_testsuite2/test_parsing/n_structure_capitalized_True.json"
          description: ""
        - type: cpp_test
          name: "accept;capitalisation"
          path: "/workspaces/json/tests/s-core/unit-literals.cpp"
        - type: cpp_test
          name: "accept;illegal literals"
          path: "/workspaces/json/tests/s-core/unit-literals.cpp"
---

The service does not accept any other literal name.
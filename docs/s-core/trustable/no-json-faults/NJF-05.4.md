---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parser class:accept:parse errors (accept)"
          path: "/workspaces/json/tests/src/unit-class_parser.cpp"
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2):test_parsing:n (previously overflowed)"
          path: "/workspaces/json/tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_structure_100000_opening_arrays.json"
          description: ""
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2):test_parsing:n"
          path: "/workspaces/json/tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_structure_close_unopened_array.json"
          description: ""
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2):test_parsing:n"
          path: "/workspaces/json/tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_structure_double_array.json"
            - "/nst_json_testsuite2/test_parsing/n_structure_end_array.json"
            - "/nst_json_testsuite2/test_parsing/n_structure_lone-invalid-utf-8.json"
            - "/nst_json_testsuite2/test_parsing/n_structure_open_array_apostrophe.json"
            - "/nst_json_testsuite2/test_parsing/n_structure_open_array_comma.json"
            - "/nst_json_testsuite2/test_parsing/n_structure_open_array_open_object.json"   
            - "/nst_json_testsuite2/test_parsing/n_structure_open_object_close_array.json"
            - "/nst_json_testsuite2/test_parsing/n_structure_unclosed_array.json"
            - "/nst_json_testsuite2/test_parsing/n_structure_unclosed_array_partial_null.json"
            - "/nst_json_testsuite2/test_parsing/n_structure_unclosed_array_unfinished_false.json"
            - "/nst_json_testsuite2/test_parsing/n_structure_unclosed_array_unfinished_true.json"
          description: ""
---

The service does not accept improperly bounded arrays.
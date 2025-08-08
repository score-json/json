---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parser class - core;accept;true"
          path: "/workspaces/json/TSF/tests/unit-class_parser_core.cpp"
        - type: cpp_test
          name: "deserialization;contiguous containers;directly"
          path: "/workspaces/json/tests/src/unit-deserialization.cpp"
        - type: JSON_testsuite
          name: "nst's JSONTestSuite;test_parsing;y"
          path: "/workspaces/json/tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite/test_parsing/y_structure_lonely_true.json"
          description: ""  
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;y"
          path: "/workspaces/json/tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/y_structure_lonely_true.json"
          description: ""
---

The service accepts the literal name true.
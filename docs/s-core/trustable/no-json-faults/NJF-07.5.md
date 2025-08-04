---
level: 1.1
normative: true

references:
        - type: cpp_test
          name: "parser class:accept:string:escaped"
          path: "/workspaces/json/tests/src/unit-class_parser.cpp"
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2):test_parsing:y"
          path: "/workspaces/json/tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/y_string_accepted_surrogate_pair.json"
            - "/nst_json_testsuite2/test_parsing/y_string_accepted_surrogate_pairs.json"
          description: "Checks that single and multiple surrogates are accepted."
        - type: cpp_test
          name: "accept:utf-16 surrogates"
          path: "/workspaces/json/tests/s-core/unit-strings.cpp"
---

The service accepts UTF-16 surrogate pairs.
---
level: 1.1
normative: true
references:
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;n"
          path: "/workspaces/json/tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_number_+Inf.json"
            - "/nst_json_testsuite2/test_parsing/n_number_-NaN.json"
            - "/nst_json_testsuite2/test_parsing/n_number_Inf.json"
            - "/nst_json_testsuite2/test_parsing/n_number_NaN.json"
            - "/nst_json_testsuite2/test_parsing/n_number_NaN.json"
          description: "Checks that NaN and Inf are rejected."
        - type: cpp_test
          name: "accept;illegal literal numbers"
          path: "/workspaces/json/tests/s-core/unit-literals.cpp"
---

The service does not accept NaN, infinity. (Could be added)



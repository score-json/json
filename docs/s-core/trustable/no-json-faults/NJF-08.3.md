---
level: 1.1
normative: true
reference:
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2):test_parsing:n"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_number_+Inf.json"
            - "/nst_json_testsuite2/test_parsing/n_number_-NaN.json"
            - "/nst_json_testsuite2/test_parsing/n_number_Inf.json"
            - "/nst_json_testsuite2/test_parsing/n_number_NaN.json"
            - "/nst_json_testsuite2/test_parsing/n_number_NaN.json"
          description: "Checks that NaN and Inf are rejected."
---

The service does not accept NaN, infinity. (Could be added)



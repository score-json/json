---
level: 1.1
normative: true
references:
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;n"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_number_+Inf.json"
            - "/nst_json_testsuite2/test_parsing/n_number_-NaN.json"
            - "/nst_json_testsuite2/test_parsing/n_number_Inf.json"
            - "/nst_json_testsuite2/test_parsing/n_number_NaN.json"
            - "/nst_json_testsuite2/test_parsing/n_number_NaN.json"
          description: "Checks that NaN and Inf are rejected."
        - type: cpp_test
          name: "parse;illegal literal numbers"
          path: "TSF/tests/unit-literals.cpp"
---

The service throws an exception on NaN, infinity.
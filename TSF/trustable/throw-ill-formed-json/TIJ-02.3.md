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
evidence:
  type: check_test_results
  configuration:
    tests: 
        - literals
        - testsuites
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

The service provided by nlohmann/json throws an exception on NaN and infinity.
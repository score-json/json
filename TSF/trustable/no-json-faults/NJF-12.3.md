---
level: 1.1
normative: true

references:
        - type: item
          items:
            - JLEX-01
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;n"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_structure_lone-invalid-utf-8.json"
          description: ""
        - type: cpp_test
          name: "Unicode;unescaped unicode"
          path: "TSF/tests/unit-strings.cpp"
evidence:
  type: check_test_results
  configuration:
    tests: 
        - strings
        - testsuites
score:
    Jonas-Kirchhoff: 0.9
    Erikhu1: 1.0
---

The service provided by nlohmann/json rejects single escaped and unescaped, and paired unescaped utf-16 surrogates.
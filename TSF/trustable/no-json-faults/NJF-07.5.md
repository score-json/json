---
level: 1.1
normative: true

references:
        - type: item
          items:
            - JLEX-01
            - NJF-07
        - type: cpp_test
          name: "parser class - core;accept;string;escaped"
          path: "TSF/tests/unit-class_parser_core.cpp"
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;y"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/y_string_accepted_surrogate_pair.json"
            - "/nst_json_testsuite2/test_parsing/y_string_accepted_surrogate_pairs.json"
          description: "Checks that single and multiple surrogates are accepted."
        - type: cpp_test
          name: "Unicode;escaped utf-16 surrogates;well-formed"
          path: "TSF/tests/unit-strings.cpp"
evidence:
  type: check_test_results
  configuration:
    tests: 
        - class_parser_core
        - testsuites
        - strings
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

The service provided by nlohmann/json accepts UTF-16 surrogate pairs.
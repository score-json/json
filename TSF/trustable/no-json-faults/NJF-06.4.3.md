---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-01
            - NJF-06.4
        - type: cpp_test
          name: "parser class - core;accept;object;nonempty object"
          path: "TSF/tests/unit-class_parser_core.cpp"
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;y"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/y_object_basic.json"
            - "/nst_json_testsuite2/test_parsing/y_object_duplicated_key.json"
            - "/nst_json_testsuite2/test_parsing/y_object_duplicated_key_and_value.json"
            - "/nst_json_testsuite2/test_parsing/y_object_empty.json"
            - "/nst_json_testsuite2/test_parsing/y_object_empty_key.json"
            - "/nst_json_testsuite2/test_parsing/y_object_escaped_null_in_key.json"
            - "/nst_json_testsuite2/test_parsing/y_object_extreme_numbers.json"
            - "/nst_json_testsuite2/test_parsing/y_object_long_strings.json"
            - "/nst_json_testsuite2/test_parsing/y_object_simple.json"
            - "/nst_json_testsuite2/test_parsing/y_object_string_unicode.json"
            - "/nst_json_testsuite2/test_parsing/y_object_with_newlines.json"      
          description: "Checks that various strings and numbers are accepted values."
        - type: cpp_test
          name: "accept;member separator"
          path: "TSF/tests/unit-objects.cpp"
evidence:
  type: check_test_results
  configuration:
    tests: 
        - class_parser_core
        - testsuites
        - objects
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

If the service provided by the nlohmann/json library accepts the value-candidate as a singleton, then the value-candidate is accepted.
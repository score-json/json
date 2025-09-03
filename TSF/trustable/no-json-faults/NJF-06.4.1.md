---
level: 1.1
normative: true
references:
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
          description: "Checks that various keys, particularly containing unicode characters, are accepted."
        - type: cpp_test
          name: "accept;names;strings;control characters"
          path: "TSF/tests/unit-objects.cpp"
        - type: cpp_test
          name: "accept;names;strings;unicode"
          path: "TSF/tests/unit-objects.cpp"
        - type: cpp_test
          name: "accept;names;strings;escaped UTF-16 surrogates"
          path: "TSF/tests/unit-objects.cpp"        
        - type: cpp_test
          name: "accept;member separator"
          path: "TSF/tests/unit-objects.cpp"  
evidence:
  type: "check_artifact_exists"
  configuration:
    check_amalgamation: exclude
    codeql: exclude
    dependency_review: exclude
    labeler: exclude
    publish_documentation: exclude
    test_trudag_extensions: exclude
    ubuntu: include
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

If the service recognises the name candidate as string, then it accepts the name candidate.
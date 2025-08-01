---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "deserialization:contiguous containers:error cases:case 15"
          path: "tests/src/unit-deserialization"
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2):test_parsing:n"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_structure_comma_instead_of_closing_brace.json"
            - "/nst_json_testsuite2/test_parsing/n_structure_object_followed_by_closing_object.json"
            - "/nst_json_testsuite2/test_parsing/n_structure_object_unclosed_no_value.json"
          description: ""
---

The service does not accept improperly bounded objects.
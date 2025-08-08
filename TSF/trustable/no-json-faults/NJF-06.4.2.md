---
level: 1.1
normative: true
references:
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;n"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_object_non_string_key.json"
            - "/nst_json_testsuite2/test_parsing/n_object_non_string_key_but_huge_number_instead.json"
          description: "Checks that numbers as keys are rejected."
        - type: cpp_test
          name: "accept;names;numbers"
          path: "TSF/tests/unit-objects.cpp"
        - type: cpp_test
          name: "accept;names;arrays"
          path: "TSF/tests/unit-objects.cpp"
        - type: cpp_test
          name: "accept;names;objects"
          path: "TSF/tests/unit-objects.cpp"
        - type: cpp_test
          name: "accept;names;literals"
          path: "TSF/tests/unit-objects.cpp"
---

The service does not accept any other token as name.
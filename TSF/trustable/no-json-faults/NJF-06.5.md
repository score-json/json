---
level: 1.1
normative: true
references:
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;n"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_object_trailing_comma.json"
            - "/nst_json_testsuite2/test_parsing/n_object_two_commas_in_a_row.json"
          description: "Checks that the empty member in a nonempty object is rejected."
---

The service provided by the nlohmann/json library does not accept objects with improper members.
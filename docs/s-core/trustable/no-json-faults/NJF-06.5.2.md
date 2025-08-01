---
level: 1.1
normative: true
reference:
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2):test_parsing:n"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_object_bad_value.json"
          description: "Checks that the invalid literal \"truth\" as value is rejected."
---

The service does not accept objects with improper value.
---
level: 1.1
normative: true
references:
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;n"
          path: "/workspaces/json/tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_array_colon_instead_of_comma.json"
          description: "Tests whether colon as value separator throws an exception."
---

The service throws an exception on improper value separators.
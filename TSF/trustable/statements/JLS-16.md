---
references:
    - type: verbose_file
      path: "./TSF/docs/list_of_test_environments.md"
      comment: "The list of all test-cases together with their execution environments"
    - type: website
      path: "https://github.com/score-json/json/actions"
      description: "Github actions page showing that score-json is using github host environment."
evidence:
    type: check_list_of_tests
    configuration: 
        sources:
            - "./tests/src"
            - "./TSF/tests"
level: 1.1
normative: true
---

A list of tests, which is extracted from the test execution, is provided, along with a list of test environments.
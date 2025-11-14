---
references:
    - type: verbose_file
      path: "./TSF/docs/list_of_test_environments.md"
      comment: "The list of all test-cases together with their execution environments"
    - type: website
      url: "https://github.com/score-json/json/actions"
      description: "Github actions page showing that score-json is using Github host environment."
evidence:
    type: check_list_of_tests
    configuration: 
        sources:
            - "./tests/src"
            - "./TSF/tests"
    type: https_response_time
    configuration:
        target: 2.0
        urls:
            - https://github.com/score-json/json/actions
level: 1.1
normative: true
---

A list of tests, which is extracted from the test execution, is provided, along with a list of test environments, a list of fault induction tests and test construction configurations and results.
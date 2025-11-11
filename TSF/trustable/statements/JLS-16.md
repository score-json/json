---
references:
    - type: verbose_file
      path: "./TSF/docs/list_of_test_environments.md"
      comment: "The list of all test-cases together with their execution environments"
evidence:
    type: check_list_of_tests
    configuration:
        sources:
            - "./tests/src"
            - "./TSF/tests"
level: 1.1
normative: true
score:
    aschemmel-tech: 0.5
---

A list of tests, which is extracted from the test execution, is provided, along with a list of test environments.

aschemmel-tech: we need a split in four statements/evidences (JLS) as defined in TA-TESTS. Here two are accumulated.

For the topic of test list: missing argument why we think tests are complete e.g. structtural coverage, linking to the RFC8259 standard?
I also see that nlohman defines fuzz testing (e.g. https://github.com/score-json/json/blob/main/tests/src/fuzzer-parse_bjdata.cpp). We should refer to this but maybe we cannot reproduce? Where are the results for this?

For the topic of test execution environment(s) : my understanding: only one environment was used: the github host environment together with Doctest (version ?)
but with a wide range of compilers and versions of these.
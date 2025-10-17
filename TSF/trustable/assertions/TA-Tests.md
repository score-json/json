#### Checklist for TA-TESTS from [Codethink](https://codethinklabs.gitlab.io/trustable/trustable/print_page.html)

* How confident are we that our test tooling and environment setups used for tests, fault inductions, and analyses are reproducible? <br>
    Answer:  The test can be reproduced any time on any machine running the versions of the operating systems and compilers as provided (TODO)
* Are any exceptions identified, documented and justified? <br>
    Answer:  Not applicable.
* How confident are we that all test components are taken from within our controlled environment? <br>
    Answer:  All tests are either self-contained or download test data from [within Eclipse S-CORE](https://github.com/eclipse-score/inc_nlohmann_json/tree/json_test_data_version_3_1_0_mirror).
* How confident are we that all of the test environments we are using are also under our control? <br>
    Answer: ????  The environments are standard docker images of ubuntu and standard versions of compilers.
* Do we record all test environment components, including hardware and infrastructure used for exercising tests and processing input/output data? <br>
    Answer:  No, since the tests are independent from hard-ware, these data are not collected.
* How confident are we that all tests scenarios are repeatable? <br>
    Answer:  Very.
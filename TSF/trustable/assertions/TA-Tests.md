#### Checklist for TA-TESTS from [Codethink](https://codethinklabs.gitlab.io/trustable/trustable/print_page.html)

* How confident are we that our test tooling and environment setups used for tests, fault inductions, and analyses are reproducible?

    **Answer**:  The test can be reproduced any time on any machine running the versions of the operating systems and compilers as provided (TODO, cf. AOU-14)

* Are any exceptions identified, documented and justified?

    **Answer**:  To the best of our understanding, there are no exceptions identified.

* How confident are we that all test components are taken from within our controlled environment?

    **Answer**:  All tests are either self-contained or download test data from [within Eclipse S-CORE](https://github.com/eclipse-score/inc_nlohmann_json/tree/json_test_data_version_3_1_0_mirror).

* How confident are we that all of the test environments we are using are also under our control? 

    **Answer**: ????  The environments are standard docker images of ubuntu and standard versions of compilers.

* Do we record all test environment components, including hardware and infrastructure used for exercising tests and processing input/output data? 

    **Answer**:  No, since the tests are independent from hard-ware, these data are not collected.

* How confident are we that all tests scenarios are repeatable? 

    **Answer**:  All test scenarios are repeated daily in the CI pipeline.

#### List of suggested evidence from [Codethink](https://codethinklabs.gitlab.io/trustable/trustable/print_page.html)

* Test build environment reproducibility

    **Comment**:

* Test build configuration

    **Comment**:

* Test build reproducibility

    **Comment**:

* Test environment configuration

    **Comment**:


#### Checklist for TA-ANALYSIS from [Codethink](https://codethinklabs.gitlab.io/trustable/trustable/print_page.html)

* What fraction of Expectations are covered by the test data?

    Answer:  Every statement supporting both of the expectations is ultimately supported by a test, except for WFJ-06. For WFJ-06 it is impossible to provide a direct tests, since this is a statement on infinitely many cases. Indirect tests are provided by the rejection of ill-formed json data.

* What fraction of Misbehaviours are covered by the monitored indicator data?

    Answer: For the intended use-case, no misbehaviours have been identified. Furthermore, no indicator data are collected.

* How confident are we that the indicator data are accurate and timely?

    Answer:  No indicator data are collected.

* How reliable is the monitoring process?

    Answer: Due to no indicator data being collected, there is no monitoring process.

* How well does the production data correlate with our test data?

    Answer:  Due to the general nature of the library, there are no production data.

* Are we publishing our data analysis?

    Answer:  Since we have no production data with which to compare our not collected indicator data or our test data, no data analysis is done, which is not published.

* Are we comparing and analysing production data vs test?

    Answer:  There are no production data.

* Are our results getting better, or worse?

    Answer:  Neither.

* Are we addressing spikes/regressions?
    Answer:  There are no spikes in the non-existent indicator data. If a test ever fails, then the spike is investigated. The results of fuzz testing are investigated in the original nlohmann/json.

* Do we have sensible/appropriate target failure rates?

    Answer:  For the unit and integration tests, zero. The target failure rate of fuzz testing is not under our control.

* Do we need to check the targets?

    Answer:  For the unit and integration tests, no. Since the fuzz testing runs and is investigated in the original nlohmann/json, there is no need to check the target.

* Are we achieving the targets?

    Answer:  For the unit and integration tests, yes. The achieving of the targets for the fuzz-testing is evaluated within the original nlohmann/json.

* Are all underlying assumptions and target conditions for the analysis specified?

    Answer:  Since none of the unit and integration tests are expected to fail, there is no further analysis of the results besides verifying the expectation. In case any test fails ever, the failure of the CI-pipeline encourages the maintainer to investigate.

* Have the underlying assumptions been verified using known good data?

    Answer:  The assumption that all unit and integration tests succeed under the expected conditions is demonstrated by the non-failure of the CI-Pipeline.

* Has the Misbehaviour identification process been verified using known bad data?

    Answer: Misbehaviours published on nlohmann/json usually provide minimal working examples for reproducing the faulty behaviour, enabling everyone to verify the identified misbehaviours. There is, however, no automatic process for the identification of misbehaviours. 

* Are results shown to be reproducible?

    Answer: It is expected that the tests can be reproduced on every modern sufficiently powerful machine.

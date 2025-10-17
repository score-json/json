#### Checklist for TA-ANALYSIS from [Codethink](https://codethinklabs.gitlab.io/trustable/trustable/print_page.html)

* What fraction of Expectations are covered by the test data? <br>
    Answer:  Every statement supporting both of the expectations is ultimately supported by a test, except for WFJ-06. For WFJ-06 it is impossible to provide a direct tests, since this is a statement on infinitely many cases. Indirect tests are provided by the rejection of ill-formed json data.
* What fraction of Misbehaviours are covered by the monitored indicator data? <br>
    Answer: For the intended use-case, no misbehaviours have been identified. Furthermore, no indicator data are collected.
* How confident are we that the indicator data are accurate and timely? <br>
    Answer:  No indicator data are collected.
* How reliable is the monitoring process? <br>
    Answer: Due to no indicator data being collected, there is no monitoring process
* How well does the production data correlate with our test data? <br>
    Answer:  Due to the general nature of the library, there are no production data.
* Are we publishing our data analysis? <br>
    Answer:  Since we have no production data with which to compare our not collected indicator data or our test data, no data analysis is done, which is not published.
* Are we comparing and analysing production data vs test? <br>
    Answer:  There are no production data.
* Are our results getting better, or worse? <br>
    Answer:  Neither.
* Are we addressing spikes/regressions? <br>
    Answer:  There are no spikes in the non-existent indicator data. If a test ever fails, then the spike is investigated. The results of fuzz testing are investigated in the original nlohmann/json.
* Do we have sensible/appropriate target failure rates? <br>
    Answer:  For the unit and integration tests, 0.
* Do we need to check the targets? <br>
    Answer:  ???????? No.
* Are we achieving the targets? <br>
    Answer:  ??????? Yes.
* Are all underlying assumptions and target conditions for the analysis specified? <br>
    Answer:  There is no analysis.
* Have the underlying assumptions been verified using known good data? <br>
    Answer:  There is no analysis so that there are no underlying assumptions.
* Has the Misbehaviour identification process been verified using known bad data? <br>
    Answer: Misbehaviours published on nlohmann/json usually provide minimal working examples for reproducing the faulty behaviour.
* Are results shown to be reproducible? <br>
    Answer: The tests can be reproduced on every machine.

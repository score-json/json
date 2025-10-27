#### Checklist for TA-VALIDATION from [Codethink](https://codethinklabs.gitlab.io/trustable/trustable/print_page.html)

I DO NOT FEEL CONFIDENT TO **Answer** THIS!

* Is the selection of tests correct?

    **Answer**:  ???? Who could tell this?

* Are the tests executed enough times? 

    **Answer**:  ???? Define "enough times"

* How confident are we that all test results are being captured?

    **Answer**: ???? How fine-grained is a test-result supposed to be?
    
* Can we look at any individual test result, and establish what it relates to?

    **Answer**:  ????

* Can we trace from any test result to the expectation it relates to? 

    **Answer**:  No, there are more tests than expectations, and in particular tests that relate to the inner workings of the library which are not used by S-CORE. 

* Can we identify precisely which environment (software and hardware) were used?

    **Answer**:  ???? How precisely shall that be? Moreover, the tests are supposed to run independent of underlying hardware, since this is a software. 

* How many pass/fail results would be expected, based on the scheduled tests?

    **Answer**:  Zero fails.

* Do we have all of the expected results?

    **Answer**:  Yes.

* Do we have time-series data for all of those results? 

    **Answer**:  Yes, there are time-series data.

* If there are any gaps, do we understand why?

    **Answer**:  ????  Define gaps

* Are the test validation strategies credible and appropriate? 

    **Answer**:  ???? Define test validation strategies

* What proportion of the implemented tests are validated? 

    **Answer**:  ???? None.

* Have the tests been verified using known good and bad data? 

    **Answer**:  ???? 

#### List of suggested evidence from [Codethink](https://codethinklabs.gitlab.io/trustable/trustable/print_page.html)

* Test results from per-change tests

    **Comment**:

* Test results from scheduled tests as time series

    **Comment**:


#### Checklist for TA-FIXES from [Codethink](https://codethinklabs.gitlab.io/trustable/trustable/print_page.html)


* How many faults have we identified in XYZ?

    Answer:  There are no identifiable faults concerning the expectations. 

* How many unknown faults remain to be found, based on the number that have been processed so far?

    Answer:  It is unlikely that there are unknown faults concerning the expectations.

* Is there any possibility that people could be motivated to manipulate the lists (e.g. bug bonus or pressure to close).

    Answer:  Since the project is entirely open source, it is quite unlikely.

* How many faults may be unrecorded (or incorrectly closed, or downplayed)?

    Answer:  There may be none concerning the expectations.

* How do we collect lists of bugs and known vulnerabilities from components?

    Answer:  We pull the list from the issues reported to nlohmann/json labelled as bug and open or opened since the last release.

* How (and how often) do we check these lists for relevant bugs and known vulnerabilities?

    Answer:  Whenever we generate the documentation, the list is pulled. If there is an issue previously unrecorded, then the maintainer is enticed to check this issue on applicability.

* How confident can we be that the lists are honestly maintained?

    Answer:  We can not imagine a reason why the list could be dishonestly maintained.

* Could some participants have incentives to manipulate information?

    Answer:  We can not think of a reason why.

* How confident are we that the lists are comprehensive? 

    Answer:  We have no reason to assume that discovered bugs are not reported to nlohmann/json.

* Could there be whole categories of bugs/vulnerabilities still undiscovered?

    Answer:  There could be a mislabelling of issues, but it is unlikely that there are bugs or vulnerabilities not labelled as bug.

* How effective is our triage/prioritisation? 

    Answer:  UNKNOWN

* How many components have never been updated? 

    Answer:  None, the single component is up to date.

* How confident are we that we could update them? 

    Answer:  If nlohmann/json would release an new version, we are very confident that we can update to that version.

* How confident are we that outstanding fixes do not impact our Expectations?

    Answer:  We have not found any outstanding fixes impacting our expectations.

* How confident are we that outstanding fixes do not address Misbehaviours?

    Answer:  We are very confident that none of the outstanding fixes do not affect the no identified misbehaviours.
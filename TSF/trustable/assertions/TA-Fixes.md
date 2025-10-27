#### Checklist for TA-FIXES from [Codethink](https://codethinklabs.gitlab.io/trustable/trustable/print_page.html)


* How many faults have we identified in XYZ?

    **Answer**:  There are no identifiable faults concerning the expectations. 

* How many unknown faults remain to be found, based on the number that have been processed so far?

    **Answer**:  It is unlikely that there are unknown faults concerning the expectations.

* Is there any possibility that people could be motivated to manipulate the lists (e.g. bug bonus or pressure to close).

    **Answer**:  Since the project is entirely open source, it is quite unlikely.

* How many faults may be unrecorded (or incorrectly closed, or downplayed)?

    **Answer**:  There may be none, at least when it concerns the expectations.

* How do we collect lists of bugs and known vulnerabilities from components?

    **Answer**:  We pull the list from the issues reported to nlohmann/json labelled as bug and open or opened since the last release. This list is then stored using github, thereby enabling a traceability of the list.

* How (and how often) do we check these lists for relevant bugs and known vulnerabilities?

    **Answer**:  Whenever we generate the documentation, the list is pulled. If there is an issue previously unrecorded, then the maintainer is encouraged by the change of the trustable score to check this issue on applicability.

* How confident can we be that the lists are honestly maintained?

    **Answer**:  We can not imagine a reason why the list could be dishonestly maintained.

* Could some participants have incentives to manipulate information?

    **Answer**:  We can not think of a reason why.

* How confident are we that the lists are comprehensive? 

    **Answer**:  We have no reason to assume that discovered bugs are not reported to nlohmann/json.

* Could there be whole categories of bugs/vulnerabilities still undiscovered?

    **Answer**:  There could be a mislabelling of issues, but it is unlikely that there are bugs or vulnerabilities not labelled as bug, instead it is likely that perceived issues due to a misunderstanding of how the library works are labelled as bug.

* How effective is our triage/prioritisation? 

    **Answer**: ????? Since it is not intended to fix the library within S-CORE, but instead leave the development to the original nlohmann/json, there is no need to have a triage or prioritisation. 

* How many components have never been updated? 

    **Answer**:  None, the single component is up to date.

* How confident are we that we could update them? 

    **Answer**:  If nlohmann/json would release an new version, we are very confident that we can update to that version.

* How confident are we that outstanding fixes do not impact our Expectations?

    **Answer**:  We have not found any outstanding fixes impacting our expectations.

* How confident are we that outstanding fixes do not address Misbehaviours?

    **Answer**: For all of the none identified misbehaviours, we are very confident that none of the outstanding fixes do not address them.

#### List of suggested evidence from [Codethink](https://codethinklabs.gitlab.io/trustable/trustable/print_page.html)

* List of known bugs fixed since last release
* List of outstanding bugs still not fixed, with triage/prioritisation based on severity/relevance/impact
* List of known vulnerabilities fixed since last release
* List of outstanding known vulnerabilities still not fixed, with triage/prioritisation based on severity/relevance/impact
* List of XYZ component versions, showing where a newer version exists upstream
* List of component version updates since last release
* List of fixes applied to developed code since last release
* List of fixes for developed code that are outstanding, not applied yet
* List of XYZ faults outstanding (O)
* List of XYZ faults fixed since last release (F)
* List of XYZ faults mitigated since last release (M)

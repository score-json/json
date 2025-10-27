#### Checklist for TA-DATA from [Codethink](https://codethinklabs.gitlab.io/trustable/trustable/print_page.html)

* Is all test data stored with long-term accessibility?

    **Answer**:  If we assume that github is long-term accessible, then yes.

* Is all monitoring data stored with long-term accessibility?

    **Answer**:  There are no monitoring data.

* Are extensible data models implemented?

    **Answer**:  The data are stored in an sqlite database.

* Is sensitive data handled correctly (broadcasted, stored, discarded, or anonymised) with appropriate encryption and redundancy?

    **Answer**:  There are no sensitive data produced, collected or stored.

* Are proper backup mechanisms in place?

    **Answer**:  Not more than the default mechanisms of github.

* Are storage and backup limits tested?

    **Answer**:  No.

* Are all data changes traceable? 

    **Answer**:  Yes, due to the usage of github.

* Are concurrent changes correctly managed and resolved? 

    **Answer**:  Yes, due to the usage of github.

* Is data accessible only to intended parties?

    **Answer**:  Since the library is open source, there are no unintended parties.

* Are any subsets of our data being published?

    **Answer**:  Yes, the collected data are publicly available.

#### List of suggested evidence from [Codethink](https://codethinklabs.gitlab.io/trustable/trustable/print_page.html)

* Time-stamped and traceable result records for each test execution, linked to associated system under test version and specification references.

    **Comment**:

* List of monitored indicators, linked to associated specification version references.

    **Comment**:

* Time-stamped and traceable test-derived data for each indicator, linked to associated system under test version and indicator specifications references.

    **Comment**:

* List of monitored deployments, linked to associated version and configuration references.

    **Comment**:

* Time-stamped and traceable production data for each indicator, linked to associated deployment metadata and specification references.

    **Comment**:


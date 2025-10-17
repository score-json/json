#### Checklist for TA-DATA from [Codethink](https://codethinklabs.gitlab.io/trustable/trustable/print_page.html)

* Is all test data stored with long-term accessibility?

    Answer:  If we assume that github is long-term accessible, then yes.

* Is all monitoring data stored with long-term accessibility?

    Answer:  There are no monitoring data.

* Are extensible data models implemented?

    Answer:  The data are stored in a sqlite database.

* Is sensitive data handled correctly (broadcasted, stored, discarded, or anonymised) with appropriate encryption and redundancy?

    Answer:  There are no sensitive data produced, collected or stored.

* Are proper backup mechanisms in place?

    Answer:  Not more than the default mechanisms of github.

* Are storage and backup limits tested?

    Answer:  No.

* Are all data changes traceable? 

    Answer:  Yes, due to the usage of github.

* Are concurrent changes correctly managed and resolved? 

    Answer:  Yes, due to the usage of github.

* Is data accessible only to intended parties?

    Answer:  There are no unintended parties.

* Are any subsets of our data being published?

    Answer:  Yes, the collected data are publicly available.
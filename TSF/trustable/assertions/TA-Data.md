# Checklist for TA-DATA from [Codethink](https://codethinklabs.gitlab.io/trustable/trustable/print_page.html)

* Is all test data stored with long-term accessibility? <br>
    Answer:  If we assume that github is long-term accessible, then yes.
* Is all monitoring data stored with long-term accessibility? <br>
    Answer:  There are no monitoring data.
* Are extensible data models implemented? <br>
    Answer:  The data are stored in a sqlite database.
* Is sensitive data handled correctly (broadcasted, stored, discarded, or anonymised) with appropriate encryption and redundancy? <br>
    Answer:  There are no sensitive data produced, collected or stored.
* Are proper backup mechanisms in place? <br>
    Answer:  Not more than the default mechanisms of github.
* Are storage and backup limits tested? <br>
    Answer:  No.
* Are all data changes traceable? <br>
    Answer:  Yes, due to the usage of github.
* Are concurrent changes correctly managed and resolved? <br>
    Answer:  Yes, due to the usage of github.
* Is data accessible only to intended parties? <br>
    Answer:  There are no unintended parties.
* Are any subsets of our data being published? <br>
    Answer:  Yes, the collected data are publicly available.
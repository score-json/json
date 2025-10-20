#### Checklist for TA-CONSTRAINTS from [Codethink](https://codethinklabs.gitlab.io/trustable/trustable/print_page.html)

* Are the constraints grounded in realistic expectations, backed by real-world examples?

    Answer:  The constraints originate from S-CORE and the library itself.

* Do they effectively guide downstream consumers in expanding upon existing Statements?

    Answer:  ?????

* Do they provide clear guidance for upstreams on reusing components with well-defined claims?

    Answer:  ?????

* Are any Statements explicitly designated as not reusable or adaptable?

    Answer:  NO?????

* Are there worked examples from downstream or upstream users demonstrating these constraints in practice?

    Answer:  ????

* Have there been any documented misunderstandings from users, and are these visibly resolved?

    Answer:  Yes, it is documented that the [brace initialisation](https://json.nlohmann.me/home/faq/) regularly leads to confusion, cf. [here](https://github.com/nlohmann/json/issues/4898).

* Do external users actively keep up with updates, and are they properly notified of any changes?

    Answer:  External users of the library are not necessarily automatically notified of an update, and are neither assumed nor required to keep up to date. If the external user forks the github repository, however, then github shows automatically whenever the upstream changes.
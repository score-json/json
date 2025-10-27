#### Checklist for TA-RELEASES from [Codethink](https://codethinklabs.gitlab.io/trustable/trustable/print_page.html)

* How confident are we that all components are taken from within our controlled environment?

    **Answer**:  This library does not take anything from outside of this repository.

* How confident are we that all of the tools we are using are also under our control?

    **Answer**:  The version of nlohmann/json that is documented with this documentation is under the full control of the Eclipse S-CORE organisation.

* Are our builds repeatable on a different server, or in a different context?

    **Answer**:  Since there is no "build" of the header-only library, yes.

* How sure are we that our builds don't access the internet?

    **Answer**:  There is no implemented access to the internet in the library itself. The testsuite is downloaded from a within Eclipse S-CORE.

* How many of our components are non-reproducible?

    **Answer**:  The single component is reproducible.

* How confident are we that our reproducibility check is correct?

    **Answer**:  Quite.

#### List of suggested evidence from [Codethink](https://codethinklabs.gitlab.io/trustable/trustable/print_page.html)

* list of reproducible SHAs

    **Comment**:

* list of non-reproducible elements with:
    * explanation and justification
    * details of what is not reproducible
    * evidence of configuration management for build instructions and infrastructure
    * evidence of repeatable builds

    **Comment**:


#### Checklist for TA-INPUTS from [Codethink](https://codethinklabs.gitlab.io/trustable/trustable/print_page.html)

The single_include/nlohmann/json.hpp is the single and only component of the library.

* Are there components that are not on the list?

    **Answer**:  No.

* Are there assessments for all components?

    **Answer**:  ?????

* Has an assessment been done for the current version of the component?

    **Answer**:  ?????

* Have sources of bug and/or vulnerability data been identified?

    **Answer**:  There are no bug and/or vulnerability data.

* Have additional tests and/or Expectations been documented and linked to component assessment?

    **Answer**:  ??????

* Are component tests run when integrating new versions of components?

    **Answer**:  There are no further components.

* Are there tools that are not on the list?

    **Answer**:  The library does not use external tools, except for the tools provided by the C++ standard library.

* Are there impact assessments for all tools?

    **Answer**:  ?????? The library does not use external tools for which an impact assessment has to be done.

* Have tools with high impact been qualified?

    **Answer**: There are no tools with high impact.

* Were assessments or reviews done for the current tool versions?

    **Answer**:  ????? The library does not use external tools for which an impact assessment has to be done.

* Have additional tests and/or Expectations been documented and linked to tool assessments?

    **Answer**:  No.

* Are tool tests run when integrating new versions of tools?

    **Answer**:  The library does not use external tools for which a new version needs to be integrated.

* Are tool and component tests included in release preparation?

    **Answer**:  Yes, the tests of the library are included in the release.

* Can patches be applied, and then upstreamed for long-term maintenance?

    **Answer**:  Yes, if ever a misbehaviour is found and patched, then a pull-request to the original nlohmann/json repository can be opened to upstream the changes.

* Do all dependencies comply with acceptable licensing terms?

    **Answer**:  Yes, the library is licensed under MIT License .

#### List of suggested evidence from [Codethink](https://codethinklabs.gitlab.io/trustable/trustable/print_page.html)

* List of components used to build XYZ, including:
    * Whether content is provided as source or binary
    * Record of component assessments:
        * Originating project and version
        * Date of assessments and identity of assessors
        * Role of component in XYZ
        * Sources of bug and risk data
        * Potential misbehaviours and risks identified and assessed
        * List of tools used to build and verify XYZ
    * Record of tool assessments:
        * Originating project and tool version
        * Date of assessments and identity of assessors
        * Role of the tool in XYZ releases
        * Potential misbehaviours and impacts
        * Detectability and severity of impacts
        * Tests or measures to address identified impacts

---
level: 1.1
normative: true
references:
        - type: verbose_file
          path: ".github/workflows/dependency-review.yml"
          description: "The workflow scans PRs for dependency changes and vulnerabilities."
evidence:
  type: "check_artifact_exists"
  configuration:
    check_amalgamation: exclude
    codeql: exclude
    dependency_review: include
    labeler: exclude
    publish_documentation: exclude
    test_trudag_extensions: exclude
    ubuntu: exclude
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
    aschemmel-tech: 0.0
---

External dependencies are checked for potential security vulnerabilities with each pull request to main. Merging is blocked until all warnings are resolved.

aschemmel-tech: Evidences asked for are:

- List of components used in construction of nlohman/json - this is not given by JLS-04: recommend to create this list of dependencies within another "statement"
- Record of component assessment - this is not given by JLS-04: recommend to check based on the above list whether the components have an ASIL certification
- List of tools used in construction and verification - this is not given by JLS-04: recommend to create this list of tools used by nlohman within another "statement"
- Record of tool impact assessments - this is not given by JLS-04 and also not by nlohman/json, need to create a tool evaluation of the tools used by nlohman/json and not also by S-CORE or consider how those can be replaced - needs another "statement"
- Record of tool qualification reviews - this is not given by JLS-04 and also not by nlohman/json, need to create a tool qualification of nlohman/json used tools as result of evaluation, can also refer to S-CORE if same tools are used - needs another "statement"
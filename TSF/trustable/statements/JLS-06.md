---
level: 1.1
normative: true
references:
        - type: website
          url: "https://github.com/score-json/json/settings/branches"
evidence:
  type: "check_artifact_exists"
  configuration:
    check_amalgamation: include
    codeql: include
    dependency_review: include
    labeler: include
    publish_documentation: include
    test_trudag_extensions: include
    ubuntu: include
---

Changes to the code (main branch) are applied only after code review and passing of all pipelines.

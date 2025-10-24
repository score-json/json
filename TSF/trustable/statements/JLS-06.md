---
level: 1.1
normative: true
references:
    - type: workflow_failures
      owner: "score-json"
      repo: "json"
      branch: "main"
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

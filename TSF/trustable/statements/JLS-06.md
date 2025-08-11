---
level: 1.1
normative: true
evidence:
  type: "check_artifact_exists"
  configuration:
    check_amalgamation: "check_amalgamation"
    codeql-analysis: "codeql"
    dependency_review: "dependency_review"
    labeler: "labeler"
    test_trudag_extensions: "test_trudag_extensions"
    ubuntu: "ubuntu"
---

Changes to the code (main branch) are applied only after code review and passing of all pipelines.

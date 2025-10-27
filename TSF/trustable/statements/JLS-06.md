---
level: 1.1
normative: true
references:
        - type: website
          url: https://github.com/score-json/json/settings/branches
          description: "Branch protection policies"
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
score:
    aschemmel-tech: 0.5
---

Changes to the code (main branch) are applied only after code review and passing of all pipelines.

aschemmel-tech: In my understanding this is mybe only half of what we want to assess, the other half are the changes in nlohman/json.

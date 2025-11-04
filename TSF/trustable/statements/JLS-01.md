---
level: 1.1
normative: true
references:
    - type: file
      path: .github/workflows/parent-workflow.yml
evidence:
    type: did_workflows_fail
    configuration:
        owner: "score-json"
        repo: "json"
        branch: "main"
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

The CI pipeline of the main branch of nlohmann/json executes on each pull request (opened, reopened, synchronized) the integration test suite, and failures in these runs are investigated by contributors.
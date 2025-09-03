---
level: 1.1
normative: true
references:
    - type: file
      path: .github/workflows/parent-workflow.yml
    - type: web_content
      url: https://github.com/score-json/json/settings/branch_protection_rules/65227858
      description: "branch protection rule for main branch specifying that failures of tests prevent merge."
score:
    Jonas-Kirchhoff: 1.0
---

The nlohmann/json library project CI executes on each pull request (opened, reopened, synchronized) the integration test suite, and failures in these runs are investigated by contributors.

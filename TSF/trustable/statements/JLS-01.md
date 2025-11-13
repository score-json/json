---
level: 1.1
normative: true
references:
        - type: web_content
          url: "https://github.com/nlohmann/json/blob/develop/.github/workflows/ubuntu.yml#L9"
          description: "The trigger condition for the CI workflow that executes the test suites."
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

The CI pipeline in nlohmann/json executes the unit and integration test suites on each pull request (opened, reopened, synchronized).
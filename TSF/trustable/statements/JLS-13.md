---
level: 1.1
normative: true
references:
        - type: project_website
          url: "https://github.com/nlohmann/json/blob/develop/.github/CODEOWNERS"
          description: "CODEOWNERS file specifying that changes to any file requests @nlohmann for code review in case of a pull request"
        - type: project_website
          url: "https://github.com/nlohmann/json?tab=contributing-ov-file#readme"
          description: "nlohmann/json contribution guidelines"
        - type: website
          url: "https://github.com/nlohmann/json/actions?query=event%3Apush+branch%3Amaster"
          description: "GitHub reviews of nlohmann/json filtered for push to master"
evidence:
    type: https_response_time    
    configuration:
        target_seconds: 2
        urls:
            - "https://github.com/nlohmann/json/actions?query=event%3Apush+branch%3Amaster"
            - "https://github.com/nlohmann/json?tab=contributing-ov-file#readme"
            - "https://github.com/nlohmann/json/blob/develop/.github/CODEOWNERS"
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

All contributions to the nlohmann/json repository are subject to a defined review process.
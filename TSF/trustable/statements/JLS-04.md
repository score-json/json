---
level: 1.1
normative: true
references:
        - type: website
          url: "https://github.com/eclipse-score/inc_nlohmann_json/blob/develop/.github/dependabot.yml"
          description: "configuration of dependabot for the mirror of the repository within S-CORE"
        - type: website
          url: "https://github.com/nlohmann/json/blob/develop/.github/dependabot.yml"
          description: "configuration of dependabot for the original nlohmann/json repository"
evidences:
        - type: https_response_time
          configuration:
                target_seconds: 2
                urls:
                    - "https://github.com/eclipse-score/inc_nlohmann_json/blob/develop/.github/dependabot.yml"
                    - "https://github.com/nlohmann/json/blob/develop/.github/dependabot.yml"
score:
    Jonas-Kirchhoff: 1.0
---

The project runs dependabot on all code entering the main branch, blocking merges until all warnings are resolved. (https://github.com/score-json/json/blob/main/nlohmann_json/.github/dependabot.yml)

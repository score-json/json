---
level: 1.1
normative: true
references:
        - type: project_website
          url: "https://github.com/nlohmann/json"
          description: "Start-page of the original nlohmann/json project"
        - type: project_website
          url: "https://github.com/eclipse-score/inc_nlohmann_json"
          description: "Start-page of the mirror of nlohmann/json within Eclipse S-CORE"
evidence:
        type: https_response_time
        configuration:
                target_seconds: 2
                urls:
                    - "https://github.com/nlohmann/json"
                    - "https://github.com/eclipse-score/inc_nlohmann_json"
score:
    Mihai Haraga: 1.0
---

The Eclipse S-CORE organization mirrors the nlohmann/json project in a github fork.
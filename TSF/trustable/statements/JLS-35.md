---
level: 1.1
normative: true
references:
        - type: project_website
          url: https://scorecard.dev/viewer/?uri=github.com%2Fnlohmann%2Fjson
          description: "OpenSSF Scorecard Report for nlohmann/json showing score for 'CI-Tests'"
evidence:
        type: https_response_time
        configuration:
                target_seconds: 2
                urls:
                    - "https://scorecard.dev/viewer/?uri=github.com%2Fnlohmann%2Fjson"
score:
    Erikhu1: 1.0
---

Pull requests in the nlohmann/json repository are merged only after running CI-tests.
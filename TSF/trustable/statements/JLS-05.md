---
level: 1.1
normative: true
references:
        - type: website
          url: "https://github.com/nlohmann/json/issues"
          description: "contains the collected github-issues for nlohmann/json"
        - type: website
          url: "https://github.com/nlohmann/json/graphs/commit-activity"
          description: "presents the commit activity of the past year"
        - type: website
          url: "https://github.com/nlohmann/json/graphs/contributors"
          description: "presents commits over time and per contributor"
        - type: website
          url: "https://github.com/nlohmann/json/forks?include=active&page=1&period=&sort_by=last_updated"
          description: "lists all forks of nlohmann/json by last updated"
evidences:
        - type: https_response_time
          configuration:
                target_seconds: 2
                urls:
                    - "https://github.com/nlohmann/json/issues"
                    - "https://github.com/nlohmann/json/graphs/commit-activity"
                    - "https://github.com/nlohmann/json/forks?include=active&page=1&period=&sort_by=last_updated"
score:
    Jonas-Kirchhoff: 1.0
---

The OSS nlohmann_json is widely used, actively maintained and uses github issues to track bugs and misbehaviours.
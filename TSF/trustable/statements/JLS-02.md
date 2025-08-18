---
level: 1.1
normative: true
references:
        - type: website
          url: "https://introspector.oss-fuzz.com/project-profile?project=json"
          description: "collects recent reports for fuzzing introspection of nlohmann/json with historical plots"
evidences:
        - type: https_response_time
          configuration:
                target_seconds: 2
                urls:
                    - "https://introspector.oss-fuzz.com/project-profile?project=json"
score:
    Jonas-Kirchhoff: 1.0
---

Fuzz testing is used in the original nlohmann_json repository (https://github.com/nlohmann/json) to uncover edge cases and failure modes throughout development. (https://github.com/nlohmann/json/blob/develop/tests/fuzzing.md)
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
    mishu-dev: 1.0
    aschemmel-tech: 1.0
---

The Eclipse S-CORE organization mirrors the nlohmann/json project in a github fork.

aschemmel-tech: Evidences asked for are:

- list of all nlohmann/json components - list as asked for in TA-INPUTS plus the nlohman/json component sources, expect nlohman/json has no external libs it depends on
- successful build of nlohmann/json from source - needs "statement" and evidence that no external source and caching is used (need to find out about caching, we qualified bazel caching)
- update logs for mirrored projects - ???
- mirrors reject history rewrites - ???
- mirroring is configured via infrastructure under direct - control covered already???
can you think about these last three and maybe add here
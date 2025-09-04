---
level: 1.1
normative: true
references:
        - type: project_website
          url: "https://introspector.oss-fuzz.com/project-profile?project=json"
          description: "collects recent reports for fuzzing introspection of nlohmann/json with historical plots"
        - type: web_content
          url: https://storage.googleapis.com/oss-fuzz-introspector/json/inspector-report/20250824/fuzz_report.html
          description: "persistent storage of fuzz-testing-report for nlohmann/json on 24.08.2025"
        - type: web_content
          url: "https://raw.githubusercontent.com/nlohmann/json/refs/heads/develop/.github/workflows/cifuzz.yml"
          description: "Configuration file for Fuzz-Testing pipeline in the original nlohmann/json repository"
evidence:
        type: https_response_time
        configuration:
                target_seconds: 2
                urls:
                    - "https://introspector.oss-fuzz.com/project-profile?project=json"
                    - "https://storage.googleapis.com/oss-fuzz-introspector/json/inspector-report/20250824/fuzz_report.html"
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

Fuzz testing is used in the original nlohmann/json repository (https://github.com/nlohmann/json) to uncover edge cases and failure modes throughout development. (https://github.com/nlohmann/json/blob/develop/tests/fuzzing.md)
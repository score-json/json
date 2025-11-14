---
level: 1.1
normative: true
references:
    - type: project_website
      url: "https://github.com/nlohmann/json/blob/develop/.github/CONTRIBUTING.md"
      description: "nlohmann/json contribution guidelines describing analysis, testing, and review expectations"
    - type: project_website
      url: "https://github.com/nlohmann/json/tree/develop/.github"
      description: "Project workflows and configuration supporting automated analysis and testing for nlohmann/json"
    - type: file
      path: "TSF/scripts/generate_list_of_misbehaviours.py"
      description: "Script generating a report of known misbehaviours of the nlohmann/json library based on GitHub issues"
    - type: verbose_file
      path: "TSF/README.md"
      description: "TSF-related description of analysis, verification processes, and update concepts for score-json"
evidence:
    type: https_response_time    
    configuration:
        target_seconds: 2
        urls:
            - "https://github.com/nlohmann/json/blob/develop/.github/CODE_OF_CONDUCT.md"
            - "https://github.com/nlohmann/json/tree/develop/.github"
---

Manual verification activities that complement automated analysis for the nlohmann/json library are documented, reviewed against defined criteria, and considered for their impact on identifying and addressing misbehaviours.

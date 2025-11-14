---
level: 1.1
normative: true
references:
    - type: project_website
      url: "https://github.com/nlohmann/json/blob/develop/.github/CODEOWNERS"
      description: "Definition of responsible owners and reviewers for the nlohmann/json repository"
    - type: project_website
      url: "https://github.com/nlohmann/json/blob/develop/.github/CONTRIBUTING.md"
      description: "nlohmann/json contribution guidelines describing contribution, testing, and review expectations"
    - type: project_website
      url: "https://github.com/nlohmann/json/blob/develop/.github/CODE_OF_CONDUCT.md"
      description: "Code of Conduct defining behavioural expectations during collaboration and review"
    - type: verbose_file
      path: "TSF/README.md"
      description: "TSF documentation describing responsibilities, verification processes, and change control for score-json"
evidence:
    type: https_response_time    
    configuration:
        target_seconds: 2
        urls:
            - "https://github.com/nlohmann/json/blob/develop/.github/CODE_OF_CONDUCT.md"
            - "https://github.com/nlohmann/json/blob/develop/.github/CONTRIBUTING.md"
            - "https://github.com/nlohmann/json/blob/develop/.github/CODEOWNERS"
---

Responsibilities for manual verification and review follow documented, competence-based processes and guidelines, and the associated processes and checks are regularly reviewed and updated under defined change control.
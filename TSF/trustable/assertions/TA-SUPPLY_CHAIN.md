---
level: 1.1
normative: true
references:
    - type: checklist
      path: ./TSF/trustable/assertions/TA-SUPPLY_CHAIN-CHECKLIST.md
---

All sources for nlohmann/json library and tools are mirrored in our controlled environment.

aschemmel-tech: I think it needs more verbose content to describe why the above statement is true. For example copy from the TA template:

Evidence

- list of all nlohmann/json (external) components
- successful build of nlohmann/json from source
- update logs for mirrored projects
- mirrors reject history rewrites
- mirroring is configured via infrastructure under direct control
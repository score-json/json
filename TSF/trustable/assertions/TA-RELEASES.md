---
level: 1.1
normative: true
---

Construction of nlohmann/json library releases is fully repeatable and the results are fully reproducible, with any exceptions documented and justified.

aschemmel-tech: I think it needs more verbose content to describe why the above statement is true. For example copy from the TA template:

Evidence:

1. list of reproducible SHAs

2. list of non-reproducible elements with:
   - explanation and justification
   - details of what is not reproducible

3. evidence of configuration management for build instructions and infrastructure

4. evidence of repeatable builds

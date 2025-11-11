---
level: 1.1
normative: true
references:
    - type: website
      url: "https://github.com/nlohmann/json/tree/v3.12.0"
      description: "release site of nlohmann/json containing the sha values"
evidence:
    type: sha_checker
    configuration:
        binary: "./single_include/nlohmann/json.hpp"
        sha: "aaf127c04cb31c406e5b04a63f1ae89369fccde6d8fa7cdda1ed4f32dfc5de63"
score:
    aschemmel-tech: 0.2
---

The SHA value of the library in use coincides with the SHA value provided by Niels Lohmann for that version.

aschemmel-tech: This should be about "list of reproducible SHAs" - my understanding for this is that 1. we have to build the nlohman lib ourselves, 2. The build must be repeatable (i.e. always the same binary is created if the same config and input is used - this means we can compare the SHAs of these builds and those are always the same, but mostly this does not work because the build contains variable content like time stamps, binary comparison should be able to find these "areas" and not consider these changes as relevant for "reproducability")

Should also add a statement about "evidence of configuration management for build instructions and infrastructure"
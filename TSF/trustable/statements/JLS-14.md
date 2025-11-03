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
---

The SHA value of the library in use coincides with the SHA value provided by Niels Lohmann for that version.

The SHA value of "./single_include/nlohmann/json.hpp" within s-core coincides with the SHA value of nlohmann/json provided by Niels Lohmann for that version.
---
level: 1.1
normative: true
references:
    - type: website
      url: "https://github.com/nlohmann/json/releases"
      description: "release site of nlohmann/json containing the sha values"
evidence:
    type: sha_checker
    configuration:
        binary: "./single_include/nlohmann/json.hpp"
        sha: "9bea4c8066ef4a1c206b2be5a36302f8926f7fdc6087af5d20b417d0cf103ea6"
---

The SHA value of the library in use coincides with the SHA value provided by Niels Lohmann for that version.
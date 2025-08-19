---
level: 1.1
normative: true

references:
        - type: cpp_test
          name: "accept;noncharacter code positions"
          path: "TSF/tests/unit-strings.cpp"
evidence:
  type: "check_artifact_exists"
  configuration:
    ubuntu: "ubuntu"
---

The service accepts Non-Characters.
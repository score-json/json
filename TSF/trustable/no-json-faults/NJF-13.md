---
level: 1.1
normative: true

references:
        - type: cpp_test
          name: "compliance tests from json.org;expected passes"
          path: "tests/src/unit-testsuites.cpp"
evidence:
  type: "check_artifact_exists"
  configuration:
    ubuntu: "ubuntu"
---

The service accepts JSON data consisting of combinations of the data types.
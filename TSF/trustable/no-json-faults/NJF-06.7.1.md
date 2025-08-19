---
level: 1.1
normative: true
references:
        - type: JSON_testsuite
          name: "json.org examples"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/json.org/1.json"
            - "/json.org/2.json"
            - "/json.org/3.json"
            - "/json.org/4.json"
            - "/json.org/5.json"     
            - "/json.org/1.json"
            - "/json.org/2.json"
            - "/json.org/3.json"
            - "/json.org/4.json"
            - "/json.org/5.json"
          description: "Checks that various arrays with more than one value are accepted."
evidence:
  type: "check_artifact_exists"
  configuration:
    ubuntu: "ubuntu"
---

The service accepts comma as member separator.
---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "Unicode;escaped unicode"
          path: "TSF/tests/unit-strings.cpp"
evidence:
  type: "check_artifact_exists"
  configuration:
    ubuntu: "ubuntu"
---

The service does not accept single unpaired utf-16 surrogates.
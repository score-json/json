---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "parse;exponents;leading zeroes"
          path: "TSF/tests/unit-numbers.cpp"
evidence:
  type: "check_artifact_exists"
  configuration:
    ubuntu: "ubuntu"
---

The service ignores leading zeroes in the exponent.
---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "regression tests 1;issue #186 miloyip/nativejson-benchmark: floating-point parsing"
          path: "tests/src/unit-regression1.cpp"
evidence:
  type: "check_artifact_exists"
  configuration:
    ubuntu: "ubuntu"
---

The service parses numbers outside the 64-bit double range without throwing an exception.
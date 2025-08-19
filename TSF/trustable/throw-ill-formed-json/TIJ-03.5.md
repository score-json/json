---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "Unicode (1/5);\\\\uxxxx sequences;incorrect sequences;incorrect surrogate values"
          path: "tests/src/unit-unicode1.cpp"
evidence:
  type: "check_artifact_exists"
  configuration:
    ubuntu: "ubuntu"
---

The service throws an exception on incorrect surrogate pairs.
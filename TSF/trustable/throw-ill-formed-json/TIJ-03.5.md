---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "Unicode (1/5);\\\\uxxxx sequences;incorrect sequences;incorrect surrogate values"
          path: "/workspaces/json/tests/src/unit-unicode1.cpp"
---

The service throws an exception on incorrect surrogate pairs.
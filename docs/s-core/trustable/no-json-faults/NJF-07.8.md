---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "accept;basic multilingual plane"
          path: "/workspaces/json/tests/s-core/unit-strings.cpp"
---

The service does not accept single unpaired utf-16 surrogates.
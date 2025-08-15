---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "Unicode;unescaped unicode"
          path: "TSF/tests/unit-strings.cpp"
---

The service throws an exception on unpaired utf-16 surrogates.
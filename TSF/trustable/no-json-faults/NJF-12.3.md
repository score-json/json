---
level: 1.1
normative: true

references:
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;n"
          path: "/workspaces/json/tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_structure_incomplete_UTF8_BOM.json"
            - "/nst_json_testsuite2/test_parsing/n_structure_lone-invalid-utf-8.json"
          description: ""
        - type: cpp_test
          name: "accept;unescaped utf-16 surrogates"
          path: "/workspaces/json/TSF/tests/unit-strings.cpp"
---

The service rejects single and paired UTF-16 surrogates.
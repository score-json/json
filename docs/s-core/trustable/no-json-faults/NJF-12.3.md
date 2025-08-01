---
level: 1.1
normative: true

references:
        - type: cpp_test
          name: "Markus Kuhn's UTF-8 decoder capability and stress test:5  Illegal code positions"
          path: "tests/src/unit-unicode1.cpp"
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2):test_parsing:n"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_structure_incomplete_UTF8_BOM.json"
            - "/nst_json_testsuite2/test_parsing/n_structure_lone-invalid-utf-8.json"
          description: ""
---

The service rejects single and paired UTF-16 surrogates.
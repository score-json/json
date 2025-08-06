---
level: 1.1
normative: true

references:
        - type: cpp_test
          name: "parser class;accept;number;integers"
          path: "/workspaces/json/tests/src/unit-class_parser.cpp"
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;n"
          path: "/workspaces/json/tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_number_hex_1_digit.json"
            - "/nst_json_testsuite2/test_parsing/n_number_hex_2_digits.json"
            - "/nst_json_testsuite2/test_parsing/n_number_hex_2_digits.json"
          description: "Rejects Hexadecimals"
        - type: cpp_test
          name: "accept;bases"
          path: "/workspaces/json/tests/s-core/unit-numbers.cpp"
---

The service does not accept any base exceeding 10 in ist standard representation. (could be added)

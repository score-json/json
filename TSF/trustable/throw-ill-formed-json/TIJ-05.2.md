---
level: 1.1
normative: true
references:
        - type: JSON_testsuite
          name: "nst's JSONTestSuite (2);test_parsing;n"
          path: "tests/src/unit-testsuites.cpp"
          test_suite_paths:
            - "/nst_json_testsuite2/test_parsing/n_object_non_string_key.json"
            - "/nst_json_testsuite2/test_parsing/n_object_non_string_key_but_huge_number_instead.json"
          description: "Checks that numbers as keys are rejected."
        - type: cpp_test
          name: "parse;names;numbers"
          path: "TSF/tests/unit-objects.cpp"
        - type: cpp_test
          name: "parse;names;arrays"
          path: "TSF/tests/unit-objects.cpp"
        - type: cpp_test
          name: "parse;names;objects"
          path: "TSF/tests/unit-objects.cpp"
        - type: cpp_test
          name: "parse;names;literals"
          path: "TSF/tests/unit-objects.cpp"
evidence:
  type: "check_artifact_exists"
  configuration:
    check_amalgamation: exclude
    codeql: exclude
    dependency_review: exclude
    labeler: exclude
    publish_documentation: exclude
    test_trudag_extensions: exclude
    ubuntu: include
score:
    Jonas-Kirchhoff: 1.0
---

The service throws an exception if a non-string is used as name of any member.
---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-02
        - type: cpp_test
          name: "parser class - core;parse;array;empty array"
          path: "TSF/tests/unit-class_parser_core.cpp"
        - type: cpp_test
          name: "parse;whitespace"
          path: "TSF/tests/unit-arrays.cpp"
        - type: function_reference
          name: "lexer::skip_whitespace"
          path: "include/nlohmann/detail/input/lexer.hpp"
          description: "function, which skips admissible whitespace during reading"
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
    Erikhu1: 1.0
---

The service ignores leading and trailing whitespace for each value.
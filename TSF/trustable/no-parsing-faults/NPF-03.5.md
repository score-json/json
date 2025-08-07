---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "compliance tests from nativejson-benchmark;strings"
          path: "/workspaces/json/tests/src/unit-testsuites.cpp"
        - type: cpp_test
          name: "parser class;parse;string;escaped"
          path: "/workspaces/json/tests/src/unit-class_parser.cpp"
---

The service parses \\, \\/, \\b,\\f, \\n, \\r, \\t and escaped quotation marks.
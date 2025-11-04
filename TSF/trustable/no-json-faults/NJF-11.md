---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-01
        - type: function_reference
          name: "lexer::skip_whitespace"
          path: "include/nlohmann/detail/input/lexer.hpp"
          description: "function, which skips admissible whitespace during reading"
        - type: cpp_test
          name: "accept;whitespace"
          path: "TSF/tests/unit-literals.cpp"
        - type: cpp_test
          name: "accept;whitespace;Leading and tailing"
          path: "TSF/tests/unit-numbers.cpp"
        - type: cpp_test
          name: "accept;whitespace"
          path: "TSF/tests/unit-strings.cpp"
        - type: cpp_test
          name: "accept;whitespace"
          path: "TSF/tests/unit-objects.cpp"
        - type: cpp_test
          name: "accept;whitespace"
          path: "TSF/tests/unit-arrays.cpp"
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

The service provided by nlohmann/json accepts leading and closing whitespaces.
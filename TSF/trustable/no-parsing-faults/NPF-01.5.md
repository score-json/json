---
level: 1.1
normative: true
references:
        - type: item
          items:
            - JLEX-02
        - type: cpp_test
          name: "deserialization;ignoring byte-order marks;2 byte of BOM"
          path: "tests/src/unit-deserialization.cpp"
        - type: cpp_test
          name: "deserialization;ignoring byte-order marks;1 byte of BOM"
          path: "tests/src/unit-deserialization.cpp"
        - type: cpp_test
          name: "deserialization;ignoring byte-order marks;variations"
          path: "tests/src/unit-deserialization.cpp"
        - type: cpp_test
          name: "Unicode (1/5);error for incomplete/wrong BOM"
          path: "tests/src/unit-unicode1.cpp"
evidence:
  type: check_test_results
  configuration:
    tests: 
        - deserialization
        - unicode1
score:
    Jonas-Kirchhoff: 1.0
    Erikhu1: 1.0
---

The service provided by nlohmann/json does not parse partial and perturbed UTF-8 byte order marks within the first three characters of the input and throws an exception.
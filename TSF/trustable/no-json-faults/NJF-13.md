---
level: 1.1
normative: true

references:
        - type: item
          items:
            - JLEX-01
        - type: cpp_test
          name: "compliance tests from json.org;expected passes"
          path: "tests/src/unit-testsuites.cpp"
evidence:
  type: check_test_results
  configuration:
    tests:
        - testsuites
score:
    Jonas-Kirchhoff: 0.95
    Erikhu1: 0.95
---

The service accepts JSON data consisting of combinations of the data types.

aschemmel-tech: I think if we score less than 1.0 we should state why, to be able to improve with reason.
Also a reference to which testcase of this "testsuite" we refer to would be a plus (e.g. "13 Examples") as not all testcases test the above statement.
The "testsuite" refers to external data as in https://json.org/JSON_checker/ ? Then do not forget to state this as a dependency in TA-INPUTS. Do we need to mirror?
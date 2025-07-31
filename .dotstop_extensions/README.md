# Custom references

The custom references can be used by specifying the arguments as specified in the constructor (see references.py) at the top of the trudag item files under references:

For the `CPPTestReferenceTestsuite` an example is:
```
---
...

references:
- type: JSON_testsuite
  name: "compliance tests from json.org:expected failures"
  path: "tests/src/unit-testsuites.cpp"
  test_suite_paths: 
    - "/json_tests/fail2.json"
    - "/json_tests/fail3.json"
  description: "invalid json"
---
```

For the `JSONTestsuiteReference` an example is:
```
---
...

references:
- type: cpp_test
  name: "compliance tests from json.org:expected failures"
  path: "tests/src/unit-testsuites.cpp"
---
```
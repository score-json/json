# Custom references

The custom references can be used by specifying the arguments as specified in the constructor (see references.py) at the top of the trudag item files under references:

For the `JSONTestsuiteReference` an example is:
```
---
...

references:
- type: JSON_testsuite
  name: "compliance tests from json.org;expected failures"
  path: "tests/src/unit-testsuites.cpp"
  test_suite_paths: 
    - "/json_tests/fail2.json"
    - "/json_tests/fail3.json"
  description: "invalid json"
  remove_other_test_data_lines: False # optional, the default value is True 
---
```

For the `CPPTestReference` an example is:
```
---
...

references:
- type: cpp_test
  name: "compliance tests from json.org;expected failures"
  path: "tests/src/unit-testsuites.cpp"
---
```
# Validators

Validators are extensions of trudag, used to validate any data that can be reduced to a floating point metric. The resulting scores are used as evidence for the trustability of items in the trustable graph.

## check_artifact_exists

The check_artifact_exists script validates the presence of artifacts from GitHub Actions workflows for the current SHA. The score is given based on the number of artifacts found vs the number of artifacts expected.

The available configuration dict keys for check_artifact_names are:
  - `check_amalgamation`
  - `codeql`
  - `dependency_review`
  - `labeler`
  - `test_trudag_extensions`
  - `ubuntu`

The available configuration dict values for check_artifact_names are:
  - 'include'
  - 'exclude'

These indicate whether a certain artifact should be included as evidence for a Trustable graph item.
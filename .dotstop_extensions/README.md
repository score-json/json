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

The available configuration dict values for check_artifact_names are:
  - `check_amalgamation`
  - `codeql`
  - `dependency_review`
  - `labeler`
  - `test_trudag_extensions`
  - `ubuntu`

## https_response_time

The automatic validator https_response_time checks the responsiveness of a given website. The expected configuration is as in the example:
```    
evidence:
    type: https_response_time    
    configuration:
        target_seconds: 2 # acceptable response time in seconds, integer or float
        urls: # list of urls to be checked, list of strings
            - "https://github.com/nlohmann/json/issues"
            - "https://github.com/nlohmann/json/graphs/commit-activity"
            - "https://github.com/nlohmann/json/forks?include=active&page=1&period=&sort_by=last_updated"
```
A response time of at least the five-fold of the acceptable response time is deemed inacceptable and gives an individual score of zero.
Likewise inacceptable is a response code other than `200`, which gives an individual score of zero.

The total score is the mean of the individual scores.

## update_checker

The automatic validator update_checker checks the change of the latest review in the specified branc. The expected configuration is as follows.
```
evidence:
    type: https_response_time    
    configuration:
        expected_hash: aa8ea45561547731b82cea2a789429edba27bc31 # the expected hash
        branch: main # the branch of which the current 
        target_seconds: 2 # acceptable response time in seconds, integer or float
        urls: # list of urls to be checked, list of strings
            - "https://github.com/nlohmann/json/issues"
            - "https://github.com/nlohmann/json/graphs/commit-activity"
            - "https://github.com/nlohmann/json/forks?include=active&page=1&period=&sort_by=last_updated"
```
The command `git rev-parse $branch` is executed and the resulting SHA1 is compared to the expected_hash. If these differ, then the latest review on branch main changed, which necessitates a re-review of the statement. To indicate this, the score 0.0 is returned together with a warning, to remind the user of of an adaption.

During this re-review, it is necessary to adapt the expected hash! Otherwise, the validator fails!

If the expected and calculated hash coincide, then https_response_time is executed.

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

For the `WebReference`, an example is:
```
---
...

references:
- type: website
  url: "https://math.stackexchange.com/"
---
```
An example of `WebReference` with non-empty description is
```
---
...

references:
- type: website
  url: "https://ncatlab.org/nlab/show/smooth+Serre-Swan+theorem"
  description: "Wiki article on the smooth Serre-Swan theorem"
---
```

A `WebContentReference` looks identical to a `WebReference` with `type: web_content` instead of `type: website`.

For the `TimeVaryingWebReference`, examples of the possible configurations are:
```
---
...

references:
- type: website
  url: "https://math.stackexchange.com/"
---
```
in case of an empty descritption,
```
---
...

references:
- type: website
  url: "https://ncatlab.org/nlab/show/smooth+Serre-Swan+theorem"
  description: "Wiki article on the smooth Serre-Swan theorem"
---
```
in case of a custom description, and
```
---
...

references:
- type: website
  url: "https://ncatlab.org/nlab/show/smooth+Serre-Swan+theorem"
  description: "Wiki article on the smooth Serre-Swan theorem"
  changelog: "../../graded_Serre_Swan.tex"
---
```
in case of a custom changelog.


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

# Data store interface
## get_my_data()

This interface is used to pull from the data store. Currently, it is only intended to record the history of scoring, so that the functionality to pull data is unused.

## push_my_data()

This function presents the interface of the data generated in the trudag-tool and an external permanent data storage solution. 
As a proof of concept, an interface to an SQLite-database stored within a separate branch of the repository is implemented.
This implementation is to be adapted by either an integrator or when the project is moved to eclipse-score/inc_nlohmann_json!
Likewise, the publish_documentation.yml is to be adapted to reflect the changed data-storage-solution!

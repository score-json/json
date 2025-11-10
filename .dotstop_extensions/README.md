# Custom references

References establish links between the documentation and artifacts of the project, either internal (e.g. lines of code) or external (e.g. files stored on a server). 

For each item of the trustable graph, the hash is calculated by trudag using:
   
* its own name
* the text of its own statement
* its normativity status
* for every of its references, the *content* of that reference
* for every of its fallacies, the description and content of the corresponding reference

Custom references are defined in `references.py`. A (custom) reference is used by adding an object into the list `references` in the header of the item file. The `type` corresponds to the classmethod `type` of a reference class of `references.py`, and the remaining object correspond to the arguments of the constructor.

## CPPTestReference

The content of a `CPPTestReference` is given by the lines of code corresponding to a test-case or a section of a test-case in a specified unit-test-file. The sections are identified in the value of "name", where the nested sections are separated by semicolons.

For the `CPPTestReference` the expected configuration is:
```
---
...

references:
- type: cpp_test
  name: "compliance tests from json.org;expected failures"
  path: "tests/src/unit-testsuites.cpp"
---
```

## JSONTestsuiteReference

The `JSONTestsuiteReference` is a variant of the function reference, which is augmented by an external file containing test-data in the form of well- or ill-formed JSON candidate data. 
A `JSONTestsuiteReference` is therefore given by the data of a `CPPTestReference` together with a list containing the paths to these external files.
The external files are stored in a separate branch of the repository, and their text is loaded via call to github.
The content of a `JSONTestsuiteReference` is given by the content of the underlying `CPPTestReference` together with the sum of the contents of the external test-suite files.

For the `JSONTestsuiteReference` the expected configuration is:
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

## FunctionReference

The content of a `FunctionReference` is given by the code inclusive all comments of a C++ function within a class in a specified file in the repository. The specific position, i.e. start- and end-line, of the code within that file is not part of the content.  

For the `FunctionReference` an example is:
```
---
...

references:
- type: function_reference
  name: "basic_json::accept"
  path: "include/nlohmann/json.hpp"
---
```

Since functions may be overloaded, a `FunctionReference` can be initialised with an optional overload-parameter. 
The overload-parameter specifies which implementation of the function is referred to, i.e. if the overload-parameter for the function ``class::function()`` is set to _n_, then the _n_-th implementation when counting the occurrences from top to bottom of ``function()`` within the class ``class`` is used, if it exists; otherwise, an error is thrown. Additionally, it is possible, but not mandatory, to give a description. The full example is:
```
---
...

references:
- type: function_reference
  name: "basic_json::accept"
  path: "include/nlohmann/json.hpp"
  description: "the public interface of the `accept`-functionality of nlohmann/json"
  overload: 2
---
```

## WebReference

The content of a `WebReference` is its url. This reference is intended to be utilised in case that the content of the web-site is constantly changing (e.g. due to a clock being implemented somewhere on the site), but the reviewer is certain that the type of the content and it being supportive of the statement is fulfilled as long a the website is reachable. An example is `https://introspector.oss-fuzz.com/project-profile?project=json`, where the most recent fuzz-testing report for nlohmann/json is published.

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

## WebContentReference

The content of a `WebContentReference` is its content. This reference is intended to be utilised in case of *static* references, that should not vary in a short time-frame, and whose content is most important for the trustability of the statement. An example is a file located on a github repository, e.g.  `https://raw.githubusercontent.com/nlohmann/json/refs/heads/develop/.github/workflows/cifuzz.yml`

A `WebContentReference` looks identical to a `WebReference` with `type: web_content` instead of `type: website`.

For the `TimeVaryingWebReference`, examples of the possible configurations are:
```
---
...

references:
- type: web_content
  url: "https://math.stackexchange.com/"
---
```
in case of an empty description, and
```
---
...

references:
- type: web_content
  url: "https://ncatlab.org/nlab/show/smooth+Serre-Swan+theorem"
  description: "Wiki article on the smooth Serre-Swan theorem"
---
```
in case of a custom description.

## TimeVaryingWebReference

The content of a `TimeVaryingWebReference` is given by the content of a changelog, whose default value is `ChangeLog.md`, which mirrors the changelog of nlohmann/json. This reference is intended for websites, whose content is constantly changing, so that a `WebContentReference` makes the item un-reviewable, but whose content at the time of an update influences the trustability. An example is `https://github.com/nlohmann/json/pulse/monthly`, which can be used to demonstrate that nlohmann/json is *up to the most recent version* under active development.

An example of the complete configuration for `TimeVaryingWebReference` is

```
---
...
references:
- type: project_website
  url: "https://ncatlab.org/nlab/show/smooth+Serre-Swan+theorem"
  description: "Wiki article on the smooth Serre-Swan theorem"
  changelog: "ideas/graded/graded_Serre_Swan.tex"
---
```
where `description` and `changelog` are optional arguments.

## ListOfTestCases

The content of a `ListOfTestCases` is given by the list of test-cases extracted from the unit-tests given in the files in the provided directories. 
It is assumed that a unit-test is saved in a file with the name unit-xxx.cpp, and only those files are used to compile the list. 
Further, it is assumed that a unit-test-file is structured as

```
...
TEST_CASE("my test case")
{
    ...
    SECTION("my section")
    {
        ...
    }
    ...
}
```

and the structure regarding test-cases and (nested) sections of test-cases is extracted. The expected configuration is 

```
---
...
references:
- type: list_of_test_cases
  test_files:
    - TSF/tests
    - tests/src
---
```

## workflow_failures

This reference queries `https://github.com/{self._owner}/{self._repo}/actions?query=is%3Afailure+branch%3A{self._branch}` and collects the number of failed workflow runs as its content.
Here, owner, repo and branch are the arguments given to the constructor of the reference.
If no branch is specified, then all failures are collected, i.e. `https://github.com/{self._owner}/{self._repo}/actions?query=is%3Afailure` is queried.
In case the website is un-reachable, or the github layout changes drastically so that the number of failed workflow runs does not exist at the expected location, an error is thrown.

The expected configuration is 

```
---
...
references:
- type: workflow_failures
      owner: "eclipse-score"
      repo: "inc_nlohmann_json"
      branch: "json_version_3_12_0"
---
```

## ItemReference

Some references support every (directly or indirectly) supporting item of an item. 
Instead of repeating these references in each supporting item, these references are listed in the supported item.
The inheritance of the references is then clarified in the documentation by an `ItemReference`.
In the final documentation in human-readable form, an ItemReference simply lists all items of which the references are inherited with hyperlinks.

To detect the inheritance of references in the content of the supporting items, the content of an ItemReference is the combination of the sha's stored in the .dotstop.dot file of the listed supported items.
If any reference of any of the listed supported items changes, then its sha changes and the review-status of the item becomes false.
After successful re-review, the review-status of the supported items is re-set to true, so that the new sha is stored in the .dotstop.dot file.
This automatically sets the review-status of the supporting items, which inherit the references, to false, thereby triggering a re-review of these.
The expected configuration is as follows

```
---
...
references:
- type: item
  items:
    - ITEM-1
    - ITEM-2
    - ...
---
...
```
Here, the elements of the list `items` must be normative nodes of the trustable graph, otherwise an error is thrown.

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

## check_test_results

The automatic validator `check_test_results` is intended to evaluate the database `MemoryEfficientTestResults.db` which is generated in the ubuntu-Workflow, and which contains the test-report of the most recent workflow run. This database is temporary, and, contrary to `TSF/MemoryEfficientTestResultData.db`, which is persistently stored on the branch `save_historical_data`, not persistently stored.

The expected configuration is given as follows:

```
evidence:
    type: check_test_results
    configuration:
        tests: # list of test-files 
            - class_lexer
            - unicode1
            - strings
        database: MemoryEfficientTestResults.db # optional argument, default: MemoryEfficientTestResults.db; path to test-result database from project root
        table: test_results # optional argument, default: test_results; name of table in database
```

The test-files are called unit-FILE_NAME.cpp. In the configuration, FILE_NAME is expected only, i.e. without the leading unit- and without the file-extension.

For each test specified in test-files, the number of passed and failed test-cases is calculated, while the number of skipped test-cases is ignored. The score of each test is then the ratio of passed test-cases compared to all non-skipped test-cases; the total score is the mean of the individual scores.

## check_issues

The automatic validator `check_issues` is intended to evaluate the json-lists `raw_open_issues.json` and `raw_closed_issues.json` and compare with the list of known issues of nlohmann/json labelled as bug opened since the release of the version of nlohmann/json that is documented. The json lists are generated in the publish_documentation-Workflow, and not persistently stored.

The expected configuration is given as follows:

```
evidence:
    type: check_issues
    configuration:
        release_date: "2025-04-11T00:00:00Z" # release date of the documented version in the format %Y-%m-%dT%H:%M:%SZ
        list_of_known_misbehaviours: "./TSF/docs/nlohmann_misbehaviours_comments.md" # path to the list of known misbehaviours relative to the root of the repository 

```

In case that the release date is not specified using the expected format, or either of the `raw_open_issues.json` and `raw_closed_issues.json` can not be opened, then the score 0.0 is returned together with an error indicating the warning.

The list of known misbehaviours collects the known issues labelled as bugs opened in nlohmann/json since the release of the version that is documented.
These issues are collected in a table containing the issue-ID, an indication whether the issue applies to the usage of nlohmann/json within Eclipse S-CORE and a comment, which is printed into the list of known misbehaviours.
From `raw_closed_issues.json`, all issue IDs are collected, which are labelled as bug and opened after the release_date; and from `raw_open_issues.json`, all issue IDs are collected.
If for any of these IDs, it is not explicitly indicated in the list of known misbehaviours that this issue does not apply to Eclipse S-CORE, then the score 0.0 is returned.
Otherwise, the score 1.0 is assigned.

## did_workflows_fail

The automatic validator `did_workflows_fail` queries the web-site `https://github.com/{owner}/{repo}/actions?query=event%3A{event}+is%3Afailure+branch%3A{branch}` and looks on the number of workflow run results which is printed at the head of the table.
In case that this number is not zero, a score of 0.0 is returned, and 1.0 otherwise.

The expected configuration is given as follows:

```
evidence:
    type: did_workflows_fail
    configuration:
        owner: "eclipse-score" # owner of the repository
        repo: "inc_nlohmann_json" # name of the repository
        branch: "json_version_3_12_0" # name of the branch
        action: "push" # optional, default is push
```

It is of utmost importance that the arguments come with quotation marks. Otherwise, the update helper does not work as intended.

## coveralls_reporter

The automatic validator `coveralls_reporter` queries the [coveralls](https://coveralls.io/) api to get the line and branch coverages calculated by the service, which is running on the repository.
Unless the version of `nlohmann/json` documented in this repository changes, it is expected that both coverage numbers remain constant.
When initialising the reference, the current code coverage is given as a parameter, to which the fetched coverages are compared.
If no branch is specified, then the most recently calculated coverage is fetched, so that it is generally recommended to specify a branch.
Moreover, it is possible to specify the number of decimal digits, which is defaulted to three, when not specified.
The validator returns a score of 1.0 if both fetched coverages rounded to the specified number of decimal digits coincide with the specified ones, and a score of 0.0 otherwise.

The expected configuration is the following:

```
evidence:
    type: coveralls_reporter
    configuration:
        owner: "score-json"
        repo: "json"
        branch: "main"
        line_coverage: 99.186
        branch_coverage: 93.865
        digits: 3
```

## combinator

The trudag tool does currently not support the use of multiple custom validators for one single TSF item. To work around this, the validator `combinator` is implemented as a meta-validator that executes multiple validators and combines their scores using a weighted average. This enables the validation of complex trustable items that require evidence from multiple sources or validation methods.

The combinator accepts a list of validators, each with its own configuration and optional weight. Each validator is executed independently, and their scores are combined using the formula: `(score1 * weight1 + score2 * weight2 + ...) / (weight1 + weight2 + ...)`. If no weights are specified, all validators are treated with equal weight (weight = 1.0).

The combinator supports the following validator types:
- `check_artifact_exists`
- `https_response_time` 
- `check_test_results`
- `file_exists`
- `sha_checker`
- `check_issues`
- `did_workflows_fail`
- `coveralls_reporter`

The expected configuration is as follows:

```
evidence:
    type: combinator
    configuration:
        validators:
            - type: "check_test_results"
              weight: 2.0  # optional, defaults to 1.0
              configuration:
                  tests:
                      - class_lexer
                      - unicode1
            - type: "https_response_time"
              weight: 1.0  # optional, defaults to 1.0  
              configuration:
                  target_seconds: 2
                  urls:
                      - "https://github.com/nlohmann/json/issues"
            - type: "coveralls_reporter"
              weight: 1.5  # optional, defaults to 1.0
              configuration:
                  owner: "score-json"
                  repo: "json"
                  branch: "main"
                  line_coverage: 99.186
                  branch_coverage: 93.865
                  digits: 3
            - type: "did_workflows_fail"
              configuration:
                  owner: "eclipse-score"
                  repo: "inc_nlohmann_json" 
                  branch: "json_version_3_12_0"
```

All weights must be non-negative. If the sum of all weights is zero, the combinator returns a score of 0.0. The combinator aggregates all exceptions and warnings from the individual validators and returns them alongside the combined score.

# Data store interface

The data store interface utilises the built-in the `dump` functionality of trudag to store the trustable score, and to include the development of the trustable score over time into the report.

Since no persistent data store is established as of now, the current implementation serves as a proof of concept, where the collected data are stored on a separate branch of the repository.

The input of the data store are the data generated by the trudag tool during the `score` or `publish` operation. These data have the format:

```
[{"scores": [{id: "ID-1", "score": score}, ...], "info": {"Repository root": "my_repository", "Commit SHA": "sha_123", "Commit date/time": "%a %b %d %H:%M:%S %Y", "Commit tag": "my_tag", "CI job id": 123, "Schema version": 123, "Branch name": "my_branch"}}]
```

## push

This functionality writes the generated data into an sqlite database `TrustableScoring.db` located in the folder `TSF`. This database contains two tables, `commit_info`, where the metadata of "info" are stored, and `scores`, where the scores are stored, and which references `commit_info` via the date as foreign key.

It is intended to store data only once per commit. If, for any reason, the same commit generates data more than once, then only the most recent data are stored, and the obsolete data are deleted. This still ensures that the scoring history of the main branch is as complete as possible.

## pull

This functionality parses the information stored in `TrustableScoring.db` into the format which is expected by trudag. In case that no data are found, the empty history is returned.
=============================================================
Update Concept for the version of nlohmann/json within S-CORE
=============================================================

Update process of the original nlohmann/json
============================================

From historical data, it is expected that the updates of nlohmann/json are announced by an announcement titled "JSON for Modern C++ version X.X.X" in the section `Announcements <https://github.com/nlohmann/json/discussions/categories/announcements?discussions_q=category%3AAnnouncements/>`_ on the discussions-page of the repository nlohmann/json.
This announcement is expected to contain the release date, SHA-256 values for json.hpp, include.zip and json.tar.xz, and a brief list containing bug fixes, improvements, further changes and deprecated functions.
The updated version is expected to be finally merged into the branch **master**, from where the most recent version can be drawn.

Update process of the S-CORE version
====================================

In the following, we shall describe the intricacies of updating the version of nlohmann/json within Eclipse S-CORE. 
This version is not a mere fork of the original master branch of nlohmann/json, but instead enriched with the documentation following the Trustable Software Framework (TSF).
The enrichment with the documentation necessitates some changes to the fork of the original repository.
For the most part, these changes are in-obtrusive, and mere additions.
In particular, the folders include and single-include remain unchanged, and should be updated without further adaptations.
In some cases, however, additional tests are run and data are generated and collected, which were not run or generated in the original nlohmann/json, so that obtrusive changes of files were necessary.
For these files, and in particular the workflow files, caution must be exercised, as to not disturb the documentation.
Moreover, some parts of the documentation must be adapted to the new version.

Finally, to ensure the long-term maintainability of projects relying on the documentation of the library nlohmann/json, it is recommended to save the current (and possibly prior) versions of the documented version in a separate branch of the repository.


What can not be updated without further precautions?
----------------------------------------------------

cmake/ci.cmake
    This file defines, in particular, the various custom cmake targets; in particular, the various configurations for the execution of the unit- and integration-tests are defined.
    The TSF requires, or, at the very least, strongly encourages us to collect test-results.
    In order to do this efficiently, the ctest command is adapted to automatically generate the junit-logs of each test-run.
    For this, the option --output-junit is set with output path "../my_logs/TARGETNAME_junit.xml", where TARGETNAME is replaced by the name of the respective cmake target; in case that this convention is insufficient to uniquely identify the logs, TARGETNAME is amended by a number.
    When updating, it must be ensured that these adaptations are preserved.
    Moreover, if the update introduces new cmake targets or new executions of ctest, it must be ensured, that the junit-log is generated and stored with a similar naming convention in the folder "../my_logs/".
    Otherwise, it can not be ensured that the test data are accurately captured.  


tests/CMakeLists.txt
    This file collects, in particular, the files containing the unit- and integration-tests in a list, which is given to cmake. 
    Custom tests were added in TSF/tests to document the fulfillment of the expectations. 
    To ensure that these tests are run, the file tests/CMakeLists.txt has been modified.
    During the update, it must be ensured, that the custom tests are still being executed.

.github/workflows/parent-workflow.yml
    To ensure a specific execution order for the individual github workflows, their execution is orchestrated by the parent-workflow.
    To guarantee that this order is respected, it must be ensured that every other workflow runs on workflow_call, only.

.github/workflows/ubuntu.yml
    The ubuntu workflow orchestrates the parallel execution of various cmake targets with varying configurations running on the latest version of ubuntu.
    The first adaptation is that every step, in which a junit-report is generated, generates an artifact.
    It must be ensured, that these artifacts are still generated after the update.
    The second adaptation is that the test-results are captured, processed and persistently stored or stored in the ubuntu-artifact.
    Therefore, it must be ensured that the jobs publish_test_data_success, publish_test_data_failure, publish_test_data_cancellation and ubuntu_artifact are executed.
    Moreover, in case that any further job is added by nlohmann, it must be ensured that this job is added to the list of jobs required before the latter workflows are executed.
    If any further job added by nlohmann generates a junit-log, it must be ensured that this job generates an artifact containing its junit-logs. 

.github/workflows/cifuzz.yml
    This workflow uses Google's oss-fuzz, which is not available to the copy within Eclipse S-CORE. 
    Therefore, this workflow needs to be disabled in the copy. 
    Currently, this is done by removing it altogether, which we recommend to do so that no confusion as to why this workflow is not executed arises. 

.github/workflows/publish_documentation.yml
    This workflow is replaced with a completely customised version, which reflects the use of trudag and the integration into the Eclipse S-CORE organisation.
    Therefore, it is recommended to not change this workflow. 
    In particular, the version of publish_documentation in the original repository nlohmann/json must not replace

Other entries of .github/workflows
    For every workflow, it must be ensured that they are executed on workflow_call, only.
    New workflows should be carefully reviewed.
    If it is determined that their execution within the project is beneficial, and that they do not interfere with, then they should be integrated within the parent workflow at an appropriate place.
    If nlohmann deletes any of the currently executed workflows, in particular  check_amalgamation.yml, codeql.yml, dependency_review.yml, labeler.yml, test_trudag_extensions.yml and ubuntu.yml, then it is strongly recommended to keep the currently executed version, since the automatic validator check_artifact_exists depends on the existence of these workflows.
    In case that it is determined that these workflows should be deleted also in the documented copy of nlohmann/json, then the validator check_artifact_exists and all its occurrences must be adapted accordingly. 

.github/workflows
    THIS REQUIRES A TAD MORE WORK THAN I WOULD LIKE.


Necessary adaptations of the documentation
------------------------------------------

The adaptations to the documentation have to be done both in the most recent as well as in the now outdated version of the documented library.

JLS-26
    It must be ensured that the branch protection rules for the branch containing the most recent documentation are set accordingly, and that the reference of JLS-26 refers to the correct rules.

JLS-14
    It must be ensured that the announcement post referring to the correct version is referenced.
    Furthermore, the sha-value of the evidence must be adapted to the one provided in that announcement post.

JLS-07
    It must be ensured that the statement and reference refers to the branch protection rules of the correct branch. Of course, these branch protection rules must be enforced.

JLS-06 
    Analogously to JLS-07, it must be ensured that the correct branch is referred to and referenced.

JLS-01
    It must be ensured that the correct branch and branch protection rules are addressed, set and referenced.

Default branch
--------------

The scheduled github workflows are executed on the default branch, only. 
To guarantee compliance with the TSF, the unit- and integration-tests are run daily.
Therefore, it must be ensured that the branch containing the most recent documented version of nlohmann/json is assigned as default branch.


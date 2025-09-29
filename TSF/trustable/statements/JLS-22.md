---
level: 1.1
normative: true
references:
    - type: verbose_file
      path: ./.github/workflows/parent-workflow.yml
      description: "github workflow running daily and triggering the workflow ubuntu"
    - type: verbose_file
      path: ./.github/workflows/ubuntu.yml
      description: "workflow, in which unit tests are executed with a myriad of test environments and test results are captured."
    - type: verbose_file
      path: ./TSF/scripts/capture_test_data.py
      description: "script, which collects the data produced by ctest in a database"
    - type: website
      url: https://github.com/score-json/json/blob/save_historical_data/TSF/MemoryEfficientTestResultData.db
      description: "the database containing the test results"
evidence:
    type: https_response_time
    configuration:
        target: 2.0
        urls:
            - https://github.com/score-json/json/blob/save_historical_data/TSF/MemoryEfficientTestResultData.db
score:
    Jonas-Kirchhoff: 1.0
---

The github workflow executes the unit tests daily and saves the results as time-series data.
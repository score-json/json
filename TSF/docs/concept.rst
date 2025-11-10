..
   # *******************************************************************************
   # Copyright (c) 2025 Contributors to the Eclipse Foundation
   #
   # See the NOTICE file(s) distributed with this work for additional
   # information regarding copyright ownership.
   #
   # This program and the accompanying materials are made available under the
   # terms of the Apache License Version 2.0 which is available at
   # https://www.apache.org/licenses/LICENSE-2.0
   #
   # SPDX-License-Identifier: Apache-2.0
   # *******************************************************************************
.. _concept:

Concept
=================

For the concept of the Trustable Software Framework (TSF), please refer to the `Eclipse Process Description <https://eclipse-score.github.io/process_description/main/trustable/index.html>`_.

Scoring
-------

The trustability scores in the TSF are calculated recursively using the underlying graph structure.
In particular, scores are provided, either manually by subject-matter-experts (SME) or automatically by automatic evidence, for the leafs of the graph only.
Then, the scores are calculated recursively using the following scheme:

+------------+---------------+---------+----------+-----------+----------------------+------------------------------+
| normative_ | review-status |   SME   | evidence | reference_ | unsuspect children   | score_                      |
+============+===============+=========+==========+===========+======================+==============================+
| ``false``  | ``*``         | ``*``   | ``*``    | ``*``     | ``*``                | no score                     |
+------------+---------------+---------+----------+-----------+----------------------+------------------------------+
| ``true``   | ``false``     | ``*``   | ``*``    | ``*``     | ``*``                | 0.0                          |
+------------+---------------+---------+----------+-----------+----------------------+------------------------------+
| ``true``   | ``true``      | ``yes`` | ``no``   | ``no``    | ``*``                | 0.0                          |
+------------+---------------+---------+----------+-----------+----------------------+------------------------------+
| ``true``   | ``true``      | ``yes`` | ``no``   | ``yes``   | ``no``               | SME                          |
+------------+---------------+---------+----------+-----------+----------------------+------------------------------+
| ``true``   | ``true``      | ``yes`` | ``yes``  | ``*``     | ``no``               | SME × evidence               |
+------------+---------------+---------+----------+-----------+----------------------+------------------------------+
| ``true``   | ``true``      | ``*``   | ``*``    | ``*``     | ``yes``              | mean of unsuspect            |
|            |               |         |          |           |                      | children-scores              |
+------------+---------------+---------+----------+-----------+----------------------+------------------------------+

.. _normative: https://codethinklabs.gitlab.io/trustable/trustable/reference/trudag/dotstop/core/item.html#trudag.dotstop.core.item.BaseItem.normative
.. _reference: https://codethinklabs.gitlab.io/trustable/trustable/reference/trudag/dotstop/core/item.html#trudag.dotstop.core.item.BaseItem.references
.. _score: https://codethinklabs.gitlab.io/trustable/trustable/trudag/scoring-roadmap.html
.. _review-status: 
.. _SME: 
.. _evidence:  

- **normative**: Indicates whether the statement is normative (`true`) or not (`false`). If a statement is not normative, no evaluation or scoring takes place.
- **review Status**: Shows the current review status of the statement. A `false` means no evaluation is available yet and the score is set to `0.0`.  
- **SME**: Indicates whether a subject matter expert has provided an assessment.  
- **evidence**: Indicates if supporting evidence exists for the statement’s assessment.  
- **reference**: Indicates whether sources are available that support or justify the statement.  
- **unsuspect children**:   
- **score**: Shows the calculated score of the statement.

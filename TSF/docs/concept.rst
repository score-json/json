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

+------------+----------------+--------+-----------+------------+--------------+------------------------------------------+
| normative_ | review-status_ | SME_   | evidence_ | reference_ | link-status_ | score_                                   |
+============+================+========+===========+============+==============+==========================================+
| ``false``  | ``*``          | ``*``  | ``*``     | ``*``      | ``*``        | no score                                 |
+------------+----------------+--------+-----------+------------+--------------+------------------------------------------+
| ``true``   | ``false``      | ``*``  | ``*``     | ``*``      | ``*``        | 0.0                                      |
+------------+----------------+--------+-----------+------------+--------------+------------------------------------------+
| ``true``   | ``true``       | ``yes``| ``no``    | ``no``     | ``*``        | 0.0                                      |
+------------+----------------+--------+-----------+------------+--------------+------------------------------------------+
| ``true``   | ``true``       | ``yes``| ``no``    | ``yes``    | ``linked``   | SME                                      |
+------------+----------------+--------+-----------+------------+--------------+------------------------------------------+
| ``true``   | ``true``       | ``yes``| ``yes``   | ``*``      | ``linked``   | SME × evidence                           |
+------------+----------------+--------+-----------+------------+--------------+------------------------------------------+
| ``true``   | ``true``       | ``*``  | ``*``     | ``*``      | ``suspect``  | mean of child items with no suspect links|
+------------+----------------+--------+-----------+------------+--------------+------------------------------------------+

.. _normative: https://codethinklabs.gitlab.io/trustable/trustable/reference/trudag/dotstop/core/item.html#trudag.dotstop.core.item.BaseItem.normative
.. _review-status: https://codethinklabs.gitlab.io/trustable/trustable/reference/trudag/dotstop/core/graph/trustable_graph.html#trudag.dotstop.core.graph.trustable_graph.TrustableGraph.set_link_status
.. _SME: https://codethinklabs.gitlab.io/trustable/trustable/reference/trudag/dotstop/core/item.html#trudag.dotstop.core.item.BaseItem.sme_scores
.. _evidence: https://codethinklabs.gitlab.io/trustable/trustable/trudag/usage.html#providing-evidence
.. _reference: https://codethinklabs.gitlab.io/trustable/trustable/reference/trudag/dotstop/core/item.html#trudag.dotstop.core.item.BaseItem.references
.. _link-status: https://codethinklabs.gitlab.io/trustable/trustable/reference/trudag/dotstop/core/graph/trustable_graph.html#trudag.dotstop.core.graph.trustable_graph.LinkStatus
.. _score: https://codethinklabs.gitlab.io/trustable/trustable/trudag/scoring-roadmap.html


- **normative**: Indicates whether the statement is normative (`true`) or not (`false`). If a statement is not normative, it is considered optional or informational, and no evaluation or scoring is performed.
- **review-status**: Shows the current review status of the statement. A `false` means no evaluation is available yet and the score is set to `0.0`.  
- **SME**: Indicates whether a subject matter expert has provided an assessment.  
- **evidence**: Indicates if supporting evidence exists for the statement’s assessment.  
- **reference**: Indicates whether sources are available that support or justify the statement.  
- **link-status**: Indicates whether there are any suspect links between child and parent items. If suspect links exist, the score is calculated based on child items without suspect links only.   
- **score**: Shows how the score is calculated.


Example
~~~~~~~

This diagram illustrates an example of the scoring process in the Trustable Software Framework (TSF). 
Please note that the numbers shown in this graph are **example values only** and do not represent real assessments.

.. image:: score_calculation_example.svg
   :alt: Graph illustrating the scoring process in the Trustable Software Framework
   :align: center
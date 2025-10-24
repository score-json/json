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
| normative  | review-status |   SME   | evidence | reference | unsuspect children   | score                        |
+============+===============+=========+==========+===========+======================+==============================+
| ``false``  | ``*``         |  ``*``  |  ``*``   |  ``*``    | ``*``                | no score                     |
+------------+---------------+---------+----------+-----------+----------------------+------------------------------+
| ``true``   | ``false``     |  ``*``  |  ``*``   |  ``*``    | ``*``                | 0.0                          |
+------------+---------------+---------+----------+-----------+----------------------+------------------------------+
| ``true``   | ``true``      | ``yes`` |  ``no``  |  ``no``   | ``*``                | 0.0                          |
+------------+---------------+---------+----------+-----------+----------------------+------------------------------+
| ``true``   | ``true``      | ``yes`` |  ``no``  |  ``yes``  | ``no``               | SME                          |
+------------+---------------+---------+----------+-----------+----------------------+------------------------------+
| ``true``   | ``true``      | ``yes`` |  ``yes`` |  ``*``    | ``no``               | SME × evidence               |
+------------+---------------+---------+----------+-----------+----------------------+------------------------------+
| ``true``   | ``true``      |  ``*``  |  ``*``   |  ``*``    | ``yes``              | mean of unsuspect            |
|            |               |         |          |           |                      | children-scores              |
+------------+---------------+---------+----------+-----------+----------------------+------------------------------+


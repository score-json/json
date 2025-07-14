
Trustable Compliance Report
===========================

Item status guide ## { .subsection }
------------------------------------

Each item in a Trustable Graph is scored with a number between 0 and 1.
The score represents aggregated organizational confidence in a given Statement, with larger numbers corresponding to higher confidence.
Scores in the report are indicated by both a numerical score and the colormap below:


.. raw:: html

   <div class="br" style="height: 26px; width: 80%;background: linear-gradient(to right in hsl, hsl(0.0, 100%, 65%) 0%, hsl(120.0, 100%, 30%) 100%);">
   <span style="float:right;">1.00&nbsp</span>
   <span style="float:left;">&nbsp0.00</span>
   </div>


The status of an item and its links also affect the score.

Unreviewed items are indicated by a strikethrough.
The score of unreviewed items is always set to zero.

Suspect links are indicated by italics.
The contribution to the score of a parent item by a suspiciously linked child is always zero, regardless of the child's own score.

Compliance for TA
-----------------

.. list-table::
   :header-rows: 1

   * - Item
     - Summary
     - Score
   * - :ref:`ta-analysis` {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}
     - Collected data from tests and monitoring of deployed software is analysed according to specified objectives.
     - 0.00
   * - :ref:`ta-behaviours` {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}
     - Expected or required behaviours for JSON-Library are identified, specified, verified and validated based on analysis.
     - 0.00
   * - :ref:`ta-confidence` {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}
     - Confidence in JSON-Library is measured based on results of analysis.
     - 0.00
   * - :ref:`ta-constraints` {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}
     - Constraints on adaptation and deployment of JSON-Library are specified.
     - 0.00
   * - :ref:`ta-data` {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}
     - Data is collected from tests, and from monitoring of deployed software, according to specified objectives.
     - 0.00
   * - :ref:`ta-fixes` {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}
     - Known bugs or misbehaviours are analysed and triaged, and critical fixes or mitigations are implemented or applied.
     - 0.00
   * - :ref:`ta-indicators` {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}
     - Advance warning indicators for misbehaviours are identified, and monitoring mechanisms are specified, verified and validated based on analysis.
     - 0.00
   * - :ref:`ta-inputs` {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}
     - All inputs to JSON-Library are assessed, to identify potential risks and issues.
     - 0.00
   * - :ref:`ta-iterations` {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}
     - All constructed iterations of JSON-Library include source code, build instructions, tests, results and attestations.
     - 0.00
   * - :ref:`ta-methodologies` {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}
     - Manual methodologies applied for JSON-Library by contributors, and their results, are managed according to specified objectives.
     - 0.00
   * - :ref:`ta-misbehaviours` {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}
     - Prohibited misbehaviours for JSON-Library are identified, and mitigations are specified, verified and validated based on analysis.
     - 0.00
   * - :ref:`ta-releases` {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}
     - Construction of JSON-Library releases is fully repeatable and the results are fully reproducible, with any exceptions documented and justified.
     - 0.00
   * - :ref:`ta-supply_chain` {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}
     - All sources for JSON-Library and tools are mirrored in our controlled environment.
     - 0.00
   * - :ref:`ta-tests` {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}
     - All tests for JSON-Library, and its build and test environments, are constructed from controlled/mirrored sources and are reproducible, with any exceptions documented.
     - 0.00
   * - :ref:`ta-updates` {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}
     - JSON-Library components, configurations and tools are updated under specified change and configuration management controls.
     - 0.00
   * - :ref:`ta-validation` {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}
     - All specified tests are executed repeatedly, under defined conditions in controlled environments, according to specified objectives.
     - 0.00


Compliance for TRUSTABLE
------------------------

.. list-table::
   :header-rows: 1

   * - Item
     - Summary
     - Score
   * - :ref:`trustable-software` {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}
     - This release of JSON-Library is Trustable.
     - 0.00


Compliance for TT
-----------------

.. list-table::
   :header-rows: 1

   * - Item
     - Summary
     - Score
   * - :ref:`tt-changes` {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}
     - JSON-Library is actively maintained, with regular updates to dependencies, and changes are verified to prevent regressions.
     - 0.00
   * - :ref:`tt-confidence` {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}
     - Confidence in JSON-Library is achieved by measuring and analysing behaviour and evidence over time.
     - 0.00
   * - :ref:`tt-construction` {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}
     - Tools are provided to build JSON-Library from trusted sources (also provided) with full reproducibility.
     - 0.00
   * - :ref:`tt-expectations` {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}
     - Documentation is provided, specifying what JSON-Library is expected to do, and what it must not do, and how this is verified.
     - 0.00
   * - :ref:`tt-provenance` {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}
     - All inputs (and attestations for claims) for JSON-Library are provided with known provenance.
     - 0.00
   * - :ref:`tt-results` {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}
     - Evidence is provided to demonstrate that JSON-Library does what it is supposed to do, and does not do what it must not do.
     - 0.00


Compliance for WFJ
------------------

.. list-table::
   :header-rows: 1

   * - Item
     - Summary
     - Score
   * - :ref:`wfj-01` {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)" .status-unreviewed}
     - The service checks for the four primitive types (strings, numbers, booleans, null).
     - 0.00


----

_Generated for: json\ *library*


* _Repository root: /home/d93609/projects/inc\ *json*
* *Commit SHA: d7cdd5c*
* *Commit date/time: Fri Jul 4 06:58:09 2025*
* *Commit tag: d7cdd5cb13ee04aeb1dbdbde7956cc09e318d100*

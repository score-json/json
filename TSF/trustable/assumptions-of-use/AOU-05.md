---
level: 1.1
normative: true
---

The integrator shall ensure that input is encoded as UTF-8 (as required by RFC8259) and that exceptions thrown in case other string formats are used are properly handled

aschemmel-tech: shouldn't we say generally that RFC8259 has to be followed, or is this error something special? I am unsure with the exception part, because if we use nlohman/json in S-CORE the exceptions well lead to a direct terminate and cannot be hanled. But I guess we describe the AOU's for nlohman/json stand alone. But when I think of it, as we also use the requirements from S-CORE (only for the parsing functionality) the AOU cannot be generic, so we need to reformulate.
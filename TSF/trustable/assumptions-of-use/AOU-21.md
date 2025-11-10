---
level: 1.1
normative: true
---

The integrator shall ensure that a string does not contain escaped unpaired utf-16 surrogate characters, and that exceptions are properly handled, whenever a string is to be parsed by nlohmann/json.

aschemmel-tech: shouldn't we say generally that RFC8259 has to be followed, or is this error something special? I am unsure with the exception part, because if we use nlohman/json in S-CORE the exceptions well lead to a direct terminate and cannot be hanled. But I guess we describe the AOU's for nlohman/json stand alone. But when I think of it, as we also use the requirements from S-CORE (only for the parsing functionality) the AOU cannot be generic, so we need to reformulate.
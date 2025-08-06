
### PJD-01 

The service provides implementations that parses JSON texts, which ignores the presence of a byte order mark rather than treating it as an error.


**Supported Requests:**

- [JLEX-02](JLEX.md#jlex-02)

**Supporting Items:**

_None_



**References:**

_None_



**Fallacies:**

_None_


---

### PJD-02 

The service transforms a JSON text into a C++ representation using C++ containers (for arrays and objects) and primitive datatypes (for strings, numbers, boolean, null).


**Supported Requests:**

- [JLEX-02](JLEX.md#jlex-02)

**Supporting Items:**

_None_



**References:**

_None_



**Fallacies:**

_None_


---

### PJD-03 

The service parses all texts that conform to the JSON grammar.


**Supported Requests:**

- [JLEX-02](JLEX.md#jlex-02)

**Supporting Items:**

_None_



**References:**

_None_



**Fallacies:**

_None_


---

### PJD-04 

The service correctly parses 64-bit integers (exceeding the range defined in RFC8259).


**Supported Requests:**

- [JLEX-02](JLEX.md#jlex-02)

**Supporting Items:**

_None_



**References:**

_None_



**Fallacies:**

_None_

---
level: 1.1
normative: true
references:
        - type: cpp_test
          name: "Unicode (2/5);RFC 3629;ill-formed first byte"
          path: "tests/src/unit-unicode2.cpp"
        - type: cpp_test
          name: "Unicode (2/5);RFC 3629;UTF8-2 (xC2-xDF UTF8-tail);ill-formed: missing second byte"
          path: "tests/src/unit-unicode2.cpp"
        - type: cpp_test
          name: "Unicode (2/5);RFC 3629;UTF8-2 (xC2-xDF UTF8-tail);ill-formed: wrong second byte"
          path: "tests/src/unit-unicode2.cpp"
        - type: cpp_test
          name: "Unicode (2/5);RFC 3629;UTF8-3 (xE0 xA0-BF UTF8-tail);ill-formed: missing second byte"
          path: "tests/src/unit-unicode2.cpp"
        - type: cpp_test
          name: "Unicode (2/5);RFC 3629;UTF8-3 (xE0 xA0-BF UTF8-tail);ill-formed: missing third byte"
          path: "tests/src/unit-unicode2.cpp"
        - type: cpp_test
          name: "Unicode (2/5);RFC 3629;UTF8-3 (xE0 xA0-BF UTF8-tail);ill-formed: wrong second byte"
          path: "tests/src/unit-unicode2.cpp"
        - type: cpp_test
          name: "Unicode (2/5);RFC 3629;UTF8-3 (xE0 xA0-BF UTF8-tail);ill-formed: wrong third byte"
          path: "tests/src/unit-unicode2.cpp"
        - type: cpp_test
          name: "Unicode (2/5);RFC 3629;UTF8-3 (xE1-xEC UTF8-tail UTF8-tail);ill-formed: missing second byte"
          path: "tests/src/unit-unicode2.cpp"
        - type: cpp_test
          name: "Unicode (2/5);RFC 3629;UTF8-3 (xE1-xEC UTF8-tail UTF8-tail);ill-formed: missing third byte"
          path: "tests/src/unit-unicode2.cpp"
        - type: cpp_test
          name: "Unicode (2/5);RFC 3629;UTF8-3 (xE1-xEC UTF8-tail UTF8-tail);ill-formed: wrong second byte"
          path: "tests/src/unit-unicode2.cpp"
        - type: cpp_test
          name: "Unicode (2/5);RFC 3629;UTF8-3 (xE1-xEC UTF8-tail UTF8-tail);ill-formed: wrong third byte"
          path: "tests/src/unit-unicode2.cpp"
        - type: cpp_test
          name: "Unicode (2/5);RFC 3629;UTF8-3 (xED x80-9F UTF8-tail);ill-formed: missing second byte"
          path: "tests/src/unit-unicode2.cpp"
        - type: cpp_test
          name: "Unicode (2/5);RFC 3629;UTF8-3 (xED x80-9F UTF8-tail);ill-formed: missing third byte"
          path: "tests/src/unit-unicode2.cpp"
        - type: cpp_test
          name: "Unicode (2/5);RFC 3629;UTF8-3 (xED x80-9F UTF8-tail);ill-formed: wrong second byte"
          path: "tests/src/unit-unicode2.cpp"
        - type: cpp_test
          name: "Unicode (2/5);RFC 3629;UTF8-3 (xED x80-9F UTF8-tail);ill-formed: wrong third byte"
          path: "tests/src/unit-unicode2.cpp"
        - type: cpp_test
          name: "Unicode (2/5);RFC 3629;UTF8-3 (xEE-xEF UTF8-tail UTF8-tail);ill-formed: missing second byte"
          path: "tests/src/unit-unicode2.cpp"
        - type: cpp_test
          name: "Unicode (2/5);RFC 3629;UTF8-3 (xEE-xEF UTF8-tail UTF8-tail);ill-formed: missing third byte"
          path: "tests/src/unit-unicode2.cpp"
        - type: cpp_test
          name: "Unicode (2/5);RFC 3629;UTF8-3 (xEE-xEF UTF8-tail UTF8-tail);ill-formed: wrong second byte"
          path: "tests/src/unit-unicode2.cpp"
        - type: cpp_test
          name: "Unicode (2/5);RFC 3629;UTF8-3 (xEE-xEF UTF8-tail UTF8-tail);ill-formed: wrong third byte"
          path: "tests/src/unit-unicode2.cpp"
        - type: cpp_test
          name: "Unicode (3/5);RFC 3629;UTF8-4 (xF0 x90-BF UTF8-tail UTF8-tail);ill-formed: missing second byte"
          path: "tests/src/unit-unicode3.cpp"
        - type: cpp_test
          name: "Unicode (3/5);RFC 3629;UTF8-4 (xF0 x90-BF UTF8-tail UTF8-tail);ill-formed: missing third byte"
          path: "tests/src/unit-unicode3.cpp"
        - type: cpp_test
          name: "Unicode (3/5);RFC 3629;UTF8-4 (xF0 x90-BF UTF8-tail UTF8-tail);ill-formed: missing fourth byte"
          path: "tests/src/unit-unicode3.cpp"
        - type: cpp_test
          name: "Unicode (3/5);RFC 3629;UTF8-4 (xF0 x90-BF UTF8-tail UTF8-tail);ill-formed: wrong second byte"
          path: "tests/src/unit-unicode3.cpp"
        - type: cpp_test
          name: "Unicode (3/5);RFC 3629;UTF8-4 (xF0 x90-BF UTF8-tail UTF8-tail);ill-formed: wrong third byte"
          path: "tests/src/unit-unicode3.cpp"
        - type: cpp_test
          name: "Unicode (3/5);RFC 3629;UTF8-4 (xF0 x90-BF UTF8-tail UTF8-tail);ill-formed: wrong fourth byte"
          path: "tests/src/unit-unicode3.cpp"
        - type: cpp_test
          name: "Unicode (4/5);RFC 3629;UTF8-4 (xF1-F3 UTF8-tail UTF8-tail UTF8-tail);ill-formed: missing second byte"
          path: "tests/src/unit-unicode4.cpp"
        - type: cpp_test
          name: "Unicode (4/5);RFC 3629;UTF8-4 (xF1-F3 UTF8-tail UTF8-tail UTF8-tail);ill-formed: missing third byte"
          path: "tests/src/unit-unicode4.cpp"
        - type: cpp_test
          name: "Unicode (4/5);RFC 3629;UTF8-4 (xF1-F3 UTF8-tail UTF8-tail UTF8-tail);ill-formed: missing fourth byte"
          path: "tests/src/unit-unicode4.cpp"
        - type: cpp_test
          name: "Unicode (4/5);RFC 3629;UTF8-4 (xF1-F3 UTF8-tail UTF8-tail UTF8-tail);ill-formed: wrong second byte"
          path: "tests/src/unit-unicode4.cpp"
        - type: cpp_test
          name: "Unicode (4/5);RFC 3629;UTF8-4 (xF1-F3 UTF8-tail UTF8-tail UTF8-tail);ill-formed: wrong third byte"
          path: "tests/src/unit-unicode4.cpp"
        - type: cpp_test
          name: "Unicode (4/5);RFC 3629;UTF8-4 (xF1-F3 UTF8-tail UTF8-tail UTF8-tail);ill-formed: wrong fourth byte"
          path: "tests/src/unit-unicode4.cpp"
        - type: cpp_test
          name: "Unicode (5/5);RFC 3629;UTF8-4 (xF4 x80-8F UTF8-tail UTF8-tail);ill-formed: missing second byte"
          path: "tests/src/unit-unicode5.cpp"
        - type: cpp_test
          name: "Unicode (5/5);RFC 3629;UTF8-4 (xF4 x80-8F UTF8-tail UTF8-tail);ill-formed: missing third byte"
          path: "tests/src/unit-unicode5.cpp"
        - type: cpp_test
          name: "Unicode (5/5);RFC 3629;UTF8-4 (xF4 x80-8F UTF8-tail UTF8-tail);ill-formed: missing fourth byte"
          path: "tests/src/unit-unicode5.cpp"
        - type: cpp_test
          name: "Unicode (5/5);RFC 3629;UTF8-4 (xF4 x80-8F UTF8-tail UTF8-tail);ill-formed: wrong second byte"
          path: "tests/src/unit-unicode5.cpp"
        - type: cpp_test
          name: "Unicode (5/5);RFC 3629;UTF8-4 (xF4 x80-8F UTF8-tail UTF8-tail);ill-formed: wrong third byte"
          path: "tests/src/unit-unicode5.cpp"
        - type: cpp_test
          name: "Unicode (5/5);RFC 3629;UTF8-4 (xF4 x80-8F UTF8-tail UTF8-tail);ill-formed: wrong fourth byte"
          path: "tests/src/unit-unicode5.cpp"
evidence:
  type: "check_artifact_exists"
  configuration:
    check_amalgamation: exclude
    codeql: exclude
    dependency_review: exclude
    labeler: exclude
    publish_documentation: exclude
    test_trudag_extensions: exclude
    ubuntu: include
---

The service throws an exception on ill-formed UTF-8 data.
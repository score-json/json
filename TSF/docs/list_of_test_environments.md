## List of all unit-tests with test environments

    This list contains all unit-tests possibly running in this project.
    These tests are compiled from the source-code, where the individual unit-tests are arranged in TEST_CASEs containing possibly nested SECTIONs.
    To reflect the structure of the nested sections, nested lists are utilised, where the top-level list represents the list of TEST_CASEs. 

    It should be noted that not all unit-tests in a test-file are executed with every compiler-configuration.
    

### List of tests in file unit-32bit.cpp

* value_in_range_of trait
* 32bit
* BJData
    * parse errors
        * array
            * optimized array: negative size
            * optimized array: integer value overflow



All tests in this file were run in the following configurations:

* Linux-g++ with standard gnu++11


### List of tests in file unit-algorithms.cpp

* algorithms
    * non-modifying sequence operations
        * std::all_of
        * std::any_of
        * std::none_of
        * std::for_each
            * reading
            * writing
        * std::count
        * std::count_if
        * std::mismatch
        * std::equal
            * using operator==
            * using user-defined comparison
        * std::find
        * std::find_if
        * std::find_if_not
        * std::adjacent_find
    * modifying sequence operations
        * std::reverse
        * std::rotate
        * std::partition
    * sorting operations
        * std::sort
            * with standard comparison
            * with user-defined comparison
            * sorting an object
        * std::partial_sort
    * set operations
        * std::merge
        * std::set_difference
        * std::set_intersection
        * std::set_union
        * std::set_symmetric_difference
    * heap operations
    * iota
        * int
        * double
        * char
    * copy
        * copy without if
        * copy if
        * copy n
        * copy n chars



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-allocator.cpp

* bad_alloc
    * bad_alloc
* controlled bad_alloc
    * class json_value
        * json_value(value_t)
            * object
            * array
            * string
        * json_value(const string_t&)
    * class basic_json
        * basic_json(const CompatibleObjectType&)
        * basic_json(const CompatibleArrayType&)
        * basic_json(const typename string_t::value_type*)
        * basic_json(const typename string_t::value_type*)
* bad my_allocator::construct
    * my_allocator::construct doesn't forward



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-alt-string.cpp

* alternative string type
    * dump
    * parse
    * items
    * equality
    * JSON pointer
    * patch
    * diff
    * flatten



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-arrays.cpp

* accept
    * boundaries
* parse
    * whitespace



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-assert_macro.cpp

* JSON_ASSERT(x)
    * basic_json(first, second)



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-binary_formats.cpp

* Binary Formats
    * canada.json
    * twitter.json
    * citm_catalog.json
    * jeopardy.json
    * sample.json



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11

In the following configuration, however, some test-cases were skipped:

* 1 test case was skipped when using GNU 14.3.0 with standard gnu++20
* 1 test case was skipped when using GNU 11.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 8.5.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++14
* 1 test case was skipped when using GNU 4.9.3 with standard gnu++11
* 1 test case was skipped when using Clang 18.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 12.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 10.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 9.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++14
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++23
* 1 test case was skipped when using GNU 6.4.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++17
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++17
* 1 test case was skipped when using Clang 19.1.7 with standard gnu++11
* 1 test case was skipped when using Clang 17.0.6 with standard gnu++11
* 1 test case was skipped when using Intel 2021.5.0.20211109 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++23
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++17
* 1 test case was skipped when using GNU 7.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.4.0 with standard gnu++11
* 1 test case was skipped when using GNU 5.5.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++23
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++14
* 1 test case was skipped when using GNU 4.8.5 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 9.4.0 with standard gnu++11
* 1 test case was skipped when using Linux-c++ with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11


### List of tests in file unit-bjdata.cpp

* value_in_range_of trait
* BJData
    * binary_reader BJData LUT arrays are sorted
    * individual values
        * discarded
        * null
        * boolean
            * true
            * false
        * byte
            * 0..255 (uint8)
        * number
            * signed
                * -9223372036854775808..-2147483649 (int64)
                * -2147483648..-32769 (int32)
                * -32768..-129 (int16)
                * -9263 (int16)
                * -128..-1 (int8)
                * 0..127 (int8)
                * 128..255 (uint8)
                * 256..32767 (int16)
                * 32768..65535 (uint16)
                * 65536..2147483647 (int32)
                * 2147483648..4294967295 (uint32)
                * 4294967296..9223372036854775807 (int64)
                * 9223372036854775808..18446744073709551615 (uint64)
            * unsigned
                * 0..127 (int8)
                * 128..255 (uint8)
                * 256..32767 (int16)
                * 32768..65535 (uint16)
                * 65536..2147483647 (int32)
                * 2147483648..4294967295 (uint32)
                * 4294967296..9223372036854775807 (int64)
                * 9223372036854775808..18446744073709551615 (uint64)
            * float64
                * 3.1415925
            * half-precision float
                * simple half floats
                * errors
                    * no byte follows
                    * only one byte follows
            * half-precision float (edge cases)
                * exp = 0b00000
                    * 0 (0 00000 0000000000)
                    * -0 (1 00000 0000000000)
                    * 2**-24 (0 00000 0000000001)
                * exp = 0b11111
                    * infinity (0 11111 0000000000)
                    * -infinity (1 11111 0000000000)
                * other values from https://en.wikipedia.org/wiki/Half-precision_floating-point_format
                    * 1 (0 01111 0000000000)
                    * -2 (1 10000 0000000000)
                    * 65504 (0 11110 1111111111)
                * infinity
                * NaN
            * high-precision number
                * unsigned integer number
                * signed integer number
                * floating-point number
                * errors
        * string
            * N = 0..127
            * N = 128..255
            * N = 256..32767
            * N = 32768..65535
            * N = 65536..2147483647
        * binary
            * N = 0..127
            * N = 128..255
            * N = 256..32767
            * N = 32768..65535
            * N = 65536..2147483647
            * Other Serializations
                * No Count No Type
                * Yes Count No Type
    * array
        * empty
            * size=false type=false
            * size=true type=false
            * size=true type=true
        * [null]
            * size=false type=false
            * size=true type=false
            * size=true type=true
        * [1,2,3,4,5]
            * size=false type=false
            * size=true type=false
            * size=true type=true
        * [[[[]]]]
            * size=false type=false
            * size=true type=false
            * size=true type=true
        * array with int16_t elements
            * size=false type=false
            * size=true type=false
        * array with uint16_t elements
            * size=false type=false
            * size=true type=false
        * array with int32_t elements
            * size=false type=false
            * size=true type=false
    * object
        * empty
            * size=false type=false
            * size=true type=false
            * size=true type=true
        * {\
            * size=false type=false
            * size=true type=false
        * {\
            * size=false type=false
            * size=true type=false
            * size=true type=true ignore object type marker
* errors
    * strict mode
        * non-strict mode
        * strict mode
* SAX aborts
    * start_array()
    * start_object()
    * key() in object
    * start_array(len)
    * start_object(len)
    * key() in object with length
    * start_array() in ndarray _ArraySize_
    * number_integer() in ndarray _ArraySize_
    * key() in ndarray _ArrayType_
    * string() in ndarray _ArrayType_
    * key() in ndarray _ArrayData_
    * string() in ndarray _ArrayData_
    * string() in ndarray _ArrayType_
    * start_array() in ndarray _ArrayData_
* parsing values
    * strings
    * number
        * float
    * array
        * optimized version (length only)
        * optimized version (type and length)
        * optimized ndarray (type and vector-size as optimized 1D array)
        * optimized ndarray (type and vector-size ndarray with JData annotations)
        * optimized ndarray (type and vector-size as 1D array)
        * optimized ndarray (type and vector-size as size-optimized array)
        * invalid ndarray annotations remains as object
* parse errors
    * empty byte vector
    * char
        * eof after C byte
        * byte out of range
    * byte
        * parse bjdata markers in ubjson
    * strings
        * eof after S byte
        * invalid byte
        * parse bjdata markers in ubjson
    * array
        * optimized array: no size following type
        * optimized array: negative size
        * optimized array: integer value overflow
        * do not accept NTFZ markers in ndarray optimized type (with count)
        * do not accept NTFZ markers in ndarray optimized type (without count)
    * strings
    * sizes
    * parse bjdata markers as array size in ubjson
    * types
    * arrays
    * ndarrays
    * objects
* writing optimized values
    * integer
        * array of i
        * array of U
        * array of I
        * array of u
        * array of l
        * array of m
        * array of L
    * unsigned integer
        * array of i
        * array of U
        * array of I
        * array of u
        * array of l
        * array of m
        * array of L
        * array of M
* Universal Binary JSON Specification Examples 1
    * Null Value
    * No-Op Value
    * Boolean Types
    * Numeric Types
    * Char Type
    * Byte Type
    * String Type
        * English
        * Russian
        * Russian
    * Array Type
        * size=false type=false
        * size=true type=false
        * size=true type=true
    * Object Type
        * size=false type=false
        * size=true type=false
        * size=true type=true
    * Optimized Format
        * Array Example
            * No Optimization
            * Optimized with count
            * Optimized with type & count
        * Object Example
            * No Optimization
            * Optimized with count
            * Optimized with type & count
        * Special Cases (Null, No-Op and Boolean)
            * Array
            * Object
* all BJData first bytes
* BJData roundtrips
    * input from self-generated BJData files



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11

In the following configuration, however, some test-cases were skipped:

* 1 test case was skipped when using GNU 14.3.0 with standard gnu++20
* 1 test case was skipped when using GNU 11.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 8.5.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++14
* 1 test case was skipped when using GNU 4.9.3 with standard gnu++11
* 1 test case was skipped when using Clang 18.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 12.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 10.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 9.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++14
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++23
* 1 test case was skipped when using GNU 6.4.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++17
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++17
* 1 test case was skipped when using Clang 19.1.7 with standard gnu++11
* 1 test case was skipped when using Clang 17.0.6 with standard gnu++11
* 1 test case was skipped when using Intel 2021.5.0.20211109 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++23
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++17
* 1 test case was skipped when using GNU 7.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.4.0 with standard gnu++11
* 1 test case was skipped when using GNU 5.5.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++23
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++14
* 1 test case was skipped when using GNU 4.8.5 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 9.4.0 with standard gnu++11
* 1 test case was skipped when using Linux-c++ with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11


### List of tests in file unit-bson.cpp

* BSON
    * individual values not supported
        * null
        * boolean
            * true
            * false
        * number
        * float
        * string
        * array
    * keys containing code-point U+0000 cannot be serialized to BSON
    * string length must be at least 1
    * objects
        * empty object
        * non-empty object with bool
        * non-empty object with bool
        * non-empty object with double
        * non-empty object with string
        * non-empty object with null member
        * non-empty object with integer (32-bit) member
        * non-empty object with integer (64-bit) member
        * non-empty object with negative integer (32-bit) member
        * non-empty object with negative integer (64-bit) member
        * non-empty object with unsigned integer (64-bit) member
        * non-empty object with small unsigned integer member
        * non-empty object with object member
        * non-empty object with array member
        * non-empty object with non-empty array member
        * non-empty object with binary member
        * non-empty object with binary member with subtype
        * Some more complex document
    * Examples from https://bsonspec.org/faq.html
        * Example 1
        * Example 2
* BSON input/output_adapters
    * roundtrips
        * std::ostringstream
        * std::string
        * std::vector
* Incomplete BSON Input
    * Incomplete BSON Input 1
    * Incomplete BSON Input 2
    * Incomplete BSON Input 3
    * Incomplete BSON Input 4
    * Improve coverage
        * key
        * array
* Negative size of binary value
* Unsupported BSON input
* BSON numerical data
    * number
        * signed
            * std::int64_t: INT64_MIN .. INT32_MIN-1
            * signed std::int32_t: INT32_MIN .. INT32_MAX
            * signed std::int64_t: INT32_MAX+1 .. INT64_MAX
        * unsigned
            * unsigned std::uint64_t: 0 .. INT32_MAX
            * unsigned std::uint64_t: INT32_MAX+1 .. INT64_MAX
            * unsigned std::uint64_t: INT64_MAX+1 .. UINT64_MAX
* BSON roundtrips
    * reference files



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11

In the following configuration, however, some test-cases were skipped:

* 1 test case was skipped when using GNU 14.3.0 with standard gnu++20
* 1 test case was skipped when using GNU 11.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 8.5.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++14
* 1 test case was skipped when using GNU 4.9.3 with standard gnu++11
* 1 test case was skipped when using Clang 18.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 12.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 10.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 9.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++14
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++23
* 1 test case was skipped when using GNU 6.4.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++17
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++17
* 1 test case was skipped when using Clang 19.1.7 with standard gnu++11
* 1 test case was skipped when using Clang 17.0.6 with standard gnu++11
* 1 test case was skipped when using Intel 2021.5.0.20211109 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++23
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++17
* 1 test case was skipped when using GNU 7.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.4.0 with standard gnu++11
* 1 test case was skipped when using GNU 5.5.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++23
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++14
* 1 test case was skipped when using GNU 4.8.5 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 9.4.0 with standard gnu++11
* 1 test case was skipped when using Linux-c++ with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11


### List of tests in file unit-byte_container_with_subtype.cpp

* byte_container_with_subtype
    * empty container
    * subtyped container
    * comparisons



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-byte_order_mark.cpp

* accept
    * UTF-8
        * single BOM
        * multiple BOM
        * unexpected BOM
    * Other byte-order marks
        * UTF-16
        * UTF-32
* parse
    * UTF-8
        * multiple BOM
        * unexpected BOM
    * other BOM
        * UTF-16
        * UTF-32



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-capacity.cpp

* capacity
    * empty()
        * boolean
            * result of empty
            * definition of empty
        * string
            * result of empty
            * definition of empty
        * array
            * empty array
                * result of empty
                * definition of empty
            * filled array
                * result of empty
                * definition of empty
        * object
            * empty object
                * result of empty
                * definition of empty
            * filled object
                * result of empty
                * definition of empty
        * number (integer)
            * result of empty
            * definition of empty
        * number (unsigned)
            * result of empty
            * definition of empty
        * number (float)
            * result of empty
            * definition of empty
        * null
            * result of empty
            * definition of empty
    * size()
        * boolean
            * result of size
            * definition of size
        * string
            * result of size
            * definition of size
        * array
            * empty array
                * result of size
                * definition of size
            * filled array
                * result of size
                * definition of size
        * object
            * empty object
                * result of size
                * definition of size
            * filled object
                * result of size
                * definition of size
        * number (integer)
            * result of size
            * definition of size
        * number (unsigned)
            * result of size
            * definition of size
        * number (float)
            * result of size
            * definition of size
        * null
            * result of size
            * definition of size
    * max_size()
        * boolean
            * result of max_size
        * string
            * result of max_size
        * array
            * empty array
                * result of max_size
            * filled array
                * result of max_size
        * object
            * empty object
                * result of max_size
            * filled object
                * result of max_size
        * number (integer)
            * result of max_size
        * number (unsigned)
            * result of max_size
        * number (float)
            * result of max_size
        * null
            * result of max_size



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-cbor.cpp

* CBOR
    * individual values
        * discarded
        * NaN
        * Infinity
        * null
        * boolean
            * true
            * false
        * number
            * signed
                * -9223372036854775808..-4294967297
                * -4294967296..-65537
                * -65536..-257
                * -9263 (int 16)
                * -256..-24
                * -24..-1
                * 0..23
                * 24..255
                * 256..65535
                * 65536..4294967295
                * 4294967296..4611686018427387903
                * -32768..-129 (int 16)
            * unsigned
                * 0..23 (Integer)
                * 24..255 (one-byte uint8_t)
                * 256..65535 (two-byte uint16_t)
                * 65536..4294967295 (four-byte uint32_t)
                * 4294967296..4611686018427387903 (eight-byte uint64_t)
            * double-precision float
                * 3.1415925
            * single-precision float
                * 0.5
                * 0.0
                * -0.0
                * 100.0
                * 200.0
                * 3.40282e+38(max float)
                * -3.40282e+38(lowest float)
                * 1 + 3.40282e+38(more than max float)
                * -1 - 3.40282e+38(less than lowest float)
            * half-precision float (edge cases)
                * errors
                    * no byte follows
                    * only one byte follows
                * exp = 0b00000
                    * 0 (0 00000 0000000000)
                    * -0 (1 00000 0000000000)
                    * 2**-24 (0 00000 0000000001)
                * exp = 0b11111
                    * infinity (0 11111 0000000000)
                    * -infinity (1 11111 0000000000)
                * other values from https://en.wikipedia.org/wiki/Half-precision_floating-point_format
                    * 1 (0 01111 0000000000)
                    * -2 (1 10000 0000000000)
                    * 65504 (0 11110 1111111111)
                * infinity
                * NaN
        * string
            * N = 0..23
            * N = 24..255
            * N = 256..65535
            * N = 65536..4294967295
        * array
            * empty
            * [null]
            * [1,2,3,4,5]
            * [[[[]]]]
            * array with uint16_t elements
            * array with uint32_t elements
        * object
            * empty
            * {\
            * {\
            * object with uint8_t elements
            * object with uint16_t elements
            * object with uint32_t elements
        * binary
            * N = 0..23
            * N = 24..255
            * N = 256..65535
            * N = 65536..4294967295
            * indefinite size
            * binary in array
            * binary in object
            * SAX callback with binary
    * additional deserialization
        * 0x5b (byte array)
        * 0x7b (string)
        * 0x9b (array)
        * 0xbb (map)
    * errors
        * empty byte vector
        * too short byte vector
        * unsupported bytes
            * concrete examples
            * all unsupported bytes
        * invalid string in map
        * strict mode
            * non-strict mode
            * strict mode
    * SAX aborts
        * start_array(len)
        * start_object(len)
        * key()
* single CBOR roundtrip
    * sample.json
        * roundtrips
            * std::ostringstream
            * std::string
* CBOR regressions
    * fuzz test results
* CBOR roundtrips
    * input from flynn
* all CBOR first bytes
* examples from RFC 7049 Appendix A
    * numbers
    * simple values
    * strings
    * byte arrays
    * arrays
    * objects
* Tagged values
    * 0xC6..0xD4
    * 0xD8 - 1 byte follows
        * success
        * missing byte after tag
    * 0xD9 - 2 byte follow
        * success
        * missing byte after tag
    * 0xDA - 4 bytes follow
        * success
        * missing bytes after tag
    * 0xDB - 8 bytes follow
        * success
        * missing byte after tag
    * tagged binary



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11

In the following configuration, however, some test-cases were skipped:

* 1 test case was skipped when using GNU 14.3.0 with standard gnu++20
* 1 test case was skipped when using GNU 11.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 8.5.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++14
* 1 test case was skipped when using GNU 4.9.3 with standard gnu++11
* 1 test case was skipped when using Clang 18.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 12.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 10.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 9.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++14
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++23
* 1 test case was skipped when using GNU 6.4.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++17
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++17
* 1 test case was skipped when using Clang 19.1.7 with standard gnu++11
* 1 test case was skipped when using Clang 17.0.6 with standard gnu++11
* 1 test case was skipped when using Intel 2021.5.0.20211109 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++23
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++17
* 1 test case was skipped when using GNU 7.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.4.0 with standard gnu++11
* 1 test case was skipped when using GNU 5.5.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++23
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++14
* 1 test case was skipped when using GNU 4.8.5 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 9.4.0 with standard gnu++11
* 1 test case was skipped when using Linux-c++ with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11


### List of tests in file unit-class_const_iterator.cpp

* const_iterator class
    * construction
        * constructor
            * null
            * object
            * array
        * copy assignment
        * copy constructor from non-const iterator
            * create from uninitialized iterator
            * create from initialized iterator
    * initialization
        * set_begin
            * null
            * object
            * array
        * set_end
            * null
            * object
            * array
    * element access
        * operator*
            * null
            * number
            * object
            * array
        * operator->
            * null
            * number
            * object
            * array
    * increment/decrement
        * post-increment
            * null
            * number
            * object
            * array
        * pre-increment
            * null
            * number
            * object
            * array
        * post-decrement
            * null
            * number
            * object
            * array
        * pre-decrement
            * null
            * number
            * object
            * array



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-class_iterator.cpp

* iterator class
    * construction
        * constructor
            * null
            * object
            * array
        * copy assignment
    * initialization
        * set_begin
            * null
            * object
            * array
        * set_end
            * null
            * object
            * array
    * element access
        * operator*
            * null
            * number
            * object
            * array
        * operator->
            * null
            * number
            * object
            * array
    * increment/decrement
        * post-increment
            * null
            * number
            * object
            * array
        * pre-increment
            * null
            * number
            * object
            * array
        * post-decrement
            * null
            * number
            * object
            * array
        * pre-decrement
            * null
            * number
            * object
            * array
    * equality-preserving
        * post-increment
            * primitive_iterator_t
            * iter_impl
            * json_reverse_iterator
        * post-decrement
            * primitive_iterator_t
            * iter_impl
            * json_reverse_iterator
    * cert-dcl21-cpp
        * post-increment
            * primitive_iterator_t
            * iter_impl
            * json_reverse_iterator
        * post-decrement
            * primitive_iterator_t
            * iter_impl
            * json_reverse_iterator



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-class_lexer.cpp

* lexer class
    * scan
        * structural characters
        * literal names
        * numbers
        * whitespace
    * token_type_name
    * parse errors on first character
    * very large string
    * fail on comments
    * ignore comments



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-class_parser.cpp

* parser class
    * parse
        * null
        * true
        * false
        * array
            * empty array
            * nonempty array
        * object
            * empty object
            * nonempty object
        * string
            * errors
                * additional test for null byte
            * escaped
        * number
            * integers
                * without exponent
                * with exponent
                * edge cases
                * over the edge cases
            * floating-point
                * without exponent
                * with exponent
            * overflow
            * invalid numbers
    * accept
        * null
        * true
        * false
        * array
            * empty array
            * nonempty array
        * object
            * empty object
            * nonempty object
        * string
            * errors
            * escaped
        * number
            * integers
                * without exponent
                * with exponent
                * edge cases
                * over the edge cases
            * floating-point
                * without exponent
                * with exponent
            * overflow
            * invalid numbers
    * parse errors
    * parse errors (accept)
    * tests found by mutate++
    * callback function
        * filter nothing
        * filter everything
        * filter specific element
        * filter object in array
        * filter specific events
            * first closing event
        * special cases
    * constructing from contiguous containers
        * from std::vector
        * from std::array
        * from array
        * from char literal
        * from std::string
        * from std::initializer_list
        * from std::valarray
    * improve test coverage
        * parser with callback
        * SAX parser
            * } without value
            * } with value
            * second key
            * ] without value
            * ] with value
            * float
            * false
            * null
            * true
            * unsigned
            * integer
            * string
    * error messages for comments



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-class_parser_core.cpp

* parser class - core
    * parse
        * null
        * true
        * false
        * array
            * empty array
            * nonempty array
        * object
            * empty object
            * nonempty object
        * string
            * errors
                * additional test for null byte
            * escaped
        * number
            * integers
                * without exponent
                * with exponent
                * edge cases
                * over the edge cases
            * floating-point
                * without exponent
                * with exponent
            * overflow
            * invalid numbers
    * accept
        * null
        * true
        * false
        * array
            * empty array
            * nonempty array
        * object
            * empty object
            * nonempty object
        * string
            * errors
            * escaped
        * number
            * integers
                * without exponent
                * with exponent
                * edge cases
                * over the edge cases
            * floating-point
                * without exponent
                * with exponent
            * overflow
            * invalid numbers
    * parse errors
    * parse errors (accept)
    * tests found by mutate++



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-class_parser_diagnostic_positions.cpp

* parser class
    * parse
        * null
        * true
        * false
        * array
            * empty array
            * nonempty array
        * object
            * empty object
            * nonempty object
        * string
            * errors
                * additional test for null byte
            * escaped
        * number
            * integers
                * without exponent
                * with exponent
                * edge cases
                * over the edge cases
            * floating-point
                * without exponent
                * with exponent
            * overflow
            * invalid numbers
    * accept
        * null
        * true
        * false
        * array
            * empty array
            * nonempty array
        * object
            * empty object
            * nonempty object
        * string
            * errors
            * escaped
        * number
            * integers
                * without exponent
                * with exponent
                * edge cases
                * over the edge cases
            * floating-point
                * without exponent
                * with exponent
            * overflow
            * invalid numbers
    * parse errors
    * parse errors (accept)
    * tests found by mutate++
    * callback function
        * filter nothing
        * filter everything
        * filter specific element
        * filter object in array
        * filter specific events
            * first closing event
        * special cases
    * constructing from contiguous containers
        * from std::vector
        * from std::array
        * from array
        * from char literal
        * from std::string
        * from std::initializer_list
        * from std::valarray
    * improve test coverage
        * parser with callback
        * SAX parser
            * } without value
            * } with value
            * second key
            * ] without value
            * ] with value
            * float
            * false
            * null
            * true
            * unsigned
            * integer
            * string
    * error messages for comments
    * with callback
        * filter nothing
        * filter element
    * without callback
    * retrieve start position and end position
        * for object
        * for array
        * for array with objects
        * for two levels of nesting objects
        * for simple types
            * no nested
                * with callback
                * without callback
            * string type
            * number type
            * boolean type
            * null type
        * with leading whitespace and newlines around root JSON



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-comparison.cpp

* lexicographical comparison operators
    * types
        * comparison: less
        * comparison: 3-way
    * values
        * compares unordered
        * compares unordered (inverse)
        * comparison: equal
        * comparison: not equal
        * comparison: less
        * comparison: less than or equal equal
        * comparison: greater than
        * comparison: greater than or equal
        * comparison: 3-way
    * parser callback regression
        * filter specific element



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++20
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++20
* GNU 11.5.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++20
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++20
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++20
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* Clang 18.1.8 with standard gnu++20
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 12.5.0 with standard gnu++20
* GNU 10.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++20
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* GNU 9.5.0 with standard gnu++11
* GNU 9.5.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++20
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 19.1.7 with standard gnu++20
* Clang 17.0.6 with standard gnu++11
* Clang 17.0.6 with standard gnu++20
* Intel 2021.5.0.20211109 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++20
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++20
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++20
* Linux-c++ with standard gnu++11
* Linux-c++ with standard gnu++20
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++20


### List of tests in file unit-concepts.cpp

* concepts
    * container requirements for json
    * class json
        * DefaultConstructible
        * MoveConstructible
        * CopyConstructible
        * MoveAssignable
        * CopyAssignable
        * Destructible
        * StandardLayoutType
    * class iterator
        * CopyConstructible
        * CopyAssignable
        * Destructible
        * Swappable



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-constructor1.cpp

* constructors
    * create an empty value with a given type
        * null
        * discarded
        * object
        * array
        * boolean
        * string
        * number_integer
        * number_unsigned
        * number_float
        * binary
    * create a null object (implicitly)
        * no parameter
    * create a null object (explicitly)
        * parameter
    * create an object (explicit)
        * empty object
        * filled object
    * create an object (implicit)
        * std::map<json::string_t, json>
        * std::map<std::string, std::string> #600
        * std::map<const char*, json>
        * std::multimap<json::string_t, json>
        * std::unordered_map<json::string_t, json>
        * std::unordered_multimap<json::string_t, json>
        * associative container literal
    * create an array (explicit)
        * empty array
        * filled array
    * create an array (implicit)
        * std::list<json>
        * std::pair
        * std::pair with discarded values
        * std::tuple
        * std::tuple with discarded values
        * std::pair/tuple/array failures
        * std::forward_list<json>
        * std::array<json, 6>
        * std::valarray<int>
        * std::valarray<double>
        * std::vector<json>
        * std::deque<json>
        * std::set<json>
        * std::unordered_set<json>
        * sequence container literal
    * create a string (explicit)
        * empty string
        * filled string
    * create a string (implicit)
        * std::string
        * char[]
        * const char*
        * string literal
    * create a boolean (explicit)
        * empty boolean
        * filled boolean (true)
        * filled boolean (false)
        * from std::vector<bool>::reference
        * from std::vector<bool>::const_reference
    * create a binary (explicit)
        * empty binary
        * filled binary
    * create an integer number (explicit)
        * uninitialized value
        * initialized value
    * create an integer number (implicit)
        * short
        * unsigned short
        * int
        * unsigned int
        * long
        * unsigned long
        * long long
        * unsigned long long
        * int8_t
        * int16_t
        * int32_t
        * int64_t
        * int_fast8_t
        * int_fast16_t
        * int_fast32_t
        * int_fast64_t
        * int_least8_t
        * int_least16_t
        * int_least32_t
        * int_least64_t
        * uint8_t
        * uint16_t
        * uint32_t
        * uint64_t
        * uint_fast8_t
        * uint_fast16_t
        * uint_fast32_t
        * uint_fast64_t
        * uint_least8_t
        * uint_least16_t
        * uint_least32_t
        * uint_least64_t
        * integer literal without suffix
        * integer literal with u suffix
        * integer literal with l suffix
        * integer literal with ul suffix
        * integer literal with ll suffix
        * integer literal with ull suffix
    * create a floating-point number (explicit)
        * uninitialized value
        * initialized value
        * NaN
        * infinity
    * create a floating-point number (implicit)
        * float
        * double
        * long double
        * floating-point literal without suffix
        * integer literal with f suffix
        * integer literal with l suffix
    * create a container (array or object) from an initializer list
        * empty initializer list
            * explicit
            * implicit
        * one element
            * array
                * explicit
                * implicit
            * object
                * explicit
                * implicit
            * string
                * explicit
                * implicit
            * boolean
                * explicit
                * implicit
            * number (integer)
                * explicit
                * implicit
            * number (unsigned)
                * explicit
                * implicit
            * number (floating-point)
                * explicit
                * implicit
        * more elements
            * explicit
            * implicit
        * implicit type deduction
            * object
            * array
        * explicit type deduction
            * empty object
            * object
            * object with error
            * empty array
            * array
        * move from initializer_list
            * string
                * constructor with implicit types (array)
                * constructor with implicit types (object)
                * constructor with implicit types (object key)
            * array
                * constructor with implicit types (array)
                * constructor with implicit types (object)
                * assignment with implicit types (array)
                * assignment with implicit types (object)
            * object
                * constructor with implicit types (array)
                * constructor with implicit types (object)
                * assignment with implicit types (array)
                * assignment with implicit types (object)
            * json
                * constructor with implicit types (array)
                * constructor with implicit types (object)
                * assignment with implicit types (array)
                * assignment with implicit types (object)
    * create an array of n copies of a given value
        * cnt = 0
        * cnt = 1
        * cnt = 3
    * create a JSON container from an iterator range
        * object
            * json(begin(), end())
            * json(begin(), begin())
            * construct from subrange
            * incompatible iterators
        * array
            * json(begin(), end())
            * json(begin(), begin())
            * construct from subrange
            * incompatible iterators
        * other values
            * construct with two valid iterators
                * null
                * string
                * number (boolean)
                * number (integer)
                * number (unsigned)
                * number (floating point)
                * binary
            * construct with two invalid iterators
                * string
                * number (boolean)
                * number (integer)
                * number (integer)
                * number (floating point)



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-constructor2.cpp

* other constructors and destructor
    * copy constructor
        * object
        * array
        * null
        * boolean
        * string
        * number (integer)
        * number (unsigned)
        * number (floating-point)
        * binary
    * move constructor
    * copy assignment
        * object
        * array
        * null
        * boolean
        * string
        * number (integer)
        * number (unsigned)
        * number (floating-point)
        * binary
    * destructor
        * object
        * array
        * string



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-convenience.cpp

* convenience functions
    * type name as string
    * string escape
    * string concat
        * std::string
        * alt_string_iter
        * alt_string_data



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-conversions.cpp

* value conversion
    * get an object (explicit)
        * json::object_t
        * std::map<json::string_t, json>
        * std::multimap<json::string_t, json>
        * std::unordered_map<json::string_t, json>
        * std::unordered_multimap<json::string_t, json>
        * exception in case of a non-object type
    * get an object (explicit, get_to)
        * json::object_t
        * std::map<json::string_t, json>
        * std::multimap<json::string_t, json>
        * std::unordered_map<json::string_t, json>
        * std::unordered_multimap<json::string_t, json>
    * get an object (implicit)
        * json::object_t
        * std::map<json::string_t, json>
        * std::multimap<json::string_t, json>
        * std::unordered_map<json::string_t, json>
        * std::unordered_multimap<json::string_t, json>
    * get an array (explicit)
        * json::array_t
        * std::list<json>
        * std::forward_list<json>
        * std::vector<json>
            * reserve is called on containers that supports it
        * built-in arrays
        * std::deque<json>
        * exception in case of a non-array type
    * get an array (explicit, get_to)
        * json::array_t
        * std::valarray<json>
        * std::list<json>
        * std::forward_list<json>
        * std::vector<json>
        * built-in arrays
        * built-in arrays: 2D
        * built-in arrays: 3D
        * built-in arrays: 4D
        * std::deque<json>
    * get an array (implicit)
        * json::array_t
        * std::list<json>
        * std::forward_list<json>
        * std::vector<json>
        * std::deque<json>
    * get a string (explicit)
        * string_t
        * std::string
        * std::string_view
        * exception in case of a non-string type
        * exception in case of a non-string type using string_view
    * get a string (explicit, get_to)
        * string_t
        * std::string
        * std::string_view
    * get null (explicit)
    * get a string (implicit)
        * string_t
        * std::string_view
        * std::string
    * get a boolean (explicit)
        * boolean_t
        * uint8_t
        * bool
        * exception in case of a non-number type
    * get a boolean (implicit)
        * boolean_t
        * bool
    * get an integer number (explicit)
        * number_integer_t
        * number_unsigned_t
        * short
        * unsigned short
        * int
        * unsigned int
        * long
        * unsigned long
        * long long
        * unsigned long long
        * int8_t
        * int16_t
        * int32_t
        * int64_t
        * int8_fast_t
        * int16_fast_t
        * int32_fast_t
        * int64_fast_t
        * int8_least_t
        * int16_least_t
        * int32_least_t
        * int64_least_t
        * uint8_t
        * uint16_t
        * uint32_t
        * uint64_t
        * uint8_fast_t
        * uint16_fast_t
        * uint32_fast_t
        * uint64_fast_t
        * uint8_least_t
        * uint16_least_t
        * uint32_least_t
        * uint64_least_t
        * exception in case of a non-number type
    * get an integer number (implicit)
        * number_integer_t
        * number_unsigned_t
        * short
        * unsigned short
        * int
        * unsigned int
        * long
        * unsigned long
        * long long
        * unsigned long long
        * int8_t
        * int16_t
        * int32_t
        * int64_t
        * int8_fast_t
        * int16_fast_t
        * int32_fast_t
        * int64_fast_t
        * int8_least_t
        * int16_least_t
        * int32_least_t
        * int64_least_t
        * uint8_t
        * uint16_t
        * uint32_t
        * uint64_t
        * uint8_fast_t
        * uint16_fast_t
        * uint32_fast_t
        * uint64_fast_t
        * uint8_least_t
        * uint16_least_t
        * uint32_least_t
        * uint64_least_t
    * get a floating-point number (explicit)
        * number_float_t
        * float
        * double
        * exception in case of a non-string type
    * get a floating-point number (implicit)
        * number_float_t
        * float
        * double
    * get a binary value (explicit)
        * binary_t
        * get_binary()
            * non-const
            * non-const
        * exception in case of a non-string type
    * get a binary value (implicit)
        * binary_t
    * get an enum
    * more involved conversions
        * object-like STL containers
            * std::map
            * std::unordered_map
            * std::multimap
            * std::unordered_multimap
            * exception in case of a non-object type
        * array-like STL containers
            * std::list
            * std::forward_list
            * std::array
                * std::array is larger than JSON
                * std::array is smaller than JSON
            * std::valarray
            * std::vector
            * std::deque
            * std::set
            * std::unordered_set
            * std::map (array of pairs)
                * superfluous entries
            * std::unordered_map (array of pairs)
                * superfluous entries
            * exception in case of a non-object type
* JSON to enum mapping
    * enum class
    * traditional enum
* std::filesystem::path
    * ascii
    * utf-8
* std::optional
    * null
    * string
    * bool
    * number
    * array
    * object



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++14
* GNU 9.4.0 with standard gnu++17
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++14
* GNU 9.4.0 with standard gnu++17
* GNU 11.5.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++14
* GNU 11.5.0 with standard gnu++17
* GNU 8.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++14
* GNU 8.5.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* Clang 20.1.8 with standard gnu++17
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++14
* GNU 13.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++14
* GNU 9.4.0 with standard gnu++17
* GNU 4.9.3 with standard gnu++11
* GNU 4.9.3 with standard gnu++14
* Clang 18.1.8 with standard gnu++11
* Clang 18.1.8 with standard gnu++14
* Clang 18.1.8 with standard gnu++17
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* GNU 14.3.0 with standard gnu++17
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++14
* GNU 13.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* Clang 20.1.8 with standard gnu++17
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 12.5.0 with standard gnu++14
* GNU 12.5.0 with standard gnu++17
* GNU 10.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++14
* GNU 10.5.0 with standard gnu++17
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++14
* GNU 13.3.0 with standard gnu++17
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++14
* GNU 9.4.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* Clang 20.1.8 with standard gnu++17
* GNU 9.5.0 with standard gnu++11
* GNU 9.5.0 with standard gnu++14
* GNU 9.5.0 with standard gnu++17
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++14
* GNU 9.4.0 with standard gnu++17
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 6.4.0 with standard gnu++14
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 19.1.7 with standard gnu++14
* Clang 19.1.7 with standard gnu++17
* Clang 17.0.6 with standard gnu++11
* Clang 17.0.6 with standard gnu++14
* Clang 17.0.6 with standard gnu++17
* Intel 2021.5.0.20211109 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++14
* Intel 2021.5.0.20211109 with standard gnu++17
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 7.5.0 with standard gnu++14
* GNU 7.5.0 with standard gnu++17
* GNU 13.4.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++14
* GNU 13.4.0 with standard gnu++17
* GNU 5.5.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* GNU 4.8.5 with standard gnu++14
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++14
* GNU 9.4.0 with standard gnu++17
* Linux-c++ with standard gnu++11
* Linux-c++ with standard gnu++14
* Linux-c++ with standard gnu++17
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++14
* GNU 13.3.0 with standard gnu++17


### List of tests in file unit-custom-base-class.cpp

* JSON Node Metadata
    * type int
    * type vector<int>
    * copy ctor
    * move ctor
    * move assign
    * copy assign
    * type unique_ptr<int>
    * type vector<int> in json array
* JSON Visit Node



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-deserialization.cpp

* deserialization
    * successful deserialization
        * stream
        * string literal
        * string_t
        * operator<<
        * operator>>
        * user-defined string literal
    * unsuccessful deserialization
        * stream
        * string
        * operator<<
        * operator>>
        * user-defined string literal
    * contiguous containers
        * directly
            * from std::vector
            * from std::array
            * from array
            * from chars
            * from std::string
            * from std::initializer_list
            * empty container
        * via iterator range
            * from std::vector
            * from std::array
            * from array
            * from std::string
            * from std::initializer_list
            * from std::valarray
            * with empty range
            * iterator_input_adapter advances iterators correctly
        * error cases
            * case 1
            * case 2
            * case 3
            * case 4
            * case 5
            * case 6
            * case 7
            * case 8
            * case 9
            * case 10
            * case 11
            * case 12
            * case 13
            * case 14
            * case 15
            * case 16
    * ignoring byte-order marks
        * BOM only
        * BOM and content
        * 2 byte of BOM
        * 1 byte of BOM
        * variations
        * preserve state after parsing
    * SAX and early abort
    * JSON Lines
        * Example file
        * Example file without trailing newline
* deserialization of different character types (ASCII)
* deserialization of different character types (UTF-8)
* deserialization of different character types (UTF-16)
* deserialization of different character types (UTF-32)



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++20
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++20
* GNU 11.5.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++20
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++20
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++20
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* Clang 18.1.8 with standard gnu++20
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 12.5.0 with standard gnu++20
* GNU 10.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++20
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* GNU 9.5.0 with standard gnu++11
* GNU 9.5.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++20
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 19.1.7 with standard gnu++20
* Clang 17.0.6 with standard gnu++11
* Clang 17.0.6 with standard gnu++20
* Intel 2021.5.0.20211109 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++20
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++20
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++20
* Linux-c++ with standard gnu++11
* Linux-c++ with standard gnu++20
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++20


### List of tests in file unit-diagnostic-positions-only.cpp

* Better diagnostics with positions only
    * invalid type
    * invalid type without positions



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-diagnostic-positions.cpp

* Better diagnostics with positions
    * invalid type
    * invalid type without positions



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-diagnostics.cpp

* Better diagnostics
    * empty JSON Pointer
    * invalid type
    * missing key
    * array index out of range
    * array index at wrong type
    * wrong iterator
    * JSON Pointer escaping
    * Parse error
    * Wrong type in update()
* Regression tests for extended diagnostics
    * Regression test for https://github.com/nlohmann/json/pull/2562#pullrequestreview-574858448
    * Regression test for https://github.com/nlohmann/json/pull/2562/files/380a613f2b5d32425021129cd1f371ddcfd54ddf#r563259793
    * Regression test for issue #2838 - Assertion failure when inserting into arrays with JSON_DIAGNOSTICS set
    * Regression test for issue #2962 - JSON_DIAGNOSTICS assertion for ordered_json
    * Regression test for issue #3007 - Parent pointers properly set when using update()
    * Regression test for issue #3032 - Yet another assertion failure when inserting into arrays with JSON_DIAGNOSTICS set
    * Regression test for issue #3915 - JSON_DIAGNOSTICS trigger assertion



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-disabled_exceptions.cpp

* Tests with disabled exceptions
    * issue #2824 - encoding of json::exception::what()



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-element_access1.cpp

* element access 1
    * array
        * access specified element with bounds checking
            * access within bounds
            * access outside bounds
            * access on non-array type
                * null
                * boolean
                * string
                * object
                * number (integer)
                * number (unsigned)
                * number (floating-point)
        * front and back
        * access specified element
            * access within bounds
            * access on non-array type
                * null
                    * standard tests
                    * implicit transformation to properly filled array
                * boolean
                * string
                * object
                * number (integer)
                * number (unsigned)
                * number (floating-point)
        * remove specified element
            * remove element by index
            * remove element by iterator
                * erase(begin())
                * erase(begin(), end())
                * erase(begin(), begin())
                * erase at offset
                * erase subrange
                * different arrays
            * remove element by index in non-array type
                * null
                * boolean
                * string
                * object
                * number (integer)
                * number (unsigned)
                * number (floating-point)
    * other values
        * front and back
            * null
            * string
            * number (boolean)
            * number (integer)
            * number (unsigned)
            * number (floating point)
        * erase with one valid iterator
            * null
            * string
            * number (boolean)
            * number (integer)
            * number (unsigned)
            * number (floating point)
            * binary
        * erase with one invalid iterator
            * string
            * number (boolean)
            * number (integer)
            * number (unsigned)
            * number (floating point)
        * erase with two valid iterators
            * null
            * string
            * number (boolean)
            * number (integer)
            * number (unsigned)
            * number (floating point)
            * binary
        * erase with two invalid iterators
            * string
            * number (boolean)
            * number (integer)
            * number (unsigned)
            * number (floating point)



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-element_access2.cpp

* element access 2
    * object
        * access specified element with bounds checking
            * access within bounds
            * access outside bounds
            * access on non-object type
                * null
                * boolean
                * string
                * array
                * number (integer)
                * number (unsigned)
                * number (floating-point)
        * access specified element with default value
            * given a key
                * access existing value
                * access non-existing value
                * access on non-object type
                    * null
                    * boolean
                    * string
                    * array
                    * number (integer)
                    * number (unsigned)
                    * number (floating-point)
            * given a JSON pointer
                * access existing value
                * access on non-object type
                    * null
                    * boolean
                    * string
                    * array
                    * number (integer)
                    * number (unsigned)
                    * number (floating-point)
        * non-const operator[]
        * front and back
        * access specified element
            * access within bounds
            * access within bounds (string_view)
            * access on non-object type
                * null
                * boolean
                * string
                * array
                * number (integer)
                * number (unsigned)
                * number (floating-point)
        * remove specified element
            * remove element by key
            * remove element by key (string_view)
            * remove element by iterator
                * erase(begin())
                * erase(begin(), end())
                * erase(begin(), begin())
                * erase at offset
                * erase subrange
                * different objects
            * remove element by key in non-object type
                * null
                * boolean
                * string
                * array
                * number (integer)
                * number (floating-point)
        * find an element in an object
            * existing element
            * nonexisting element
            * all types
                * null
                * string
                * object
                * array
                * boolean
                * number (integer)
                * number (unsigned)
                * number (floating-point)
        * count keys in an object
            * existing element
            * nonexisting element
            * all types
                * null
                * string
                * object
                * array
                * boolean
                * number (integer)
                * number (unsigned)
                * number (floating-point)
        * check existence of key in an object
            * existing element
            * nonexisting element
            * all types
                * null
                * string
                * object
                * array
                * boolean
                * number (integer)
                * number (unsigned)
                * number (floating-point)
* element access 2 (throwing tests)
    * object
        * access specified element with default value
            * given a JSON pointer
                * access non-existing value
* element access 2 (additional value() tests)
    * deduced ValueType
        * literal key
        * const char * key
        * const char(&)[] key
        * string_t/object_t::key_type key
        * std::string_view key
    * explicit ValueType
        * literal key
        * const char * key
        * const char(&)[] key
        * string_t/object_t::key_type key
        * std::string_view key



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++14
* GNU 9.4.0 with standard gnu++17
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++14
* GNU 9.4.0 with standard gnu++17
* GNU 11.5.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++14
* GNU 11.5.0 with standard gnu++17
* GNU 8.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++14
* GNU 8.5.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* Clang 20.1.8 with standard gnu++17
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++14
* GNU 13.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++14
* GNU 9.4.0 with standard gnu++17
* GNU 4.9.3 with standard gnu++11
* GNU 4.9.3 with standard gnu++14
* Clang 18.1.8 with standard gnu++11
* Clang 18.1.8 with standard gnu++14
* Clang 18.1.8 with standard gnu++17
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* GNU 14.3.0 with standard gnu++17
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++14
* GNU 13.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* Clang 20.1.8 with standard gnu++17
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 12.5.0 with standard gnu++14
* GNU 12.5.0 with standard gnu++17
* GNU 10.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++14
* GNU 10.5.0 with standard gnu++17
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++14
* GNU 13.3.0 with standard gnu++17
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++14
* GNU 9.4.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* Clang 20.1.8 with standard gnu++17
* GNU 9.5.0 with standard gnu++11
* GNU 9.5.0 with standard gnu++14
* GNU 9.5.0 with standard gnu++17
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++14
* GNU 9.4.0 with standard gnu++17
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 6.4.0 with standard gnu++14
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 19.1.7 with standard gnu++14
* Clang 19.1.7 with standard gnu++17
* Clang 17.0.6 with standard gnu++11
* Clang 17.0.6 with standard gnu++14
* Clang 17.0.6 with standard gnu++17
* Intel 2021.5.0.20211109 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++14
* Intel 2021.5.0.20211109 with standard gnu++17
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 7.5.0 with standard gnu++14
* GNU 7.5.0 with standard gnu++17
* GNU 13.4.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++14
* GNU 13.4.0 with standard gnu++17
* GNU 5.5.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* GNU 4.8.5 with standard gnu++14
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++14
* GNU 9.4.0 with standard gnu++17
* Linux-c++ with standard gnu++11
* Linux-c++ with standard gnu++14
* Linux-c++ with standard gnu++17
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++14
* GNU 13.3.0 with standard gnu++17


### List of tests in file unit-hash.cpp

* hash<nlohmann::json>
* hash<nlohmann::ordered_json>



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-inspection.cpp

* object inspection
    * convenience type checker
        * object
        * array
        * null
        * boolean
        * string
        * number (integer)
        * number (unsigned)
        * number (floating-point)
        * binary
        * discarded
    * serialization
        * no indent / indent=-1
        * indent=0
        * indent=1, space='\t'
        * indent=4
        * indent=x
        * dump and floating-point numbers
        * dump and small floating-point numbers
        * dump and non-ASCII characters
        * dump with ensure_ascii and non-ASCII characters
        * full Unicode escaping to ASCII
            * parsing yields the same JSON value
            * dumping yields the same JSON text
        * serialization of discarded element
        * check that precision is reset after serialization
    * round trips
    * return the type of the object (explicit)
        * null
        * object
        * array
        * boolean
        * string
        * number (integer)
        * number (unsigned)
        * number (floating-point)
    * return the type of the object (implicit)
        * null
        * object
        * array
        * boolean
        * string
        * number (integer)
        * number (unsigned)
        * number (floating-point)
        * binary



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-items.cpp

* iterator_wrapper
    * object
        * value
        * reference
        * const value
        * const reference
    * const object
        * value
        * reference
        * const value
        * const reference
    * array
        * value
        * reference
        * const value
        * const reference
    * const array
        * value
        * reference
        * const value
        * const reference
    * primitive
        * value
        * reference
        * const value
        * const reference
    * const primitive
        * value
        * reference
        * const value
        * const reference
* items()
    * object
        * value
        * reference
        * const value
        * const reference
        * structured bindings
    * const object
        * value
        * reference
        * const value
        * const reference
    * array
        * value
        * reference
        * const value
        * const reference
    * const array
        * value
        * reference
        * const value
        * const reference
    * primitive
        * value
        * reference
        * const value
        * const reference
    * const primitive
        * value
        * reference
        * const value
        * const reference



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++17
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++17
* GNU 11.5.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++17
* GNU 8.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++17
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++17
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* Clang 18.1.8 with standard gnu++17
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++17
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 12.5.0 with standard gnu++17
* GNU 10.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++17
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++17
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++17
* GNU 9.5.0 with standard gnu++11
* GNU 9.5.0 with standard gnu++17
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++17
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 19.1.7 with standard gnu++17
* Clang 17.0.6 with standard gnu++11
* Clang 17.0.6 with standard gnu++17
* Intel 2021.5.0.20211109 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++17
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 7.5.0 with standard gnu++17
* GNU 13.4.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++17
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++17
* Linux-c++ with standard gnu++11
* Linux-c++ with standard gnu++17
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++17


### List of tests in file unit-iterators1.cpp

* iterators 1
    * basic behavior
        * uninitialized
        * boolean
            * json + begin/end
            * const json + begin/end
            * json + cbegin/cend
            * const json + cbegin/cend
            * json + rbegin/rend
            * json + crbegin/crend
            * const json + crbegin/crend
            * additional tests
                * !(begin != begin)
                * !(end != end)
                * begin < end
                * begin <= end
                * end > begin
                * end >= begin
                * end == end
                * end <= end
                * begin == begin
                * begin <= begin
                * begin >= begin
                * !(begin == end)
                * begin != end
                * begin+1 == end
                * begin == end-1
                * begin != end+1
                * end != end+1
                * begin+1 != begin+2
                * begin+1 < begin+2
                * begin+1 <= begin+2
                * end+1 != end+2
            * key/value
        * string
            * json + begin/end
            * const json + begin/end
            * json + cbegin/cend
            * const json + cbegin/cend
            * json + rbegin/rend
            * json + crbegin/crend
            * const json + crbegin/crend
            * key/value
        * array
            * json + begin/end
            * const json + begin/end
            * json + cbegin/cend
            * const json + cbegin/cend
            * json + rbegin/rend
            * json + crbegin/crend
            * const json + crbegin/crend
            * key/value
        * object
            * json + begin/end
            * const json + begin/end
            * json + cbegin/cend
            * const json + cbegin/cend
            * json + rbegin/rend
            * json + crbegin/crend
            * const json + crbegin/crend
            * key/value
        * number (integer)
            * json + begin/end
            * const json + begin/end
            * json + cbegin/cend
            * const json + cbegin/cend
            * json + rbegin/rend
            * json + crbegin/crend
            * const json + crbegin/crend
            * key/value
        * number (unsigned)
            * json + begin/end
            * const json + begin/end
            * json + cbegin/cend
            * const json + cbegin/cend
            * json + rbegin/rend
            * json + crbegin/crend
            * const json + crbegin/crend
            * key/value
        * number (float)
            * json + begin/end
            * const json + begin/end
            * json + cbegin/cend
            * const json + cbegin/cend
            * json + rbegin/rend
            * json + crbegin/crend
            * const json + crbegin/crend
            * key/value
        * null
            * json + begin/end
            * const json + begin/end
            * json + cbegin/cend
            * const json + cbegin/cend
            * json + rbegin/rend
            * json + crbegin/crend
            * const json + crbegin/crend
            * key/value
    * conversion from iterator to const iterator
        * boolean
        * string
        * array
        * object
        * number (integer)
        * number (unsigned)
        * number (float)
        * null



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-iterators2.cpp

* iterators 2
    * iterator comparisons
    * iterator arithmetic
        * addition and subtraction
            * object
            * array
            * null
            * value
        * subscript operator
            * object
            * array
            * null
            * value
    * reverse iterator comparisons
    * reverse iterator arithmetic
        * addition and subtraction
            * object
            * array
            * null
            * value
        * subscript operator
            * object
            * array
            * null
            * value
    * ranges
        * concepts
        * algorithms
            * copy
            * find_if
        * views
            * reverse
            * transform



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++20
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++20
* GNU 11.5.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++20
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++20
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++20
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* Clang 18.1.8 with standard gnu++20
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 12.5.0 with standard gnu++20
* GNU 10.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++20
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* GNU 9.5.0 with standard gnu++11
* GNU 9.5.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++20
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 19.1.7 with standard gnu++20
* Clang 17.0.6 with standard gnu++11
* Clang 17.0.6 with standard gnu++20
* Intel 2021.5.0.20211109 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++20
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++20
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++20
* Linux-c++ with standard gnu++11
* Linux-c++ with standard gnu++20
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++20


### List of tests in file unit-iterators3.cpp

* checking forward-iterators



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++14
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++14
* GNU 11.5.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++14
* GNU 8.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++14
* GNU 4.9.3 with standard gnu++11
* GNU 4.9.3 with standard gnu++14
* Clang 18.1.8 with standard gnu++11
* Clang 18.1.8 with standard gnu++14
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 12.5.0 with standard gnu++14
* GNU 10.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++14
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.5.0 with standard gnu++11
* GNU 9.5.0 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++14
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 6.4.0 with standard gnu++14
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 19.1.7 with standard gnu++14
* Clang 17.0.6 with standard gnu++11
* Clang 17.0.6 with standard gnu++14
* Intel 2021.5.0.20211109 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++14
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 7.5.0 with standard gnu++14
* GNU 13.4.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++14
* GNU 5.5.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* GNU 4.8.5 with standard gnu++14
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++14
* Linux-c++ with standard gnu++11
* Linux-c++ with standard gnu++14
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++14


### List of tests in file unit-json_patch.cpp

* JSON patch
    * examples from RFC 6902
        * 4. Operations
        * 4.1 add
        * 4.2 remove
        * A.1. Adding an Object Member
        * A.2. Adding an Array Element
        * A.3. Removing an Object Member
        * A.4. Removing an Array Element
        * A.5. Replacing a Value
        * A.6. Moving a Value
        * A.7. Moving a Value
        * A.8. Testing a Value: Success
        * A.9. Testing a Value: Error
        * A.10. Adding a Nested Member Object
        * A.11. Ignoring Unrecognized Elements
        * A.12. Adding to a Nonexistent Target
        * A.14. Escape Ordering
        * A.15. Comparing Strings and Numbers
        * A.16. Adding an Array Value
    * own examples
        * add
            * add to the root element
            * add to end of the array
        * copy
        * replace
        * documentation GIF
    * errors
        * unknown operation
            * not an array
            * not an array of objects
            * missing 'op'
            * non-string 'op'
            * invalid operation
        * add
            * missing 'path'
            * non-string 'path'
            * missing 'value'
            * invalid array index
        * remove
            * missing 'path'
            * non-string 'path'
            * nonexisting target location (array)
            * nonexisting target location (object)
            * root element as target location
        * replace
            * missing 'path'
            * non-string 'path'
            * missing 'value'
            * nonexisting target location (array)
            * nonexisting target location (object)
        * move
            * missing 'path'
            * non-string 'path'
            * missing 'from'
            * non-string 'from'
            * nonexisting from location (array)
            * nonexisting from location (object)
        * copy
            * missing 'path'
            * non-string 'path'
            * missing 'from'
            * non-string 'from'
            * nonexisting from location (array)
            * nonexisting from location (object)
        * test
            * missing 'path'
            * non-string 'path'
            * missing 'value'
    * Examples from jsonpatch.com
        * Simple Example
        * Operations
            * add
            * remove
            * replace
            * copy
            * move
            * test
    * Examples from bruth.github.io/jsonpatch-js
        * add
        * remove
        * replace
        * move
        * copy
        * copy
    * Tests from github.com/json-patch/json-patch-tests



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-json_pointer.cpp

* JSON pointers
    * errors
        * array index error
    * examples from RFC 6901
        * nonconst access
        * const access
        * user-defined string literal
    * array access
        * nonconst access
        * const access
    * flatten
    * string representation
    * conversion
        * array
        * object
    * empty, push, pop and parent
    * operators
    * equality comparison
        * exceptions
    * less-than comparison
    * usable as map key
    * backwards compatibility and mixing
        * equality comparison



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++20
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++20
* GNU 11.5.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++20
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++20
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++20
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* Clang 18.1.8 with standard gnu++20
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 12.5.0 with standard gnu++20
* GNU 10.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++20
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* GNU 9.5.0 with standard gnu++11
* GNU 9.5.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++20
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 19.1.7 with standard gnu++20
* Clang 17.0.6 with standard gnu++11
* Clang 17.0.6 with standard gnu++20
* Intel 2021.5.0.20211109 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++20
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++20
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++20
* Linux-c++ with standard gnu++11
* Linux-c++ with standard gnu++20
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++20


### List of tests in file unit-large_json.cpp

* tests on very large JSONs
    * issue #1419 - Segmentation fault (stack overflow) due to unbounded recursion



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-literals.cpp

* accept
    * unicode
    * capitalisation
        * true
        * null
        * false
    * illegal literals
        * nil
        * truth
        * const
        * none
        * self
        * super
        * this
        * undefined
    * illegal literal numbers
        * inf
        * infinity
        * NaN
* parse
    * values
    * whitespace
    * capitalisation
        * true
        * null
        * false
    * illegal literals
        * nil
        * truth
        * const
        * none
        * self
        * super
        * this
        * undefined
    * illegal literal numbers
        * inf
        * infinity
        * NaN



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-locale-cpp.cpp

* locale-dependent test (LC_NUMERIC=C)
    * check if locale is properly set
    * parsing
    * SAX parsing
* locale-dependent test (LC_NUMERIC=de_DE)
    * check if locale is properly set
    * parsing
    * SAX parsing



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-merge_patch.cpp

* JSON Merge Patch
    * examples from RFC 7396
        * Section 1
        * Section 3
        * Appendix A
            * Example 1
            * Example 2
            * Example 3
            * Example 4
            * Example 5
            * Example 6
            * Example 7
            * Example 8
            * Example 9
            * Example 10
            * Example 11
            * Example 12
            * Example 13
            * Example 14
            * Example 15



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-meta.cpp

* version information
    * meta()



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-modifiers.cpp

* modifiers
    * clear()
        * boolean
        * string
        * array
            * empty array
            * filled array
        * object
            * empty object
            * filled object
        * binary
            * empty binary
            * filled binary
        * number (integer)
        * number (unsigned)
        * number (float)
        * null
    * push_back()
        * to array
            * json&&
                * null
                * array
                * other type
            * const json&
                * null
                * array
                * other type
        * to object
            * null
            * object
            * other type
        * with initializer_list
            * null
            * array
            * object
    * emplace_back()
        * to array
            * null
            * array
            * multiple values
        * other type
    * emplace()
        * to object
            * null
            * object
        * other type
    * operator+=
        * to array
            * json&&
                * null
                * array
                * other type
            * const json&
                * null
                * array
                * other type
        * to object
            * null
            * object
            * other type
        * with initializer_list
            * null
            * array
            * object
    * insert()
        * value at position
            * insert before begin()
            * insert in the middle
            * insert before end()
        * rvalue at position
            * insert before begin()
            * insert in the middle
            * insert before end()
        * copies at position
            * insert before begin()
            * insert in the middle
            * insert before end()
            * insert nothing (count = 0)
        * range for array
            * proper usage
            * empty range
            * invalid iterators
        * range for object
            * proper usage
            * empty range
            * invalid iterators
        * initializer list at position
            * insert before begin()
            * insert in the middle
            * insert before end()
        * invalid iterator
        * non-array type
    * update()
        * non-recursive (default)
            * const reference
                * proper usage
                * wrong types
            * iterator range
                * proper usage
                * empty range
                * invalid iterators
        * recursive
            * const reference
                * extend object
                * replace object
    * swap()
        * json
            * member swap
            * nonmember swap
        * array_t
            * array_t type
            * non-array_t type
        * object_t
            * object_t type
            * non-object_t type
        * string_t
            * string_t type
            * non-string_t type
        * binary_t
            * binary_t type
            * binary_t::container_type type
            * non-binary_t type



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-msgpack.cpp

* MessagePack
    * individual values
        * discarded
        * null
        * boolean
            * true
            * false
        * number
            * signed
                * -32..-1 (negative fixnum)
                * 0..127 (positive fixnum)
                * 128..255 (int 8)
                * 256..65535 (int 16)
                * 65536..4294967295 (int 32)
                * 4294967296..9223372036854775807 (int 64)
                * -128..-33 (int 8)
                * -9263 (int 16)
                * -32768..-129 (int 16)
                * -32769..-2147483648
                * -9223372036854775808..-2147483649 (int 64)
            * unsigned
                * 0..127 (positive fixnum)
                * 128..255 (uint 8)
                * 256..65535 (uint 16)
                * 65536..4294967295 (uint 32)
                * 4294967296..18446744073709551615 (uint 64)
            * float
                * 3.1415925
                * 1.0
                * 128.128
        * string
            * N = 0..31
            * N = 32..255
            * N = 256..65535
            * N = 65536..4294967295
        * array
            * empty
            * [null]
            * [1,2,3,4,5]
            * [[[[]]]]
            * array 16
            * array 32
        * object
            * empty
            * {\
            * {\
            * map 16
            * map 32
        * extension
            * N = 0..255
            * N = 256..65535
            * N = 65536..4294967295
        * binary
            * N = 0..255
            * N = 256..65535
            * N = 65536..4294967295
    * from float32
    * errors
        * empty byte vector
        * too short byte vector
        * unexpected end inside int with stream
        * misuse wchar for binary
        * unsupported bytes
            * concrete examples
            * all unsupported bytes
        * invalid string in map
        * strict mode
            * non-strict mode
            * strict mode
    * SAX aborts
        * start_array(len)
        * start_object(len)
        * key()
* single MessagePack roundtrip
    * sample.json
        * roundtrips
            * std::ostringstream
            * std::string
* MessagePack roundtrips
    * input from msgpack-python



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11

In the following configuration, however, some test-cases were skipped:

* 1 test case was skipped when using GNU 14.3.0 with standard gnu++20
* 1 test case was skipped when using GNU 11.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 8.5.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++14
* 1 test case was skipped when using GNU 4.9.3 with standard gnu++11
* 1 test case was skipped when using Clang 18.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 12.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 10.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 9.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++14
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++23
* 1 test case was skipped when using GNU 6.4.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++17
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++17
* 1 test case was skipped when using Clang 19.1.7 with standard gnu++11
* 1 test case was skipped when using Clang 17.0.6 with standard gnu++11
* 1 test case was skipped when using Intel 2021.5.0.20211109 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++23
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++17
* 1 test case was skipped when using GNU 7.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.4.0 with standard gnu++11
* 1 test case was skipped when using GNU 5.5.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++23
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++14
* 1 test case was skipped when using GNU 4.8.5 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 9.4.0 with standard gnu++11
* 1 test case was skipped when using Linux-c++ with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11


### List of tests in file unit-no-mem-leak-on-adl-serialize.cpp

* check_for_mem_leak_on_adl_to_json-1
* check_for_mem_leak_on_adl_to_json-2
* check_for_mem_leak_on_adl_to_json-2



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-noexcept.cpp

* noexcept
    * nothrow-copy-constructible exceptions



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-numbers.cpp

* accept
    * exponents
        * U+0425
        * U+0436
        * leading zeroes
    * operators
        * plus
        * minus
        * brackets
        * factorial
        * multiplication
        * division
        * comma
    * whitespace
        * space
        * tab
        * new line
        * Carriage return
        * Leading and tailing
            * space
            * tab
            * newline
            * Carriage return
            * Mixed
    * Leading zeroes
    * bases
        * Octal
        * Hexadecimal
* parse
    * exponents
        * U+0425
        * U+0436
        * leading zeroes
        * leading plus
        * Capitalisation
    * operators
        * plus
        * minus
        * brackets
        * factorial
        * multiplication
        * division
        * comma
    * trailing zeroes
    * whitespace
    * invalid whitespace
        * space
        * tab
        * new line
        * Carriage return
    * Leading zeroes
    * Precision



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-objects.cpp

* accept
    * names
        * numbers
        * arrays
        * objects
        * literals
        * strings
            * control characters
            * unicode
            * escaped UTF-16 surrogates
    * whitespace
        * empty object
        * non-empty object
    * member separator
* parse
    * whitespace
        * empty object
        * non-empty object
    * member separator
    * names
        * numbers
        * arrays
        * objects
        * literals
    * duplicate names
        * 100,000 identical keys
        * first and last key duplicate



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-ordered_json.cpp

* ordered_json



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-ordered_map.cpp

* ordered_map
    * constructor
        * constructor from iterator range
        * copy assignment
    * at
        * with Key&&
        * with const Key&&
        * with string literal
    * operator[]
        * with Key&&
        * with const Key&&
        * with string literal
    * erase
        * with Key&&
        * with const Key&&
        * with string literal
        * with iterator
        * with iterator pair
            * range in the middle
            * range at the beginning
            * range at the end
    * count
    * find
    * insert
        * const value_type&
        * value_type&&



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-pointer_access.cpp

* pointer access
    * pointer access to object_t
    * pointer access to const object_t
    * pointer access to array_t
    * pointer access to const array_t
    * pointer access to string_t
    * pointer access to const string_t
    * pointer access to boolean_t
    * pointer access to const boolean_t
    * pointer access to number_integer_t
    * pointer access to const number_integer_t
    * pointer access to number_unsigned_t
    * pointer access to const number_unsigned_t
    * pointer access to number_float_t
    * pointer access to const number_float_t
    * pointer access to const binary_t
    * pointer access to const binary_t



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-readme.cpp

* README



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11

In the following configuration, however, some test-cases were skipped:

* 1 test case was skipped when using GNU 14.3.0 with standard gnu++20
* 1 test case was skipped when using GNU 11.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 8.5.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++14
* 1 test case was skipped when using GNU 4.9.3 with standard gnu++11
* 1 test case was skipped when using Clang 18.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 12.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 10.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 9.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++14
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++23
* 1 test case was skipped when using GNU 6.4.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++17
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++17
* 1 test case was skipped when using Clang 19.1.7 with standard gnu++11
* 1 test case was skipped when using Clang 17.0.6 with standard gnu++11
* 1 test case was skipped when using Intel 2021.5.0.20211109 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++23
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++17
* 1 test case was skipped when using GNU 7.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.4.0 with standard gnu++11
* 1 test case was skipped when using GNU 5.5.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++23
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++14
* 1 test case was skipped when using GNU 4.8.5 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 9.4.0 with standard gnu++11
* 1 test case was skipped when using Linux-c++ with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11


### List of tests in file unit-reference_access.cpp

* reference access
    * reference access to object_t
    * const reference access to const object_t
    * reference access to array_t
    * reference access to string_t
    * reference access to boolean_t
    * reference access to number_integer_t
    * reference access to number_unsigned_t
    * reference access to number_float_t



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-regression1.cpp

* regression tests 1
    * issue #60 - Double quotation mark is not parsed correctly
        * escape_doublequote
    * issue #70 - Handle infinity and NaN cases
        * NAN value
        * infinity
        * NAN value
        * infinity
    * pull request #71 - handle enum type
    * issue #76 - dump() / parse() not idempotent
    * issue #82 - lexer::get_number return NAN
    * issue #89 - nonstandard integer type
    * issue #93 reverse_iterator operator inheritance problem
    * issue #100 - failed to iterator json object with reverse_iterator
    * issue #101 - binary string causes numbers to be dumped as hex
    * issue #111 - subsequent unicode chars
    * issue #144 - implicit assignment to std::string fails
    * issue #146 - character following a surrogate pair is skipped
    * issue #171 - Cannot index by key of type static constexpr const char*
    * issue #186 miloyip/nativejson-benchmark: floating-point parsing
    * issue #228 - double values are serialized with commas as decimal points
    * issue #378 - locale-independent num-to-str
    * issue #379 - locale-independent str-to-num
    * issue #233 - Can't use basic_json::iterator as a base iterator for std::move_iterator
    * issue #235 - ambiguous overload for 'push_back' and 'operator+='
    * issue #269 - diff generates incorrect patch when removing multiple array elements
    * issue #283 - value() does not work with _json_pointer types
    * issue #304 - Unused variable warning
    * issue #306 - Parsing fails without space at end of file
    * issue #310 - make json_benchmarks no longer working in 2.0.4
    * issue #323 - add nested object capabilities to pointers
    * issue #329 - serialized value not always can be parsed
    * issue #360 - Loss of precision when serializing <double>
    * issue #366 - json::parse on failed stream gets stuck
    * issue #367 - calling stream at EOF
    * issue #367 - behavior of operator>> should more closely resemble that of built-in overloads
        * (empty)
        * (whitespace)
        * one value
        * one value + whitespace
        * whitespace + one value
        * three values
        * literals without whitespace
        * example from #529
        * second example from #529
    * issue #389 - Integer-overflow (OSS-Fuzz issue 267)
    * issue #380 - bug in overflow detection when parsing integers
    * issue #405 - Heap-buffer-overflow (OSS-Fuzz issue 342)
    * issue #407 - Heap-buffer-overflow (OSS-Fuzz issue 343)
    * issue #408 - Heap-buffer-overflow (OSS-Fuzz issue 344)
    * issue #411 - Heap-buffer-overflow (OSS-Fuzz issue 366)
    * issue #412 - Heap-buffer-overflow (OSS-Fuzz issue 367)
    * issue #414 - compare with literal 0)
    * issue #416 - Use-of-uninitialized-value (OSS-Fuzz issue 377)
    * issue #452 - Heap-buffer-overflow (OSS-Fuzz issue 585)
    * issue #454 - doubles are printed as integers
    * issue #464 - VS2017 implicit to std::string conversion fix
    * issue #465 - roundtrip error while parsing 1000000000000000010E5
    * issue #473 - inconsistent behavior in conversion to array type
        * std::vector
        * std::list
        * std::forward_list
    * issue #486 - json::value_t can't be a map's key type in VC++ 2015
    * issue #494 - conversion from vector<bool> to json fails to build
    * issue #504 - assertion error (OSS-Fuzz 856)
    * issue #512 - use of overloaded operator '<=' is ambiguous
    * issue #575 - heap-buffer-overflow (OSS-Fuzz 1400)
    * issue #600 - how does one convert a map in Json back to std::map?
        * example 1
        * example 2
    * issue #602 - BOM not skipped when using json:parse(iterator)
    * issue #702 - conversion from valarray<double> to json fails to build
        * original example
        * full example
    * issue #367 - Behavior of operator>> should more closely resemble that of built-in overloads.
        * example 1
    * issue #714 - throw std::ios_base::failure exception when failbit set to true
    * issue #805 - copy constructor is used with std::initializer_list constructor.
    * issue #838 - incorrect parse error with binary data in keys
    * issue #843 - converting to array not working
    * issue #894 - invalid RFC6902 copy operation succeeds
    * issue #961 - incorrect parsing of indefinite length CBOR strings
    * issue #962 - Timeout (OSS-Fuzz 6034)
    * issue #971 - Add a SAX parser - late bug
    * issue #972 - Segmentation fault on G++ when trying to assign json string literal to custom json type
    * issue #977 - Assigning between different json types
* regression tests, exceptions dependent
    * issue #1340 - eof not set on exhausted input stream



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++17
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++17
* GNU 11.5.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++17
* GNU 8.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++17
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++17
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* Clang 18.1.8 with standard gnu++17
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++17
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 12.5.0 with standard gnu++17
* GNU 10.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++17
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++17
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++17
* GNU 9.5.0 with standard gnu++11
* GNU 9.5.0 with standard gnu++17
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++17
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 19.1.7 with standard gnu++17
* Clang 17.0.6 with standard gnu++11
* Clang 17.0.6 with standard gnu++17
* Intel 2021.5.0.20211109 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++17
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 7.5.0 with standard gnu++17
* GNU 13.4.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++17
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++17
* Linux-c++ with standard gnu++11
* Linux-c++ with standard gnu++17
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++17


### List of tests in file unit-regression2.cpp

* regression tests 2
    * issue #1001 - Fix memory leak during parser callback
    * issue #1021 - to/from_msgpack only works with standard typization
    * issue #1045 - Using STL algorithms with JSON containers with expected results?
    * issue #1292 - Serializing std::variant causes stack overflow
    * issue #1299 - compile error in from_json converting to container 
    * issue #1445 - buffer overflow in dumping invalid utf-8 strings
        * a bunch of -1, ensure_ascii=true
        * a bunch of -2, ensure_ascii=false
        * test case in issue #1445
    * issue #1447 - Integer Overflow (OSS-Fuzz 12506)
    * issue #1708 - minimum value of int64_t can be outputted
    * issue #1727 - Contains with non-const lvalue json_pointer picks the wrong overload
    * issue #1647 - compile error when deserializing enum if both non-default from_json and non-member operator== exists for other type
    * issue #1715 - json::from_cbor does not respect allow_exceptions = false when input is string literal
        * string literal
        * string array
        * std::string
    * issue #1805 - A pair<T1, T2> is json constructible only if T1 and T2 are json constructible
    * issue #1825 - A tuple<Args..> is json constructible only if all T in Args are json constructible
    * issue #1983 - JSON patch diff for op=add formation is not as per standard (RFC 6902)
    * issue #2067 - cannot serialize binary data to text JSON
    * PR #2181 - regression bug with lvalue
    * issue #2293 - eof doesn't cause parsing to stop
    * issue #2315 - json.update and vector<pair>does not work with ordered_json
    * issue #2330 - ignore_comment=true fails on multiple consecutive lines starting with comments
    * issue #2546 - parsing containers of std::byte
    * issue #2574 - Deserialization to std::array, std::pair, and std::tuple with non-default constructable types fails
        * std::array
        * std::pair
        * std::tuple
    * issue #4530 - Serialization of empty tuple
    * issue #2865 - ASAN detects memory leaks
    * issue #2824 - encoding of json::exception::what()
    * issue #2825 - Properly constrain the basic_json conversion operator
    * issue #2958 - Inserting in unordered json using a pointer retains the leading slash
    * issue #2982 - to_{binary format} does not provide a mechanism for specifying a custom allocator for the returned type
    * issue #3070 - Version 3.10.3 breaks backward-compatibility with 3.10.2 
    * issue #3077 - explicit constructor with default does not compile
    * issue #3108 - ordered_json doesn't support range based erase
    * issue #3343 - json and ordered_json are not interchangeable
    * issue #3171 - if class is_constructible from std::string wrong from_json overload is being selected, compilation failed
    * issue #3312 - Parse to custom class from unordered_json breaks on G++11.2.0 with C++20
    * issue #3428 - Error occurred when converting nlohmann::json to std::any
    * issue #3204 - ambiguous regression
    * issue #3333 - Ambiguous conversion from nlohmann::basic_json<> to custom class
    * issue #3810 - ordered_json doesn't support construction from C array of custom type



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++17
* GNU 9.4.0 with standard gnu++20
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++17
* GNU 9.4.0 with standard gnu++20
* GNU 11.5.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++17
* GNU 11.5.0 with standard gnu++20
* GNU 8.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++17
* GNU 13.3.0 with standard gnu++20
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++17
* GNU 9.4.0 with standard gnu++20
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* Clang 18.1.8 with standard gnu++17
* Clang 18.1.8 with standard gnu++20
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* GNU 14.3.0 with standard gnu++20
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++17
* GNU 13.3.0 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* GNU 14.3.0 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 12.5.0 with standard gnu++17
* GNU 12.5.0 with standard gnu++20
* GNU 10.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++17
* GNU 10.5.0 with standard gnu++20
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++17
* GNU 13.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++17
* GNU 9.4.0 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* Clang 20.1.8 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* GNU 9.5.0 with standard gnu++11
* GNU 9.5.0 with standard gnu++17
* GNU 9.5.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++17
* GNU 9.4.0 with standard gnu++20
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 19.1.7 with standard gnu++17
* Clang 19.1.7 with standard gnu++20
* Clang 17.0.6 with standard gnu++11
* Clang 17.0.6 with standard gnu++17
* Clang 17.0.6 with standard gnu++20
* Intel 2021.5.0.20211109 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++17
* Intel 2021.5.0.20211109 with standard gnu++20
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 7.5.0 with standard gnu++17
* GNU 13.4.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++17
* GNU 13.4.0 with standard gnu++20
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++17
* GNU 9.4.0 with standard gnu++20
* Linux-c++ with standard gnu++11
* Linux-c++ with standard gnu++17
* Linux-c++ with standard gnu++20
* GNU 13.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++17
* GNU 13.3.0 with standard gnu++20


### List of tests in file unit-serialization.cpp

* serialization
    * operator<<
        * no given width
        * given width
        * given fill
    * operator>>
        * no given width
        * given width
        * given fill
    * dump
        * invalid character
        * ending with incomplete character
        * unexpected character
        * U+FFFD Substitution of Maximal Subparts
    * to_string
* serialization for extreme integer values
    * minimum
    * maximum
* dump with binary values
    * normal
    * pretty-printed



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-strings.cpp

* accept
    * noncharacter code positions
    * overlong sequences
        * Examples of an overlong ASCII character
        * Maximum overlong sequences
        * Overlong representation of the NUL character
    * malformed sequences
        * Unexpected continuation bytes
        * Lonely start characters
        * Sequences with last continuation byte missing
        * Concatenation of incomplete sequences
        * Impossible bytes
* Unicode
    * escaped unicode
    * unescaped unicode
    * escaped utf-16 surrogates
        * well-formed
        * ill-formed
* parse
    * whitespace



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11

In the following configuration, however, some test-cases were skipped:

* 1 test case was skipped when using GNU 14.3.0 with standard gnu++20
* 1 test case was skipped when using GNU 11.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 8.5.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++14
* 1 test case was skipped when using GNU 4.9.3 with standard gnu++11
* 1 test case was skipped when using Clang 18.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 12.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 10.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 9.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++14
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++23
* 1 test case was skipped when using GNU 6.4.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++17
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++17
* 1 test case was skipped when using Clang 19.1.7 with standard gnu++11
* 1 test case was skipped when using Clang 17.0.6 with standard gnu++11
* 1 test case was skipped when using Intel 2021.5.0.20211109 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++23
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++17
* 1 test case was skipped when using GNU 7.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.4.0 with standard gnu++11
* 1 test case was skipped when using GNU 5.5.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++23
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++14
* 1 test case was skipped when using GNU 4.8.5 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 9.4.0 with standard gnu++11
* 1 test case was skipped when using Linux-c++ with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11


### List of tests in file unit-testsuites.cpp

* compliance tests from json.org
    * expected failures
    * no failures with trailing literals (relaxed)
    * expected passes
* compliance tests from nativejson-benchmark
    * doubles
    * strings
    * roundtrip
* test suite from json-test-suite
    * read all sample.json
* json.org examples
    * 1.json
    * 2.json
    * 3.json
    * 4.json
    * 5.json
    * FILE 1.json
    * FILE 2.json
    * FILE 3.json
    * FILE 4.json
    * FILE 5.json
* RFC 8259 examples
    * 7. Strings
    * 8.3 String Comparison
    * 13 Examples
* nst's JSONTestSuite
    * test_parsing
        * y
        * n
        * n -> y (relaxed)
        * i -> y
        * i/y -> n (out of range)
        * i -> n
* nst's JSONTestSuite (2)
    * test_parsing
        * y
        * n
        * n (previously overflowed)
        * i -> y
        * i -> n
* Big List of Naughty Strings
    * parsing blns.json
    * roundtripping



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-to_chars.cpp

* digit gen
    * single precision
    * double precision
* formatting
    * single precision
    * double precision
    * integer



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-type_traits.cpp

* type traits
    * is_c_string
        * char *
        * char[]



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-ubjson.cpp

* UBJSON
    * individual values
        * discarded
        * null
        * boolean
            * true
            * false
        * number
            * signed
                * -9223372036854775808..-2147483649 (int64)
                * -2147483648..-32769 (int32)
                * -32768..-129 (int16)
                * -9263 (int16)
                * -128..-1 (int8)
                * 0..127 (int8)
                * 128..255 (uint8)
                * 256..32767 (int16)
                * 65536..2147483647 (int32)
                * 2147483648..9223372036854775807 (int64)
            * unsigned
                * 0..127 (int8)
                * 128..255 (uint8)
                * 256..32767 (int16)
                * 65536..2147483647 (int32)
                * 2147483648..9223372036854775807 (int64)
            * float64
                * 3.1415925
            * high-precision number
                * unsigned integer number
                * signed integer number
                * floating-point number
                * errors
                * serialization
        * string
            * N = 0..127
            * N = 128..255
            * N = 256..32767
            * N = 65536..2147483647
        * binary
            * N = 0..127
            * N = 128..255
            * N = 256..32767
            * N = 32768..2147483647
            * Other Serializations
                * No Count No Type
                * Yes Count No Type
        * array
            * empty
                * size=false type=false
                * size=true type=false
                * size=true type=true
            * [null]
                * size=false type=false
                * size=true type=false
                * size=true type=true
            * [1,2,3,4,5]
                * size=false type=false
                * size=true type=false
                * size=true type=true
            * [[[[]]]]
                * size=false type=false
                * size=true type=false
                * size=true type=true
            * array with uint16_t elements
                * size=false type=false
                * size=true type=false
                * size=true type=true
            * array with uint32_t elements
                * size=false type=false
                * size=true type=false
                * size=true type=true
        * object
            * empty
                * size=false type=false
                * size=true type=false
                * size=true type=true
            * {\
                * size=false type=false
                * size=true type=false
                * size=true type=true
            * {\
                * size=false type=false
                * size=true type=false
                * size=true type=true
    * errors
        * strict mode
            * non-strict mode
            * strict mode
        * excessive size
            * array
            * object
    * SAX aborts
        * start_array()
        * start_object()
        * key() in object
        * start_array(len)
        * start_object(len)
        * key() in object with length
    * parsing values
        * strings
        * number
            * float
        * array
            * optimized version (length only)
            * optimized version (type and length)
    * parse errors
        * empty byte vector
        * char
            * eof after C byte
            * byte out of range
        * strings
            * eof after S byte
            * invalid byte
        * array
            * optimized array: no size following type
        * strings
        * sizes
        * types
        * arrays
        * objects
    * writing optimized values
        * integer
            * array of i
            * array of U
            * array of I
            * array of l
            * array of L
        * unsigned integer
            * array of i
            * array of U
            * array of I
            * array of l
            * array of L
        * discarded
* Universal Binary JSON Specification Examples 1
    * Null Value
    * No-Op Value
    * Boolean Types
    * Numeric Types
    * Char Type
    * String Type
        * English
        * Russian
        * Russian
    * Array Type
        * size=false type=false
        * size=true type=false
        * size=true type=true
    * Object Type
        * size=false type=false
        * size=true type=false
        * size=true type=true
    * Optimized Format
        * Array Example
            * No Optimization
            * Optimized with count
            * Optimized with type & count
        * Object Example
            * No Optimization
            * Optimized with count
            * Optimized with type & count
        * Special Cases (Null, No-Op and Boolean)
            * Array
            * Object
* all UBJSON first bytes
* UBJSON roundtrips
    * input from self-generated UBJSON files



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11

In the following configuration, however, some test-cases were skipped:

* 1 test case was skipped when using GNU 14.3.0 with standard gnu++20
* 1 test case was skipped when using GNU 11.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 8.5.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++14
* 1 test case was skipped when using GNU 4.9.3 with standard gnu++11
* 1 test case was skipped when using Clang 18.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 12.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 10.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 9.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++14
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++23
* 1 test case was skipped when using GNU 6.4.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++17
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++17
* 1 test case was skipped when using Clang 19.1.7 with standard gnu++11
* 1 test case was skipped when using Clang 17.0.6 with standard gnu++11
* 1 test case was skipped when using Intel 2021.5.0.20211109 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++23
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++17
* 1 test case was skipped when using GNU 7.5.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.4.0 with standard gnu++11
* 1 test case was skipped when using GNU 5.5.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++23
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++14
* 1 test case was skipped when using GNU 4.8.5 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 9.4.0 with standard gnu++11
* 1 test case was skipped when using Linux-c++ with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11


### List of tests in file unit-udl.cpp

* user-defined string literals
    * using namespace nlohmann::literals::json_literals
    * using namespace nlohmann::json_literals
    * using namespace nlohmann::literals
    * using namespace nlohmann
    * global namespace



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-udt.cpp

* basic usage
    * conversion to json via free-functions
    * conversion from json via free-functions
        * via explicit calls to get
        * via explicit calls to get_to
        * implicit conversions
* adl_serializer specialization
    * partial specialization
        * to_json
        * from_json
    * total specialization
        * to_json
        * from_json
* even supported types can be specialized
* Non-copyable types
    * to_json
    * from_json
* custom serializer for pods
* custom serializer that does adl by default
* different basic_json types conversions
    * null
    * boolean
    * discarded
    * array
    * integer
    * float
    * unsigned
    * string
    * binary
    * object
    * get<custom_json>
* an incomplete type does not trigger a compiler error in non-evaluated context
* Issue #924
* Issue #1237
* compatible array type, without iterator type alias



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-udt_macro.cpp

* Serialization/deserialization via NLOHMANN_DEFINE_TYPE_INTRUSIVE and NLOHMANN_DEFINE_TYPE_NON_INTRUSIVE
    * person
* Serialization/deserialization via NLOHMANN_DEFINE_DERIVED_TYPE_INTRUSIVE and NLOHMANN_DEFINE_DERIVED_TYPE_NON_INTRUSIVE
    * person
* Serialization/deserialization via NLOHMANN_DEFINE_TYPE_INTRUSIVE_WITH_DEFAULT and NLOHMANN_DEFINE_TYPE_NON_INTRUSIVE_WITH_DEFAULT
    * person with default values
* Serialization/deserialization via NLOHMANN_DEFINE_DERIVED_TYPE_INTRUSIVE_WITH_DEFAULT and NLOHMANN_DEFINE_DERIVED_TYPE_NON_INTRUSIVE_WITH_DEFAULT
    * derived person with default values
* Serialization/deserialization of classes with 26 public/private member variables via NLOHMANN_DEFINE_TYPE_INTRUSIVE and NLOHMANN_DEFINE_TYPE_NON_INTRUSIVE
    * alphabet
* Serialization of non-default-constructible classes via NLOHMANN_DEFINE_TYPE_INTRUSIVE_ONLY_SERIALIZE and NLOHMANN_DEFINE_TYPE_NON_INTRUSIVE_ONLY_SERIALIZE
    * person
* Serialization of non-default-constructible classes via NLOHMANN_DEFINE_DERIVED_TYPE_INTRUSIVE_ONLY_SERIALIZE and NLOHMANN_DEFINE_DERIVED_TYPE_NON_INTRUSIVE_ONLY_SERIALIZE
    * derived person only serialize



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-unicode1.cpp

* Unicode (1/5)
    * \\uxxxx sequences
        * correct sequences
        * incorrect sequences
            * incorrect surrogate values
        * incorrect sequences
            * high surrogate without low surrogate
            * high surrogate with wrong low surrogate
            * low surrogate without high surrogate
    * read all unicode characters
        * check JSON Pointers
    * ignore byte-order-mark
        * in a stream
        * with an iterator
    * error for incomplete/wrong BOM
* Markus Kuhn's UTF-8 decoder capability and stress test
    * 1  Some correct UTF-8 text
    * 2  Boundary condition test cases
        * 2.1  First possible sequence of a certain length
        * 2.2  Last possible sequence of a certain length
        * 2.3  Other boundary conditions
    * 3  Malformed sequences
        * 3.1  Unexpected continuation bytes
        * 3.2  Lonely start characters
        * 3.3  Sequences with last continuation byte missing
        * 3.4  Concatenation of incomplete sequences
        * 3.5  Impossible bytes
    * 4  Overlong sequences
        * 4.1  Examples of an overlong ASCII character
        * 4.2  Maximum overlong sequences
        * 4.3  Overlong representation of the NUL character
    * 5  Illegal code positions
        * 5.1 Single UTF-16 surrogates
        * 5.2 Paired UTF-16 surrogates
        * 5.3 Noncharacter code positions



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11

In the following configuration, however, some test-cases were skipped:

* 1 test case was skipped when using GNU 14.3.0 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++14
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++14
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++23
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++17
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++17
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++23
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++17
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++23
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++14
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 9.4.0 with standard gnu++11
* 1 test case was skipped when using Linux-c++ with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11


### List of tests in file unit-unicode2.cpp

* Unicode (2/5)
    * RFC 3629
        * ill-formed first byte
        * UTF8-1 (x00-x7F)
            * well-formed
        * UTF8-2 (xC2-xDF UTF8-tail)
            * well-formed
            * ill-formed: missing second byte
            * ill-formed: wrong second byte
        * UTF8-3 (xE0 xA0-BF UTF8-tail)
            * well-formed
            * ill-formed: missing second byte
            * ill-formed: missing third byte
            * ill-formed: wrong second byte
            * ill-formed: wrong third byte
        * UTF8-3 (xE1-xEC UTF8-tail UTF8-tail)
            * well-formed
            * ill-formed: missing second byte
            * ill-formed: missing third byte
            * ill-formed: wrong second byte
            * ill-formed: wrong third byte
        * UTF8-3 (xED x80-9F UTF8-tail)
            * well-formed
            * ill-formed: missing second byte
            * ill-formed: missing third byte
            * ill-formed: wrong second byte
            * ill-formed: wrong third byte
        * UTF8-3 (xEE-xEF UTF8-tail UTF8-tail)
            * well-formed
            * ill-formed: missing second byte
            * ill-formed: missing third byte
            * ill-formed: wrong second byte
            * ill-formed: wrong third byte



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11

In the following configuration, however, some test-cases were skipped:

* 1 test case was skipped when using GNU 14.3.0 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++14
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++14
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++23
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++17
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++17
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++23
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++17
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++23
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++14
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 9.4.0 with standard gnu++11
* 1 test case was skipped when using Linux-c++ with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11


### List of tests in file unit-unicode3.cpp

* Unicode (3/5)
    * RFC 3629
        * UTF8-4 (xF0 x90-BF UTF8-tail UTF8-tail)
            * well-formed
            * ill-formed: missing second byte
            * ill-formed: missing third byte
            * ill-formed: missing fourth byte
            * ill-formed: wrong second byte
            * ill-formed: wrong third byte
            * ill-formed: wrong fourth byte



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11

In the following configuration, however, some test-cases were skipped:

* 1 test case was skipped when using GNU 14.3.0 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++14
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++14
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++23
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++17
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++17
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++23
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++17
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++23
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++14
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 9.4.0 with standard gnu++11
* 1 test case was skipped when using Linux-c++ with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11


### List of tests in file unit-unicode4.cpp

* Unicode (4/5)
    * RFC 3629
        * UTF8-4 (xF1-F3 UTF8-tail UTF8-tail UTF8-tail)
            * well-formed
            * ill-formed: missing second byte
            * ill-formed: missing third byte
            * ill-formed: missing fourth byte
            * ill-formed: wrong second byte
            * ill-formed: wrong third byte
            * ill-formed: wrong fourth byte



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11

In the following configuration, however, some test-cases were skipped:

* 1 test case was skipped when using GNU 14.3.0 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++14
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++14
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++23
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++17
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++17
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++23
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++17
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++23
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++14
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 9.4.0 with standard gnu++11
* 1 test case was skipped when using Linux-c++ with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11


### List of tests in file unit-unicode5.cpp

* Unicode (5/5)
    * RFC 3629
        * UTF8-4 (xF4 x80-8F UTF8-tail UTF8-tail)
            * well-formed
            * ill-formed: missing second byte
            * ill-formed: missing third byte
            * ill-formed: missing fourth byte
            * ill-formed: wrong second byte
            * ill-formed: wrong third byte
            * ill-formed: wrong fourth byte



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11

In the following configuration, however, some test-cases were skipped:

* 1 test case was skipped when using GNU 14.3.0 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++14
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++14
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++23
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++17
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++17
* 1 test case was skipped when using GNU 14.3.0 with standard gnu++23
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++17
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++23
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++14
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++20
* 1 test case was skipped when using Clang 20.1.8 with standard gnu++11
* 1 test case was skipped when using GNU 9.4.0 with standard gnu++11
* 1 test case was skipped when using Linux-c++ with standard gnu++11
* 1 test case was skipped when using GNU 13.3.0 with standard gnu++11


### List of tests in file unit-user_defined_input.cpp

* Use arbitrary stdlib container
* Custom container non-member begin/end
* Custom container member begin/end
* Custom iterator



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-windows_h.cpp

* include windows.h



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


### List of tests in file unit-wstring.cpp

* wide strings
    * std::wstring
    * invalid std::wstring
    * std::u16string
    * invalid std::u16string
    * std::u32string
    * invalid std::u32string



All tests in this file were run in the following configurations:

* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++20
* GNU 9.4.0 with standard gnu++11
* GNU 11.5.0 with standard gnu++11
* GNU 8.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++14
* GNU 9.4.0 with standard gnu++11
* GNU 4.9.3 with standard gnu++11
* Clang 18.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 14.3.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 12.5.0 with standard gnu++11
* GNU 10.5.0 with standard gnu++11
* GNU 13.3.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++11
* GNU 9.5.0 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++14
* Clang 20.1.8 with standard gnu++23
* GNU 6.4.0 with standard gnu++11
* GNU 14.3.0 with standard gnu++17
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++17
* Clang 19.1.7 with standard gnu++11
* Clang 17.0.6 with standard gnu++11
* Intel 2021.5.0.20211109 with standard gnu++11
* GNU 14.3.0 with standard gnu++23
* Clang 20.1.8 with standard gnu++17
* GNU 7.5.0 with standard gnu++11
* GNU 13.4.0 with standard gnu++11
* GNU 5.5.0 with standard gnu++11
* Clang 20.1.8 with standard gnu++23
* Clang 20.1.8 with standard gnu++14
* GNU 4.8.5 with standard gnu++11
* Clang 20.1.8 with standard gnu++20
* Clang 20.1.8 with standard gnu++11
* GNU 9.4.0 with standard gnu++11
* Linux-c++ with standard gnu++11
* GNU 13.3.0 with standard gnu++11


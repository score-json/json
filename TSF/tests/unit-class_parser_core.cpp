//     __ _____ _____ _____
//  __|  |   __|     |   | |  JSON for Modern C++ (supporting code)
// |  |  |__   |  |  | | | |  version 3.12.0
// |_____|_____|_____|_|___|  https://github.com/nlohmann/json
//
// SPDX-FileCopyrightText: 2013 - 2025 Niels Lohmann <https://nlohmann.me>
// SPDX-License-Identifier: MIT

/*
This file has been adapted from the original nlohmann/json library (tests/src/unit-class_parser.cpp)
to use the plain json::accept() and json::parse() functions instead of advanced helper functions, 
which make many additional function calls (see the definitions of parse_helper and accept_helper in 
tests/src/unit-class_parser.cpp). This allows to directly attribute a test result to the accept() or 
parse() function, which is needed to use the test results as evidence for the well-formedness and parsing 
 of JSON requirements. Unnecessary code and test sections have been removed.
*/

#include "doctest_compatibility.h"

#define JSON_TESTS_PRIVATE
#include <nlohmann/json.hpp>
using nlohmann::json;
#ifdef JSON_TEST_NO_GLOBAL_UDLS
    using namespace nlohmann::literals; // NOLINT(google-build-using-namespace)
#endif

#include <valarray>

namespace
{

json parser_helper(const std::string& s);
bool accept_helper(const std::string& s);

json parser_helper(const std::string& s)
{
    return json::parse(s); 
}

bool accept_helper(const std::string& s)
{
    CAPTURE(s)
    return json::accept(s);
}

} // namespace

TEST_CASE("parser class - core")
{
    SECTION("parse")
    {
        SECTION("null")
        {
            CHECK(parser_helper("null") == json(nullptr));
        }

        SECTION("true")
        {
            CHECK(parser_helper("true") == json(true));
        }

        SECTION("false")
        {
            CHECK(parser_helper("false") == json(false));
        }

        SECTION("array")
        {
            SECTION("empty array")
            {
                CHECK(parser_helper("[]") == json(json::value_t::array));
                CHECK(parser_helper("[ ]") == json(json::value_t::array));
            }

            SECTION("nonempty array")
            {
                CHECK(parser_helper("[true, false, null]") == json({true, false, nullptr}));
            }
        }

        SECTION("object")
        {
            SECTION("empty object")
            {
                CHECK(parser_helper("{}") == json(json::value_t::object));
                CHECK(parser_helper("{ }") == json(json::value_t::object));
            }

            SECTION("nonempty object")
            {
                CHECK(parser_helper("{\"\": true, \"one\": 1, \"two\": null}") == json({{"", true}, {"one", 1}, {"two", nullptr}}));
            }
        }

        SECTION("string")
        {
            // empty string
            CHECK(parser_helper("\"\"") == json(json::value_t::string));

            SECTION("errors")
            {
                // error: tab in string
                CHECK_THROWS_WITH_AS(parser_helper("\"\t\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+0009 (HT) must be escaped to \\u0009 or \\t; last read: '\"<U+0009>'", json::parse_error&);
                // error: newline in string
                CHECK_THROWS_WITH_AS(parser_helper("\"\n\""), "[json.exception.parse_error.101] parse error at line 2, column 0: syntax error while parsing value - invalid string: control character U+000A (LF) must be escaped to \\u000A or \\n; last read: '\"<U+000A>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\r\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+000D (CR) must be escaped to \\u000D or \\r; last read: '\"<U+000D>'", json::parse_error&);
                // error: backspace in string
                CHECK_THROWS_WITH_AS(parser_helper("\"\b\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+0008 (BS) must be escaped to \\u0008 or \\b; last read: '\"<U+0008>'", json::parse_error&);
                // improve code coverage
                CHECK_THROWS_AS(parser_helper("\uFF01"), json::parse_error&);
                CHECK_THROWS_AS(parser_helper("[-4:1,]"), json::parse_error&);
                // unescaped control characters
                CHECK_THROWS_WITH_AS(parser_helper("\"\x00\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: missing closing quote; last read: '\"'", json::parse_error&); // NOLINT(bugprone-string-literal-with-embedded-nul)
                CHECK_THROWS_WITH_AS(parser_helper("\"\x01\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+0001 (SOH) must be escaped to \\u0001; last read: '\"<U+0001>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x02\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+0002 (STX) must be escaped to \\u0002; last read: '\"<U+0002>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x03\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+0003 (ETX) must be escaped to \\u0003; last read: '\"<U+0003>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x04\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+0004 (EOT) must be escaped to \\u0004; last read: '\"<U+0004>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x05\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+0005 (ENQ) must be escaped to \\u0005; last read: '\"<U+0005>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x06\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+0006 (ACK) must be escaped to \\u0006; last read: '\"<U+0006>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x07\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+0007 (BEL) must be escaped to \\u0007; last read: '\"<U+0007>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x08\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+0008 (BS) must be escaped to \\u0008 or \\b; last read: '\"<U+0008>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x09\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+0009 (HT) must be escaped to \\u0009 or \\t; last read: '\"<U+0009>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x0a\""), "[json.exception.parse_error.101] parse error at line 2, column 0: syntax error while parsing value - invalid string: control character U+000A (LF) must be escaped to \\u000A or \\n; last read: '\"<U+000A>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x0b\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+000B (VT) must be escaped to \\u000B; last read: '\"<U+000B>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x0c\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+000C (FF) must be escaped to \\u000C or \\f; last read: '\"<U+000C>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x0d\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+000D (CR) must be escaped to \\u000D or \\r; last read: '\"<U+000D>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x0e\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+000E (SO) must be escaped to \\u000E; last read: '\"<U+000E>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x0f\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+000F (SI) must be escaped to \\u000F; last read: '\"<U+000F>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x10\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+0010 (DLE) must be escaped to \\u0010; last read: '\"<U+0010>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x11\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+0011 (DC1) must be escaped to \\u0011; last read: '\"<U+0011>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x12\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+0012 (DC2) must be escaped to \\u0012; last read: '\"<U+0012>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x13\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+0013 (DC3) must be escaped to \\u0013; last read: '\"<U+0013>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x14\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+0014 (DC4) must be escaped to \\u0014; last read: '\"<U+0014>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x15\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+0015 (NAK) must be escaped to \\u0015; last read: '\"<U+0015>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x16\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+0016 (SYN) must be escaped to \\u0016; last read: '\"<U+0016>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x17\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+0017 (ETB) must be escaped to \\u0017; last read: '\"<U+0017>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x18\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+0018 (CAN) must be escaped to \\u0018; last read: '\"<U+0018>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x19\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+0019 (EM) must be escaped to \\u0019; last read: '\"<U+0019>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x1a\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+001A (SUB) must be escaped to \\u001A; last read: '\"<U+001A>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x1b\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+001B (ESC) must be escaped to \\u001B; last read: '\"<U+001B>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x1c\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+001C (FS) must be escaped to \\u001C; last read: '\"<U+001C>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x1d\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+001D (GS) must be escaped to \\u001D; last read: '\"<U+001D>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x1e\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+001E (RS) must be escaped to \\u001E; last read: '\"<U+001E>'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("\"\x1f\""), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+001F (US) must be escaped to \\u001F; last read: '\"<U+001F>'", json::parse_error&);

                SECTION("additional test for null byte")
                {
                    // The test above for the null byte is wrong, because passing
                    // a string to the parser only reads int until it encounters
                    // a null byte. This test inserts the null byte later on and
                    // uses an iterator range.
                    std::string s = "\"1\"";
                    s[1] = '\0';
                    json _;
                    CHECK_THROWS_WITH_AS(_ = json::parse(s.begin(), s.end()), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: control character U+0000 (NUL) must be escaped to \\u0000; last read: '\"<U+0000>'", json::parse_error&);
                }
            }

            SECTION("escaped")
            {
                // quotation mark "\""
                auto r1 = R"("\"")"_json;
                CHECK(parser_helper("\"\\\"\"") == r1);
                // reverse solidus "\\"
                auto r2 = R"("\\")"_json;
                CHECK(parser_helper("\"\\\\\"") == r2);
                // solidus
                CHECK(parser_helper("\"\\/\"") == R"("/")"_json);
                // backspace
                CHECK(parser_helper("\"\\b\"") == json("\b"));
                // formfeed
                CHECK(parser_helper("\"\\f\"") == json("\f"));
                // newline
                CHECK(parser_helper("\"\\n\"") == json("\n"));
                // carriage return
                CHECK(parser_helper("\"\\r\"") == json("\r"));
                // horizontal tab
                CHECK(parser_helper("\"\\t\"") == json("\t"));

                CHECK(parser_helper("\"\\u0001\"").get<json::string_t>() == "\x01");
                CHECK(parser_helper("\"\\u000a\"").get<json::string_t>() == "\n");
                CHECK(parser_helper("\"\\u00b0\"").get<json::string_t>() == "°");
                CHECK(parser_helper("\"\\u0c00\"").get<json::string_t>() == "ఀ");
                CHECK(parser_helper("\"\\ud000\"").get<json::string_t>() == "퀀");
                CHECK(parser_helper("\"\\u000E\"").get<json::string_t>() == "\x0E");
                CHECK(parser_helper("\"\\u00F0\"").get<json::string_t>() == "ð");
                CHECK(parser_helper("\"\\u0100\"").get<json::string_t>() == "Ā");
                CHECK(parser_helper("\"\\u2000\"").get<json::string_t>() == " ");
                CHECK(parser_helper("\"\\uFFFF\"").get<json::string_t>() == "￿");
                CHECK(parser_helper("\"\\u20AC\"").get<json::string_t>() == "€");
                CHECK(parser_helper("\"€\"").get<json::string_t>() == "€");
                CHECK(parser_helper("\"🎈\"").get<json::string_t>() == "🎈");

                CHECK(parser_helper("\"\\ud80c\\udc60\"").get<json::string_t>() == "\xf0\x93\x81\xa0");
                CHECK(parser_helper("\"\\ud83c\\udf1e\"").get<json::string_t>() == "🌞");
            }
        }

        SECTION("number")
        {
            SECTION("integers")
            {
                SECTION("without exponent")
                {
                    CHECK(parser_helper("-128") == json(-128));
                    CHECK(parser_helper("-0") == json(-0));
                    CHECK(parser_helper("0") == json(0));
                    CHECK(parser_helper("128") == json(128));
                }

                SECTION("with exponent")
                {
                    CHECK(parser_helper("0e1") == json(0e1));
                    CHECK(parser_helper("0E1") == json(0e1));

                    CHECK(parser_helper("10000E-4") == json(10000e-4));
                    CHECK(parser_helper("10000E-3") == json(10000e-3));
                    CHECK(parser_helper("10000E-2") == json(10000e-2));
                    CHECK(parser_helper("10000E-1") == json(10000e-1));
                    CHECK(parser_helper("10000E0") == json(10000e0));
                    CHECK(parser_helper("10000E1") == json(10000e1));
                    CHECK(parser_helper("10000E2") == json(10000e2));
                    CHECK(parser_helper("10000E3") == json(10000e3));
                    CHECK(parser_helper("10000E4") == json(10000e4));

                    CHECK(parser_helper("10000e-4") == json(10000e-4));
                    CHECK(parser_helper("10000e-3") == json(10000e-3));
                    CHECK(parser_helper("10000e-2") == json(10000e-2));
                    CHECK(parser_helper("10000e-1") == json(10000e-1));
                    CHECK(parser_helper("10000e0") == json(10000e0));
                    CHECK(parser_helper("10000e1") == json(10000e1));
                    CHECK(parser_helper("10000e2") == json(10000e2));
                    CHECK(parser_helper("10000e3") == json(10000e3));
                    CHECK(parser_helper("10000e4") == json(10000e4));

                    CHECK(parser_helper("-0e1") == json(-0e1));
                    CHECK(parser_helper("-0E1") == json(-0e1));
                    CHECK(parser_helper("-0E123") == json(-0e123));

                    // numbers after exponent
                    CHECK(parser_helper("10E0") == json(10e0));
                    CHECK(parser_helper("10E1") == json(10e1));
                    CHECK(parser_helper("10E2") == json(10e2));
                    CHECK(parser_helper("10E3") == json(10e3));
                    CHECK(parser_helper("10E4") == json(10e4));
                    CHECK(parser_helper("10E5") == json(10e5));
                    CHECK(parser_helper("10E6") == json(10e6));
                    CHECK(parser_helper("10E7") == json(10e7));
                    CHECK(parser_helper("10E8") == json(10e8));
                    CHECK(parser_helper("10E9") == json(10e9));
                    CHECK(parser_helper("10E+0") == json(10e0));
                    CHECK(parser_helper("10E+1") == json(10e1));
                    CHECK(parser_helper("10E+2") == json(10e2));
                    CHECK(parser_helper("10E+3") == json(10e3));
                    CHECK(parser_helper("10E+4") == json(10e4));
                    CHECK(parser_helper("10E+5") == json(10e5));
                    CHECK(parser_helper("10E+6") == json(10e6));
                    CHECK(parser_helper("10E+7") == json(10e7));
                    CHECK(parser_helper("10E+8") == json(10e8));
                    CHECK(parser_helper("10E+9") == json(10e9));
                    CHECK(parser_helper("10E-1") == json(10e-1));
                    CHECK(parser_helper("10E-2") == json(10e-2));
                    CHECK(parser_helper("10E-3") == json(10e-3));
                    CHECK(parser_helper("10E-4") == json(10e-4));
                    CHECK(parser_helper("10E-5") == json(10e-5));
                    CHECK(parser_helper("10E-6") == json(10e-6));
                    CHECK(parser_helper("10E-7") == json(10e-7));
                    CHECK(parser_helper("10E-8") == json(10e-8));
                    CHECK(parser_helper("10E-9") == json(10e-9));
                }

                SECTION("edge cases")
                {
                    // From RFC8259, Section 6:
                    // Note that when such software is used, numbers that are
                    // integers and are in the range [-(2**53)+1, (2**53)-1]
                    // are interoperable in the sense that implementations will
                    // agree exactly on their numeric values.

                    // -(2**53)+1
                    CHECK(parser_helper("-9007199254740991").get<int64_t>() == -9007199254740991);
                    // (2**53)-1
                    CHECK(parser_helper("9007199254740991").get<int64_t>() == 9007199254740991);
                }

                SECTION("over the edge cases")  // issue #178 - Integer conversion to unsigned (incorrect handling of 64-bit integers)
                {
                    // While RFC8259, Section 6 specifies a preference for support
                    // for ranges in range of IEEE 754-2008 binary64 (double precision)
                    // this does not accommodate 64-bit integers without loss of accuracy.
                    // As 64-bit integers are now widely used in software, it is desirable
                    // to expand support to the full 64 bit (signed and unsigned) range
                    // i.e. -(2**63) -> (2**64)-1.

                    // -(2**63)    ** Note: compilers see negative literals as negated positive numbers (hence the -1))
                    CHECK(parser_helper("-9223372036854775808").get<int64_t>() == -9223372036854775807 - 1);
                    // (2**63)-1
                    CHECK(parser_helper("9223372036854775807").get<int64_t>() == 9223372036854775807);
                    // (2**64)-1
                    CHECK(parser_helper("18446744073709551615").get<uint64_t>() == 18446744073709551615u);
                }
            }

            SECTION("floating-point")
            {
                SECTION("without exponent")
                {
                    CHECK(parser_helper("-128.5") == json(-128.5));
                    CHECK(parser_helper("0.999") == json(0.999));
                    CHECK(parser_helper("128.5") == json(128.5));
                    CHECK(parser_helper("-0.0") == json(-0.0));
                }

                SECTION("with exponent")
                {
                    CHECK(parser_helper("-128.5E3") == json(-128.5E3));
                    CHECK(parser_helper("-128.5E-3") == json(-128.5E-3));
                    CHECK(parser_helper("-0.0e1") == json(-0.0e1));
                    CHECK(parser_helper("-0.0E1") == json(-0.0e1));
                }
            }

            SECTION("overflow")
            {
                // overflows during parsing yield an exception
                CHECK_THROWS_WITH_AS(parser_helper("1.18973e+4932").empty(), "[json.exception.out_of_range.406] number overflow parsing '1.18973e+4932'", json::out_of_range&);
            }

            SECTION("invalid numbers")
            {
                // numbers must not begin with "+"
                CHECK_THROWS_AS(parser_helper("+1"), json::parse_error&);
                CHECK_THROWS_AS(parser_helper("+0"), json::parse_error&);

                CHECK_THROWS_WITH_AS(parser_helper("01"),
                                     "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - unexpected number literal; expected end of input", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("-01"),
                                     "[json.exception.parse_error.101] parse error at line 1, column 3: syntax error while parsing value - unexpected number literal; expected end of input", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("--1"),
                                     "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid number; expected digit after '-'; last read: '--'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("1."),
                                     "[json.exception.parse_error.101] parse error at line 1, column 3: syntax error while parsing value - invalid number; expected digit after '.'; last read: '1.'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("1E"),
                                     "[json.exception.parse_error.101] parse error at line 1, column 3: syntax error while parsing value - invalid number; expected '+', '-', or digit after exponent; last read: '1E'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("1E-"),
                                     "[json.exception.parse_error.101] parse error at line 1, column 4: syntax error while parsing value - invalid number; expected digit after exponent sign; last read: '1E-'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("1.E1"),
                                     "[json.exception.parse_error.101] parse error at line 1, column 3: syntax error while parsing value - invalid number; expected digit after '.'; last read: '1.E'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("-1E"),
                                     "[json.exception.parse_error.101] parse error at line 1, column 4: syntax error while parsing value - invalid number; expected '+', '-', or digit after exponent; last read: '-1E'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("-0E#"),
                                     "[json.exception.parse_error.101] parse error at line 1, column 4: syntax error while parsing value - invalid number; expected '+', '-', or digit after exponent; last read: '-0E#'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("-0E-#"),
                                     "[json.exception.parse_error.101] parse error at line 1, column 5: syntax error while parsing value - invalid number; expected digit after exponent sign; last read: '-0E-#'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("-0#"),
                                     "[json.exception.parse_error.101] parse error at line 1, column 3: syntax error while parsing value - invalid literal; last read: '-0#'; expected end of input", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("-0.0:"),
                                     "[json.exception.parse_error.101] parse error at line 1, column 5: syntax error while parsing value - unexpected ':'; expected end of input", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("-0.0Z"),
                                     "[json.exception.parse_error.101] parse error at line 1, column 5: syntax error while parsing value - invalid literal; last read: '-0.0Z'; expected end of input", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("-0E123:"),
                                     "[json.exception.parse_error.101] parse error at line 1, column 7: syntax error while parsing value - unexpected ':'; expected end of input", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("-0e0-:"),
                                     "[json.exception.parse_error.101] parse error at line 1, column 6: syntax error while parsing value - invalid number; expected digit after '-'; last read: '-:'; expected end of input", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("-0e-:"),
                                     "[json.exception.parse_error.101] parse error at line 1, column 5: syntax error while parsing value - invalid number; expected digit after exponent sign; last read: '-0e-:'", json::parse_error&);
                CHECK_THROWS_WITH_AS(parser_helper("-0f"),
                                     "[json.exception.parse_error.101] parse error at line 1, column 4: syntax error while parsing value - invalid literal; last read: '-0f'; expected end of input", json::parse_error&);
            }
        }
    }

    SECTION("accept")
    {
        SECTION("null")
        {
            CHECK(accept_helper("null"));
        }

        SECTION("true")
        {
            CHECK(accept_helper("true"));
        }

        SECTION("false")
        {
            CHECK(accept_helper("false"));
        }

        SECTION("array")
        {
            SECTION("empty array")
            {
                CHECK(accept_helper("[]"));
                CHECK(accept_helper("[ ]"));
            }

            SECTION("nonempty array")
            {
                CHECK(accept_helper("[true, false, null]"));
            }
        }

        SECTION("object")
        {
            SECTION("empty object")
            {
                CHECK(accept_helper("{}"));
                CHECK(accept_helper("{ }"));
            }

            SECTION("nonempty object")
            {
                CHECK(accept_helper("{\"\": true, \"one\": 1, \"two\": null}"));
            }
        }

        SECTION("string")
        {
            // empty string
            CHECK(accept_helper("\"\""));

            SECTION("errors")
            {
                // error: tab in string
                CHECK(accept_helper("\"\t\"") == false);
                // error: newline in string
                CHECK(accept_helper("\"\n\"") == false);
                CHECK(accept_helper("\"\r\"") == false);
                // error: backspace in string
                CHECK(accept_helper("\"\b\"") == false);
                // improve code coverage
                CHECK(accept_helper("\uFF01") == false);
                CHECK(accept_helper("[-4:1,]") == false);
                // unescaped control characters
                CHECK(accept_helper("\"\x00\"") == false); // NOLINT(bugprone-string-literal-with-embedded-nul)
                CHECK(accept_helper("\"\x01\"") == false);
                CHECK(accept_helper("\"\x02\"") == false);
                CHECK(accept_helper("\"\x03\"") == false);
                CHECK(accept_helper("\"\x04\"") == false);
                CHECK(accept_helper("\"\x05\"") == false);
                CHECK(accept_helper("\"\x06\"") == false);
                CHECK(accept_helper("\"\x07\"") == false);
                CHECK(accept_helper("\"\x08\"") == false);
                CHECK(accept_helper("\"\x09\"") == false);
                CHECK(accept_helper("\"\x0a\"") == false);
                CHECK(accept_helper("\"\x0b\"") == false);
                CHECK(accept_helper("\"\x0c\"") == false);
                CHECK(accept_helper("\"\x0d\"") == false);
                CHECK(accept_helper("\"\x0e\"") == false);
                CHECK(accept_helper("\"\x0f\"") == false);
                CHECK(accept_helper("\"\x10\"") == false);
                CHECK(accept_helper("\"\x11\"") == false);
                CHECK(accept_helper("\"\x12\"") == false);
                CHECK(accept_helper("\"\x13\"") == false);
                CHECK(accept_helper("\"\x14\"") == false);
                CHECK(accept_helper("\"\x15\"") == false);
                CHECK(accept_helper("\"\x16\"") == false);
                CHECK(accept_helper("\"\x17\"") == false);
                CHECK(accept_helper("\"\x18\"") == false);
                CHECK(accept_helper("\"\x19\"") == false);
                CHECK(accept_helper("\"\x1a\"") == false);
                CHECK(accept_helper("\"\x1b\"") == false);
                CHECK(accept_helper("\"\x1c\"") == false);
                CHECK(accept_helper("\"\x1d\"") == false);
                CHECK(accept_helper("\"\x1e\"") == false);
                CHECK(accept_helper("\"\x1f\"") == false);
            }

            SECTION("escaped")
            {
                // quotation mark "\""
                auto r1 = R"("\"")"_json;
                CHECK(accept_helper("\"\\\"\""));
                // reverse solidus "\\"
                auto r2 = R"("\\")"_json;
                CHECK(accept_helper("\"\\\\\""));
                // solidus
                CHECK(accept_helper("\"\\/\""));
                // backspace
                CHECK(accept_helper("\"\\b\""));
                // formfeed
                CHECK(accept_helper("\"\\f\""));
                // newline
                CHECK(accept_helper("\"\\n\""));
                // carriage return
                CHECK(accept_helper("\"\\r\""));
                // horizontal tab
                CHECK(accept_helper("\"\\t\""));

                CHECK(accept_helper("\"\\u0001\""));
                CHECK(accept_helper("\"\\u000a\""));
                CHECK(accept_helper("\"\\u00b0\""));
                CHECK(accept_helper("\"\\u0c00\""));
                CHECK(accept_helper("\"\\ud000\""));
                CHECK(accept_helper("\"\\u000E\""));
                CHECK(accept_helper("\"\\u00F0\""));
                CHECK(accept_helper("\"\\u0100\""));
                CHECK(accept_helper("\"\\u2000\""));
                CHECK(accept_helper("\"\\uFFFF\""));
                CHECK(accept_helper("\"\\u20AC\""));
                CHECK(accept_helper("\"€\""));
                CHECK(accept_helper("\"🎈\""));

                CHECK(accept_helper("\"\\ud80c\\udc60\""));
                CHECK(accept_helper("\"\\ud83c\\udf1e\""));
            }
        }

        SECTION("number")
        {
            SECTION("integers")
            {
                SECTION("without exponent")
                {
                    CHECK(accept_helper("-128"));
                    CHECK(accept_helper("-0"));
                    CHECK(accept_helper("0"));
                    CHECK(accept_helper("128"));
                }

                SECTION("with exponent")
                {
                    CHECK(accept_helper("0e1"));
                    CHECK(accept_helper("0E1"));

                    CHECK(accept_helper("10000E-4"));
                    CHECK(accept_helper("10000E-3"));
                    CHECK(accept_helper("10000E-2"));
                    CHECK(accept_helper("10000E-1"));
                    CHECK(accept_helper("10000E0"));
                    CHECK(accept_helper("10000E1"));
                    CHECK(accept_helper("10000E2"));
                    CHECK(accept_helper("10000E3"));
                    CHECK(accept_helper("10000E4"));

                    CHECK(accept_helper("10000e-4"));
                    CHECK(accept_helper("10000e-3"));
                    CHECK(accept_helper("10000e-2"));
                    CHECK(accept_helper("10000e-1"));
                    CHECK(accept_helper("10000e0"));
                    CHECK(accept_helper("10000e1"));
                    CHECK(accept_helper("10000e2"));
                    CHECK(accept_helper("10000e3"));
                    CHECK(accept_helper("10000e4"));

                    CHECK(accept_helper("-0e1"));
                    CHECK(accept_helper("-0E1"));
                    CHECK(accept_helper("-0E123"));
                }

                SECTION("edge cases")
                {
                    // From RFC8259, Section 6:
                    // Note that when such software is used, numbers that are
                    // integers and are in the range [-(2**53)+1, (2**53)-1]
                    // are interoperable in the sense that implementations will
                    // agree exactly on their numeric values.

                    // -(2**53)+1
                    CHECK(accept_helper("-9007199254740991"));
                    // (2**53)-1
                    CHECK(accept_helper("9007199254740991"));
                }

                SECTION("over the edge cases")  // issue #178 - Integer conversion to unsigned (incorrect handling of 64-bit integers)
                {
                    // While RFC8259, Section 6 specifies a preference for support
                    // for ranges in range of IEEE 754-2008 binary64 (double precision)
                    // this does not accommodate 64 bit integers without loss of accuracy.
                    // As 64 bit integers are now widely used in software, it is desirable
                    // to expand support to the full 64 bit (signed and unsigned) range
                    // i.e. -(2**63) -> (2**64)-1.

                    // -(2**63)    ** Note: compilers see negative literals as negated positive numbers (hence the -1))
                    CHECK(accept_helper("-9223372036854775808"));
                    // (2**63)-1
                    CHECK(accept_helper("9223372036854775807"));
                    // (2**64)-1
                    CHECK(accept_helper("18446744073709551615"));
                }
            }

            SECTION("floating-point")
            {
                SECTION("without exponent")
                {
                    CHECK(accept_helper("-128.5"));
                    CHECK(accept_helper("0.999"));
                    CHECK(accept_helper("128.5"));
                    CHECK(accept_helper("-0.0"));
                }

                SECTION("with exponent")
                {
                    CHECK(accept_helper("-128.5E3"));
                    CHECK(accept_helper("-128.5E-3"));
                    CHECK(accept_helper("-0.0e1"));
                    CHECK(accept_helper("-0.0E1"));
                }
            }

            SECTION("overflow")
            {
                // overflows during parsing
                CHECK(!accept_helper("1.18973e+4932"));
            }

            SECTION("invalid numbers")
            {
                CHECK(accept_helper("01") == false);
                CHECK(accept_helper("--1") == false);
                CHECK(accept_helper("1.") == false);
                CHECK(accept_helper("1E") == false);
                CHECK(accept_helper("1E-") == false);
                CHECK(accept_helper("1.E1") == false);
                CHECK(accept_helper("-1E") == false);
                CHECK(accept_helper("-0E#") == false);
                CHECK(accept_helper("-0E-#") == false);
                CHECK(accept_helper("-0#") == false);
                CHECK(accept_helper("-0.0:") == false);
                CHECK(accept_helper("-0.0Z") == false);
                CHECK(accept_helper("-0E123:") == false);
                CHECK(accept_helper("-0e0-:") == false);
                CHECK(accept_helper("-0e-:") == false);
                CHECK(accept_helper("-0f") == false);

                // numbers must not begin with "+"
                CHECK(accept_helper("+1") == false);
                CHECK(accept_helper("+0") == false);
            }
        }
    }

    SECTION("parse errors")
    {
        // unexpected end of number
        CHECK_THROWS_WITH_AS(parser_helper("0."),
                             "[json.exception.parse_error.101] parse error at line 1, column 3: syntax error while parsing value - invalid number; expected digit after '.'; last read: '0.'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("-"),
                             "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid number; expected digit after '-'; last read: '-'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("--"),
                             "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid number; expected digit after '-'; last read: '--'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("-0."),
                             "[json.exception.parse_error.101] parse error at line 1, column 4: syntax error while parsing value - invalid number; expected digit after '.'; last read: '-0.'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("-."),
                             "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid number; expected digit after '-'; last read: '-.'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("-:"),
                             "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid number; expected digit after '-'; last read: '-:'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("0.:"),
                             "[json.exception.parse_error.101] parse error at line 1, column 3: syntax error while parsing value - invalid number; expected digit after '.'; last read: '0.:'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("e."),
                             "[json.exception.parse_error.101] parse error at line 1, column 1: syntax error while parsing value - invalid literal; last read: 'e'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("1e."),
                             "[json.exception.parse_error.101] parse error at line 1, column 3: syntax error while parsing value - invalid number; expected '+', '-', or digit after exponent; last read: '1e.'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("1e/"),
                             "[json.exception.parse_error.101] parse error at line 1, column 3: syntax error while parsing value - invalid number; expected '+', '-', or digit after exponent; last read: '1e/'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("1e:"),
                             "[json.exception.parse_error.101] parse error at line 1, column 3: syntax error while parsing value - invalid number; expected '+', '-', or digit after exponent; last read: '1e:'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("1E."),
                             "[json.exception.parse_error.101] parse error at line 1, column 3: syntax error while parsing value - invalid number; expected '+', '-', or digit after exponent; last read: '1E.'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("1E/"),
                             "[json.exception.parse_error.101] parse error at line 1, column 3: syntax error while parsing value - invalid number; expected '+', '-', or digit after exponent; last read: '1E/'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("1E:"),
                             "[json.exception.parse_error.101] parse error at line 1, column 3: syntax error while parsing value - invalid number; expected '+', '-', or digit after exponent; last read: '1E:'", json::parse_error&);

        // unexpected end of null
        CHECK_THROWS_WITH_AS(parser_helper("n"),
                             "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid literal; last read: 'n'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("nu"),
                             "[json.exception.parse_error.101] parse error at line 1, column 3: syntax error while parsing value - invalid literal; last read: 'nu'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("nul"),
                             "[json.exception.parse_error.101] parse error at line 1, column 4: syntax error while parsing value - invalid literal; last read: 'nul'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("nulk"),
                             "[json.exception.parse_error.101] parse error at line 1, column 4: syntax error while parsing value - invalid literal; last read: 'nulk'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("nulm"),
                             "[json.exception.parse_error.101] parse error at line 1, column 4: syntax error while parsing value - invalid literal; last read: 'nulm'", json::parse_error&);

        // unexpected end of true
        CHECK_THROWS_WITH_AS(parser_helper("t"),
                             "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid literal; last read: 't'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("tr"),
                             "[json.exception.parse_error.101] parse error at line 1, column 3: syntax error while parsing value - invalid literal; last read: 'tr'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("tru"),
                             "[json.exception.parse_error.101] parse error at line 1, column 4: syntax error while parsing value - invalid literal; last read: 'tru'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("trud"),
                             "[json.exception.parse_error.101] parse error at line 1, column 4: syntax error while parsing value - invalid literal; last read: 'trud'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("truf"),
                             "[json.exception.parse_error.101] parse error at line 1, column 4: syntax error while parsing value - invalid literal; last read: 'truf'", json::parse_error&);

        // unexpected end of false
        CHECK_THROWS_WITH_AS(parser_helper("f"),
                             "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid literal; last read: 'f'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("fa"),
                             "[json.exception.parse_error.101] parse error at line 1, column 3: syntax error while parsing value - invalid literal; last read: 'fa'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("fal"),
                             "[json.exception.parse_error.101] parse error at line 1, column 4: syntax error while parsing value - invalid literal; last read: 'fal'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("fals"),
                             "[json.exception.parse_error.101] parse error at line 1, column 5: syntax error while parsing value - invalid literal; last read: 'fals'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("falsd"),
                             "[json.exception.parse_error.101] parse error at line 1, column 5: syntax error while parsing value - invalid literal; last read: 'falsd'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("falsf"),
                             "[json.exception.parse_error.101] parse error at line 1, column 5: syntax error while parsing value - invalid literal; last read: 'falsf'", json::parse_error&);

        // missing/unexpected end of array
        CHECK_THROWS_WITH_AS(parser_helper("["),
                             "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - unexpected end of input; expected '[', '{', or a literal", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("[1"),
                             "[json.exception.parse_error.101] parse error at line 1, column 3: syntax error while parsing array - unexpected end of input; expected ']'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("[1,"),
                             "[json.exception.parse_error.101] parse error at line 1, column 4: syntax error while parsing value - unexpected end of input; expected '[', '{', or a literal", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("[1,]"),
                             "[json.exception.parse_error.101] parse error at line 1, column 4: syntax error while parsing value - unexpected ']'; expected '[', '{', or a literal", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("]"),
                             "[json.exception.parse_error.101] parse error at line 1, column 1: syntax error while parsing value - unexpected ']'; expected '[', '{', or a literal", json::parse_error&);

        // missing/unexpected end of object
        CHECK_THROWS_WITH_AS(parser_helper("{"),
                             "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing object key - unexpected end of input; expected string literal", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("{\"foo\""),
                             "[json.exception.parse_error.101] parse error at line 1, column 7: syntax error while parsing object separator - unexpected end of input; expected ':'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("{\"foo\":"),
                             "[json.exception.parse_error.101] parse error at line 1, column 8: syntax error while parsing value - unexpected end of input; expected '[', '{', or a literal", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("{\"foo\":}"),
                             "[json.exception.parse_error.101] parse error at line 1, column 8: syntax error while parsing value - unexpected '}'; expected '[', '{', or a literal", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("{\"foo\":1,}"),
                             "[json.exception.parse_error.101] parse error at line 1, column 10: syntax error while parsing object key - unexpected '}'; expected string literal", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("}"),
                             "[json.exception.parse_error.101] parse error at line 1, column 1: syntax error while parsing value - unexpected '}'; expected '[', '{', or a literal", json::parse_error&);

        // missing/unexpected end of string
        CHECK_THROWS_WITH_AS(parser_helper("\""),
                             "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing value - invalid string: missing closing quote; last read: '\"'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("\"\\\""),
                             "[json.exception.parse_error.101] parse error at line 1, column 4: syntax error while parsing value - invalid string: missing closing quote; last read: '\"\\\"'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("\"\\u\""),
                             "[json.exception.parse_error.101] parse error at line 1, column 4: syntax error while parsing value - invalid string: '\\u' must be followed by 4 hex digits; last read: '\"\\u\"'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("\"\\u0\""),
                             "[json.exception.parse_error.101] parse error at line 1, column 5: syntax error while parsing value - invalid string: '\\u' must be followed by 4 hex digits; last read: '\"\\u0\"'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("\"\\u01\""),
                             "[json.exception.parse_error.101] parse error at line 1, column 6: syntax error while parsing value - invalid string: '\\u' must be followed by 4 hex digits; last read: '\"\\u01\"'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("\"\\u012\""),
                             "[json.exception.parse_error.101] parse error at line 1, column 7: syntax error while parsing value - invalid string: '\\u' must be followed by 4 hex digits; last read: '\"\\u012\"'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("\"\\u"),
                             "[json.exception.parse_error.101] parse error at line 1, column 4: syntax error while parsing value - invalid string: '\\u' must be followed by 4 hex digits; last read: '\"\\u'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("\"\\u0"),
                             "[json.exception.parse_error.101] parse error at line 1, column 5: syntax error while parsing value - invalid string: '\\u' must be followed by 4 hex digits; last read: '\"\\u0'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("\"\\u01"),
                             "[json.exception.parse_error.101] parse error at line 1, column 6: syntax error while parsing value - invalid string: '\\u' must be followed by 4 hex digits; last read: '\"\\u01'", json::parse_error&);
        CHECK_THROWS_WITH_AS(parser_helper("\"\\u012"),
                             "[json.exception.parse_error.101] parse error at line 1, column 7: syntax error while parsing value - invalid string: '\\u' must be followed by 4 hex digits; last read: '\"\\u012'", json::parse_error&);

        // invalid escapes
        for (int c = 1; c < 128; ++c)
        {
            auto s = std::string("\"\\") + std::string(1, static_cast<char>(c)) + "\"";

            switch (c)
            {
                // valid escapes
                case ('"'):
                case ('\\'):
                case ('/'):
                case ('b'):
                case ('f'):
                case ('n'):
                case ('r'):
                case ('t'):
                {
                    CHECK_NOTHROW(parser_helper(s));
                    break;
                }

                // \u must be followed with four numbers, so we skip it here
                case ('u'):
                {
                    break;
                }

                // any other combination of backslash and character is invalid
                default:
                {
                    CHECK_THROWS_AS(parser_helper(s), json::parse_error&);
                    // only check error message if c is not a control character
                    if (c > 0x1f)
                    {
                        CHECK_THROWS_WITH_STD_STR(parser_helper(s),
                                                  "[json.exception.parse_error.101] parse error at line 1, column 3: syntax error while parsing value - invalid string: forbidden character after backslash; last read: '\"\\" + std::string(1, static_cast<char>(c)) + "'");
                    }
                    break;
                }
            }
        }

        // invalid \uxxxx escapes
        {
            // check whether character is a valid hex character
            const auto valid = [](int c)
            {
                switch (c)
                {
                    case ('0'):
                    case ('1'):
                    case ('2'):
                    case ('3'):
                    case ('4'):
                    case ('5'):
                    case ('6'):
                    case ('7'):
                    case ('8'):
                    case ('9'):
                    case ('a'):
                    case ('b'):
                    case ('c'):
                    case ('d'):
                    case ('e'):
                    case ('f'):
                    case ('A'):
                    case ('B'):
                    case ('C'):
                    case ('D'):
                    case ('E'):
                    case ('F'):
                    {
                        return true;
                    }

                    default:
                    {
                        return false;
                    }
                }
            };

            for (int c = 1; c < 128; ++c)
            {
                std::string const s = "\"\\u";

                // create a string with the iterated character at each position
                auto s1 = s + "000" + std::string(1, static_cast<char>(c)) + "\"";
                auto s2 = s + "00" + std::string(1, static_cast<char>(c)) + "0\"";
                auto s3 = s + "0" + std::string(1, static_cast<char>(c)) + "00\"";
                auto s4 = s + std::string(1, static_cast<char>(c)) + "000\"";

                if (valid(c))
                {
                    CAPTURE(s1)
                    CHECK_NOTHROW(parser_helper(s1));
                    CAPTURE(s2)
                    CHECK_NOTHROW(parser_helper(s2));
                    CAPTURE(s3)
                    CHECK_NOTHROW(parser_helper(s3));
                    CAPTURE(s4)
                    CHECK_NOTHROW(parser_helper(s4));
                }
                else
                {
                    CAPTURE(s1)
                    CHECK_THROWS_AS(parser_helper(s1), json::parse_error&);
                    // only check error message if c is not a control character
                    if (c > 0x1f)
                    {
                        CHECK_THROWS_WITH_STD_STR(parser_helper(s1),
                                                  "[json.exception.parse_error.101] parse error at line 1, column 7: syntax error while parsing value - invalid string: '\\u' must be followed by 4 hex digits; last read: '" + s1.substr(0, 7) + "'");
                    }

                    CAPTURE(s2)
                    CHECK_THROWS_AS(parser_helper(s2), json::parse_error&);
                    // only check error message if c is not a control character
                    if (c > 0x1f)
                    {
                        CHECK_THROWS_WITH_STD_STR(parser_helper(s2),
                                                  "[json.exception.parse_error.101] parse error at line 1, column 6: syntax error while parsing value - invalid string: '\\u' must be followed by 4 hex digits; last read: '" + s2.substr(0, 6) + "'");
                    }

                    CAPTURE(s3)
                    CHECK_THROWS_AS(parser_helper(s3), json::parse_error&);
                    // only check error message if c is not a control character
                    if (c > 0x1f)
                    {
                        CHECK_THROWS_WITH_STD_STR(parser_helper(s3),
                                                  "[json.exception.parse_error.101] parse error at line 1, column 5: syntax error while parsing value - invalid string: '\\u' must be followed by 4 hex digits; last read: '" + s3.substr(0, 5) + "'");
                    }

                    CAPTURE(s4)
                    CHECK_THROWS_AS(parser_helper(s4), json::parse_error&);
                    // only check error message if c is not a control character
                    if (c > 0x1f)
                    {
                        CHECK_THROWS_WITH_STD_STR(parser_helper(s4),
                                                  "[json.exception.parse_error.101] parse error at line 1, column 4: syntax error while parsing value - invalid string: '\\u' must be followed by 4 hex digits; last read: '" + s4.substr(0, 4) + "'");
                    }
                }
            }
        }

        json _;

        // missing part of a surrogate pair
        CHECK_THROWS_WITH_AS(_ = json::parse("\"\\uD80C\""), "[json.exception.parse_error.101] parse error at line 1, column 8: syntax error while parsing value - invalid string: surrogate U+D800..U+DBFF must be followed by U+DC00..U+DFFF; last read: '\"\\uD80C\"'", json::parse_error&);
        // invalid surrogate pair
        CHECK_THROWS_WITH_AS(_ = json::parse("\"\\uD80C\\uD80C\""),
                             "[json.exception.parse_error.101] parse error at line 1, column 13: syntax error while parsing value - invalid string: surrogate U+D800..U+DBFF must be followed by U+DC00..U+DFFF; last read: '\"\\uD80C\\uD80C'", json::parse_error&);
        CHECK_THROWS_WITH_AS(_ = json::parse("\"\\uD80C\\u0000\""),
                             "[json.exception.parse_error.101] parse error at line 1, column 13: syntax error while parsing value - invalid string: surrogate U+D800..U+DBFF must be followed by U+DC00..U+DFFF; last read: '\"\\uD80C\\u0000'", json::parse_error&);
        CHECK_THROWS_WITH_AS(_ = json::parse("\"\\uD80C\\uFFFF\""),
                             "[json.exception.parse_error.101] parse error at line 1, column 13: syntax error while parsing value - invalid string: surrogate U+D800..U+DBFF must be followed by U+DC00..U+DFFF; last read: '\"\\uD80C\\uFFFF'", json::parse_error&);
    }

    SECTION("parse errors (accept)")
    {
        // unexpected end of number
        CHECK(accept_helper("0.") == false);
        CHECK(accept_helper("-") == false);
        CHECK(accept_helper("--") == false);
        CHECK(accept_helper("-0.") == false);
        CHECK(accept_helper("-.") == false);
        CHECK(accept_helper("-:") == false);
        CHECK(accept_helper("0.:") == false);
        CHECK(accept_helper("e.") == false);
        CHECK(accept_helper("1e.") == false);
        CHECK(accept_helper("1e/") == false);
        CHECK(accept_helper("1e:") == false);
        CHECK(accept_helper("1E.") == false);
        CHECK(accept_helper("1E/") == false);
        CHECK(accept_helper("1E:") == false);

        // unexpected end of null
        CHECK(accept_helper("n") == false);
        CHECK(accept_helper("nu") == false);
        CHECK(accept_helper("nul") == false);

        // unexpected end of true
        CHECK(accept_helper("t") == false);
        CHECK(accept_helper("tr") == false);
        CHECK(accept_helper("tru") == false);

        // unexpected end of false
        CHECK(accept_helper("f") == false);
        CHECK(accept_helper("fa") == false);
        CHECK(accept_helper("fal") == false);
        CHECK(accept_helper("fals") == false);

        // missing/unexpected end of array
        CHECK(accept_helper("[") == false);
        CHECK(accept_helper("[1") == false);
        CHECK(accept_helper("[1,") == false);
        CHECK(accept_helper("[1,]") == false);
        CHECK(accept_helper("]") == false);

        // missing/unexpected end of object
        CHECK(accept_helper("{") == false);
        CHECK(accept_helper("{\"foo\"") == false);
        CHECK(accept_helper("{\"foo\":") == false);
        CHECK(accept_helper("{\"foo\":}") == false);
        CHECK(accept_helper("{\"foo\":1,}") == false);
        CHECK(accept_helper("}") == false);

        // missing/unexpected end of string
        CHECK(accept_helper("\"") == false);
        CHECK(accept_helper("\"\\\"") == false);
        CHECK(accept_helper("\"\\u\"") == false);
        CHECK(accept_helper("\"\\u0\"") == false);
        CHECK(accept_helper("\"\\u01\"") == false);
        CHECK(accept_helper("\"\\u012\"") == false);
        CHECK(accept_helper("\"\\u") == false);
        CHECK(accept_helper("\"\\u0") == false);
        CHECK(accept_helper("\"\\u01") == false);
        CHECK(accept_helper("\"\\u012") == false);

        // unget of newline
        CHECK(parser_helper("\n123\n") == 123);

        // invalid escapes
        for (int c = 1; c < 128; ++c)
        {
            auto s = std::string("\"\\") + std::string(1, static_cast<char>(c)) + "\"";

            switch (c)
            {
                // valid escapes
                case ('"'):
                case ('\\'):
                case ('/'):
                case ('b'):
                case ('f'):
                case ('n'):
                case ('r'):
                case ('t'):
                {
                    CHECK(json::parser(nlohmann::detail::input_adapter(s)).accept());
                    break;
                }

                // \u must be followed with four numbers, so we skip it here
                case ('u'):
                {
                    break;
                }

                // any other combination of backslash and character is invalid
                default:
                {
                    CHECK(json::parser(nlohmann::detail::input_adapter(s)).accept() == false);
                    break;
                }
            }
        }

        // invalid \uxxxx escapes
        {
            // check whether character is a valid hex character
            const auto valid = [](int c)
            {
                switch (c)
                {
                    case ('0'):
                    case ('1'):
                    case ('2'):
                    case ('3'):
                    case ('4'):
                    case ('5'):
                    case ('6'):
                    case ('7'):
                    case ('8'):
                    case ('9'):
                    case ('a'):
                    case ('b'):
                    case ('c'):
                    case ('d'):
                    case ('e'):
                    case ('f'):
                    case ('A'):
                    case ('B'):
                    case ('C'):
                    case ('D'):
                    case ('E'):
                    case ('F'):
                    {
                        return true;
                    }

                    default:
                    {
                        return false;
                    }
                }
            };

            for (int c = 1; c < 128; ++c)
            {
                std::string const s = "\"\\u";

                // create a string with the iterated character at each position
                const auto s1 = s + "000" + std::string(1, static_cast<char>(c)) + "\"";
                const auto s2 = s + "00" + std::string(1, static_cast<char>(c)) + "0\"";
                const auto s3 = s + "0" + std::string(1, static_cast<char>(c)) + "00\"";
                const auto s4 = s + std::string(1, static_cast<char>(c)) + "000\"";

                if (valid(c))
                {
                    CAPTURE(s1)
                    CHECK(json::parser(nlohmann::detail::input_adapter(s1)).accept());
                    CAPTURE(s2)
                    CHECK(json::parser(nlohmann::detail::input_adapter(s2)).accept());
                    CAPTURE(s3)
                    CHECK(json::parser(nlohmann::detail::input_adapter(s3)).accept());
                    CAPTURE(s4)
                    CHECK(json::parser(nlohmann::detail::input_adapter(s4)).accept());
                }
                else
                {
                    CAPTURE(s1)
                    CHECK(json::parser(nlohmann::detail::input_adapter(s1)).accept() == false);

                    CAPTURE(s2)
                    CHECK(json::parser(nlohmann::detail::input_adapter(s2)).accept() == false);

                    CAPTURE(s3)
                    CHECK(json::parser(nlohmann::detail::input_adapter(s3)).accept() == false);

                    CAPTURE(s4)
                    CHECK(json::parser(nlohmann::detail::input_adapter(s4)).accept() == false);
                }
            }
        }

        // missing part of a surrogate pair
        CHECK(accept_helper("\"\\uD80C\"") == false);
        // invalid surrogate pair
        CHECK(accept_helper("\"\\uD80C\\uD80C\"") == false);
        CHECK(accept_helper("\"\\uD80C\\u0000\"") == false);
        CHECK(accept_helper("\"\\uD80C\\uFFFF\"") == false);
    }

    SECTION("tests found by mutate++")
    {
        // test case to make sure no comma precedes the first key
        CHECK_THROWS_WITH_AS(parser_helper("{,\"key\": false}"), "[json.exception.parse_error.101] parse error at line 1, column 2: syntax error while parsing object key - unexpected ','; expected string literal", json::parse_error&);
        // test case to make sure an object is properly closed
        CHECK_THROWS_WITH_AS(parser_helper("[{\"key\": false true]"), "[json.exception.parse_error.101] parse error at line 1, column 19: syntax error while parsing object - unexpected true literal; expected '}'", json::parse_error&);

        // test case to make sure the callback is properly evaluated after reading a key
        {
            json::parser_callback_t const cb = [](int /*unused*/, json::parse_event_t event, json& /*unused*/) noexcept
            {
                return event != json::parse_event_t::key;
            };

            json x = json::parse("{\"key\": false}", cb);
            CHECK(x == json::object());
        }
    }
}

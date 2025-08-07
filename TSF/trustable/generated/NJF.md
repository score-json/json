

---

### NJF-01 

The service accepts the literal name null. 


**Supported Requests;**


**Supporting Items;**

_None_



**References;**

- `cpp-test; [parser class]
(/workspaces/json/tests/src/unit-class_parser.cpp)`


		```cpp
		TEST_CASE("parser class")
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
		                CHECK(parser_helper("[]") == json(json::value_t;;array));
		                CHECK(parser_helper("[ ]") == json(json::value_t;;array));
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
		                CHECK(parser_helper("{}") == json(json::value_t;;object));
		                CHECK(parser_helper("{ }") == json(json::value_t;;object));
		            }
		
		            SECTION("nonempty object")
		            {
		                CHECK(parser_helper("{\"\"; true, \"one\"; 1, \"two\"; null}") == json({{"", true}, {"one", 1}, {"two", nullptr}}));
		            }
		        }
		
		        SECTION("string")
		        {
		            // empty string
		            CHECK(parser_helper("\"\"") == json(json::value_t;;string));
		
		            SECTION("errors")
		            {
		                // error; tab in string
		                CHECK_THROWS_WITH_AS(parser_helper("\"\t\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+0009 (HT) must be escaped to \\u0009 or \\t; last read; '\"&lt;U+0009&gt;'", json::parse_error&);
		                // error; newline in string
		                CHECK_THROWS_WITH_AS(parser_helper("\"\n\""), "[json.exception.parse_error.101] parse error at line 2, column 0; syntax error while parsing value - invalid string; control character U+000A (LF) must be escaped to \\u000A or \\n; last read; '\"&lt;U+000A&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\r\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+000D (CR) must be escaped to \\u000D or \\r; last read; '\"&lt;U+000D&gt;'", json::parse_error&);
		                // error; backspace in string
		                CHECK_THROWS_WITH_AS(parser_helper("\"\b\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+0008 (BS) must be escaped to \\u0008 or \\b; last read; '\"&lt;U+0008&gt;'", json::parse_error&);
		                // improve code coverage
		                CHECK_THROWS_AS(parser_helper("\uFF01"), json::parse_error&);
		                CHECK_THROWS_AS(parser_helper("[-4;1,]"), json::parse_error&);
		                // unescaped control characters
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x00\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; missing closing quote; last read; '\"'", json::parse_error&); // NOLINT(bugprone-string-literal-with-embedded-nul)
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x01\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+0001 (SOH) must be escaped to \\u0001; last read; '\"&lt;U+0001&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x02\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+0002 (STX) must be escaped to \\u0002; last read; '\"&lt;U+0002&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x03\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+0003 (ETX) must be escaped to \\u0003; last read; '\"&lt;U+0003&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x04\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+0004 (EOT) must be escaped to \\u0004; last read; '\"&lt;U+0004&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x05\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+0005 (ENQ) must be escaped to \\u0005; last read; '\"&lt;U+0005&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x06\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+0006 (ACK) must be escaped to \\u0006; last read; '\"&lt;U+0006&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x07\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+0007 (BEL) must be escaped to \\u0007; last read; '\"&lt;U+0007&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x08\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+0008 (BS) must be escaped to \\u0008 or \\b; last read; '\"&lt;U+0008&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x09\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+0009 (HT) must be escaped to \\u0009 or \\t; last read; '\"&lt;U+0009&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x0a\""), "[json.exception.parse_error.101] parse error at line 2, column 0; syntax error while parsing value - invalid string; control character U+000A (LF) must be escaped to \\u000A or \\n; last read; '\"&lt;U+000A&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x0b\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+000B (VT) must be escaped to \\u000B; last read; '\"&lt;U+000B&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x0c\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+000C (FF) must be escaped to \\u000C or \\f; last read; '\"&lt;U+000C&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x0d\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+000D (CR) must be escaped to \\u000D or \\r; last read; '\"&lt;U+000D&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x0e\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+000E (SO) must be escaped to \\u000E; last read; '\"&lt;U+000E&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x0f\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+000F (SI) must be escaped to \\u000F; last read; '\"&lt;U+000F&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x10\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+0010 (DLE) must be escaped to \\u0010; last read; '\"&lt;U+0010&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x11\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+0011 (DC1) must be escaped to \\u0011; last read; '\"&lt;U+0011&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x12\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+0012 (DC2) must be escaped to \\u0012; last read; '\"&lt;U+0012&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x13\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+0013 (DC3) must be escaped to \\u0013; last read; '\"&lt;U+0013&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x14\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+0014 (DC4) must be escaped to \\u0014; last read; '\"&lt;U+0014&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x15\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+0015 (NAK) must be escaped to \\u0015; last read; '\"&lt;U+0015&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x16\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+0016 (SYN) must be escaped to \\u0016; last read; '\"&lt;U+0016&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x17\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+0017 (ETB) must be escaped to \\u0017; last read; '\"&lt;U+0017&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x18\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+0018 (CAN) must be escaped to \\u0018; last read; '\"&lt;U+0018&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x19\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+0019 (EM) must be escaped to \\u0019; last read; '\"&lt;U+0019&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x1a\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+001A (SUB) must be escaped to \\u001A; last read; '\"&lt;U+001A&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x1b\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+001B (ESC) must be escaped to \\u001B; last read; '\"&lt;U+001B&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x1c\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+001C (FS) must be escaped to \\u001C; last read; '\"&lt;U+001C&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x1d\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+001D (GS) must be escaped to \\u001D; last read; '\"&lt;U+001D&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x1e\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+001E (RS) must be escaped to \\u001E; last read; '\"&lt;U+001E&gt;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("\"\x1f\""), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+001F (US) must be escaped to \\u001F; last read; '\"&lt;U+001F&gt;'", json::parse_error&);
		
		                SECTION("additional test for null byte")
		                {
		                    // The test above for the null byte is wrong, because passing
		                    // a string to the parser only reads int until it encounters
		                    // a null byte. This test inserts the null byte later on and
		                    // uses an iterator range.
		                    std::string s = "\"1\"";
		                    s[1] = '\0';
		                    json _;
		                    CHECK_THROWS_WITH_AS(_ = json::parse(s.begin(), s.end()), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; control character U+0000 (NUL) must be escaped to \\u0000; last read; '\"&lt;U+0000&gt;'", json::parse_error&);
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
		
		                CHECK(parser_helper("\"\\u0001\"").get&lt;json::string_t&gt;() == "\x01");
		                CHECK(parser_helper("\"\\u000a\"").get&lt;json::string_t&gt;() == "\n");
		                CHECK(parser_helper("\"\\u00b0\"").get&lt;json::string_t&gt;() == "°");
		                CHECK(parser_helper("\"\\u0c00\"").get&lt;json::string_t&gt;() == "ఀ");
		                CHECK(parser_helper("\"\\ud000\"").get&lt;json::string_t&gt;() == "퀀");
		                CHECK(parser_helper("\"\\u000E\"").get&lt;json::string_t&gt;() == "\x0E");
		                CHECK(parser_helper("\"\\u00F0\"").get&lt;json::string_t&gt;() == "ð");
		                CHECK(parser_helper("\"\\u0100\"").get&lt;json::string_t&gt;() == "Ā");
		                CHECK(parser_helper("\"\\u2000\"").get&lt;json::string_t&gt;() == " ");
		                CHECK(parser_helper("\"\\uFFFF\"").get&lt;json::string_t&gt;() == "￿");
		                CHECK(parser_helper("\"\\u20AC\"").get&lt;json::string_t&gt;() == "€");
		                CHECK(parser_helper("\"€\"").get&lt;json::string_t&gt;() == "€");
		                CHECK(parser_helper("\"🎈\"").get&lt;json::string_t&gt;() == "🎈");
		
		                CHECK(parser_helper("\"\\ud80c\\udc60\"").get&lt;json::string_t&gt;() == "\xf0\x93\x81\xa0");
		                CHECK(parser_helper("\"\\ud83c\\udf1e\"").get&lt;json::string_t&gt;() == "🌞");
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
		                    // From RFC8259, Section 6;
		                    // Note that when such software is used, numbers that are
		                    // integers and are in the range [-(2**53)+1, (2**53)-1]
		                    // are interoperable in the sense that implementations will
		                    // agree exactly on their numeric values.
		
		                    // -(2**53)+1
		                    CHECK(parser_helper("-9007199254740991").get&lt;int64_t&gt;() == -9007199254740991);
		                    // (2**53)-1
		                    CHECK(parser_helper("9007199254740991").get&lt;int64_t&gt;() == 9007199254740991);
		                }
		
		                SECTION("over the edge cases")  // issue #178 - Integer conversion to unsigned (incorrect handling of 64-bit integers)
		                {
		                    // While RFC8259, Section 6 specifies a preference for support
		                    // for ranges in range of IEEE 754-2008 binary64 (double precision)
		                    // this does not accommodate 64-bit integers without loss of accuracy.
		                    // As 64-bit integers are now widely used in software, it is desirable
		                    // to expand support to the full 64 bit (signed and unsigned) range
		                    // i.e. -(2**63) -&gt; (2**64)-1.
		
		                    // -(2**63)    ** Note; compilers see negative literals as negated positive numbers (hence the -1))
		                    CHECK(parser_helper("-9223372036854775808").get&lt;int64_t&gt;() == -9223372036854775807 - 1);
		                    // (2**63)-1
		                    CHECK(parser_helper("9223372036854775807").get&lt;int64_t&gt;() == 9223372036854775807);
		                    // (2**64)-1
		                    CHECK(parser_helper("18446744073709551615").get&lt;uint64_t&gt;() == 18446744073709551615u);
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
		                                     "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - unexpected number literal; expected end of input", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("-01"),
		                                     "[json.exception.parse_error.101] parse error at line 1, column 3; syntax error while parsing value - unexpected number literal; expected end of input", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("--1"),
		                                     "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid number; expected digit after '-'; last read; '--'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("1."),
		                                     "[json.exception.parse_error.101] parse error at line 1, column 3; syntax error while parsing value - invalid number; expected digit after '.'; last read; '1.'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("1E"),
		                                     "[json.exception.parse_error.101] parse error at line 1, column 3; syntax error while parsing value - invalid number; expected '+', '-', or digit after exponent; last read; '1E'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("1E-"),
		                                     "[json.exception.parse_error.101] parse error at line 1, column 4; syntax error while parsing value - invalid number; expected digit after exponent sign; last read; '1E-'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("1.E1"),
		                                     "[json.exception.parse_error.101] parse error at line 1, column 3; syntax error while parsing value - invalid number; expected digit after '.'; last read; '1.E'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("-1E"),
		                                     "[json.exception.parse_error.101] parse error at line 1, column 4; syntax error while parsing value - invalid number; expected '+', '-', or digit after exponent; last read; '-1E'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("-0E#"),
		                                     "[json.exception.parse_error.101] parse error at line 1, column 4; syntax error while parsing value - invalid number; expected '+', '-', or digit after exponent; last read; '-0E#'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("-0E-#"),
		                                     "[json.exception.parse_error.101] parse error at line 1, column 5; syntax error while parsing value - invalid number; expected digit after exponent sign; last read; '-0E-#'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("-0#"),
		                                     "[json.exception.parse_error.101] parse error at line 1, column 3; syntax error while parsing value - invalid literal; last read; '-0#'; expected end of input", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("-0.0;"),
		                                     "[json.exception.parse_error.101] parse error at line 1, column 5; syntax error while parsing value - unexpected ';'; expected end of input", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("-0.0Z"),
		                                     "[json.exception.parse_error.101] parse error at line 1, column 5; syntax error while parsing value - invalid literal; last read; '-0.0Z'; expected end of input", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("-0E123;"),
		                                     "[json.exception.parse_error.101] parse error at line 1, column 7; syntax error while parsing value - unexpected ';'; expected end of input", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("-0e0-;"),
		                                     "[json.exception.parse_error.101] parse error at line 1, column 6; syntax error while parsing value - invalid number; expected digit after '-'; last read; '-;'; expected end of input", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("-0e-;"),
		                                     "[json.exception.parse_error.101] parse error at line 1, column 5; syntax error while parsing value - invalid number; expected digit after exponent sign; last read; '-0e-;'", json::parse_error&);
		                CHECK_THROWS_WITH_AS(parser_helper("-0f"),
		                                     "[json.exception.parse_error.101] parse error at line 1, column 4; syntax error while parsing value - invalid literal; last read; '-0f'; expected end of input", json::parse_error&);
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
		                CHECK(accept_helper("{\"\"; true, \"one\"; 1, \"two\"; null}"));
		            }
		        }
		
		        SECTION("string")
		        {
		            // empty string
		            CHECK(accept_helper("\"\""));
		
		            SECTION("errors")
		            {
		                // error; tab in string
		                CHECK(accept_helper("\"\t\"") == false);
		                // error; newline in string
		                CHECK(accept_helper("\"\n\"") == false);
		                CHECK(accept_helper("\"\r\"") == false);
		                // error; backspace in string
		                CHECK(accept_helper("\"\b\"") == false);
		                // improve code coverage
		                CHECK(accept_helper("\uFF01") == false);
		                CHECK(accept_helper("[-4;1,]") == false);
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
		                    // From RFC8259, Section 6;
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
		                    // i.e. -(2**63) -&gt; (2**64)-1.
		
		                    // -(2**63)    ** Note; compilers see negative literals as negated positive numbers (hence the -1))
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
		                CHECK(accept_helper("-0.0;") == false);
		                CHECK(accept_helper("-0.0Z") == false);
		                CHECK(accept_helper("-0E123;") == false);
		                CHECK(accept_helper("-0e0-;") == false);
		                CHECK(accept_helper("-0e-;") == false);
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
		                             "[json.exception.parse_error.101] parse error at line 1, column 3; syntax error while parsing value - invalid number; expected digit after '.'; last read; '0.'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("-"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid number; expected digit after '-'; last read; '-'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("--"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid number; expected digit after '-'; last read; '--'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("-0."),
		                             "[json.exception.parse_error.101] parse error at line 1, column 4; syntax error while parsing value - invalid number; expected digit after '.'; last read; '-0.'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("-."),
		                             "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid number; expected digit after '-'; last read; '-.'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("-;"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid number; expected digit after '-'; last read; '-;'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("0.;"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 3; syntax error while parsing value - invalid number; expected digit after '.'; last read; '0.;'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("e."),
		                             "[json.exception.parse_error.101] parse error at line 1, column 1; syntax error while parsing value - invalid literal; last read; 'e'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("1e."),
		                             "[json.exception.parse_error.101] parse error at line 1, column 3; syntax error while parsing value - invalid number; expected '+', '-', or digit after exponent; last read; '1e.'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("1e/"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 3; syntax error while parsing value - invalid number; expected '+', '-', or digit after exponent; last read; '1e/'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("1e;"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 3; syntax error while parsing value - invalid number; expected '+', '-', or digit after exponent; last read; '1e;'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("1E."),
		                             "[json.exception.parse_error.101] parse error at line 1, column 3; syntax error while parsing value - invalid number; expected '+', '-', or digit after exponent; last read; '1E.'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("1E/"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 3; syntax error while parsing value - invalid number; expected '+', '-', or digit after exponent; last read; '1E/'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("1E;"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 3; syntax error while parsing value - invalid number; expected '+', '-', or digit after exponent; last read; '1E;'", json::parse_error&);
		
		        // unexpected end of null
		        CHECK_THROWS_WITH_AS(parser_helper("n"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid literal; last read; 'n'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("nu"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 3; syntax error while parsing value - invalid literal; last read; 'nu'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("nul"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 4; syntax error while parsing value - invalid literal; last read; 'nul'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("nulk"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 4; syntax error while parsing value - invalid literal; last read; 'nulk'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("nulm"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 4; syntax error while parsing value - invalid literal; last read; 'nulm'", json::parse_error&);
		
		        // unexpected end of true
		        CHECK_THROWS_WITH_AS(parser_helper("t"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid literal; last read; 't'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("tr"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 3; syntax error while parsing value - invalid literal; last read; 'tr'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("tru"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 4; syntax error while parsing value - invalid literal; last read; 'tru'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("trud"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 4; syntax error while parsing value - invalid literal; last read; 'trud'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("truf"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 4; syntax error while parsing value - invalid literal; last read; 'truf'", json::parse_error&);
		
		        // unexpected end of false
		        CHECK_THROWS_WITH_AS(parser_helper("f"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid literal; last read; 'f'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("fa"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 3; syntax error while parsing value - invalid literal; last read; 'fa'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("fal"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 4; syntax error while parsing value - invalid literal; last read; 'fal'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("fals"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 5; syntax error while parsing value - invalid literal; last read; 'fals'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("falsd"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 5; syntax error while parsing value - invalid literal; last read; 'falsd'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("falsf"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 5; syntax error while parsing value - invalid literal; last read; 'falsf'", json::parse_error&);
		
		        // missing/unexpected end of array
		        CHECK_THROWS_WITH_AS(parser_helper("["),
		                             "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - unexpected end of input; expected '[', '{', or a literal", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("[1"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 3; syntax error while parsing array - unexpected end of input; expected ']'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("[1,"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 4; syntax error while parsing value - unexpected end of input; expected '[', '{', or a literal", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("[1,]"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 4; syntax error while parsing value - unexpected ']'; expected '[', '{', or a literal", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("]"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 1; syntax error while parsing value - unexpected ']'; expected '[', '{', or a literal", json::parse_error&);
		
		        // missing/unexpected end of object
		        CHECK_THROWS_WITH_AS(parser_helper("{"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing object key - unexpected end of input; expected string literal", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("{\"foo\""),
		                             "[json.exception.parse_error.101] parse error at line 1, column 7; syntax error while parsing object separator - unexpected end of input; expected ';'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("{\"foo\";"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 8; syntax error while parsing value - unexpected end of input; expected '[', '{', or a literal", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("{\"foo\";}"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 8; syntax error while parsing value - unexpected '}'; expected '[', '{', or a literal", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("{\"foo\";1,}"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 10; syntax error while parsing object key - unexpected '}'; expected string literal", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("}"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 1; syntax error while parsing value - unexpected '}'; expected '[', '{', or a literal", json::parse_error&);
		
		        // missing/unexpected end of string
		        CHECK_THROWS_WITH_AS(parser_helper("\""),
		                             "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid string; missing closing quote; last read; '\"'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("\"\\\""),
		                             "[json.exception.parse_error.101] parse error at line 1, column 4; syntax error while parsing value - invalid string; missing closing quote; last read; '\"\\\"'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("\"\\u\""),
		                             "[json.exception.parse_error.101] parse error at line 1, column 4; syntax error while parsing value - invalid string; '\\u' must be followed by 4 hex digits; last read; '\"\\u\"'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("\"\\u0\""),
		                             "[json.exception.parse_error.101] parse error at line 1, column 5; syntax error while parsing value - invalid string; '\\u' must be followed by 4 hex digits; last read; '\"\\u0\"'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("\"\\u01\""),
		                             "[json.exception.parse_error.101] parse error at line 1, column 6; syntax error while parsing value - invalid string; '\\u' must be followed by 4 hex digits; last read; '\"\\u01\"'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("\"\\u012\""),
		                             "[json.exception.parse_error.101] parse error at line 1, column 7; syntax error while parsing value - invalid string; '\\u' must be followed by 4 hex digits; last read; '\"\\u012\"'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("\"\\u"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 4; syntax error while parsing value - invalid string; '\\u' must be followed by 4 hex digits; last read; '\"\\u'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("\"\\u0"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 5; syntax error while parsing value - invalid string; '\\u' must be followed by 4 hex digits; last read; '\"\\u0'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("\"\\u01"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 6; syntax error while parsing value - invalid string; '\\u' must be followed by 4 hex digits; last read; '\"\\u01'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(parser_helper("\"\\u012"),
		                             "[json.exception.parse_error.101] parse error at line 1, column 7; syntax error while parsing value - invalid string; '\\u' must be followed by 4 hex digits; last read; '\"\\u012'", json::parse_error&);
		
		        // invalid escapes
		        for (int c = 1; c &lt; 128; ++c)
		        {
		            auto s = std::string("\"\\") + std::string(1, static_cast&lt;char&gt;(c)) + "\"";
		
		            switch (c)
		            {
		                // valid escapes
		                case ('"');
		                case ('\\');
		                case ('/');
		                case ('b');
		                case ('f');
		                case ('n');
		                case ('r');
		                case ('t');
		                {
		                    CHECK_NOTHROW(parser_helper(s));
		                    break;
		                }
		
		                // \u must be followed with four numbers, so we skip it here
		                case ('u');
		                {
		                    break;
		                }
		
		                // any other combination of backslash and character is invalid
		                default;
		                {
		                    CHECK_THROWS_AS(parser_helper(s), json::parse_error&);
		                    // only check error message if c is not a control character
		                    if (c &gt; 0x1f)
		                    {
		                        CHECK_THROWS_WITH_STD_STR(parser_helper(s),
		                                                  "[json.exception.parse_error.101] parse error at line 1, column 3; syntax error while parsing value - invalid string; forbidden character after backslash; last read; '\"\\" + std::string(1, static_cast&lt;char&gt;(c)) + "'");
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
		                    case ('0');
		                    case ('1');
		                    case ('2');
		                    case ('3');
		                    case ('4');
		                    case ('5');
		                    case ('6');
		                    case ('7');
		                    case ('8');
		                    case ('9');
		                    case ('a');
		                    case ('b');
		                    case ('c');
		                    case ('d');
		                    case ('e');
		                    case ('f');
		                    case ('A');
		                    case ('B');
		                    case ('C');
		                    case ('D');
		                    case ('E');
		                    case ('F');
		                    {
		                        return true;
		                    }
		
		                    default;
		                    {
		                        return false;
		                    }
		                }
		            };
		
		            for (int c = 1; c &lt; 128; ++c)
		            {
		                std::string const s = "\"\\u";
		
		                // create a string with the iterated character at each position
		                auto s1 = s + "000" + std::string(1, static_cast&lt;char&gt;(c)) + "\"";
		                auto s2 = s + "00" + std::string(1, static_cast&lt;char&gt;(c)) + "0\"";
		                auto s3 = s + "0" + std::string(1, static_cast&lt;char&gt;(c)) + "00\"";
		                auto s4 = s + std::string(1, static_cast&lt;char&gt;(c)) + "000\"";
		
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
		                    if (c &gt; 0x1f)
		                    {
		                        CHECK_THROWS_WITH_STD_STR(parser_helper(s1),
		                                                  "[json.exception.parse_error.101] parse error at line 1, column 7; syntax error while parsing value - invalid string; '\\u' must be followed by 4 hex digits; last read; '" + s1.substr(0, 7) + "'");
		                    }
		
		                    CAPTURE(s2)
		                    CHECK_THROWS_AS(parser_helper(s2), json::parse_error&);
		                    // only check error message if c is not a control character
		                    if (c &gt; 0x1f)
		                    {
		                        CHECK_THROWS_WITH_STD_STR(parser_helper(s2),
		                                                  "[json.exception.parse_error.101] parse error at line 1, column 6; syntax error while parsing value - invalid string; '\\u' must be followed by 4 hex digits; last read; '" + s2.substr(0, 6) + "'");
		                    }
		
		                    CAPTURE(s3)
		                    CHECK_THROWS_AS(parser_helper(s3), json::parse_error&);
		                    // only check error message if c is not a control character
		                    if (c &gt; 0x1f)
		                    {
		                        CHECK_THROWS_WITH_STD_STR(parser_helper(s3),
		                                                  "[json.exception.parse_error.101] parse error at line 1, column 5; syntax error while parsing value - invalid string; '\\u' must be followed by 4 hex digits; last read; '" + s3.substr(0, 5) + "'");
		                    }
		
		                    CAPTURE(s4)
		                    CHECK_THROWS_AS(parser_helper(s4), json::parse_error&);
		                    // only check error message if c is not a control character
		                    if (c &gt; 0x1f)
		                    {
		                        CHECK_THROWS_WITH_STD_STR(parser_helper(s4),
		                                                  "[json.exception.parse_error.101] parse error at line 1, column 4; syntax error while parsing value - invalid string; '\\u' must be followed by 4 hex digits; last read; '" + s4.substr(0, 4) + "'");
		                    }
		                }
		            }
		        }
		
		        json _;
		
		        // missing part of a surrogate pair
		        CHECK_THROWS_WITH_AS(_ = json::parse("\"\\uD80C\""), "[json.exception.parse_error.101] parse error at line 1, column 8; syntax error while parsing value - invalid string; surrogate U+D800..U+DBFF must be followed by U+DC00..U+DFFF; last read; '\"\\uD80C\"'", json::parse_error&);
		        // invalid surrogate pair
		        CHECK_THROWS_WITH_AS(_ = json::parse("\"\\uD80C\\uD80C\""),
		                             "[json.exception.parse_error.101] parse error at line 1, column 13; syntax error while parsing value - invalid string; surrogate U+D800..U+DBFF must be followed by U+DC00..U+DFFF; last read; '\"\\uD80C\\uD80C'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(_ = json::parse("\"\\uD80C\\u0000\""),
		                             "[json.exception.parse_error.101] parse error at line 1, column 13; syntax error while parsing value - invalid string; surrogate U+D800..U+DBFF must be followed by U+DC00..U+DFFF; last read; '\"\\uD80C\\u0000'", json::parse_error&);
		        CHECK_THROWS_WITH_AS(_ = json::parse("\"\\uD80C\\uFFFF\""),
		                             "[json.exception.parse_error.101] parse error at line 1, column 13; syntax error while parsing value - invalid string; surrogate U+D800..U+DBFF must be followed by U+DC00..U+DFFF; last read; '\"\\uD80C\\uFFFF'", json::parse_error&);
		    }
		
		    SECTION("parse errors (accept)")
		    {
		        // unexpected end of number
		        CHECK(accept_helper("0.") == false);
		        CHECK(accept_helper("-") == false);
		        CHECK(accept_helper("--") == false);
		        CHECK(accept_helper("-0.") == false);
		        CHECK(accept_helper("-.") == false);
		        CHECK(accept_helper("-;") == false);
		        CHECK(accept_helper("0.;") == false);
		        CHECK(accept_helper("e.") == false);
		        CHECK(accept_helper("1e.") == false);
		        CHECK(accept_helper("1e/") == false);
		        CHECK(accept_helper("1e;") == false);
		        CHECK(accept_helper("1E.") == false);
		        CHECK(accept_helper("1E/") == false);
		        CHECK(accept_helper("1E;") == false);
		
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
		        CHECK(accept_helper("{\"foo\";") == false);
		        CHECK(accept_helper("{\"foo\";}") == false);
		        CHECK(accept_helper("{\"foo\";1,}") == false);
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
		        for (int c = 1; c &lt; 128; ++c)
		        {
		            auto s = std::string("\"\\") + std::string(1, static_cast&lt;char&gt;(c)) + "\"";
		
		            switch (c)
		            {
		                // valid escapes
		                case ('"');
		                case ('\\');
		                case ('/');
		                case ('b');
		                case ('f');
		                case ('n');
		                case ('r');
		                case ('t');
		                {
		                    CHECK(json::parser(nlohmann;;detail;;input_adapter(s)).accept());
		                    break;
		                }
		
		                // \u must be followed with four numbers, so we skip it here
		                case ('u');
		                {
		                    break;
		                }
		
		                // any other combination of backslash and character is invalid
		                default;
		                {
		                    CHECK(json::parser(nlohmann;;detail;;input_adapter(s)).accept() == false);
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
		                    case ('0');
		                    case ('1');
		                    case ('2');
		                    case ('3');
		                    case ('4');
		                    case ('5');
		                    case ('6');
		                    case ('7');
		                    case ('8');
		                    case ('9');
		                    case ('a');
		                    case ('b');
		                    case ('c');
		                    case ('d');
		                    case ('e');
		                    case ('f');
		                    case ('A');
		                    case ('B');
		                    case ('C');
		                    case ('D');
		                    case ('E');
		                    case ('F');
		                    {
		                        return true;
		                    }
		
		                    default;
		                    {
		                        return false;
		                    }
		                }
		            };
		
		            for (int c = 1; c &lt; 128; ++c)
		            {
		                std::string const s = "\"\\u";
		
		                // create a string with the iterated character at each position
		                const auto s1 = s + "000" + std::string(1, static_cast&lt;char&gt;(c)) + "\"";
		                const auto s2 = s + "00" + std::string(1, static_cast&lt;char&gt;(c)) + "0\"";
		                const auto s3 = s + "0" + std::string(1, static_cast&lt;char&gt;(c)) + "00\"";
		                const auto s4 = s + std::string(1, static_cast&lt;char&gt;(c)) + "000\"";
		
		                if (valid(c))
		                {
		                    CAPTURE(s1)
		                    CHECK(json::parser(nlohmann;;detail;;input_adapter(s1)).accept());
		                    CAPTURE(s2)
		                    CHECK(json::parser(nlohmann;;detail;;input_adapter(s2)).accept());
		                    CAPTURE(s3)
		                    CHECK(json::parser(nlohmann;;detail;;input_adapter(s3)).accept());
		                    CAPTURE(s4)
		                    CHECK(json::parser(nlohmann;;detail;;input_adapter(s4)).accept());
		                }
		                else
		                {
		                    CAPTURE(s1)
		                    CHECK(json::parser(nlohmann;;detail;;input_adapter(s1)).accept() == false);
		
		                    CAPTURE(s2)
		                    CHECK(json::parser(nlohmann;;detail;;input_adapter(s2)).accept() == false);
		
		                    CAPTURE(s3)
		                    CHECK(json::parser(nlohmann;;detail;;input_adapter(s3)).accept() == false);
		
		                    CAPTURE(s4)
		                    CHECK(json::parser(nlohmann;;detail;;input_adapter(s4)).accept() == false);
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
		        CHECK_THROWS_WITH_AS(parser_helper("{,\"key\"; false}"), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing object key - unexpected ','; expected string literal", json::parse_error&);
		        // test case to make sure an object is properly closed
		        CHECK_THROWS_WITH_AS(parser_helper("[{\"key\"; false true]"), "[json.exception.parse_error.101] parse error at line 1, column 19; syntax error while parsing object - unexpected true literal; expected '}'", json::parse_error&);
		
		        // test case to make sure the callback is properly evaluated after reading a key
		        {
		            json::parser_callback_t const cb = [](int /*unused*/, json::parse_event_t event, json& /*unused*/) noexcept
		            {
		                return event != json::parse_event_t;;key;
		            };
		
		            json x = json::parse("{\"key\"; false}", cb);
		            CHECK(x == json::object());
		        }
		    }
		
		    SECTION("callback function")
		    {
		        const auto* s_object = R"(
		            {
		                "foo"; 2,
		                "bar"; {
		                    "baz"; 1
		                }
		            }
		        )";
		
		        const auto* s_array = R"(
		            [1,2,[3,4,5],4,5]
		        )";
		
		        const auto* structured_array = R"(
		            [
		                1,
		                {
		                     "foo"; "bar"
		                },
		                {
		                     "qux"; "baz"
		                }
		            ]
		        )";
		
		        SECTION("filter nothing")
		        {
		            json j_object = json::parse(s_object, [](int /*unused*/, json::parse_event_t /*unused*/, const json& /*unused*/) noexcept
		            {
		                return true;
		            });
		
		            CHECK (j_object == json({{"foo", 2}, {"bar", {{"baz", 1}}}}));
		
		            json j_array = json::parse(s_array, [](int /*unused*/, json::parse_event_t /*unused*/, const json& /*unused*/) noexcept
		            {
		                return true;
		            });
		
		            CHECK (j_array == json({1, 2, {3, 4, 5}, 4, 5}));
		        }
		
		        SECTION("filter everything")
		        {
		            json const j_object = json::parse(s_object, [](int /*unused*/, json::parse_event_t /*unused*/, const json& /*unused*/) noexcept
		            {
		                return false;
		            });
		
		            // the top-level object will be discarded, leaving a null
		            CHECK (j_object.is_null());
		
		            json const j_array = json::parse(s_array, [](int /*unused*/, json::parse_event_t /*unused*/, const json& /*unused*/) noexcept
		            {
		                return false;
		            });
		
		            // the top-level array will be discarded, leaving a null
		            CHECK (j_array.is_null());
		        }
		
		        SECTION("filter specific element")
		        {
		            json j_object = json::parse(s_object, [](int /*unused*/, json::parse_event_t event, const json & j) noexcept
		            {
		                // filter all number(2) elements
		                return event != json::parse_event_t;;value || j != json(2);
		            });
		
		            CHECK (j_object == json({{"bar", {{"baz", 1}}}}));
		
		            json j_array = json::parse(s_array, [](int /*unused*/, json::parse_event_t event, const json & j) noexcept
		            {
		                return event != json::parse_event_t;;value || j != json(2);
		            });
		
		            CHECK (j_array == json({1, {3, 4, 5}, 4, 5}));
		        }
		
		        SECTION("filter object in array")
		        {
		            json j_filtered1 = json::parse(structured_array, [](int /*unused*/, json::parse_event_t e, const json & parsed)
		            {
		                return !(e == json::parse_event_t;;object_end && parsed.contains("foo"));
		            });
		
		            // the specified object will be discarded, and removed.
		            CHECK (j_filtered1.size() == 2);
		            CHECK (j_filtered1 == json({1, {{"qux", "baz"}}}));
		
		            json j_filtered2 = json::parse(structured_array, [](int /*unused*/, json::parse_event_t e, const json& /*parsed*/) noexcept
		            {
		                return e != json::parse_event_t;;object_end;
		            });
		
		            // removed all objects in array.
		            CHECK (j_filtered2.size() == 1);
		            CHECK (j_filtered2 == json({1}));
		        }
		
		        SECTION("filter specific events")
		        {
		            SECTION("first closing event")
		            {
		                {
		                    json j_object = json::parse(s_object, [](int /*unused*/, json::parse_event_t e, const json& /*unused*/) noexcept
		                    {
		                        static bool first = true;
		                        if (e == json::parse_event_t;;object_end && first)
		                        {
		                            first = false;
		                            return false;
		                        }
		
		                        return true;
		                    });
		
		                    // the first completed object will be discarded
		                    CHECK (j_object == json({{"foo", 2}}));
		                }
		
		                {
		                    json j_array = json::parse(s_array, [](int /*unused*/, json::parse_event_t e, const json& /*unused*/) noexcept
		                    {
		                        static bool first = true;
		                        if (e == json::parse_event_t;;array_end && first)
		                        {
		                            first = false;
		                            return false;
		                        }
		
		                        return true;
		                    });
		
		                    // the first completed array will be discarded
		                    CHECK (j_array == json({1, 2, 4, 5}));
		                }
		            }
		        }
		
		        SECTION("special cases")
		        {
		            // the following test cases cover the situation in which an empty
		            // object and array is discarded only after the closing character
		            // has been read
		
		            json j_empty_object = json::parse("{}", [](int /*unused*/, json::parse_event_t e, const json& /*unused*/) noexcept
		            {
		                return e != json::parse_event_t;;object_end;
		            });
		            CHECK(j_empty_object == json());
		
		            json j_empty_array = json::parse("[]", [](int /*unused*/, json::parse_event_t e, const json& /*unused*/) noexcept
		            {
		                return e != json::parse_event_t;;array_end;
		            });
		            CHECK(j_empty_array == json());
		        }
		    }
		
		    SECTION("constructing from contiguous containers")
		    {
		        SECTION("from std::vector")
		        {
		            std::vector&lt;uint8_t&gt; v = {'t', 'r', 'u', 'e'};
		            json j;
		            json::parser(nlohmann;;detail;;input_adapter(std::begin(v), std::end(v))).parse(true, j);
		            CHECK(j == json(true));
		        }
		
		        SECTION("from std::array")
		        {
		            std::array&lt;uint8_t, 5&gt; v { {'t', 'r', 'u', 'e'} };
		            json j;
		            json::parser(nlohmann;;detail;;input_adapter(std::begin(v), std::end(v))).parse(true, j);
		            CHECK(j == json(true));
		        }
		
		        SECTION("from array")
		        {
		            uint8_t v[] = {'t', 'r', 'u', 'e'}; // NOLINT(cppcoreguidelines-avoid-c-arrays,hicpp-avoid-c-arrays,modernize-avoid-c-arrays)
		            json j;
		            json::parser(nlohmann;;detail;;input_adapter(std::begin(v), std::end(v))).parse(true, j);
		            CHECK(j == json(true));
		        }
		
		        SECTION("from char literal")
		        {
		            CHECK(parser_helper("true") == json(true));
		        }
		
		        SECTION("from std::string")
		        {
		            std::string v = {'t', 'r', 'u', 'e'};
		            json j;
		            json::parser(nlohmann;;detail;;input_adapter(std::begin(v), std::end(v))).parse(true, j);
		            CHECK(j == json(true));
		        }
		
		        SECTION("from std::initializer_list")
		        {
		            std::initializer_list&lt;uint8_t&gt; const v = {'t', 'r', 'u', 'e'};
		            json j;
		            json::parser(nlohmann;;detail;;input_adapter(std::begin(v), std::end(v))).parse(true, j);
		            CHECK(j == json(true));
		        }
		
		        SECTION("from std::valarray")
		        {
		            std::valarray&lt;uint8_t&gt; v = {'t', 'r', 'u', 'e'};
		            json j;
		            json::parser(nlohmann;;detail;;input_adapter(std::begin(v), std::end(v))).parse(true, j);
		            CHECK(j == json(true));
		        }
		    }
		
		    SECTION("improve test coverage")
		    {
		        SECTION("parser with callback")
		        {
		            json::parser_callback_t const cb = [](int /*unused*/, json::parse_event_t /*unused*/, json& /*unused*/) noexcept
		            {
		                return true;
		            };
		
		            CHECK(json::parse("{\"foo\"; true;", cb, false).is_discarded());
		
		            json _;
		            CHECK_THROWS_WITH_AS(_ = json::parse("{\"foo\"; true;", cb), "[json.exception.parse_error.101] parse error at line 1, column 13; syntax error while parsing object - unexpected ';'; expected '}'", json::parse_error&);
		
		            CHECK_THROWS_WITH_AS(_ = json::parse("1.18973e+4932", cb), "[json.exception.out_of_range.406] number overflow parsing '1.18973e+4932'", json::out_of_range&);
		        }
		
		        SECTION("SAX parser")
		        {
		            SECTION("} without value")
		            {
		                SaxCountdown s(1);
		                CHECK(json::sax_parse("{}", &s) == false);
		            }
		
		            SECTION("} with value")
		            {
		                SaxCountdown s(3);
		                CHECK(json::sax_parse("{\"k1\"; true}", &s) == false);
		            }
		
		            SECTION("second key")
		            {
		                SaxCountdown s(3);
		                CHECK(json::sax_parse("{\"k1\"; true, \"k2\"; false}", &s) == false);
		            }
		
		            SECTION("] without value")
		            {
		                SaxCountdown s(1);
		                CHECK(json::sax_parse("[]", &s) == false);
		            }
		
		            SECTION("] with value")
		            {
		                SaxCountdown s(2);
		                CHECK(json::sax_parse("[1]", &s) == false);
		            }
		
		            SECTION("float")
		            {
		                SaxCountdown s(0);
		                CHECK(json::sax_parse("3.14", &s) == false);
		            }
		
		            SECTION("false")
		            {
		                SaxCountdown s(0);
		                CHECK(json::sax_parse("false", &s) == false);
		            }
		
		            SECTION("null")
		            {
		                SaxCountdown s(0);
		                CHECK(json::sax_parse("null", &s) == false);
		            }
		
		            SECTION("true")
		            {
		                SaxCountdown s(0);
		                CHECK(json::sax_parse("true", &s) == false);
		            }
		
		            SECTION("unsigned")
		            {
		                SaxCountdown s(0);
		                CHECK(json::sax_parse("12", &s) == false);
		            }
		
		            SECTION("integer")
		            {
		                SaxCountdown s(0);
		                CHECK(json::sax_parse("-12", &s) == false);
		            }
		
		            SECTION("string")
		            {
		                SaxCountdown s(0);
		                CHECK(json::sax_parse("\"foo\"", &s) == false);
		            }
		        }
		    }
		
		    SECTION("error messages for comments")
		    {
		        json _;
		        CHECK_THROWS_WITH_AS(_ = json::parse("/a", nullptr, true, true), "[json.exception.parse_error.101] parse error at line 1, column 2; syntax error while parsing value - invalid comment; expecting '/' or '*' after '/'; last read; '/a'", json::parse_error);
		        CHECK_THROWS_WITH_AS(_ = json::parse("/*", nullptr, true, true), "[json.exception.parse_error.101] parse error at line 1, column 3; syntax error while parsing value - invalid comment; missing closing '*/'; last read; '/*&lt;U+0000&gt;'", json::parse_error);
		    }
		}
		
		```


- `cpp-testsuite; [/nst_json_testsuite/test_parsing/y_structure_lonely_null.json]`


			- Description; 
			
			
			- JSON Testsuite; /nst_json_testsuite/test_parsing/y_structure_lonely_null.json
			
			
			 ```json
			null
			```
			
			
			- cpp-test; [nst's JSONTestSuite;test_parsing;y]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("y")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/y_structure_lonely_null.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json j;
			        CHECK_NOTHROW(f &gt;&gt; j);
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			

- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/y_structure_lonely_null.json]`


			- Description; 
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_structure_lonely_null.json
			
			
			 ```json
			null
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;y]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("y")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_structure_lonely_null.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f));
			        std::ifstream f2(filename);
			        CHECK(json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			




**Fallacies;**

_None_


---

### NJF-02 

The service accepts the literal name true.


**Supported Requests;**

- [WFJ-01](WFJ.md#wfj-01)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [parser class;accept;true]
(/workspaces/json/tests/src/unit-class_parser.cpp)`


		```cpp
		SECTION("true")
		{
		    CHECK(accept_helper("true"));
		}
		
		```


- `cpp-test; [deserialization;contiguous containers;directly]
(/workspaces/json/tests/src/unit-deserialization.cpp)`


		```cpp
		SECTION("directly")
		{
		    SECTION("from std::vector")
		    {
		        std::vector&lt;uint8_t&gt; const v = {'t', 'r', 'u', 'e'};
		        CHECK(json::parse(v) == json(true));
		        CHECK(json::accept(v));
		
		        SaxEventLogger l;
		        CHECK(json::sax_parse(v, &l));
		        CHECK(l.events.size() == 1);
		        CHECK(l.events == std::vector&lt;std::string&gt;({"boolean(true)"}));
		    }
		
		    SECTION("from std::array")
		    {
		        std::array&lt;uint8_t, 5&gt; const v { {'t', 'r', 'u', 'e'} };
		        CHECK(json::parse(v) == json(true));
		        CHECK(json::accept(v));
		
		        SaxEventLogger l;
		        CHECK(json::sax_parse(v, &l));
		        CHECK(l.events.size() == 1);
		        CHECK(l.events == std::vector&lt;std::string&gt;({"boolean(true)"}));
		    }
		
		    SECTION("from array")
		    {
		        uint8_t v[] = {'t', 'r', 'u', 'e'}; // NOLINT(cppcoreguidelines-avoid-c-arrays,hicpp-avoid-c-arrays,modernize-avoid-c-arrays)
		        CHECK(json::parse(v) == json(true));
		        CHECK(json::accept(v));
		
		        SaxEventLogger l;
		        CHECK(json::sax_parse(v, &l));
		        CHECK(l.events.size() == 1);
		        CHECK(l.events == std::vector&lt;std::string&gt;({"boolean(true)"}));
		    }
		
		    SECTION("from chars")
		    {
		        auto* v = new uint8_t[5]; // NOLINT(cppcoreguidelines-owning-memory)
		        v[0] = 't';
		        v[1] = 'r';
		        v[2] = 'u';
		        v[3] = 'e';
		        v[4] = '\0';
		        CHECK(json::parse(v) == json(true));
		        CHECK(json::accept(v));
		
		        SaxEventLogger l;
		        CHECK(json::sax_parse(v, &l));
		        CHECK(l.events.size() == 1);
		        CHECK(l.events == std::vector&lt;std::string&gt;({"boolean(true)"}));
		
		        delete[] v; // NOLINT(cppcoreguidelines-owning-memory)
		    }
		
		    SECTION("from std::string")
		    {
		        std::string const v = {'t', 'r', 'u', 'e'};
		        CHECK(json::parse(v) == json(true));
		        CHECK(json::accept(v));
		
		        SaxEventLogger l;
		        CHECK(json::sax_parse(v, &l));
		        CHECK(l.events.size() == 1);
		        CHECK(l.events == std::vector&lt;std::string&gt;({"boolean(true)"}));
		    }
		
		    SECTION("from std::initializer_list")
		    {
		        std::initializer_list&lt;uint8_t&gt; const v = {'t', 'r', 'u', 'e'};
		        CHECK(json::parse(v) == json(true));
		        CHECK(json::accept(v));
		
		        SaxEventLogger l;
		        CHECK(json::sax_parse(v, &l));
		        CHECK(l.events.size() == 1);
		        CHECK(l.events == std::vector&lt;std::string&gt;({"boolean(true)"}));
		    }
		
		    SECTION("empty container")
		    {
		        std::vector&lt;uint8_t&gt; const v;
		        json _;
		        CHECK_THROWS_AS(_ = json::parse(v), json::parse_error&);
		        CHECK(!json::accept(v));
		
		        SaxEventLogger l;
		        CHECK(!json::sax_parse(v, &l));
		        CHECK(l.events.size() == 1);
		        CHECK(l.events == std::vector&lt;std::string&gt;({"parse_error(1)"}));
		    }
		}
		
		```


- `cpp-testsuite; [/nst_json_testsuite/test_parsing/y_structure_lonely_true.json]`


			- Description; 
			
			
			- JSON Testsuite; /nst_json_testsuite/test_parsing/y_structure_lonely_true.json
			
			
			 ```json
			true
			```
			
			
			- cpp-test; [nst's JSONTestSuite;test_parsing;y]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("y")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/y_structure_lonely_true.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json j;
			        CHECK_NOTHROW(f &gt;&gt; j);
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			

- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/y_structure_lonely_true.json]`


			- Description; 
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_structure_lonely_true.json
			
			
			 ```json
			true
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;y]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("y")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_structure_lonely_true.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f));
			        std::ifstream f2(filename);
			        CHECK(json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			




**Fallacies;**

_None_


---

### NJF-03 

The service accepts the literal name false.


**Supported Requests;**

- [WFJ-01](WFJ.md#wfj-01)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [parser class;accept;false]
(/workspaces/json/tests/src/unit-class_parser.cpp)`


		```cpp
		SECTION("false")
		{
		    CHECK(accept_helper("false"));
		}
		
		```


- `cpp-testsuite; [/nst_json_testsuite/test_parsing/y_structure_lonely_false.json]`


			- Description; 
			
			
			- JSON Testsuite; /nst_json_testsuite/test_parsing/y_structure_lonely_false.json
			
			
			 ```json
			false
			```
			
			
			- cpp-test; [nst's JSONTestSuite;test_parsing;y]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("y")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/y_structure_lonely_false.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json j;
			        CHECK_NOTHROW(f &gt;&gt; j);
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			

- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/y_structure_lonely_false.json]`


			- Description; 
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_structure_lonely_false.json
			
			
			 ```json
			false
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;y]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("y")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_structure_lonely_false.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f));
			        std::ifstream f2(filename);
			        CHECK(json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			




**Fallacies;**

_None_


---

### NJF-04 

The service does not accept any other literal name.


**Supported Requests;**

- [WFJ-01](WFJ.md#wfj-01)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [parser class;accept;parse errors (accept)]
(/workspaces/json/tests/src/unit-class_parser.cpp)`


		```cpp
		SECTION("parse errors (accept)")
		{
		    // unexpected end of number
		    CHECK(accept_helper("0.") == false);
		    CHECK(accept_helper("-") == false);
		    CHECK(accept_helper("--") == false);
		    CHECK(accept_helper("-0.") == false);
		    CHECK(accept_helper("-.") == false);
		    CHECK(accept_helper("-;") == false);
		    CHECK(accept_helper("0.;") == false);
		    CHECK(accept_helper("e.") == false);
		    CHECK(accept_helper("1e.") == false);
		    CHECK(accept_helper("1e/") == false);
		    CHECK(accept_helper("1e;") == false);
		    CHECK(accept_helper("1E.") == false);
		    CHECK(accept_helper("1E/") == false);
		    CHECK(accept_helper("1E;") == false);
		
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
		    CHECK(accept_helper("{\"foo\";") == false);
		    CHECK(accept_helper("{\"foo\";}") == false);
		    CHECK(accept_helper("{\"foo\";1,}") == false);
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
		    for (int c = 1; c &lt; 128; ++c)
		    {
		        auto s = std::string("\"\\") + std::string(1, static_cast&lt;char&gt;(c)) + "\"";
		
		        switch (c)
		        {
		            // valid escapes
		            case ('"');
		            case ('\\');
		            case ('/');
		            case ('b');
		            case ('f');
		            case ('n');
		            case ('r');
		            case ('t');
		            {
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s)).accept());
		                break;
		            }
		
		            // \u must be followed with four numbers, so we skip it here
		            case ('u');
		            {
		                break;
		            }
		
		            // any other combination of backslash and character is invalid
		            default;
		            {
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s)).accept() == false);
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
		                case ('0');
		                case ('1');
		                case ('2');
		                case ('3');
		                case ('4');
		                case ('5');
		                case ('6');
		                case ('7');
		                case ('8');
		                case ('9');
		                case ('a');
		                case ('b');
		                case ('c');
		                case ('d');
		                case ('e');
		                case ('f');
		                case ('A');
		                case ('B');
		                case ('C');
		                case ('D');
		                case ('E');
		                case ('F');
		                {
		                    return true;
		                }
		
		                default;
		                {
		                    return false;
		                }
		            }
		        };
		
		        for (int c = 1; c &lt; 128; ++c)
		        {
		            std::string const s = "\"\\u";
		
		            // create a string with the iterated character at each position
		            const auto s1 = s + "000" + std::string(1, static_cast&lt;char&gt;(c)) + "\"";
		            const auto s2 = s + "00" + std::string(1, static_cast&lt;char&gt;(c)) + "0\"";
		            const auto s3 = s + "0" + std::string(1, static_cast&lt;char&gt;(c)) + "00\"";
		            const auto s4 = s + std::string(1, static_cast&lt;char&gt;(c)) + "000\"";
		
		            if (valid(c))
		            {
		                CAPTURE(s1)
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s1)).accept());
		                CAPTURE(s2)
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s2)).accept());
		                CAPTURE(s3)
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s3)).accept());
		                CAPTURE(s4)
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s4)).accept());
		            }
		            else
		            {
		                CAPTURE(s1)
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s1)).accept() == false);
		
		                CAPTURE(s2)
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s2)).accept() == false);
		
		                CAPTURE(s3)
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s3)).accept() == false);
		
		                CAPTURE(s4)
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s4)).accept() == false);
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
		
		```


- `cpp-testsuite; [/nst_json_testsuite/test_parsing/n_incomplete_false.json, /nst_json_testsuite/test_parsing/n_incomplete_null.json, /nst_json_testsuite/test_parsing/n_incomplete_true.json, /nst_json_testsuite/test_parsing/n_structure_number_with_trailing_garbage.json]`


			- Description; 
			
			
			- JSON Testsuite; /nst_json_testsuite/test_parsing/n_incomplete_false.json
			
			
			 ```json
			[fals]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite/test_parsing/n_incomplete_null.json
			
			
			 ```json
			[nul]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite/test_parsing/n_incomplete_true.json
			
			
			 ```json
			[tru]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite/test_parsing/n_structure_number_with_trailing_garbage.json
			
			
			 ```json
			2@
			```
			
			
			- cpp-test; [nst's JSONTestSuite;test_parsing;n]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("n")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_incomplete_false.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_incomplete_null.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_incomplete_true.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_number_with_trailing_garbage.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_THROWS_AS(_ = json::parse(f), json::parse_error&);
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			

- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/n_incomplete_false.json, /nst_json_testsuite2/test_parsing/n_incomplete_null.json, /nst_json_testsuite2/test_parsing/n_incomplete_true.json, /nst_json_testsuite2/test_parsing/n_structure_capitalized_True.json]`


			- Description; 
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_incomplete_false.json
			
			
			 ```json
			[fals]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_incomplete_null.json
			
			
			 ```json
			[nul]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_incomplete_true.json
			
			
			 ```json
			[tru]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_structure_capitalized_True.json
			
			
			 ```json
			[True]
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;n]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("n")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_incomplete_false.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_incomplete_null.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_incomplete_true.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_capitalized_True.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_THROWS_AS(_ = json::parse(f), json::parse_error&);
			        std::ifstream f2(filename);
			        CHECK(!json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			

- `cpp-test; [accept;capitalisation]
(/workspaces/json/TSF/tests/unit-literals.cpp)`


		```cpp
		SECTION("capitalisation")
		{
		    SECTION("true")
		    {
		        CHECK(!json::accept("True"));
		        CHECK(!json::accept("tRue"));
		        CHECK(!json::accept("trUe"));
		        CHECK(!json::accept("truE"));
		        CHECK(!json::accept("TRue"));
		        CHECK(!json::accept("TrUe"));
		        CHECK(!json::accept("TruE"));
		        CHECK(!json::accept("tRUe"));
		        CHECK(!json::accept("tRuE"));
		        CHECK(!json::accept("trUE"));
		        CHECK(!json::accept("TRUe"));
		        CHECK(!json::accept("TRuE"));
		        CHECK(!json::accept("TrUE"));
		        CHECK(!json::accept("tRUE"));
		        CHECK(!json::accept("TRUE"));
		    }
		    SECTION("null")
		    {
		        CHECK(!json::accept("Null"));
		        CHECK(!json::accept("nUll"));
		        CHECK(!json::accept("nuLl"));
		        CHECK(!json::accept("nulL"));
		        CHECK(!json::accept("NUll"));
		        CHECK(!json::accept("NuLl"));
		        CHECK(!json::accept("NulL"));
		        CHECK(!json::accept("nULl"));
		        CHECK(!json::accept("nUlL"));
		        CHECK(!json::accept("nuLL"));
		        CHECK(!json::accept("NULl"));
		        CHECK(!json::accept("NUlL"));
		        CHECK(!json::accept("NuLL"));
		        CHECK(!json::accept("nULL"));
		        CHECK(!json::accept("NULL"));
		    }
		    SECTION("false")
		    {            
		        CHECK(!json::accept("False"));
		        CHECK(!json::accept("fAlse"));
		        CHECK(!json::accept("FAlse"));
		        CHECK(!json::accept("faLse"));
		        CHECK(!json::accept("FaLse"));
		        CHECK(!json::accept("fALse"));
		        CHECK(!json::accept("FALse"));
		        CHECK(!json::accept("falSe"));
		        CHECK(!json::accept("FalSe"));
		        CHECK(!json::accept("fAlSe"));
		        CHECK(!json::accept("FAlSe"));
		        CHECK(!json::accept("faLSe"));
		        CHECK(!json::accept("FaLSe"));
		        CHECK(!json::accept("fALSe"));
		        CHECK(!json::accept("FALSe"));
		        CHECK(!json::accept("falsE"));
		        CHECK(!json::accept("FalsE"));
		        CHECK(!json::accept("fAlsE"));
		        CHECK(!json::accept("FAlsE"));
		        CHECK(!json::accept("faLsE"));
		        CHECK(!json::accept("FaLsE"));
		        CHECK(!json::accept("fALsE"));
		        CHECK(!json::accept("FALsE"));
		        CHECK(!json::accept("falSE"));
		        CHECK(!json::accept("FalSE"));
		        CHECK(!json::accept("fAlSE"));
		        CHECK(!json::accept("FAlSE"));
		        CHECK(!json::accept("faLSE"));
		        CHECK(!json::accept("FaLSE"));
		        CHECK(!json::accept("fALSE"));
		        CHECK(!json::accept("FALSE"));
		    }
		}
		
		```


- `cpp-test; [accept;illegal literals]
(/workspaces/json/TSF/tests/unit-literals.cpp)`


		```cpp
		SECTION("illegal literals")
		{
		    SECTION("nil")
		    {
		        CHECK(!json::accept("nil"));
		        CHECK(!json::accept("Nil"));
		        CHECK(!json::accept("nIl"));
		        CHECK(!json::accept("NIl"));
		        CHECK(!json::accept("niL"));
		        CHECK(!json::accept("NiL"));
		        CHECK(!json::accept("nIL"));
		        CHECK(!json::accept("NIL"));
		    }
		    SECTION("truth")
		    {
		        CHECK(!json::accept("truth"));
		        CHECK(!json::accept("Truth"));
		        CHECK(!json::accept("tRuth"));
		        CHECK(!json::accept("TRuth"));
		        CHECK(!json::accept("trUth"));
		        CHECK(!json::accept("TrUth"));
		        CHECK(!json::accept("tRUth"));
		        CHECK(!json::accept("TRUth"));
		        CHECK(!json::accept("truTh"));
		        CHECK(!json::accept("TruTh"));
		        CHECK(!json::accept("tRuTh"));
		        CHECK(!json::accept("TRuTh"));
		        CHECK(!json::accept("trUTh"));
		        CHECK(!json::accept("TrUTh"));
		        CHECK(!json::accept("tRUTh"));
		        CHECK(!json::accept("TRUTh"));
		        CHECK(!json::accept("trutH"));
		        CHECK(!json::accept("TrutH"));
		        CHECK(!json::accept("tRutH"));
		        CHECK(!json::accept("TRutH"));
		        CHECK(!json::accept("trUtH"));
		        CHECK(!json::accept("TrUtH"));
		        CHECK(!json::accept("tRUtH"));
		        CHECK(!json::accept("TRUtH"));
		        CHECK(!json::accept("truTH"));
		        CHECK(!json::accept("TruTH"));
		        CHECK(!json::accept("tRuTH"));
		        CHECK(!json::accept("TRuTH"));
		        CHECK(!json::accept("trUTH"));
		        CHECK(!json::accept("TrUTH"));
		        CHECK(!json::accept("tRUTH"));
		        CHECK(!json::accept("TRUTH"));
		    }
		    SECTION("const")
		    {
		        CHECK(!json::accept("const"));
		        CHECK(!json::accept("Const"));
		        CHECK(!json::accept("cOnst"));
		        CHECK(!json::accept("COnst"));
		        CHECK(!json::accept("coNst"));
		        CHECK(!json::accept("CoNst"));
		        CHECK(!json::accept("cONst"));
		        CHECK(!json::accept("CONst"));
		        CHECK(!json::accept("conSt"));
		        CHECK(!json::accept("ConSt"));
		        CHECK(!json::accept("cOnSt"));
		        CHECK(!json::accept("COnSt"));
		        CHECK(!json::accept("coNSt"));
		        CHECK(!json::accept("CoNSt"));
		        CHECK(!json::accept("cONSt"));
		        CHECK(!json::accept("CONSt"));
		        CHECK(!json::accept("consT"));
		        CHECK(!json::accept("ConsT"));
		        CHECK(!json::accept("cOnsT"));
		        CHECK(!json::accept("COnsT"));
		        CHECK(!json::accept("coNsT"));
		        CHECK(!json::accept("CoNsT"));
		        CHECK(!json::accept("cONsT"));
		        CHECK(!json::accept("CONsT"));
		        CHECK(!json::accept("conST"));
		        CHECK(!json::accept("ConST"));
		        CHECK(!json::accept("cOnST"));
		        CHECK(!json::accept("COnST"));
		        CHECK(!json::accept("coNST"));
		        CHECK(!json::accept("CoNST"));
		        CHECK(!json::accept("cONST"));
		        CHECK(!json::accept("CONST"));
		    }
		    SECTION("none")
		    {
		        CHECK(!json::accept("none"));
		        CHECK(!json::accept("None"));
		        CHECK(!json::accept("nOne"));
		        CHECK(!json::accept("NOne"));
		        CHECK(!json::accept("noNe"));
		        CHECK(!json::accept("NoNe"));
		        CHECK(!json::accept("nONe"));
		        CHECK(!json::accept("NONe"));
		        CHECK(!json::accept("nonE"));
		        CHECK(!json::accept("NonE"));
		        CHECK(!json::accept("nOnE"));
		        CHECK(!json::accept("NOnE"));
		        CHECK(!json::accept("noNE"));
		        CHECK(!json::accept("NoNE"));
		        CHECK(!json::accept("nONE"));
		        CHECK(!json::accept("NONE"));
		    }
		    SECTION("self")
		    {
		        CHECK(!json::accept("self"));
		        CHECK(!json::accept("Self"));
		        CHECK(!json::accept("sElf"));
		        CHECK(!json::accept("SElf"));
		        CHECK(!json::accept("seLf"));
		        CHECK(!json::accept("SeLf"));
		        CHECK(!json::accept("sELf"));
		        CHECK(!json::accept("SELf"));
		        CHECK(!json::accept("selF"));
		        CHECK(!json::accept("SelF"));
		        CHECK(!json::accept("sElF"));
		        CHECK(!json::accept("SElF"));
		        CHECK(!json::accept("seLF"));
		        CHECK(!json::accept("SeLF"));
		        CHECK(!json::accept("sELF"));
		        CHECK(!json::accept("SELF"));
		    }
		    SECTION("super")
		    {
		        CHECK(!json::accept("super"));
		        CHECK(!json::accept("Super"));
		        CHECK(!json::accept("sUper"));
		        CHECK(!json::accept("SUper"));
		        CHECK(!json::accept("suPer"));
		        CHECK(!json::accept("SuPer"));
		        CHECK(!json::accept("sUPer"));
		        CHECK(!json::accept("SUPer"));
		        CHECK(!json::accept("supEr"));
		        CHECK(!json::accept("SupEr"));
		        CHECK(!json::accept("sUpEr"));
		        CHECK(!json::accept("SUpEr"));
		        CHECK(!json::accept("suPEr"));
		        CHECK(!json::accept("SuPEr"));
		        CHECK(!json::accept("sUPEr"));
		        CHECK(!json::accept("SUPEr"));
		        CHECK(!json::accept("supeR"));
		        CHECK(!json::accept("SupeR"));
		        CHECK(!json::accept("sUpeR"));
		        CHECK(!json::accept("SUpeR"));
		        CHECK(!json::accept("suPeR"));
		        CHECK(!json::accept("SuPeR"));
		        CHECK(!json::accept("sUPeR"));
		        CHECK(!json::accept("SUPeR"));
		        CHECK(!json::accept("supER"));
		        CHECK(!json::accept("SupER"));
		        CHECK(!json::accept("sUpER"));
		        CHECK(!json::accept("SUpER"));
		        CHECK(!json::accept("suPER"));
		        CHECK(!json::accept("SuPER"));
		        CHECK(!json::accept("sUPER"));
		        CHECK(!json::accept("SUPER"));
		    }
		    SECTION("this")
		    {
		        CHECK(!json::accept("this"));
		        CHECK(!json::accept("This"));
		        CHECK(!json::accept("tHis"));
		        CHECK(!json::accept("THis"));
		        CHECK(!json::accept("thIs"));
		        CHECK(!json::accept("ThIs"));
		        CHECK(!json::accept("tHIs"));
		        CHECK(!json::accept("THIs"));
		        CHECK(!json::accept("thiS"));
		        CHECK(!json::accept("ThiS"));
		        CHECK(!json::accept("tHiS"));
		        CHECK(!json::accept("THiS"));
		        CHECK(!json::accept("thIS"));
		        CHECK(!json::accept("ThIS"));
		        CHECK(!json::accept("tHIS"));
		        CHECK(!json::accept("THIS"));
		    }
		    SECTION("undefined")
		    {
		        CHECK(!json::accept("undefined"));
		        CHECK(!json::accept("Undefined"));
		        CHECK(!json::accept("uNdefined"));
		        CHECK(!json::accept("UNdefined"));
		        CHECK(!json::accept("unDefined"));
		        CHECK(!json::accept("UnDefined"));
		        CHECK(!json::accept("uNDefined"));
		        CHECK(!json::accept("UNDefined"));
		        CHECK(!json::accept("undEfined"));
		        CHECK(!json::accept("UndEfined"));
		        CHECK(!json::accept("uNdEfined"));
		        CHECK(!json::accept("UNdEfined"));
		        CHECK(!json::accept("unDEfined"));
		        CHECK(!json::accept("UnDEfined"));
		        CHECK(!json::accept("uNDEfined"));
		        CHECK(!json::accept("UNDEfined"));
		        CHECK(!json::accept("undeFined"));
		        CHECK(!json::accept("UndeFined"));
		        CHECK(!json::accept("uNdeFined"));
		        CHECK(!json::accept("UNdeFined"));
		        CHECK(!json::accept("unDeFined"));
		        CHECK(!json::accept("UnDeFined"));
		        CHECK(!json::accept("uNDeFined"));
		        CHECK(!json::accept("UNDeFined"));
		        CHECK(!json::accept("undEFined"));
		        CHECK(!json::accept("UndEFined"));
		        CHECK(!json::accept("uNdEFined"));
		        CHECK(!json::accept("UNdEFined"));
		        CHECK(!json::accept("unDEFined"));
		        CHECK(!json::accept("UnDEFined"));
		        CHECK(!json::accept("uNDEFined"));
		        CHECK(!json::accept("UNDEFined"));
		        CHECK(!json::accept("undefIned"));
		        CHECK(!json::accept("UndefIned"));
		        CHECK(!json::accept("uNdefIned"));
		        CHECK(!json::accept("UNdefIned"));
		        CHECK(!json::accept("unDefIned"));
		        CHECK(!json::accept("UnDefIned"));
		        CHECK(!json::accept("uNDefIned"));
		        CHECK(!json::accept("UNDefIned"));
		        CHECK(!json::accept("undEfIned"));
		        CHECK(!json::accept("UndEfIned"));
		        CHECK(!json::accept("uNdEfIned"));
		        CHECK(!json::accept("UNdEfIned"));
		        CHECK(!json::accept("unDEfIned"));
		        CHECK(!json::accept("UnDEfIned"));
		        CHECK(!json::accept("uNDEfIned"));
		        CHECK(!json::accept("UNDEfIned"));
		        CHECK(!json::accept("undeFIned"));
		        CHECK(!json::accept("UndeFIned"));
		        CHECK(!json::accept("uNdeFIned"));
		        CHECK(!json::accept("UNdeFIned"));
		        CHECK(!json::accept("unDeFIned"));
		        CHECK(!json::accept("UnDeFIned"));
		        CHECK(!json::accept("uNDeFIned"));
		        CHECK(!json::accept("UNDeFIned"));
		        CHECK(!json::accept("undEFIned"));
		        CHECK(!json::accept("UndEFIned"));
		        CHECK(!json::accept("uNdEFIned"));
		        CHECK(!json::accept("UNdEFIned"));
		        CHECK(!json::accept("unDEFIned"));
		        CHECK(!json::accept("UnDEFIned"));
		        CHECK(!json::accept("uNDEFIned"));
		        CHECK(!json::accept("UNDEFIned"));
		        CHECK(!json::accept("undefiNed"));
		        CHECK(!json::accept("UndefiNed"));
		        CHECK(!json::accept("uNdefiNed"));
		        CHECK(!json::accept("UNdefiNed"));
		        CHECK(!json::accept("unDefiNed"));
		        CHECK(!json::accept("UnDefiNed"));
		        CHECK(!json::accept("uNDefiNed"));
		        CHECK(!json::accept("UNDefiNed"));
		        CHECK(!json::accept("undEfiNed"));
		        CHECK(!json::accept("UndEfiNed"));
		        CHECK(!json::accept("uNdEfiNed"));
		        CHECK(!json::accept("UNdEfiNed"));
		        CHECK(!json::accept("unDEfiNed"));
		        CHECK(!json::accept("UnDEfiNed"));
		        CHECK(!json::accept("uNDEfiNed"));
		        CHECK(!json::accept("UNDEfiNed"));
		        CHECK(!json::accept("undeFiNed"));
		        CHECK(!json::accept("UndeFiNed"));
		        CHECK(!json::accept("uNdeFiNed"));
		        CHECK(!json::accept("UNdeFiNed"));
		        CHECK(!json::accept("unDeFiNed"));
		        CHECK(!json::accept("UnDeFiNed"));
		        CHECK(!json::accept("uNDeFiNed"));
		        CHECK(!json::accept("UNDeFiNed"));
		        CHECK(!json::accept("undEFiNed"));
		        CHECK(!json::accept("UndEFiNed"));
		        CHECK(!json::accept("uNdEFiNed"));
		        CHECK(!json::accept("UNdEFiNed"));
		        CHECK(!json::accept("unDEFiNed"));
		        CHECK(!json::accept("UnDEFiNed"));
		        CHECK(!json::accept("uNDEFiNed"));
		        CHECK(!json::accept("UNDEFiNed"));
		        CHECK(!json::accept("undefINed"));
		        CHECK(!json::accept("UndefINed"));
		        CHECK(!json::accept("uNdefINed"));
		        CHECK(!json::accept("UNdefINed"));
		        CHECK(!json::accept("unDefINed"));
		        CHECK(!json::accept("UnDefINed"));
		        CHECK(!json::accept("uNDefINed"));
		        CHECK(!json::accept("UNDefINed"));
		        CHECK(!json::accept("undEfINed"));
		        CHECK(!json::accept("UndEfINed"));
		        CHECK(!json::accept("uNdEfINed"));
		        CHECK(!json::accept("UNdEfINed"));
		        CHECK(!json::accept("unDEfINed"));
		        CHECK(!json::accept("UnDEfINed"));
		        CHECK(!json::accept("uNDEfINed"));
		        CHECK(!json::accept("UNDEfINed"));
		        CHECK(!json::accept("undeFINed"));
		        CHECK(!json::accept("UndeFINed"));
		        CHECK(!json::accept("uNdeFINed"));
		        CHECK(!json::accept("UNdeFINed"));
		        CHECK(!json::accept("unDeFINed"));
		        CHECK(!json::accept("UnDeFINed"));
		        CHECK(!json::accept("uNDeFINed"));
		        CHECK(!json::accept("UNDeFINed"));
		        CHECK(!json::accept("undEFINed"));
		        CHECK(!json::accept("UndEFINed"));
		        CHECK(!json::accept("uNdEFINed"));
		        CHECK(!json::accept("UNdEFINed"));
		        CHECK(!json::accept("unDEFINed"));
		        CHECK(!json::accept("UnDEFINed"));
		        CHECK(!json::accept("uNDEFINed"));
		        CHECK(!json::accept("UNDEFINed"));
		        CHECK(!json::accept("undefinEd"));
		        CHECK(!json::accept("UndefinEd"));
		        CHECK(!json::accept("uNdefinEd"));
		        CHECK(!json::accept("UNdefinEd"));
		        CHECK(!json::accept("unDefinEd"));
		        CHECK(!json::accept("UnDefinEd"));
		        CHECK(!json::accept("uNDefinEd"));
		        CHECK(!json::accept("UNDefinEd"));
		        CHECK(!json::accept("undEfinEd"));
		        CHECK(!json::accept("UndEfinEd"));
		        CHECK(!json::accept("uNdEfinEd"));
		        CHECK(!json::accept("UNdEfinEd"));
		        CHECK(!json::accept("unDEfinEd"));
		        CHECK(!json::accept("UnDEfinEd"));
		        CHECK(!json::accept("uNDEfinEd"));
		        CHECK(!json::accept("UNDEfinEd"));
		        CHECK(!json::accept("undeFinEd"));
		        CHECK(!json::accept("UndeFinEd"));
		        CHECK(!json::accept("uNdeFinEd"));
		        CHECK(!json::accept("UNdeFinEd"));
		        CHECK(!json::accept("unDeFinEd"));
		        CHECK(!json::accept("UnDeFinEd"));
		        CHECK(!json::accept("uNDeFinEd"));
		        CHECK(!json::accept("UNDeFinEd"));
		        CHECK(!json::accept("undEFinEd"));
		        CHECK(!json::accept("UndEFinEd"));
		        CHECK(!json::accept("uNdEFinEd"));
		        CHECK(!json::accept("UNdEFinEd"));
		        CHECK(!json::accept("unDEFinEd"));
		        CHECK(!json::accept("UnDEFinEd"));
		        CHECK(!json::accept("uNDEFinEd"));
		        CHECK(!json::accept("UNDEFinEd"));
		        CHECK(!json::accept("undefInEd"));
		        CHECK(!json::accept("UndefInEd"));
		        CHECK(!json::accept("uNdefInEd"));
		        CHECK(!json::accept("UNdefInEd"));
		        CHECK(!json::accept("unDefInEd"));
		        CHECK(!json::accept("UnDefInEd"));
		        CHECK(!json::accept("uNDefInEd"));
		        CHECK(!json::accept("UNDefInEd"));
		        CHECK(!json::accept("undEfInEd"));
		        CHECK(!json::accept("UndEfInEd"));
		        CHECK(!json::accept("uNdEfInEd"));
		        CHECK(!json::accept("UNdEfInEd"));
		        CHECK(!json::accept("unDEfInEd"));
		        CHECK(!json::accept("UnDEfInEd"));
		        CHECK(!json::accept("uNDEfInEd"));
		        CHECK(!json::accept("UNDEfInEd"));
		        CHECK(!json::accept("undeFInEd"));
		        CHECK(!json::accept("UndeFInEd"));
		        CHECK(!json::accept("uNdeFInEd"));
		        CHECK(!json::accept("UNdeFInEd"));
		        CHECK(!json::accept("unDeFInEd"));
		        CHECK(!json::accept("UnDeFInEd"));
		        CHECK(!json::accept("uNDeFInEd"));
		        CHECK(!json::accept("UNDeFInEd"));
		        CHECK(!json::accept("undEFInEd"));
		        CHECK(!json::accept("UndEFInEd"));
		        CHECK(!json::accept("uNdEFInEd"));
		        CHECK(!json::accept("UNdEFInEd"));
		        CHECK(!json::accept("unDEFInEd"));
		        CHECK(!json::accept("UnDEFInEd"));
		        CHECK(!json::accept("uNDEFInEd"));
		        CHECK(!json::accept("UNDEFInEd"));
		        CHECK(!json::accept("undefiNEd"));
		        CHECK(!json::accept("UndefiNEd"));
		        CHECK(!json::accept("uNdefiNEd"));
		        CHECK(!json::accept("UNdefiNEd"));
		        CHECK(!json::accept("unDefiNEd"));
		        CHECK(!json::accept("UnDefiNEd"));
		        CHECK(!json::accept("uNDefiNEd"));
		        CHECK(!json::accept("UNDefiNEd"));
		        CHECK(!json::accept("undEfiNEd"));
		        CHECK(!json::accept("UndEfiNEd"));
		        CHECK(!json::accept("uNdEfiNEd"));
		        CHECK(!json::accept("UNdEfiNEd"));
		        CHECK(!json::accept("unDEfiNEd"));
		        CHECK(!json::accept("UnDEfiNEd"));
		        CHECK(!json::accept("uNDEfiNEd"));
		        CHECK(!json::accept("UNDEfiNEd"));
		        CHECK(!json::accept("undeFiNEd"));
		        CHECK(!json::accept("UndeFiNEd"));
		        CHECK(!json::accept("uNdeFiNEd"));
		        CHECK(!json::accept("UNdeFiNEd"));
		        CHECK(!json::accept("unDeFiNEd"));
		        CHECK(!json::accept("UnDeFiNEd"));
		        CHECK(!json::accept("uNDeFiNEd"));
		        CHECK(!json::accept("UNDeFiNEd"));
		        CHECK(!json::accept("undEFiNEd"));
		        CHECK(!json::accept("UndEFiNEd"));
		        CHECK(!json::accept("uNdEFiNEd"));
		        CHECK(!json::accept("UNdEFiNEd"));
		        CHECK(!json::accept("unDEFiNEd"));
		        CHECK(!json::accept("UnDEFiNEd"));
		        CHECK(!json::accept("uNDEFiNEd"));
		        CHECK(!json::accept("UNDEFiNEd"));
		        CHECK(!json::accept("undefINEd"));
		        CHECK(!json::accept("UndefINEd"));
		        CHECK(!json::accept("uNdefINEd"));
		        CHECK(!json::accept("UNdefINEd"));
		        CHECK(!json::accept("unDefINEd"));
		        CHECK(!json::accept("UnDefINEd"));
		        CHECK(!json::accept("uNDefINEd"));
		        CHECK(!json::accept("UNDefINEd"));
		        CHECK(!json::accept("undEfINEd"));
		        CHECK(!json::accept("UndEfINEd"));
		        CHECK(!json::accept("uNdEfINEd"));
		        CHECK(!json::accept("UNdEfINEd"));
		        CHECK(!json::accept("unDEfINEd"));
		        CHECK(!json::accept("UnDEfINEd"));
		        CHECK(!json::accept("uNDEfINEd"));
		        CHECK(!json::accept("UNDEfINEd"));
		        CHECK(!json::accept("undeFINEd"));
		        CHECK(!json::accept("UndeFINEd"));
		        CHECK(!json::accept("uNdeFINEd"));
		        CHECK(!json::accept("UNdeFINEd"));
		        CHECK(!json::accept("unDeFINEd"));
		        CHECK(!json::accept("UnDeFINEd"));
		        CHECK(!json::accept("uNDeFINEd"));
		        CHECK(!json::accept("UNDeFINEd"));
		        CHECK(!json::accept("undEFINEd"));
		        CHECK(!json::accept("UndEFINEd"));
		        CHECK(!json::accept("uNdEFINEd"));
		        CHECK(!json::accept("UNdEFINEd"));
		        CHECK(!json::accept("unDEFINEd"));
		        CHECK(!json::accept("UnDEFINEd"));
		        CHECK(!json::accept("uNDEFINEd"));
		        CHECK(!json::accept("UNDEFINEd"));
		        CHECK(!json::accept("undefineD"));
		        CHECK(!json::accept("UndefineD"));
		        CHECK(!json::accept("uNdefineD"));
		        CHECK(!json::accept("UNdefineD"));
		        CHECK(!json::accept("unDefineD"));
		        CHECK(!json::accept("UnDefineD"));
		        CHECK(!json::accept("uNDefineD"));
		        CHECK(!json::accept("UNDefineD"));
		        CHECK(!json::accept("undEfineD"));
		        CHECK(!json::accept("UndEfineD"));
		        CHECK(!json::accept("uNdEfineD"));
		        CHECK(!json::accept("UNdEfineD"));
		        CHECK(!json::accept("unDEfineD"));
		        CHECK(!json::accept("UnDEfineD"));
		        CHECK(!json::accept("uNDEfineD"));
		        CHECK(!json::accept("UNDEfineD"));
		        CHECK(!json::accept("undeFineD"));
		        CHECK(!json::accept("UndeFineD"));
		        CHECK(!json::accept("uNdeFineD"));
		        CHECK(!json::accept("UNdeFineD"));
		        CHECK(!json::accept("unDeFineD"));
		        CHECK(!json::accept("UnDeFineD"));
		        CHECK(!json::accept("uNDeFineD"));
		        CHECK(!json::accept("UNDeFineD"));
		        CHECK(!json::accept("undEFineD"));
		        CHECK(!json::accept("UndEFineD"));
		        CHECK(!json::accept("uNdEFineD"));
		        CHECK(!json::accept("UNdEFineD"));
		        CHECK(!json::accept("unDEFineD"));
		        CHECK(!json::accept("UnDEFineD"));
		        CHECK(!json::accept("uNDEFineD"));
		        CHECK(!json::accept("UNDEFineD"));
		        CHECK(!json::accept("undefIneD"));
		        CHECK(!json::accept("UndefIneD"));
		        CHECK(!json::accept("uNdefIneD"));
		        CHECK(!json::accept("UNdefIneD"));
		        CHECK(!json::accept("unDefIneD"));
		        CHECK(!json::accept("UnDefIneD"));
		        CHECK(!json::accept("uNDefIneD"));
		        CHECK(!json::accept("UNDefIneD"));
		        CHECK(!json::accept("undEfIneD"));
		        CHECK(!json::accept("UndEfIneD"));
		        CHECK(!json::accept("uNdEfIneD"));
		        CHECK(!json::accept("UNdEfIneD"));
		        CHECK(!json::accept("unDEfIneD"));
		        CHECK(!json::accept("UnDEfIneD"));
		        CHECK(!json::accept("uNDEfIneD"));
		        CHECK(!json::accept("UNDEfIneD"));
		        CHECK(!json::accept("undeFIneD"));
		        CHECK(!json::accept("UndeFIneD"));
		        CHECK(!json::accept("uNdeFIneD"));
		        CHECK(!json::accept("UNdeFIneD"));
		        CHECK(!json::accept("unDeFIneD"));
		        CHECK(!json::accept("UnDeFIneD"));
		        CHECK(!json::accept("uNDeFIneD"));
		        CHECK(!json::accept("UNDeFIneD"));
		        CHECK(!json::accept("undEFIneD"));
		        CHECK(!json::accept("UndEFIneD"));
		        CHECK(!json::accept("uNdEFIneD"));
		        CHECK(!json::accept("UNdEFIneD"));
		        CHECK(!json::accept("unDEFIneD"));
		        CHECK(!json::accept("UnDEFIneD"));
		        CHECK(!json::accept("uNDEFIneD"));
		        CHECK(!json::accept("UNDEFIneD"));
		        CHECK(!json::accept("undefiNeD"));
		        CHECK(!json::accept("UndefiNeD"));
		        CHECK(!json::accept("uNdefiNeD"));
		        CHECK(!json::accept("UNdefiNeD"));
		        CHECK(!json::accept("unDefiNeD"));
		        CHECK(!json::accept("UnDefiNeD"));
		        CHECK(!json::accept("uNDefiNeD"));
		        CHECK(!json::accept("UNDefiNeD"));
		        CHECK(!json::accept("undEfiNeD"));
		        CHECK(!json::accept("UndEfiNeD"));
		        CHECK(!json::accept("uNdEfiNeD"));
		        CHECK(!json::accept("UNdEfiNeD"));
		        CHECK(!json::accept("unDEfiNeD"));
		        CHECK(!json::accept("UnDEfiNeD"));
		        CHECK(!json::accept("uNDEfiNeD"));
		        CHECK(!json::accept("UNDEfiNeD"));
		        CHECK(!json::accept("undeFiNeD"));
		        CHECK(!json::accept("UndeFiNeD"));
		        CHECK(!json::accept("uNdeFiNeD"));
		        CHECK(!json::accept("UNdeFiNeD"));
		        CHECK(!json::accept("unDeFiNeD"));
		        CHECK(!json::accept("UnDeFiNeD"));
		        CHECK(!json::accept("uNDeFiNeD"));
		        CHECK(!json::accept("UNDeFiNeD"));
		        CHECK(!json::accept("undEFiNeD"));
		        CHECK(!json::accept("UndEFiNeD"));
		        CHECK(!json::accept("uNdEFiNeD"));
		        CHECK(!json::accept("UNdEFiNeD"));
		        CHECK(!json::accept("unDEFiNeD"));
		        CHECK(!json::accept("UnDEFiNeD"));
		        CHECK(!json::accept("uNDEFiNeD"));
		        CHECK(!json::accept("UNDEFiNeD"));
		        CHECK(!json::accept("undefINeD"));
		        CHECK(!json::accept("UndefINeD"));
		        CHECK(!json::accept("uNdefINeD"));
		        CHECK(!json::accept("UNdefINeD"));
		        CHECK(!json::accept("unDefINeD"));
		        CHECK(!json::accept("UnDefINeD"));
		        CHECK(!json::accept("uNDefINeD"));
		        CHECK(!json::accept("UNDefINeD"));
		        CHECK(!json::accept("undEfINeD"));
		        CHECK(!json::accept("UndEfINeD"));
		        CHECK(!json::accept("uNdEfINeD"));
		        CHECK(!json::accept("UNdEfINeD"));
		        CHECK(!json::accept("unDEfINeD"));
		        CHECK(!json::accept("UnDEfINeD"));
		        CHECK(!json::accept("uNDEfINeD"));
		        CHECK(!json::accept("UNDEfINeD"));
		        CHECK(!json::accept("undeFINeD"));
		        CHECK(!json::accept("UndeFINeD"));
		        CHECK(!json::accept("uNdeFINeD"));
		        CHECK(!json::accept("UNdeFINeD"));
		        CHECK(!json::accept("unDeFINeD"));
		        CHECK(!json::accept("UnDeFINeD"));
		        CHECK(!json::accept("uNDeFINeD"));
		        CHECK(!json::accept("UNDeFINeD"));
		        CHECK(!json::accept("undEFINeD"));
		        CHECK(!json::accept("UndEFINeD"));
		        CHECK(!json::accept("uNdEFINeD"));
		        CHECK(!json::accept("UNdEFINeD"));
		        CHECK(!json::accept("unDEFINeD"));
		        CHECK(!json::accept("UnDEFINeD"));
		        CHECK(!json::accept("uNDEFINeD"));
		        CHECK(!json::accept("UNDEFINeD"));
		        CHECK(!json::accept("undefinED"));
		        CHECK(!json::accept("UndefinED"));
		        CHECK(!json::accept("uNdefinED"));
		        CHECK(!json::accept("UNdefinED"));
		        CHECK(!json::accept("unDefinED"));
		        CHECK(!json::accept("UnDefinED"));
		        CHECK(!json::accept("uNDefinED"));
		        CHECK(!json::accept("UNDefinED"));
		        CHECK(!json::accept("undEfinED"));
		        CHECK(!json::accept("UndEfinED"));
		        CHECK(!json::accept("uNdEfinED"));
		        CHECK(!json::accept("UNdEfinED"));
		        CHECK(!json::accept("unDEfinED"));
		        CHECK(!json::accept("UnDEfinED"));
		        CHECK(!json::accept("uNDEfinED"));
		        CHECK(!json::accept("UNDEfinED"));
		        CHECK(!json::accept("undeFinED"));
		        CHECK(!json::accept("UndeFinED"));
		        CHECK(!json::accept("uNdeFinED"));
		        CHECK(!json::accept("UNdeFinED"));
		        CHECK(!json::accept("unDeFinED"));
		        CHECK(!json::accept("UnDeFinED"));
		        CHECK(!json::accept("uNDeFinED"));
		        CHECK(!json::accept("UNDeFinED"));
		        CHECK(!json::accept("undEFinED"));
		        CHECK(!json::accept("UndEFinED"));
		        CHECK(!json::accept("uNdEFinED"));
		        CHECK(!json::accept("UNdEFinED"));
		        CHECK(!json::accept("unDEFinED"));
		        CHECK(!json::accept("UnDEFinED"));
		        CHECK(!json::accept("uNDEFinED"));
		        CHECK(!json::accept("UNDEFinED"));
		        CHECK(!json::accept("undefInED"));
		        CHECK(!json::accept("UndefInED"));
		        CHECK(!json::accept("uNdefInED"));
		        CHECK(!json::accept("UNdefInED"));
		        CHECK(!json::accept("unDefInED"));
		        CHECK(!json::accept("UnDefInED"));
		        CHECK(!json::accept("uNDefInED"));
		        CHECK(!json::accept("UNDefInED"));
		        CHECK(!json::accept("undEfInED"));
		        CHECK(!json::accept("UndEfInED"));
		        CHECK(!json::accept("uNdEfInED"));
		        CHECK(!json::accept("UNdEfInED"));
		        CHECK(!json::accept("unDEfInED"));
		        CHECK(!json::accept("UnDEfInED"));
		        CHECK(!json::accept("uNDEfInED"));
		        CHECK(!json::accept("UNDEfInED"));
		        CHECK(!json::accept("undeFInED"));
		        CHECK(!json::accept("UndeFInED"));
		        CHECK(!json::accept("uNdeFInED"));
		        CHECK(!json::accept("UNdeFInED"));
		        CHECK(!json::accept("unDeFInED"));
		        CHECK(!json::accept("UnDeFInED"));
		        CHECK(!json::accept("uNDeFInED"));
		        CHECK(!json::accept("UNDeFInED"));
		        CHECK(!json::accept("undEFInED"));
		        CHECK(!json::accept("UndEFInED"));
		        CHECK(!json::accept("uNdEFInED"));
		        CHECK(!json::accept("UNdEFInED"));
		        CHECK(!json::accept("unDEFInED"));
		        CHECK(!json::accept("UnDEFInED"));
		        CHECK(!json::accept("uNDEFInED"));
		        CHECK(!json::accept("UNDEFInED"));
		        CHECK(!json::accept("undefiNED"));
		        CHECK(!json::accept("UndefiNED"));
		        CHECK(!json::accept("uNdefiNED"));
		        CHECK(!json::accept("UNdefiNED"));
		        CHECK(!json::accept("unDefiNED"));
		        CHECK(!json::accept("UnDefiNED"));
		        CHECK(!json::accept("uNDefiNED"));
		        CHECK(!json::accept("UNDefiNED"));
		        CHECK(!json::accept("undEfiNED"));
		        CHECK(!json::accept("UndEfiNED"));
		        CHECK(!json::accept("uNdEfiNED"));
		        CHECK(!json::accept("UNdEfiNED"));
		        CHECK(!json::accept("unDEfiNED"));
		        CHECK(!json::accept("UnDEfiNED"));
		        CHECK(!json::accept("uNDEfiNED"));
		        CHECK(!json::accept("UNDEfiNED"));
		        CHECK(!json::accept("undeFiNED"));
		        CHECK(!json::accept("UndeFiNED"));
		        CHECK(!json::accept("uNdeFiNED"));
		        CHECK(!json::accept("UNdeFiNED"));
		        CHECK(!json::accept("unDeFiNED"));
		        CHECK(!json::accept("UnDeFiNED"));
		        CHECK(!json::accept("uNDeFiNED"));
		        CHECK(!json::accept("UNDeFiNED"));
		        CHECK(!json::accept("undEFiNED"));
		        CHECK(!json::accept("UndEFiNED"));
		        CHECK(!json::accept("uNdEFiNED"));
		        CHECK(!json::accept("UNdEFiNED"));
		        CHECK(!json::accept("unDEFiNED"));
		        CHECK(!json::accept("UnDEFiNED"));
		        CHECK(!json::accept("uNDEFiNED"));
		        CHECK(!json::accept("UNDEFiNED"));
		        CHECK(!json::accept("undefINED"));
		        CHECK(!json::accept("UndefINED"));
		        CHECK(!json::accept("uNdefINED"));
		        CHECK(!json::accept("UNdefINED"));
		        CHECK(!json::accept("unDefINED"));
		        CHECK(!json::accept("UnDefINED"));
		        CHECK(!json::accept("uNDefINED"));
		        CHECK(!json::accept("UNDefINED"));
		        CHECK(!json::accept("undEfINED"));
		        CHECK(!json::accept("UndEfINED"));
		        CHECK(!json::accept("uNdEfINED"));
		        CHECK(!json::accept("UNdEfINED"));
		        CHECK(!json::accept("unDEfINED"));
		        CHECK(!json::accept("UnDEfINED"));
		        CHECK(!json::accept("uNDEfINED"));
		        CHECK(!json::accept("UNDEfINED"));
		        CHECK(!json::accept("undeFINED"));
		        CHECK(!json::accept("UndeFINED"));
		        CHECK(!json::accept("uNdeFINED"));
		        CHECK(!json::accept("UNdeFINED"));
		        CHECK(!json::accept("unDeFINED"));
		        CHECK(!json::accept("UnDeFINED"));
		        CHECK(!json::accept("uNDeFINED"));
		        CHECK(!json::accept("UNDeFINED"));
		        CHECK(!json::accept("undEFINED"));
		        CHECK(!json::accept("UndEFINED"));
		        CHECK(!json::accept("uNdEFINED"));
		        CHECK(!json::accept("UNdEFINED"));
		        CHECK(!json::accept("unDEFINED"));
		        CHECK(!json::accept("UnDEFINED"));
		        CHECK(!json::accept("uNDEFINED"));
		        CHECK(!json::accept("UNDEFINED"));
		    }
		}
		
		```





**Fallacies;**

_None_


---

### NJF-05 

The service accepts and rejects arrays according to RFC8259 §5.


**Supported Requests;**

- [WFJ-04](WFJ.md#wfj-04)

**Supporting Items;**

- [NJF-05.1](NJF.md#njf-05.1)
- [NJF-05.2](NJF.md#njf-05.2)
- [NJF-05.3](NJF.md#njf-05.3)
- [NJF-05.4](NJF.md#njf-05.4)
- [NJF-05.5](NJF.md#njf-05.5)
- [NJF-05.6](NJF.md#njf-05.6)
- [NJF-05.7](NJF.md#njf-05.7)



**References;**

_None_



**Fallacies;**

_None_


---

### NJF-05.1 

The service accepts the empty array.


**Supported Requests;**

- [NJF-05](NJF.md#njf-05)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [parser class;accept;array;empty array]
(/workspaces/json/tests/src/unit-class_parser.cpp)`


		```cpp
		SECTION("empty array")
		{
		    CHECK(accept_helper("[]"));
		    CHECK(accept_helper("[ ]"));
		}
		
		```


- `cpp-testsuite; [/nst_json_testsuite/test_parsing/y_array_empty.json]`


			- Description; 
			
			
			- JSON Testsuite; /nst_json_testsuite/test_parsing/y_array_empty.json
			
			
			 ```json
			[]
			```
			
			
			- cpp-test; [nst's JSONTestSuite;test_parsing;y]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("y")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/y_array_empty.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json j;
			        CHECK_NOTHROW(f &gt;&gt; j);
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			

- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/y_array_empty.json, /nst_json_testsuite2/test_parsing/y_array_arraysWithSpaces.json, /nst_json_testsuite2/test_parsing/y_array_empty-string.json]`


			- Description; Checks that the empty array [] is accepted.
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_array_empty.json
			
			
			 ```json
			[]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_array_arraysWithSpaces.json
			
			
			 ```json
			[[]   ]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_array_empty-string.json
			
			
			 ```json
			[""]
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;y]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("y")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_array_arraysWithSpaces.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_array_empty-string.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_array_empty.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f));
			        std::ifstream f2(filename);
			        CHECK(json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			

- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/y_array_ending_with_newline.json]`


			- Description; 
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_array_ending_with_newline.json
			
			
			 ```json
			["a"]
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;y]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("y")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_array_ending_with_newline.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f));
			        std::ifstream f2(filename);
			        CHECK(json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			




**Fallacies;**

_None_


---

### NJF-05.2 

The service accepts non-empty arrays.


**Supported Requests;**

- [NJF-05](NJF.md#njf-05)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [parser class;accept;array;nonempty array]
(/workspaces/json/tests/src/unit-class_parser.cpp)`


		```cpp
		SECTION("nonempty array")
		{
		    CHECK(accept_helper("[true, false, null]"));
		}
		
		```


- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/y_array_false.json, /nst_json_testsuite2/test_parsing/y_array_heterogeneous.json, /nst_json_testsuite2/test_parsing/y_array_null.json, /nst_json_testsuite2/test_parsing/y_array_with_1_and_newline.json, /nst_json_testsuite2/test_parsing/y_array_with_leading_space.json, /nst_json_testsuite2/test_parsing/y_array_with_several_null.json, /nst_json_testsuite2/test_parsing/y_array_with_trailing_space.json]`


			- Description; Checks that various valid arrays are accepted.
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_array_false.json
			
			
			 ```json
			[false]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_array_heterogeneous.json
			
			
			 ```json
			[null, 1, "1", {}]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_array_null.json
			
			
			 ```json
			[null]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_array_with_1_and_newline.json
			
			
			 ```json
			[1
			]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_array_with_leading_space.json
			
			
			 ```json
			 [1]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_array_with_several_null.json
			
			
			 ```json
			[1,null,null,null,2]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_array_with_trailing_space.json
			
			
			 ```json
			[2] 
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;y]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("y")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_array_false.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_array_heterogeneous.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_array_null.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_array_with_1_and_newline.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_array_with_leading_space.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_array_with_several_null.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_array_with_trailing_space.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f));
			        std::ifstream f2(filename);
			        CHECK(json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			

- `cpp-testsuite; [/json.org/1.json, /json.org/2.json, /json.org/3.json, /json.org/4.json, /json.org/5.json, /json.org/1.json, /json.org/2.json, /json.org/3.json, /json.org/4.json, /json.org/5.json]`


			- Description; Checks that various valid arrays in combination with objects are accepted.
			
			
			- JSON Testsuite; /json.org/1.json
			
			
			 ```json
			{
			    "glossary"; {
			        "title"; "example glossary",
					"GlossDiv"; {
			            "title"; "S",
						"GlossList"; {
			                "GlossEntry"; {
			                    "ID"; "SGML",
								"SortAs"; "SGML",
								"GlossTerm"; "Standard Generalized Markup Language",
								"Acronym"; "SGML",
								"Abbrev"; "ISO 8879;1986",
								"GlossDef"; {
			                        "para"; "A meta-markup language, used to create markup languages such as DocBook.",
									"GlossSeeAlso"; ["GML", "XML"]
			                    },
								"GlossSee"; "markup"
			                }
			            }
			        }
			    }
			}
			
			```
			
			
			
			
			- JSON Testsuite; /json.org/2.json
			
			
			 ```json
			{"menu"; {
			  "id"; "file",
			  "value"; "File",
			  "popup"; {
			    "menuitem"; [
			      {"value"; "New", "onclick"; "CreateNewDoc()"},
			      {"value"; "Open", "onclick"; "OpenDoc()"},
			      {"value"; "Close", "onclick"; "CloseDoc()"}
			    ]
			  }
			}}
			
			```
			
			
			
			
			- JSON Testsuite; /json.org/3.json
			
			
			 [Link to file](https://raw.githubusercontent.com/nlohmann/json_test_data/master//json.org/3.json) [Content too large - 26 lines]
			
			
			
			
			
			- JSON Testsuite; /json.org/4.json
			
			
			 [Link to file](https://raw.githubusercontent.com/nlohmann/json_test_data/master//json.org/4.json) [Content too large - 88 lines]
			
			
			
			
			
			- JSON Testsuite; /json.org/5.json
			
			
			 [Link to file](https://raw.githubusercontent.com/nlohmann/json_test_data/master//json.org/5.json) [Content too large - 27 lines]
			
			
			
			
			
			- JSON Testsuite; /json.org/1.json
			
			
			 ```json
			{
			    "glossary"; {
			        "title"; "example glossary",
					"GlossDiv"; {
			            "title"; "S",
						"GlossList"; {
			                "GlossEntry"; {
			                    "ID"; "SGML",
								"SortAs"; "SGML",
								"GlossTerm"; "Standard Generalized Markup Language",
								"Acronym"; "SGML",
								"Abbrev"; "ISO 8879;1986",
								"GlossDef"; {
			                        "para"; "A meta-markup language, used to create markup languages such as DocBook.",
									"GlossSeeAlso"; ["GML", "XML"]
			                    },
								"GlossSee"; "markup"
			                }
			            }
			        }
			    }
			}
			
			```
			
			
			
			
			- JSON Testsuite; /json.org/2.json
			
			
			 ```json
			{"menu"; {
			  "id"; "file",
			  "value"; "File",
			  "popup"; {
			    "menuitem"; [
			      {"value"; "New", "onclick"; "CreateNewDoc()"},
			      {"value"; "Open", "onclick"; "OpenDoc()"},
			      {"value"; "Close", "onclick"; "CloseDoc()"}
			    ]
			  }
			}}
			
			```
			
			
			
			
			- JSON Testsuite; /json.org/3.json
			
			
			 [Link to file](https://raw.githubusercontent.com/nlohmann/json_test_data/master//json.org/3.json) [Content too large - 26 lines]
			
			
			
			
			
			- JSON Testsuite; /json.org/4.json
			
			
			 [Link to file](https://raw.githubusercontent.com/nlohmann/json_test_data/master//json.org/4.json) [Content too large - 88 lines]
			
			
			
			
			
			- JSON Testsuite; /json.org/5.json
			
			
			 [Link to file](https://raw.githubusercontent.com/nlohmann/json_test_data/master//json.org/5.json) [Content too large - 27 lines]
			
			
			
			- cpp-test; [json.org examples]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			TEST_CASE("json.org examples")
			{
			    // here, we list all JSON values from https://json.org/example
			    using FilePtr = std::unique_ptr&lt;FILE, int(*)(FILE*)&gt;;
			
			    SECTION("1.json")
			    {
			        std::ifstream f(TEST_DATA_DIRECTORY "/json.org/1.json");
			        json j;
			        CHECK_NOTHROW(f &gt;&gt; j);
			    }
			
			    SECTION("2.json")
			    {
			        std::ifstream f(TEST_DATA_DIRECTORY "/json.org/2.json");
			        json j;
			        CHECK_NOTHROW(f &gt;&gt; j);
			    }
			
			    SECTION("3.json")
			    {
			        std::ifstream f(TEST_DATA_DIRECTORY "/json.org/3.json");
			        json j;
			        CHECK_NOTHROW(f &gt;&gt; j);
			    }
			
			    SECTION("4.json")
			    {
			        std::ifstream f(TEST_DATA_DIRECTORY "/json.org/4.json");
			        json j;
			        CHECK_NOTHROW(f &gt;&gt; j);
			    }
			
			    SECTION("5.json")
			    {
			        std::ifstream f(TEST_DATA_DIRECTORY "/json.org/5.json");
			        json j;
			        CHECK_NOTHROW(f &gt;&gt; j);
			    }
			    SECTION("FILE 1.json")
			    {
			        const FilePtr f(std::fopen(TEST_DATA_DIRECTORY "/json.org/1.json", "r"), &std::fclose);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f.get()));
			    }
			
			    SECTION("FILE 2.json")
			    {
			        const FilePtr f(std::fopen(TEST_DATA_DIRECTORY "/json.org/2.json", "r"), &std::fclose);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f.get()));
			    }
			
			    SECTION("FILE 3.json")
			    {
			        const FilePtr f(std::fopen(TEST_DATA_DIRECTORY "/json.org/3.json", "r"), &std::fclose);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f.get()));
			    }
			
			    SECTION("FILE 4.json")
			    {
			        const FilePtr f(std::fopen(TEST_DATA_DIRECTORY "/json.org/4.json", "r"), &std::fclose);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f.get()));
			    }
			
			    SECTION("FILE 5.json")
			    {
			        const FilePtr f(std::fopen(TEST_DATA_DIRECTORY "/json.org/5.json", "r"), &std::fclose);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f.get()));
			    }
			}
			
			```
			




**Fallacies;**

_None_


---

### NJF-05.3 

The service accepts arrays with different types.


**Supported Requests;**

- [NJF-05](NJF.md#njf-05)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [deserialization;successful deserialization;stream]
(/workspaces/json/tests/src/unit-deserialization.cpp)`


		```cpp
		SECTION("stream")
		{
		    std::stringstream ss1;
		    std::stringstream ss2;
		    std::stringstream ss3;
		    ss1 &lt;&lt; R"(["foo",1,2,3,false,{"one";1}])";
		    ss2 &lt;&lt; R"(["foo",1,2,3,false,{"one";1}])";
		    ss3 &lt;&lt; R"(["foo",1,2,3,false,{"one";1}])";
		    json j = json::parse(ss1);
		    CHECK(json::accept(ss2));
		    CHECK(j == json({"foo", 1, 2, 3, false, {{"one", 1}}}));
		
		    SaxEventLogger l;
		    CHECK(json::sax_parse(ss3, &l));
		    CHECK(l.events.size() == 11);
		    CHECK(l.events == std::vector&lt;std::string&gt;(
		    {
		        "start_array()", "string(foo)", "number_unsigned(1)",
		        "number_unsigned(2)", "number_unsigned(3)", "boolean(false)",
		        "start_object()", "key(one)", "number_unsigned(1)",
		        "end_object()", "end_array()"
		    }));
		}
		
		```


- `cpp-testsuite; [/json.org/1.json, /json.org/2.json, /json.org/3.json, /json.org/4.json, /json.org/5.json, /json.org/1.json, /json.org/2.json, /json.org/3.json, /json.org/4.json, /json.org/5.json]`


			- Description; Checks that various valid arrays in combination with objects are accepted.
			
			
			- JSON Testsuite; /json.org/1.json
			
			
			 ```json
			{
			    "glossary"; {
			        "title"; "example glossary",
					"GlossDiv"; {
			            "title"; "S",
						"GlossList"; {
			                "GlossEntry"; {
			                    "ID"; "SGML",
								"SortAs"; "SGML",
								"GlossTerm"; "Standard Generalized Markup Language",
								"Acronym"; "SGML",
								"Abbrev"; "ISO 8879;1986",
								"GlossDef"; {
			                        "para"; "A meta-markup language, used to create markup languages such as DocBook.",
									"GlossSeeAlso"; ["GML", "XML"]
			                    },
								"GlossSee"; "markup"
			                }
			            }
			        }
			    }
			}
			
			```
			
			
			
			
			- JSON Testsuite; /json.org/2.json
			
			
			 ```json
			{"menu"; {
			  "id"; "file",
			  "value"; "File",
			  "popup"; {
			    "menuitem"; [
			      {"value"; "New", "onclick"; "CreateNewDoc()"},
			      {"value"; "Open", "onclick"; "OpenDoc()"},
			      {"value"; "Close", "onclick"; "CloseDoc()"}
			    ]
			  }
			}}
			
			```
			
			
			
			
			- JSON Testsuite; /json.org/3.json
			
			
			 [Link to file](https://raw.githubusercontent.com/nlohmann/json_test_data/master//json.org/3.json) [Content too large - 26 lines]
			
			
			
			
			
			- JSON Testsuite; /json.org/4.json
			
			
			 [Link to file](https://raw.githubusercontent.com/nlohmann/json_test_data/master//json.org/4.json) [Content too large - 88 lines]
			
			
			
			
			
			- JSON Testsuite; /json.org/5.json
			
			
			 [Link to file](https://raw.githubusercontent.com/nlohmann/json_test_data/master//json.org/5.json) [Content too large - 27 lines]
			
			
			
			
			
			- JSON Testsuite; /json.org/1.json
			
			
			 ```json
			{
			    "glossary"; {
			        "title"; "example glossary",
					"GlossDiv"; {
			            "title"; "S",
						"GlossList"; {
			                "GlossEntry"; {
			                    "ID"; "SGML",
								"SortAs"; "SGML",
								"GlossTerm"; "Standard Generalized Markup Language",
								"Acronym"; "SGML",
								"Abbrev"; "ISO 8879;1986",
								"GlossDef"; {
			                        "para"; "A meta-markup language, used to create markup languages such as DocBook.",
									"GlossSeeAlso"; ["GML", "XML"]
			                    },
								"GlossSee"; "markup"
			                }
			            }
			        }
			    }
			}
			
			```
			
			
			
			
			- JSON Testsuite; /json.org/2.json
			
			
			 ```json
			{"menu"; {
			  "id"; "file",
			  "value"; "File",
			  "popup"; {
			    "menuitem"; [
			      {"value"; "New", "onclick"; "CreateNewDoc()"},
			      {"value"; "Open", "onclick"; "OpenDoc()"},
			      {"value"; "Close", "onclick"; "CloseDoc()"}
			    ]
			  }
			}}
			
			```
			
			
			
			
			- JSON Testsuite; /json.org/3.json
			
			
			 [Link to file](https://raw.githubusercontent.com/nlohmann/json_test_data/master//json.org/3.json) [Content too large - 26 lines]
			
			
			
			
			
			- JSON Testsuite; /json.org/4.json
			
			
			 [Link to file](https://raw.githubusercontent.com/nlohmann/json_test_data/master//json.org/4.json) [Content too large - 88 lines]
			
			
			
			
			
			- JSON Testsuite; /json.org/5.json
			
			
			 [Link to file](https://raw.githubusercontent.com/nlohmann/json_test_data/master//json.org/5.json) [Content too large - 27 lines]
			
			
			
			- cpp-test; [json.org examples]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			TEST_CASE("json.org examples")
			{
			    // here, we list all JSON values from https://json.org/example
			    using FilePtr = std::unique_ptr&lt;FILE, int(*)(FILE*)&gt;;
			
			    SECTION("1.json")
			    {
			        std::ifstream f(TEST_DATA_DIRECTORY "/json.org/1.json");
			        json j;
			        CHECK_NOTHROW(f &gt;&gt; j);
			    }
			
			    SECTION("2.json")
			    {
			        std::ifstream f(TEST_DATA_DIRECTORY "/json.org/2.json");
			        json j;
			        CHECK_NOTHROW(f &gt;&gt; j);
			    }
			
			    SECTION("3.json")
			    {
			        std::ifstream f(TEST_DATA_DIRECTORY "/json.org/3.json");
			        json j;
			        CHECK_NOTHROW(f &gt;&gt; j);
			    }
			
			    SECTION("4.json")
			    {
			        std::ifstream f(TEST_DATA_DIRECTORY "/json.org/4.json");
			        json j;
			        CHECK_NOTHROW(f &gt;&gt; j);
			    }
			
			    SECTION("5.json")
			    {
			        std::ifstream f(TEST_DATA_DIRECTORY "/json.org/5.json");
			        json j;
			        CHECK_NOTHROW(f &gt;&gt; j);
			    }
			    SECTION("FILE 1.json")
			    {
			        const FilePtr f(std::fopen(TEST_DATA_DIRECTORY "/json.org/1.json", "r"), &std::fclose);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f.get()));
			    }
			
			    SECTION("FILE 2.json")
			    {
			        const FilePtr f(std::fopen(TEST_DATA_DIRECTORY "/json.org/2.json", "r"), &std::fclose);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f.get()));
			    }
			
			    SECTION("FILE 3.json")
			    {
			        const FilePtr f(std::fopen(TEST_DATA_DIRECTORY "/json.org/3.json", "r"), &std::fclose);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f.get()));
			    }
			
			    SECTION("FILE 4.json")
			    {
			        const FilePtr f(std::fopen(TEST_DATA_DIRECTORY "/json.org/4.json", "r"), &std::fclose);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f.get()));
			    }
			
			    SECTION("FILE 5.json")
			    {
			        const FilePtr f(std::fopen(TEST_DATA_DIRECTORY "/json.org/5.json", "r"), &std::fclose);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f.get()));
			    }
			}
			
			```
			

- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/y_string_in_array.json, /nst_json_testsuite2/test_parsing/y_string_in_array_with_leading_space.json, /nst_json_testsuite2/test_parsing/y_structure_true_in_array.json]`


			- Description; 
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_string_in_array.json
			
			
			 ```json
			["asd"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_string_in_array_with_leading_space.json
			
			
			 ```json
			[ "asd"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_structure_true_in_array.json
			
			
			 ```json
			[true]
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;y]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("y")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_string_in_array.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_string_in_array_with_leading_space.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_structure_true_in_array.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f));
			        std::ifstream f2(filename);
			        CHECK(json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			




**Fallacies;**

_None_


---

### NJF-05.4 

The service does not accept improperly bounded arrays.


**Supported Requests;**

- [NJF-05](NJF.md#njf-05)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [parser class;accept;parse errors (accept)]
(/workspaces/json/tests/src/unit-class_parser.cpp)`


		```cpp
		SECTION("parse errors (accept)")
		{
		    // unexpected end of number
		    CHECK(accept_helper("0.") == false);
		    CHECK(accept_helper("-") == false);
		    CHECK(accept_helper("--") == false);
		    CHECK(accept_helper("-0.") == false);
		    CHECK(accept_helper("-.") == false);
		    CHECK(accept_helper("-;") == false);
		    CHECK(accept_helper("0.;") == false);
		    CHECK(accept_helper("e.") == false);
		    CHECK(accept_helper("1e.") == false);
		    CHECK(accept_helper("1e/") == false);
		    CHECK(accept_helper("1e;") == false);
		    CHECK(accept_helper("1E.") == false);
		    CHECK(accept_helper("1E/") == false);
		    CHECK(accept_helper("1E;") == false);
		
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
		    CHECK(accept_helper("{\"foo\";") == false);
		    CHECK(accept_helper("{\"foo\";}") == false);
		    CHECK(accept_helper("{\"foo\";1,}") == false);
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
		    for (int c = 1; c &lt; 128; ++c)
		    {
		        auto s = std::string("\"\\") + std::string(1, static_cast&lt;char&gt;(c)) + "\"";
		
		        switch (c)
		        {
		            // valid escapes
		            case ('"');
		            case ('\\');
		            case ('/');
		            case ('b');
		            case ('f');
		            case ('n');
		            case ('r');
		            case ('t');
		            {
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s)).accept());
		                break;
		            }
		
		            // \u must be followed with four numbers, so we skip it here
		            case ('u');
		            {
		                break;
		            }
		
		            // any other combination of backslash and character is invalid
		            default;
		            {
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s)).accept() == false);
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
		                case ('0');
		                case ('1');
		                case ('2');
		                case ('3');
		                case ('4');
		                case ('5');
		                case ('6');
		                case ('7');
		                case ('8');
		                case ('9');
		                case ('a');
		                case ('b');
		                case ('c');
		                case ('d');
		                case ('e');
		                case ('f');
		                case ('A');
		                case ('B');
		                case ('C');
		                case ('D');
		                case ('E');
		                case ('F');
		                {
		                    return true;
		                }
		
		                default;
		                {
		                    return false;
		                }
		            }
		        };
		
		        for (int c = 1; c &lt; 128; ++c)
		        {
		            std::string const s = "\"\\u";
		
		            // create a string with the iterated character at each position
		            const auto s1 = s + "000" + std::string(1, static_cast&lt;char&gt;(c)) + "\"";
		            const auto s2 = s + "00" + std::string(1, static_cast&lt;char&gt;(c)) + "0\"";
		            const auto s3 = s + "0" + std::string(1, static_cast&lt;char&gt;(c)) + "00\"";
		            const auto s4 = s + std::string(1, static_cast&lt;char&gt;(c)) + "000\"";
		
		            if (valid(c))
		            {
		                CAPTURE(s1)
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s1)).accept());
		                CAPTURE(s2)
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s2)).accept());
		                CAPTURE(s3)
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s3)).accept());
		                CAPTURE(s4)
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s4)).accept());
		            }
		            else
		            {
		                CAPTURE(s1)
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s1)).accept() == false);
		
		                CAPTURE(s2)
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s2)).accept() == false);
		
		                CAPTURE(s3)
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s3)).accept() == false);
		
		                CAPTURE(s4)
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s4)).accept() == false);
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
		
		```


- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/n_structure_100000_opening_arrays.json]`


			- Description; 
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_structure_100000_opening_arrays.json
			
			
			 ```json
			[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;n (previously overflowed)]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("n (previously overflowed)")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_100000_opening_arrays.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        CHECK(!json::accept(f));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			

- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/n_structure_close_unopened_array.json]`


			- Description; 
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_structure_close_unopened_array.json
			
			
			 ```json
			1]
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;n]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("n")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_close_unopened_array.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_THROWS_AS(_ = json::parse(f), json::parse_error&);
			        std::ifstream f2(filename);
			        CHECK(!json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			

- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/n_structure_double_array.json, /nst_json_testsuite2/test_parsing/n_structure_end_array.json, /nst_json_testsuite2/test_parsing/n_structure_lone-invalid-utf-8.json, /nst_json_testsuite2/test_parsing/n_structure_open_array_apostrophe.json, /nst_json_testsuite2/test_parsing/n_structure_open_array_comma.json, /nst_json_testsuite2/test_parsing/n_structure_open_array_open_object.json, /nst_json_testsuite2/test_parsing/n_structure_open_object_close_array.json, /nst_json_testsuite2/test_parsing/n_structure_unclosed_array.json, /nst_json_testsuite2/test_parsing/n_structure_unclosed_array_partial_null.json, /nst_json_testsuite2/test_parsing/n_structure_unclosed_array_unfinished_false.json, /nst_json_testsuite2/test_parsing/n_structure_unclosed_array_unfinished_true.json]`


			- Description; 
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_structure_double_array.json
			
			
			 ```json
			[][]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_structure_end_array.json
			
			
			 ```json
			]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_structure_lone-invalid-utf-8.json
			
			
			 ```json
			V
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_structure_open_array_apostrophe.json
			
			
			 ```json
			['
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_structure_open_array_comma.json
			
			
			 ```json
			[,
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_structure_open_array_open_object.json
			
			
			 ```json
			[{
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_structure_open_object_close_array.json
			
			
			 ```json
			{]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_structure_unclosed_array.json
			
			
			 ```json
			[1
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_structure_unclosed_array_partial_null.json
			
			
			 ```json
			[ false, nul
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_structure_unclosed_array_unfinished_false.json
			
			
			 ```json
			[ true, fals
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_structure_unclosed_array_unfinished_true.json
			
			
			 ```json
			[ false, tru
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;n]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("n")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_double_array.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_end_array.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_lone-invalid-utf-8.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_array_apostrophe.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_array_comma.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_array_open_object.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_object_close_array.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_unclosed_array.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_unclosed_array_partial_null.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_unclosed_array_unfinished_false.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_unclosed_array_unfinished_true.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_THROWS_AS(_ = json::parse(f), json::parse_error&);
			        std::ifstream f2(filename);
			        CHECK(!json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			




**Fallacies;**

_None_


---

### NJF-05.5 

The service does not accept arrays with improper values.


**Supported Requests;**

- [NJF-05](NJF.md#njf-05)

**Supporting Items;**

_None_



**References;**

- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/n_array_double_comma.json, /nst_json_testsuite2/test_parsing/n_array_double_extra_comma.json, /nst_json_testsuite2/test_parsing/n_array_just_comma.json, /nst_json_testsuite2/test_parsing/n_array_number_and_comma.json, /nst_json_testsuite2/test_parsing/n_array_number_and_several_commas.json, /nst_json_testsuite2/test_parsing/n_structure_array_with_unclosed_string.json, /nst_json_testsuite2/test_parsing/n_array_invalid_utf8.json, /nst_json_testsuite2/test_parsing/n_array_just_minus.json]`


			- Description; Checks that various "proper" arrays with improper elements are rejected.
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_array_double_comma.json
			
			
			 ```json
			[1,,2]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_array_double_extra_comma.json
			
			
			 ```json
			["x",,]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_array_just_comma.json
			
			
			 ```json
			[,]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_array_number_and_comma.json
			
			
			 ```json
			[1,]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_array_number_and_several_commas.json
			
			
			 ```json
			[1,,]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_structure_array_with_unclosed_string.json
			
			
			 ```json
			["asd]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_array_invalid_utf8.json
			
			
			 ```json
			[ﹽ]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_array_just_minus.json
			
			
			 ```json
			[-]
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;n]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("n")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_double_comma.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_double_extra_comma.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_invalid_utf8.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_just_comma.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_just_minus.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_number_and_comma.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_number_and_several_commas.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_array_with_unclosed_string.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_THROWS_AS(_ = json::parse(f), json::parse_error&);
			        std::ifstream f2(filename);
			        CHECK(!json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			




**Fallacies;**

_None_


---

### NJF-05.5_CONTEXT 

An improper value is either an empty value within a non-empty array or an inadmissible token according to RFC8259.


**Supported Requests;**


**Supporting Items;**

_None_



**References;**

_None_



**Fallacies;**

_None_


---

### NJF-05.6 

The service accepts nested arrays.


**Supported Requests;**

- [NJF-05](NJF.md#njf-05)

**Supporting Items;**

_None_



**References;**

- `cpp-testsuite; [/json_tests/pass2.json]`


			- Description; 
			
			
			- JSON Testsuite; /json_tests/pass2.json
			
			
			 ```json
			[[[[[[[[[[[[[[[[[[["Not too deep"]]]]]]]]]]]]]]]]]]]
			```
			
			
			- cpp-test; [compliance tests from json.org;expected passes]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("expected passes")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/json_tests/pass2.json",
			            })
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json j;
			        CHECK_NOTHROW(f &gt;&gt; j);
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			

- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/i_structure_500_nested_arrays.json]`


			- Description; 
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/i_structure_500_nested_arrays.json
			
			
			 ```json
			[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;i -&gt; y]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("i -&gt; y")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/i_structure_500_nested_arrays.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f));
			        std::ifstream f2(filename);
			        CHECK(json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			




**Fallacies;**

_None_


---

### NJF-05.7 

The service does only accept comma as value separator.


**Supported Requests;**

- [NJF-05](NJF.md#njf-05)

**Supporting Items;**

- [NJF-05.7.1](NJF.md#njf-05.7.1)
- [NJF-05.7.2](NJF.md#njf-05.7.2)



**References;**

_None_



**Fallacies;**

_None_


---

### NJF-05.7.1 

The service does accept comma as value separator.


**Supported Requests;**

- [NJF-05.7](NJF.md#njf-05.7)

**Supporting Items;**

_None_



**References;**

- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/y_array_with_several_null.json]`


			- Description; Checks that [1,null,null,null,2] is accepted.
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_array_with_several_null.json
			
			
			 ```json
			[1,null,null,null,2]
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;y]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("y")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_array_with_several_null.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f));
			        std::ifstream f2(filename);
			        CHECK(json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			

- `cpp-testsuite; [/json.org/4.json]`


			- Description; 
			
			
			- JSON Testsuite; /json.org/4.json
			
			
			 [Link to file](https://raw.githubusercontent.com/nlohmann/json_test_data/master//json.org/4.json) [Content too large - 88 lines]
			
			
			
			- cpp-test; [json.org examples;4.json]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("4.json")
			{
			    std::ifstream f(TEST_DATA_DIRECTORY "/json.org/4.json");
			    json j;
			    CHECK_NOTHROW(f &gt;&gt; j);
			}
			
			```
			

- `cpp-testsuite; [/json.org/5.json]`


			- Description; 
			
			
			- JSON Testsuite; /json.org/5.json
			
			
			 [Link to file](https://raw.githubusercontent.com/nlohmann/json_test_data/master//json.org/5.json) [Content too large - 27 lines]
			
			
			
			- cpp-test; [json.org examples;5.json]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("5.json")
			{
			    std::ifstream f(TEST_DATA_DIRECTORY "/json.org/5.json");
			    json j;
			    CHECK_NOTHROW(f &gt;&gt; j);
			}
			
			```
			




**Fallacies;**

_None_


---

### NJF-05.7.2 

The service does not accept any other value separator.


**Supported Requests;**

- [NJF-05.7](NJF.md#njf-05.7)

**Supporting Items;**

_None_



**References;**

- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/n_array_colon_instead_of_comma.json]`


			- Description; 
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_array_colon_instead_of_comma.json
			
			
			 ```json
			[""; 1]
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;n]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("n")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_colon_instead_of_comma.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_THROWS_AS(_ = json::parse(f), json::parse_error&);
			        std::ifstream f2(filename);
			        CHECK(!json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			




**Fallacies;**

_None_


---

### NJF-06 

The service accepts and rejects objects according to RFC8259 §4


**Supported Requests;**

- [WFJ-05](WFJ.md#wfj-05)

**Supporting Items;**

- [NJF-06.1](NJF.md#njf-06.1)
- [NJF-06.2](NJF.md#njf-06.2)
- [NJF-06.3](NJF.md#njf-06.3)
- [NJF-06.4](NJF.md#njf-06.4)
- [NJF-06.5](NJF.md#njf-06.5)
- [NJF-06.6](NJF.md#njf-06.6)
- [NJF-06.7](NJF.md#njf-06.7)



**References;**

_None_



**Fallacies;**

_None_


---

### NJF-06.1 

The service accepts the empty object.


**Supported Requests;**

- [NJF-06](NJF.md#njf-06)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [parser class;accept;object;empty object]
(/workspaces/json/tests/src/unit-class_parser.cpp)`


		```cpp
		SECTION("empty object")
		{
		    CHECK(accept_helper("{}"));
		    CHECK(accept_helper("{ }"));
		}
		
		```


- `cpp-test; [accept;whitespace;empty object]
(/workspaces/json/TSF/tests/unit-objects.cpp)`


		```cpp
		SECTION("empty object")
		{
		    CHECK(json::accept("{          }"));
		    CHECK(json::accept("{\t}"));
		    CHECK(json::accept("{\n}"));
		    CHECK(json::accept("{\u000d}"));
		    CHECK(json::accept("{\u000d\u000d\u000d  \t\t\t\n\n   \u000d \n\t  \t \u000d}"));
		}
		
		```





**Fallacies;**

_None_


---

### NJF-06.2 

The service does not accept improperly bounded objects.


**Supported Requests;**

- [NJF-06](NJF.md#njf-06)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [deserialization;contiguous containers;error cases;case 15]
(/workspaces/json/tests/src/unit-deserialization.cpp)`


		```cpp
		SECTION("case 15")
		{
		    std::array&lt;std::uint8_t, 4&gt; v = {{'\"', 0x7F, 0xF4, 0x7F}};
		    json _;
		    CHECK_THROWS_AS(_ = json::parse(std::begin(v), std::end(v)), json::parse_error&);
		    CHECK(!json::accept(std::begin(v), std::end(v)));
		
		    json j_error;
		    CHECK_NOTHROW(j_error = json::parse(std::begin(v), std::end(v), nullptr, false));
		    CHECK(j_error.is_discarded());
		
		    SaxEventLogger l;
		    CHECK(!json::sax_parse(std::begin(v), std::end(v), &l));
		    CHECK(l.events.size() == 1);
		    CHECK(l.events == std::vector&lt;std::string&gt;({"parse_error(4)"}));
		}
		
		```


- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/n_structure_comma_instead_of_closing_brace.json, /nst_json_testsuite2/test_parsing/n_structure_object_followed_by_closing_object.json, /nst_json_testsuite2/test_parsing/n_structure_object_unclosed_no_value.json]`


			- Description; 
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_structure_comma_instead_of_closing_brace.json
			
			
			 ```json
			{"x"; true,
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_structure_object_followed_by_closing_object.json
			
			
			 ```json
			{}}
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_structure_object_unclosed_no_value.json
			
			
			 ```json
			{"";
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;n]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("n")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_comma_instead_of_closing_brace.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_object_followed_by_closing_object.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_object_unclosed_no_value.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_THROWS_AS(_ = json::parse(f), json::parse_error&);
			        std::ifstream f2(filename);
			        CHECK(!json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			




**Fallacies;**

_None_


---

### NJF-06.3 

The service accepts non-empty objects.


**Supported Requests;**

- [NJF-06](NJF.md#njf-06)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [deserialization;JSON Lines]
(/workspaces/json/tests/src/unit-deserialization.cpp)`


		```cpp
		    SECTION("JSON Lines")
		    {
		        SECTION("Example file")
		        {
		            std::stringstream ss;
		            ss &lt;&lt; R"({"name"; "Gilbert", "wins"; [["straight", "7♣"], ["one pair", "10♥"]]}
		                    {"name"; "Alexa", "wins"; [["two pair", "4♠"], ["two pair", "9♠"]]}
		                    {"name"; "May", "wins"; []}
		                    {"name"; "Deloise", "wins"; [["three of a kind", "5♣"]]}
		)";
		
		            std::string line;
		            int object_count = 0;
		            while (std::getline(ss, line))
		            {
		                ++object_count;
		                CHECK(json::accept(line));
		            }
		
		            CHECK(object_count == 4);
		        }
		
		        SECTION("Example file without trailing newline")
		        {
		            std::stringstream ss;
		            ss &lt;&lt; R"({"name"; "Gilbert", "wins"; [["straight", "7♣"], ["one pair", "10♥"]]}
		                    {"name"; "Alexa", "wins"; [["two pair", "4♠"], ["two pair", "9♠"]]}
		                    {"name"; "May", "wins"; []}
		                    {"name"; "Deloise", "wins"; [["three of a kind", "5♣"]]})";
		
		            std::string line;
		            int object_count = 0;
		            while (std::getline(ss, line))
		            {
		                ++object_count;
		                CHECK(json::accept(line));
		            }
		
		            CHECK(object_count == 4);
		        }
		    }
		
		```


- `cpp-test; [parser class;accept;object;nonempty object]
(/workspaces/json/tests/src/unit-class_parser.cpp)`


		```cpp
		SECTION("nonempty object")
		{
		    CHECK(accept_helper("{\"\"; true, \"one\"; 1, \"two\"; null}"));
		}
		
		```





**Fallacies;**

_None_


---

### NJF-06.4 

The admissible members of an object have the form name ; value.


**Supported Requests;**

- [NJF-06](NJF.md#njf-06)

**Supporting Items;**

- [NJF-06.4.1](NJF.md#njf-06.4.1)
- [NJF-06.4.2](NJF.md#njf-06.4.2)
- [NJF-06.4.3](NJF.md#njf-06.4.3)



**References;**

- `cpp-test; [nst's JSONTestSuite;test_parsing;n]
(/workspaces/json/tests/src/unit-testsuites.cpp)`


		```cpp
		SECTION("n")
		{
		    for (const auto* filename ;
		            {
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_array_1_true_without_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_array_a_invalid_utf8.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_array_colon_instead_of_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_array_comma_after_close.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_array_comma_and_number.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_array_double_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_array_double_extra_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_array_extra_close.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_array_extra_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_array_incomplete.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_array_incomplete_invalid_value.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_array_inner_array_no_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_array_invalid_utf8.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_array_items_separated_by_semicolon.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_array_just_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_array_just_minus.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_array_missing_value.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_array_newlines_unclosed.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_array_number_and_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_array_number_and_several_commas.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_array_spaces_vertical_tab_formfeed.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_array_star_inside.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_array_unclosed.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_array_unclosed_trailing_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_array_unclosed_with_new_lines.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_array_unclosed_with_object_inside.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_incomplete_false.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_incomplete_null.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_incomplete_true.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_++.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_+1.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_+Inf.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_-01.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_-1.0..json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_-2..json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_-NaN.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_.-1.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_.2e-3.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_0.1.2.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_0.3e+.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_0.3e.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_0.e1.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_0_capital_E+.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_0_capital_E.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_0e+.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_0e.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_1.0e+.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_1.0e-.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_1.0e.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_1_000.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_1eE2.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_2.e+3.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_2.e-3.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_2.e3.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_9.e+.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_Inf.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_NaN.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_U+FF11_fullwidth_digit_one.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_expression.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_hex_1_digit.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_hex_2_digits.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_infinity.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_invalid+-.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_invalid-negative-real.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_invalid-utf-8-in-bigger-int.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_invalid-utf-8-in-exponent.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_invalid-utf-8-in-int.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_minus_infinity.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_minus_sign_with_trailing_garbage.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_minus_space_1.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_neg_int_starting_with_zero.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_neg_real_without_int_part.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_neg_with_garbage_at_end.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_real_garbage_after_e.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_real_with_invalid_utf8_after_e.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_real_without_fractional_part.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_starting_with_dot.json",
		                //TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_then_00.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_with_alpha.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_with_alpha_char.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_number_with_leading_zero.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_bad_value.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_bracket_key.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_comma_instead_of_colon.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_double_colon.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_emoji.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_garbage_at_end.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_key_with_single_quotes.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_missing_colon.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_missing_key.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_missing_semicolon.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_missing_value.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_no-colon.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_non_string_key.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_non_string_key_but_huge_number_instead.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_pi_in_key_and_trailing_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_repeated_null_null.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_several_trailing_commas.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_single_quote.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_trailing_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_trailing_comment.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_trailing_comment_open.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_trailing_comment_slash_open.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_trailing_comment_slash_open_incomplete.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_two_commas_in_a_row.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_unquoted_key.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_unterminated-value.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_with_single_string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_object_with_trailing_garbage.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_single_space.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_1_surrogate_then_escape u.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_1_surrogate_then_escape u1.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_1_surrogate_then_escape u1x.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_1_surrogate_then_escape.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_UTF-16_incomplete_surrogate.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_UTF8_surrogate_U+D800.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_accentuated_char_no_quotes.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_backslash_00.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_escape_x.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_escaped_backslash_bad.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_escaped_ctrl_char_tab.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_escaped_emoji.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_incomplete_escape.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_incomplete_escaped_character.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_incomplete_surrogate_escape_invalid.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_invalid-utf-8-in-escape.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_invalid_backslash_esc.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_invalid_unicode_escape.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_invalid_utf-8.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_invalid_utf8_after_escape.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_iso_latin_1.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_leading_uescaped_thinspace.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_lone_utf8_continuation_byte.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_no_quotes_with_bad_escape.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_overlong_sequence_2_bytes.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_overlong_sequence_6_bytes.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_overlong_sequence_6_bytes_null.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_single_doublequote.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_single_quote.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_single_string_no_double_quotes.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_start_escape_unclosed.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_unescaped_crtl_char.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_unescaped_newline.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_unescaped_tab.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_unicode_CapitalU.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_string_with_trailing_garbage.json",
		                //!TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_100000_opening_arrays.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_3C.3E.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_3Cnull3E.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_U+2060_word_joined.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_UTF8_BOM_no_data.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_array_trailing_garbage.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_array_with_extra_array_close.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_array_with_unclosed_string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_ascii-unicode-identifier.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_capitalized_True.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_close_unopened_array.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_comma_instead_of_closing_brace.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_double_array.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_end_array.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_incomplete_UTF8_BOM.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_lone-invalid-utf-8.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_lone-open-bracket.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_no_data.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_null-byte-outside-string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_number_with_trailing_garbage.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_object_followed_by_closing_object.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_object_unclosed_no_value.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_object_with_comment.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_object_with_trailing_garbage.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_open_array_apostrophe.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_open_array_comma.json",
		                //!TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_open_array_object.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_open_array_open_object.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_open_array_open_string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_open_array_string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_open_object.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_open_object_close_array.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_open_object_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_open_object_open_array.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_open_object_open_string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_open_object_string_with_apostrophes.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_open_open.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_single_point.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_single_star.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_trailing_#.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_uescaped_LF_before_string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_unclosed_array.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_unclosed_array_partial_null.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_unclosed_array_unfinished_false.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_unclosed_array_unfinished_true.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_unclosed_object.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_unicode-identifier.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_whitespace_U+2060_word_joiner.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite/test_parsing/n_structure_whitespace_formfeed.json"
		            }
		        )
		    {
		        CAPTURE(filename)
		        std::ifstream f(filename);
		        json _;
		        CHECK_THROWS_AS(_ = json::parse(f), json::parse_error&);
		    }
		}
		
		```


- `cpp-test; [nst's JSONTestSuite (2);test_parsing;n]
(/workspaces/json/tests/src/unit-testsuites.cpp)`


		```cpp
		SECTION("n")
		{
		    for (const auto* filename ;
		            {
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_1_true_without_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_a_invalid_utf8.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_colon_instead_of_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_comma_after_close.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_comma_and_number.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_double_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_double_extra_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_extra_close.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_extra_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_incomplete.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_incomplete_invalid_value.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_inner_array_no_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_invalid_utf8.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_items_separated_by_semicolon.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_just_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_just_minus.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_missing_value.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_newlines_unclosed.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_number_and_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_number_and_several_commas.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_spaces_vertical_tab_formfeed.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_star_inside.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_unclosed.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_unclosed_trailing_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_unclosed_with_new_lines.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_unclosed_with_object_inside.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_incomplete_false.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_incomplete_null.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_incomplete_true.json",
		                //TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_multidigit_number_then_00.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_++.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_+1.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_+Inf.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_-01.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_-1.0..json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_-2..json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_-NaN.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_.-1.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_.2e-3.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_0.1.2.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_0.3e+.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_0.3e.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_0.e1.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_0_capital_E+.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_0_capital_E.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_0e+.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_0e.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_1.0e+.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_1.0e-.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_1.0e.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_1_000.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_1eE2.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_2.e+3.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_2.e-3.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_2.e3.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_9.e+.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_Inf.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_NaN.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_U+FF11_fullwidth_digit_one.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_expression.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_hex_1_digit.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_hex_2_digits.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_infinity.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_invalid+-.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_invalid-negative-real.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_invalid-utf-8-in-bigger-int.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_invalid-utf-8-in-exponent.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_invalid-utf-8-in-int.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_minus_infinity.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_minus_sign_with_trailing_garbage.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_minus_space_1.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_neg_int_starting_with_zero.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_neg_real_without_int_part.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_neg_with_garbage_at_end.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_real_garbage_after_e.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_real_with_invalid_utf8_after_e.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_real_without_fractional_part.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_starting_with_dot.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_with_alpha.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_with_alpha_char.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_with_leading_zero.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_bad_value.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_bracket_key.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_comma_instead_of_colon.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_double_colon.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_emoji.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_garbage_at_end.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_key_with_single_quotes.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_lone_continuation_byte_in_key_and_trailing_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_missing_colon.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_missing_key.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_missing_semicolon.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_missing_value.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_no-colon.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_non_string_key.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_non_string_key_but_huge_number_instead.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_repeated_null_null.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_several_trailing_commas.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_single_quote.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_trailing_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_trailing_comment.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_trailing_comment_open.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_trailing_comment_slash_open.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_trailing_comment_slash_open_incomplete.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_two_commas_in_a_row.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_unquoted_key.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_unterminated-value.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_with_single_string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_with_trailing_garbage.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_single_space.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape_u.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape_u1.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape_u1x.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_accentuated_char_no_quotes.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_backslash_00.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_escape_x.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_escaped_backslash_bad.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_escaped_ctrl_char_tab.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_escaped_emoji.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_incomplete_escape.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_incomplete_escaped_character.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_incomplete_surrogate.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_incomplete_surrogate_escape_invalid.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_invalid-utf-8-in-escape.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_invalid_backslash_esc.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_invalid_unicode_escape.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_invalid_utf8_after_escape.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_leading_uescaped_thinspace.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_no_quotes_with_bad_escape.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_single_doublequote.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_single_quote.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_single_string_no_double_quotes.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_start_escape_unclosed.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_unescaped_crtl_char.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_unescaped_newline.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_unescaped_tab.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_unicode_CapitalU.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_with_trailing_garbage.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_U+2060_word_joined.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_UTF8_BOM_no_data.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_angle_bracket_..json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_angle_bracket_null.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_array_trailing_garbage.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_array_with_extra_array_close.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_array_with_unclosed_string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_ascii-unicode-identifier.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_capitalized_True.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_close_unopened_array.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_comma_instead_of_closing_brace.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_double_array.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_end_array.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_incomplete_UTF8_BOM.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_lone-invalid-utf-8.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_lone-open-bracket.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_no_data.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_null-byte-outside-string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_number_with_trailing_garbage.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_object_followed_by_closing_object.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_object_unclosed_no_value.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_object_with_comment.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_object_with_trailing_garbage.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_array_apostrophe.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_array_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_array_open_object.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_array_open_string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_array_string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_object.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_object_close_array.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_object_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_object_open_array.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_object_open_string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_object_string_with_apostrophes.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_open.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_single_eacute.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_single_star.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_trailing_#.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_uescaped_LF_before_string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_unclosed_array.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_unclosed_array_partial_null.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_unclosed_array_unfinished_false.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_unclosed_array_unfinished_true.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_unclosed_object.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_unicode-identifier.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_whitespace_U+2060_word_joiner.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_whitespace_formfeed.json"
		            }
		        )
		    {
		        CAPTURE(filename)
		        std::ifstream f(filename);
		        json _;
		        CHECK_THROWS_AS(_ = json::parse(f), json::parse_error&);
		        std::ifstream f2(filename);
		        CHECK(!json::accept(f2));
		    }
		}
		
		```


- `cpp-test; [compliance tests from json.org;expected failures]
(/workspaces/json/tests/src/unit-testsuites.cpp)`


		```cpp
		SECTION("expected failures")
		{
		    for (const auto* filename ;
		            {
		                //TEST_DATA_DIRECTORY "/json_tests/fail1.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail2.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail3.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail4.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail5.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail6.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail7.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail8.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail9.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail10.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail11.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail12.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail13.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail14.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail15.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail16.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail17.json",
		                //TEST_DATA_DIRECTORY "/json_tests/fail18.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail19.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail20.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail21.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail22.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail23.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail24.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail25.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail26.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail27.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail28.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail29.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail30.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail31.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail32.json",
		                TEST_DATA_DIRECTORY "/json_tests/fail33.json"
		            })
		    {
		        CAPTURE(filename)
		        std::ifstream f(filename);
		        json _;
		        CHECK_THROWS_AS(_ = json::parse(f), json::parse_error&);
		    }
		}
		
		```





**Fallacies;**

_None_


---

### NJF-06.4.1 

The service accepts strings as names. 


**Supported Requests;**

- [NJF-06.4](NJF.md#njf-06.4)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [parser class;accept;object;nonempty object]
(/workspaces/json/tests/src/unit-class_parser.cpp)`


		```cpp
		SECTION("nonempty object")
		{
		    CHECK(accept_helper("{\"\"; true, \"one\"; 1, \"two\"; null}"));
		}
		
		```


- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/y_object_basic.json, /nst_json_testsuite2/test_parsing/y_object_duplicated_key.json, /nst_json_testsuite2/test_parsing/y_object_duplicated_key_and_value.json, /nst_json_testsuite2/test_parsing/y_object_empty.json, /nst_json_testsuite2/test_parsing/y_object_empty_key.json, /nst_json_testsuite2/test_parsing/y_object_escaped_null_in_key.json, /nst_json_testsuite2/test_parsing/y_object_extreme_numbers.json, /nst_json_testsuite2/test_parsing/y_object_long_strings.json, /nst_json_testsuite2/test_parsing/y_object_simple.json, /nst_json_testsuite2/test_parsing/y_object_string_unicode.json, /nst_json_testsuite2/test_parsing/y_object_with_newlines.json]`


			- Description; Checks that various keys, particularly containing unicode characters, are accepted.
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_object_basic.json
			
			
			 ```json
			{"asd";"sdf"}
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_object_duplicated_key.json
			
			
			 ```json
			{"a";"b","a";"c"}
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_object_duplicated_key_and_value.json
			
			
			 ```json
			{"a";"b","a";"b"}
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_object_empty.json
			
			
			 ```json
			{}
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_object_empty_key.json
			
			
			 ```json
			{"";0}
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_object_escaped_null_in_key.json
			
			
			 ```json
			{"foo\u0000bar"; 42}
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_object_extreme_numbers.json
			
			
			 ```json
			{ "min"; -1.0e+28, "max"; 1.0e+28 }
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_object_long_strings.json
			
			
			 ```json
			{"x";[{"id"; "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}], "id"; "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_object_simple.json
			
			
			 ```json
			{"a";[]}
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_object_string_unicode.json
			
			
			 ```json
			{"title";"\u041f\u043e\u043b\u0442\u043e\u0440\u0430 \u0417\u0435\u043c\u043b\u0435\u043a\u043e\u043f\u0430" }
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_object_with_newlines.json
			
			
			 ```json
			{
			"a"; "b"
			}
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;y]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("y")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_object_basic.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_object_duplicated_key.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_object_duplicated_key_and_value.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_object_empty.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_object_empty_key.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_object_escaped_null_in_key.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_object_extreme_numbers.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_object_long_strings.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_object_simple.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_object_string_unicode.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_object_with_newlines.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f));
			        std::ifstream f2(filename);
			        CHECK(json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			

- `cpp-test; [accept;names;strings;control characters]
(/workspaces/json/TSF/tests/unit-objects.cpp)`


		```cpp
		SECTION("control characters")
		{
		    CHECK(json::accept("{\"foo\\u0000bar\";123}"));
		    CHECK(json::accept("{\"foo\\u0001bar\";123}"));
		    CHECK(json::accept("{\"foo\\u0002bar\";123}"));
		    CHECK(json::accept("{\"foo\\u0003bar\";123}"));
		    CHECK(json::accept("{\"foo\\u0004bar\";123}"));
		    CHECK(json::accept("{\"foo\\u0005bar\";123}"));
		    CHECK(json::accept("{\"foo\\u0006bar\";123}"));
		    CHECK(json::accept("{\"foo\\u0007bar\";123}"));
		    CHECK(json::accept("{\"foo\\u0008bar\";123}"));
		    CHECK(json::accept("{\"foo\\u0009bar\";123}"));
		    CHECK(json::accept("{\"foo\\u000abar\";123}"));
		    CHECK(json::accept("{\"foo\\u000bbar\";123}"));
		    CHECK(json::accept("{\"foo\\u000cbar\";123}"));
		    CHECK(json::accept("{\"foo\\u000dbar\";123}"));
		    CHECK(json::accept("{\"foo\\u000ebar\";123}"));
		    CHECK(json::accept("{\"foo\\u000fbar\";123}"));
		    CHECK(json::accept("{\"foo\\u0010bar\";123}"));
		    CHECK(json::accept("{\"foo\\u0011bar\";123}"));
		    CHECK(json::accept("{\"foo\\u0012bar\";123}"));
		    CHECK(json::accept("{\"foo\\u0013bar\";123}"));
		    CHECK(json::accept("{\"foo\\u0014bar\";123}"));
		    CHECK(json::accept("{\"foo\\u0015bar\";123}"));
		    CHECK(json::accept("{\"foo\\u0016bar\";123}"));
		    CHECK(json::accept("{\"foo\\u0017bar\";123}"));
		    CHECK(json::accept("{\"foo\\u0018bar\";123}"));
		    CHECK(json::accept("{\"foo\\u0019bar\";123}"));
		    CHECK(json::accept("{\"foo\\u001abar\";123}"));
		    CHECK(json::accept("{\"foo\\u001bbar\";123}"));
		    CHECK(json::accept("{\"foo\\u001cbar\";123}"));
		    CHECK(json::accept("{\"foo\\u001dbar\";123}"));
		    CHECK(json::accept("{\"foo\\u001ebar\";123}"));
		    CHECK(json::accept("{\"foo\\u001fbar\";123}"));
		}
		
		```


- `cpp-test; [accept;names;strings;unicode]
(/workspaces/json/TSF/tests/unit-objects.cpp)`


		```cpp
		SECTION("unicode")
		{  
		    // escaped
		    CHECK(json::accept("{\"\\u0066\\u006f\\u006f\\u0062\\u0061\\u0072\";123}"));
		    // unescaped
		    CHECK(json::accept("{\"\u0066\u006f\u006f\u0062\u0061\u0072\";123}"));
		}
		
		```


- `cpp-test; [accept;names;strings;UTF-16 surrogates]
(/workspaces/json/TSF/tests/unit-objects.cpp)`


		```cpp
		SECTION("UTF-16 surrogates")
		{
		    CHECK(json::accept("{\"\\ud834\\udd1e\";123}"));
		    CHECK(json::accept("{\"\\ud83d\\ude00\";123}"));
		    CHECK(json::accept("{\"\\ud83d\\udca9\";123}"));
		    CHECK(json::accept("{\"\\ud83e\\udda5\";123}"));
		    CHECK(json::accept("{\"\\ud83d\\ude80\";123}"));
		    CHECK(json::accept("{\"\\ud840\\udc00\";123}"));
		    CHECK(json::accept("{\"\\udbff\\udfff\";123}"));
		    CHECK(json::accept("{\"\\ud83c\\udfc3\";123}"));
		    CHECK(json::accept("{\"\\ud801\\udc37\";123}"));
		    CHECK(json::accept("{\"\\ud83d\\udcbb\";123}"));
		}
		
		```





**Fallacies;**

_None_


---

### NJF-06.4.2 

The service does not accept any other token as name.


**Supported Requests;**

- [NJF-06.4](NJF.md#njf-06.4)

**Supporting Items;**

_None_



**References;**

_None_



**Fallacies;**

_None_


---

### NJF-06.4.3 

The service does accept different types of values.


**Supported Requests;**

- [NJF-06.4](NJF.md#njf-06.4)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [parser class;accept;object;nonempty object]
(/workspaces/json/tests/src/unit-class_parser.cpp)`


		```cpp
		SECTION("nonempty object")
		{
		    CHECK(accept_helper("{\"\"; true, \"one\"; 1, \"two\"; null}"));
		}
		
		```


- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/y_object_basic.json, /nst_json_testsuite2/test_parsing/y_object_duplicated_key.json, /nst_json_testsuite2/test_parsing/y_object_duplicated_key_and_value.json, /nst_json_testsuite2/test_parsing/y_object_empty.json, /nst_json_testsuite2/test_parsing/y_object_empty_key.json, /nst_json_testsuite2/test_parsing/y_object_escaped_null_in_key.json, /nst_json_testsuite2/test_parsing/y_object_extreme_numbers.json, /nst_json_testsuite2/test_parsing/y_object_long_strings.json, /nst_json_testsuite2/test_parsing/y_object_simple.json, /nst_json_testsuite2/test_parsing/y_object_string_unicode.json, /nst_json_testsuite2/test_parsing/y_object_with_newlines.json]`


			- Description; Checks that various strings and numbers are accepted values.
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_object_basic.json
			
			
			 ```json
			{"asd";"sdf"}
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_object_duplicated_key.json
			
			
			 ```json
			{"a";"b","a";"c"}
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_object_duplicated_key_and_value.json
			
			
			 ```json
			{"a";"b","a";"b"}
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_object_empty.json
			
			
			 ```json
			{}
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_object_empty_key.json
			
			
			 ```json
			{"";0}
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_object_escaped_null_in_key.json
			
			
			 ```json
			{"foo\u0000bar"; 42}
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_object_extreme_numbers.json
			
			
			 ```json
			{ "min"; -1.0e+28, "max"; 1.0e+28 }
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_object_long_strings.json
			
			
			 ```json
			{"x";[{"id"; "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}], "id"; "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_object_simple.json
			
			
			 ```json
			{"a";[]}
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_object_string_unicode.json
			
			
			 ```json
			{"title";"\u041f\u043e\u043b\u0442\u043e\u0440\u0430 \u0417\u0435\u043c\u043b\u0435\u043a\u043e\u043f\u0430" }
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_object_with_newlines.json
			
			
			 ```json
			{
			"a"; "b"
			}
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;y]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("y")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_object_basic.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_object_duplicated_key.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_object_duplicated_key_and_value.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_object_empty.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_object_empty_key.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_object_escaped_null_in_key.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_object_extreme_numbers.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_object_long_strings.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_object_simple.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_object_string_unicode.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_object_with_newlines.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f));
			        std::ifstream f2(filename);
			        CHECK(json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			




**Fallacies;**

_None_


---

### NJF-06.5 

The service does not accept objects with improper members.


**Supported Requests;**

- [NJF-06](NJF.md#njf-06)

**Supporting Items;**

- [NJF-06.5.1](NJF.md#njf-06.5.1)
- [NJF-06.5.2](NJF.md#njf-06.5.2)



**References;**

- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/n_object_trailing_comma.json, /nst_json_testsuite2/test_parsing/n_object_two_commas_in_a_row.json]`


			- Description; Checks that the empty member in a nonempty object is rejected.
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_object_trailing_comma.json
			
			
			 ```json
			{"id";0,}
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_object_two_commas_in_a_row.json
			
			
			 ```json
			{"a";"b",,"c";"d"}
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;n]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("n")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_trailing_comma.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_two_commas_in_a_row.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_THROWS_AS(_ = json::parse(f), json::parse_error&);
			        std::ifstream f2(filename);
			        CHECK(!json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			




**Fallacies;**

_None_


---

### NJF-06.5.1 

The service does not accept objects with improper name.


**Supported Requests;**

- [NJF-06.5](NJF.md#njf-06.5)

**Supporting Items;**

_None_



**References;**

_None_



**Fallacies;**

_None_


---

### NJF-06.5.2 

The service does not accept objects with improper value.


**Supported Requests;**

- [NJF-06.5](NJF.md#njf-06.5)

**Supporting Items;**

_None_



**References;**

_None_



**Fallacies;**

_None_


---

### NJF-06.5_CONTEXT 

An improper name is either not a string (i.e. any other token, or empty), or a string-candidate which does not fulfil the requirements of RFC8259.

An improper value is either empty or an inadmissible token according to RFC8259.


**Supported Requests;**


**Supporting Items;**

_None_



**References;**

_None_



**Fallacies;**

_None_


---

### NJF-06.6 

The service accepts nested objects.


**Supported Requests;**

- [NJF-06](NJF.md#njf-06)

**Supporting Items;**

_None_



**References;**

- `cpp-testsuite; [/json.org/1.json, /json.org/2.json, /json.org/3.json, /json.org/4.json, /json.org/5.json, /json.org/1.json, /json.org/2.json, /json.org/3.json, /json.org/4.json, /json.org/5.json]`


			- Description; Checks that various nested objects are accepted.
			
			
			- JSON Testsuite; /json.org/1.json
			
			
			 ```json
			{
			    "glossary"; {
			        "title"; "example glossary",
					"GlossDiv"; {
			            "title"; "S",
						"GlossList"; {
			                "GlossEntry"; {
			                    "ID"; "SGML",
								"SortAs"; "SGML",
								"GlossTerm"; "Standard Generalized Markup Language",
								"Acronym"; "SGML",
								"Abbrev"; "ISO 8879;1986",
								"GlossDef"; {
			                        "para"; "A meta-markup language, used to create markup languages such as DocBook.",
									"GlossSeeAlso"; ["GML", "XML"]
			                    },
								"GlossSee"; "markup"
			                }
			            }
			        }
			    }
			}
			
			```
			
			
			
			
			- JSON Testsuite; /json.org/2.json
			
			
			 ```json
			{"menu"; {
			  "id"; "file",
			  "value"; "File",
			  "popup"; {
			    "menuitem"; [
			      {"value"; "New", "onclick"; "CreateNewDoc()"},
			      {"value"; "Open", "onclick"; "OpenDoc()"},
			      {"value"; "Close", "onclick"; "CloseDoc()"}
			    ]
			  }
			}}
			
			```
			
			
			
			
			- JSON Testsuite; /json.org/3.json
			
			
			 [Link to file](https://raw.githubusercontent.com/nlohmann/json_test_data/master//json.org/3.json) [Content too large - 26 lines]
			
			
			
			
			
			- JSON Testsuite; /json.org/4.json
			
			
			 [Link to file](https://raw.githubusercontent.com/nlohmann/json_test_data/master//json.org/4.json) [Content too large - 88 lines]
			
			
			
			
			
			- JSON Testsuite; /json.org/5.json
			
			
			 [Link to file](https://raw.githubusercontent.com/nlohmann/json_test_data/master//json.org/5.json) [Content too large - 27 lines]
			
			
			
			
			
			- JSON Testsuite; /json.org/1.json
			
			
			 ```json
			{
			    "glossary"; {
			        "title"; "example glossary",
					"GlossDiv"; {
			            "title"; "S",
						"GlossList"; {
			                "GlossEntry"; {
			                    "ID"; "SGML",
								"SortAs"; "SGML",
								"GlossTerm"; "Standard Generalized Markup Language",
								"Acronym"; "SGML",
								"Abbrev"; "ISO 8879;1986",
								"GlossDef"; {
			                        "para"; "A meta-markup language, used to create markup languages such as DocBook.",
									"GlossSeeAlso"; ["GML", "XML"]
			                    },
								"GlossSee"; "markup"
			                }
			            }
			        }
			    }
			}
			
			```
			
			
			
			
			- JSON Testsuite; /json.org/2.json
			
			
			 ```json
			{"menu"; {
			  "id"; "file",
			  "value"; "File",
			  "popup"; {
			    "menuitem"; [
			      {"value"; "New", "onclick"; "CreateNewDoc()"},
			      {"value"; "Open", "onclick"; "OpenDoc()"},
			      {"value"; "Close", "onclick"; "CloseDoc()"}
			    ]
			  }
			}}
			
			```
			
			
			
			
			- JSON Testsuite; /json.org/3.json
			
			
			 [Link to file](https://raw.githubusercontent.com/nlohmann/json_test_data/master//json.org/3.json) [Content too large - 26 lines]
			
			
			
			
			
			- JSON Testsuite; /json.org/4.json
			
			
			 [Link to file](https://raw.githubusercontent.com/nlohmann/json_test_data/master//json.org/4.json) [Content too large - 88 lines]
			
			
			
			
			
			- JSON Testsuite; /json.org/5.json
			
			
			 [Link to file](https://raw.githubusercontent.com/nlohmann/json_test_data/master//json.org/5.json) [Content too large - 27 lines]
			
			
			
			- cpp-test; [json.org examples]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			TEST_CASE("json.org examples")
			{
			    // here, we list all JSON values from https://json.org/example
			    using FilePtr = std::unique_ptr&lt;FILE, int(*)(FILE*)&gt;;
			
			    SECTION("1.json")
			    {
			        std::ifstream f(TEST_DATA_DIRECTORY "/json.org/1.json");
			        json j;
			        CHECK_NOTHROW(f &gt;&gt; j);
			    }
			
			    SECTION("2.json")
			    {
			        std::ifstream f(TEST_DATA_DIRECTORY "/json.org/2.json");
			        json j;
			        CHECK_NOTHROW(f &gt;&gt; j);
			    }
			
			    SECTION("3.json")
			    {
			        std::ifstream f(TEST_DATA_DIRECTORY "/json.org/3.json");
			        json j;
			        CHECK_NOTHROW(f &gt;&gt; j);
			    }
			
			    SECTION("4.json")
			    {
			        std::ifstream f(TEST_DATA_DIRECTORY "/json.org/4.json");
			        json j;
			        CHECK_NOTHROW(f &gt;&gt; j);
			    }
			
			    SECTION("5.json")
			    {
			        std::ifstream f(TEST_DATA_DIRECTORY "/json.org/5.json");
			        json j;
			        CHECK_NOTHROW(f &gt;&gt; j);
			    }
			    SECTION("FILE 1.json")
			    {
			        const FilePtr f(std::fopen(TEST_DATA_DIRECTORY "/json.org/1.json", "r"), &std::fclose);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f.get()));
			    }
			
			    SECTION("FILE 2.json")
			    {
			        const FilePtr f(std::fopen(TEST_DATA_DIRECTORY "/json.org/2.json", "r"), &std::fclose);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f.get()));
			    }
			
			    SECTION("FILE 3.json")
			    {
			        const FilePtr f(std::fopen(TEST_DATA_DIRECTORY "/json.org/3.json", "r"), &std::fclose);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f.get()));
			    }
			
			    SECTION("FILE 4.json")
			    {
			        const FilePtr f(std::fopen(TEST_DATA_DIRECTORY "/json.org/4.json", "r"), &std::fclose);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f.get()));
			    }
			
			    SECTION("FILE 5.json")
			    {
			        const FilePtr f(std::fopen(TEST_DATA_DIRECTORY "/json.org/5.json", "r"), &std::fclose);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f.get()));
			    }
			}
			
			```
			




**Fallacies;**

_None_


---

### NJF-06.7 

The service does only accept comma as member separator.


**Supported Requests;**

- [NJF-06](NJF.md#njf-06)

**Supporting Items;**

- [NJF-06.7.1](NJF.md#njf-06.7.1)
- [NJF-06.7.2](NJF.md#njf-06.7.2)



**References;**

_None_



**Fallacies;**

_None_


---

### NJF-06.7.1 

The service accepts comma as member separator.


**Supported Requests;**

- [NJF-06.7](NJF.md#njf-06.7)

**Supporting Items;**

_None_



**References;**

- `cpp-testsuite; [/json.org/1.json, /json.org/2.json, /json.org/3.json, /json.org/4.json, /json.org/5.json, /json.org/1.json, /json.org/2.json, /json.org/3.json, /json.org/4.json, /json.org/5.json]`


			- Description; Checks that various arrays with more than one value are accepted.
			
			
			- JSON Testsuite; /json.org/1.json
			
			
			 ```json
			{
			    "glossary"; {
			        "title"; "example glossary",
					"GlossDiv"; {
			            "title"; "S",
						"GlossList"; {
			                "GlossEntry"; {
			                    "ID"; "SGML",
								"SortAs"; "SGML",
								"GlossTerm"; "Standard Generalized Markup Language",
								"Acronym"; "SGML",
								"Abbrev"; "ISO 8879;1986",
								"GlossDef"; {
			                        "para"; "A meta-markup language, used to create markup languages such as DocBook.",
									"GlossSeeAlso"; ["GML", "XML"]
			                    },
								"GlossSee"; "markup"
			                }
			            }
			        }
			    }
			}
			
			```
			
			
			
			
			- JSON Testsuite; /json.org/2.json
			
			
			 ```json
			{"menu"; {
			  "id"; "file",
			  "value"; "File",
			  "popup"; {
			    "menuitem"; [
			      {"value"; "New", "onclick"; "CreateNewDoc()"},
			      {"value"; "Open", "onclick"; "OpenDoc()"},
			      {"value"; "Close", "onclick"; "CloseDoc()"}
			    ]
			  }
			}}
			
			```
			
			
			
			
			- JSON Testsuite; /json.org/3.json
			
			
			 [Link to file](https://raw.githubusercontent.com/nlohmann/json_test_data/master//json.org/3.json) [Content too large - 26 lines]
			
			
			
			
			
			- JSON Testsuite; /json.org/4.json
			
			
			 [Link to file](https://raw.githubusercontent.com/nlohmann/json_test_data/master//json.org/4.json) [Content too large - 88 lines]
			
			
			
			
			
			- JSON Testsuite; /json.org/5.json
			
			
			 [Link to file](https://raw.githubusercontent.com/nlohmann/json_test_data/master//json.org/5.json) [Content too large - 27 lines]
			
			
			
			
			
			- JSON Testsuite; /json.org/1.json
			
			
			 ```json
			{
			    "glossary"; {
			        "title"; "example glossary",
					"GlossDiv"; {
			            "title"; "S",
						"GlossList"; {
			                "GlossEntry"; {
			                    "ID"; "SGML",
								"SortAs"; "SGML",
								"GlossTerm"; "Standard Generalized Markup Language",
								"Acronym"; "SGML",
								"Abbrev"; "ISO 8879;1986",
								"GlossDef"; {
			                        "para"; "A meta-markup language, used to create markup languages such as DocBook.",
									"GlossSeeAlso"; ["GML", "XML"]
			                    },
								"GlossSee"; "markup"
			                }
			            }
			        }
			    }
			}
			
			```
			
			
			
			
			- JSON Testsuite; /json.org/2.json
			
			
			 ```json
			{"menu"; {
			  "id"; "file",
			  "value"; "File",
			  "popup"; {
			    "menuitem"; [
			      {"value"; "New", "onclick"; "CreateNewDoc()"},
			      {"value"; "Open", "onclick"; "OpenDoc()"},
			      {"value"; "Close", "onclick"; "CloseDoc()"}
			    ]
			  }
			}}
			
			```
			
			
			
			
			- JSON Testsuite; /json.org/3.json
			
			
			 [Link to file](https://raw.githubusercontent.com/nlohmann/json_test_data/master//json.org/3.json) [Content too large - 26 lines]
			
			
			
			
			
			- JSON Testsuite; /json.org/4.json
			
			
			 [Link to file](https://raw.githubusercontent.com/nlohmann/json_test_data/master//json.org/4.json) [Content too large - 88 lines]
			
			
			
			
			
			- JSON Testsuite; /json.org/5.json
			
			
			 [Link to file](https://raw.githubusercontent.com/nlohmann/json_test_data/master//json.org/5.json) [Content too large - 27 lines]
			
			
			
			- cpp-test; [json.org examples]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			TEST_CASE("json.org examples")
			{
			    // here, we list all JSON values from https://json.org/example
			    using FilePtr = std::unique_ptr&lt;FILE, int(*)(FILE*)&gt;;
			
			    SECTION("1.json")
			    {
			        std::ifstream f(TEST_DATA_DIRECTORY "/json.org/1.json");
			        json j;
			        CHECK_NOTHROW(f &gt;&gt; j);
			    }
			
			    SECTION("2.json")
			    {
			        std::ifstream f(TEST_DATA_DIRECTORY "/json.org/2.json");
			        json j;
			        CHECK_NOTHROW(f &gt;&gt; j);
			    }
			
			    SECTION("3.json")
			    {
			        std::ifstream f(TEST_DATA_DIRECTORY "/json.org/3.json");
			        json j;
			        CHECK_NOTHROW(f &gt;&gt; j);
			    }
			
			    SECTION("4.json")
			    {
			        std::ifstream f(TEST_DATA_DIRECTORY "/json.org/4.json");
			        json j;
			        CHECK_NOTHROW(f &gt;&gt; j);
			    }
			
			    SECTION("5.json")
			    {
			        std::ifstream f(TEST_DATA_DIRECTORY "/json.org/5.json");
			        json j;
			        CHECK_NOTHROW(f &gt;&gt; j);
			    }
			    SECTION("FILE 1.json")
			    {
			        const FilePtr f(std::fopen(TEST_DATA_DIRECTORY "/json.org/1.json", "r"), &std::fclose);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f.get()));
			    }
			
			    SECTION("FILE 2.json")
			    {
			        const FilePtr f(std::fopen(TEST_DATA_DIRECTORY "/json.org/2.json", "r"), &std::fclose);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f.get()));
			    }
			
			    SECTION("FILE 3.json")
			    {
			        const FilePtr f(std::fopen(TEST_DATA_DIRECTORY "/json.org/3.json", "r"), &std::fclose);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f.get()));
			    }
			
			    SECTION("FILE 4.json")
			    {
			        const FilePtr f(std::fopen(TEST_DATA_DIRECTORY "/json.org/4.json", "r"), &std::fclose);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f.get()));
			    }
			
			    SECTION("FILE 5.json")
			    {
			        const FilePtr f(std::fopen(TEST_DATA_DIRECTORY "/json.org/5.json", "r"), &std::fclose);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f.get()));
			    }
			}
			
			```
			




**Fallacies;**

_None_


---

### NJF-06.7.2 

The service does not accept any other member separator.


**Supported Requests;**

- [NJF-06.7](NJF.md#njf-06.7)

**Supporting Items;**

_None_



**References;**

- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/n_object_comma_instead_of_colon.json]`


			- Description; Checks that comma instead of colon is rejected.
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_object_comma_instead_of_colon.json
			
			
			 ```json
			{"x", null}
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;n]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("n")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_comma_instead_of_colon.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_THROWS_AS(_ = json::parse(f), json::parse_error&);
			        std::ifstream f2(filename);
			        CHECK(!json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			

- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/n_object_double_colon.json]`


			- Description; Checks that double colon is rejected.
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_object_double_colon.json
			
			
			 ```json
			{"x";;"b"}
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;n]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("n")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_double_colon.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_THROWS_AS(_ = json::parse(f), json::parse_error&);
			        std::ifstream f2(filename);
			        CHECK(!json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			

- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/n_object_missing_colon.json, /nst_json_testsuite2/test_parsing/n_object_missing_semicolon.json, /nst_json_testsuite2/test_parsing/n_object_missing_semicolon.json]`


			- Description; Checks that the empty member separator is rejected.
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_object_missing_colon.json
			
			
			 ```json
			{"a" b}
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_object_missing_semicolon.json
			
			
			 ```json
			{"a" "b"}
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_object_missing_semicolon.json
			
			
			 ```json
			{"a" "b"}
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;n]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("n")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_missing_colon.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_missing_semicolon.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_THROWS_AS(_ = json::parse(f), json::parse_error&);
			        std::ifstream f2(filename);
			        CHECK(!json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			

- `cpp-test; [accept;member separator]
(/workspaces/json/TSF/tests/unit-objects.cpp)`


		```cpp
		SECTION("member separator")
		{
		    CHECK(json::accept("{\"foo\"\u003a\"bar\"}"));      //;
		    CHECK(!json::accept("{\"foo\"\uff1a\"bar\"}"));     
		    CHECK(!json::accept("{\"foo\"\ua789\"bar\"}"));
		    CHECK(!json::accept("{\"foo\"\u005b\"bar\"}"));     //[
		    CHECK(!json::accept("{\"foo\"\u007b\"bar\"}"));     //{
		    CHECK(!json::accept("{\"foo\"\u005d\"bar\"}"));     //]
		    CHECK(!json::accept("{\"foo\"\u007d\"bar\"}"));     //}
		    CHECK(!json::accept("{\"foo\"\u002c\"bar\"}"));     //,
		    CHECK(!json::accept("{\"foo\"\u003b\"bar\"}"));     //;
		}
		
		```





**Fallacies;**

_None_


---

### NJF-07 

The service accepts and rejects strings according to RFC8259 §7


**Supported Requests;**

- [WFJ-02](WFJ.md#wfj-02)

**Supporting Items;**

- [NJF-07.1](NJF.md#njf-07.1)
- [NJF-07.2](NJF.md#njf-07.2)
- [NJF-07.3](NJF.md#njf-07.3)
- [NJF-07.4](NJF.md#njf-07.4)
- [NJF-07.5](NJF.md#njf-07.5)
- [NJF-07.7](NJF.md#njf-07.7)
- [NJF-07.6](NJF.md#njf-07.6)



**References;**

_None_



**Fallacies;**

_None_


---

### NJF-07.1 

The service does accept empty string.


**Supported Requests;**

- [NJF-07](NJF.md#njf-07)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [parser class;accept;string]
(/workspaces/json/tests/src/unit-class_parser.cpp)`


		```cpp
		SECTION("string")
		{
		    // empty string
		    CHECK(accept_helper("\"\""));
		
		    SECTION("errors")
		    {
		        // error; tab in string
		        CHECK(accept_helper("\"\t\"") == false);
		        // error; newline in string
		        CHECK(accept_helper("\"\n\"") == false);
		        CHECK(accept_helper("\"\r\"") == false);
		        // error; backspace in string
		        CHECK(accept_helper("\"\b\"") == false);
		        // improve code coverage
		        CHECK(accept_helper("\uFF01") == false);
		        CHECK(accept_helper("[-4;1,]") == false);
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
		
		```


- `cpp-test; [compliance tests from nativejson-benchmark;strings]
(/workspaces/json/tests/src/unit-testsuites.cpp)`


		```cpp
		SECTION("strings")
		{
		    auto TEST_STRING = [](const std::string & json_string, const std::string & expected)
		    {
		        CAPTURE(json_string)
		        CAPTURE(expected)
		        CHECK(json::parse(json_string)[0].get&lt;std::string&gt;() == expected);
		    };
		
		    TEST_STRING("[\"\"]", "");
		    TEST_STRING("[\"Hello\"]", "Hello");
		    TEST_STRING(R"(["Hello\nWorld"])", "Hello\nWorld");
		    //TEST_STRING("[\"Hello\\u0000World\"]", "Hello\0World");
		    TEST_STRING(R"(["\"\\/\b\f\n\r\t"])", "\"\\/\b\f\n\r\t");
		    TEST_STRING(R"(["\u0024"])", "$");         // Dollar sign U+0024
		    TEST_STRING(R"(["\u00A2"])", "\xC2\xA2");     // Cents sign U+00A2
		    TEST_STRING(R"(["\u20AC"])", "\xE2\x82\xAC"); // Euro sign U+20AC
		    TEST_STRING(R"(["\uD834\uDD1E"])", "\xF0\x9D\x84\x9E");  // G clef sign U+1D11E
		}
		
		```





**Fallacies;**

_None_


---

### NJF-07.2 

The service does not accept improperly bounded string.


**Supported Requests;**

- [NJF-07](NJF.md#njf-07)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [parser class;accept;parse errors (accept)]
(/workspaces/json/tests/src/unit-class_parser.cpp)`


		```cpp
		SECTION("parse errors (accept)")
		{
		    // unexpected end of number
		    CHECK(accept_helper("0.") == false);
		    CHECK(accept_helper("-") == false);
		    CHECK(accept_helper("--") == false);
		    CHECK(accept_helper("-0.") == false);
		    CHECK(accept_helper("-.") == false);
		    CHECK(accept_helper("-;") == false);
		    CHECK(accept_helper("0.;") == false);
		    CHECK(accept_helper("e.") == false);
		    CHECK(accept_helper("1e.") == false);
		    CHECK(accept_helper("1e/") == false);
		    CHECK(accept_helper("1e;") == false);
		    CHECK(accept_helper("1E.") == false);
		    CHECK(accept_helper("1E/") == false);
		    CHECK(accept_helper("1E;") == false);
		
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
		    CHECK(accept_helper("{\"foo\";") == false);
		    CHECK(accept_helper("{\"foo\";}") == false);
		    CHECK(accept_helper("{\"foo\";1,}") == false);
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
		    for (int c = 1; c &lt; 128; ++c)
		    {
		        auto s = std::string("\"\\") + std::string(1, static_cast&lt;char&gt;(c)) + "\"";
		
		        switch (c)
		        {
		            // valid escapes
		            case ('"');
		            case ('\\');
		            case ('/');
		            case ('b');
		            case ('f');
		            case ('n');
		            case ('r');
		            case ('t');
		            {
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s)).accept());
		                break;
		            }
		
		            // \u must be followed with four numbers, so we skip it here
		            case ('u');
		            {
		                break;
		            }
		
		            // any other combination of backslash and character is invalid
		            default;
		            {
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s)).accept() == false);
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
		                case ('0');
		                case ('1');
		                case ('2');
		                case ('3');
		                case ('4');
		                case ('5');
		                case ('6');
		                case ('7');
		                case ('8');
		                case ('9');
		                case ('a');
		                case ('b');
		                case ('c');
		                case ('d');
		                case ('e');
		                case ('f');
		                case ('A');
		                case ('B');
		                case ('C');
		                case ('D');
		                case ('E');
		                case ('F');
		                {
		                    return true;
		                }
		
		                default;
		                {
		                    return false;
		                }
		            }
		        };
		
		        for (int c = 1; c &lt; 128; ++c)
		        {
		            std::string const s = "\"\\u";
		
		            // create a string with the iterated character at each position
		            const auto s1 = s + "000" + std::string(1, static_cast&lt;char&gt;(c)) + "\"";
		            const auto s2 = s + "00" + std::string(1, static_cast&lt;char&gt;(c)) + "0\"";
		            const auto s3 = s + "0" + std::string(1, static_cast&lt;char&gt;(c)) + "00\"";
		            const auto s4 = s + std::string(1, static_cast&lt;char&gt;(c)) + "000\"";
		
		            if (valid(c))
		            {
		                CAPTURE(s1)
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s1)).accept());
		                CAPTURE(s2)
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s2)).accept());
		                CAPTURE(s3)
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s3)).accept());
		                CAPTURE(s4)
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s4)).accept());
		            }
		            else
		            {
		                CAPTURE(s1)
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s1)).accept() == false);
		
		                CAPTURE(s2)
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s2)).accept() == false);
		
		                CAPTURE(s3)
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s3)).accept() == false);
		
		                CAPTURE(s4)
		                CHECK(json::parser(nlohmann;;detail;;input_adapter(s4)).accept() == false);
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
		
		```


- `cpp-test; [deserialization;contiguous containers;error cases]
(/workspaces/json/tests/src/unit-deserialization.cpp)`


		```cpp
		SECTION("error cases")
		{
		    SECTION("case 1")
		    {
		        std::array&lt;std::uint8_t, 9&gt; v = {{'\"', 'a', 'a', 'a', 'a', 'a', 'a', '\\', 'u'}};
		        json _;
		        CHECK_THROWS_AS(_ = json::parse(std::begin(v), std::end(v)), json::parse_error&);
		        CHECK(!json::accept(std::begin(v), std::end(v)));
		
		        json j_error;
		        CHECK_NOTHROW(j_error = json::parse(std::begin(v), std::end(v), nullptr, false));
		        CHECK(j_error.is_discarded());
		
		        SaxEventLogger l;
		        CHECK(!json::sax_parse(std::begin(v), std::end(v), &l));
		        CHECK(l.events.size() == 1);
		        CHECK(l.events == std::vector&lt;std::string&gt;({"parse_error(10)"}));
		    }
		
		    SECTION("case 2")
		    {
		        std::array&lt;std::uint8_t, 10&gt; v = {{'\"', 'a', 'a', 'a', 'a', 'a', 'a', '\\', 'u', '1'}};
		        json _;
		        CHECK_THROWS_AS(_ = json::parse(std::begin(v), std::end(v)), json::parse_error&);
		        CHECK(!json::accept(std::begin(v), std::end(v)));
		
		        json j_error;
		        CHECK_NOTHROW(j_error = json::parse(std::begin(v), std::end(v), nullptr, false));
		        CHECK(j_error.is_discarded());
		
		        SaxEventLogger l;
		        CHECK(!json::sax_parse(std::begin(v), std::end(v), &l));
		        CHECK(l.events.size() == 1);
		        CHECK(l.events == std::vector&lt;std::string&gt;({"parse_error(11)"}));
		    }
		
		    SECTION("case 3")
		    {
		        std::array&lt;std::uint8_t, 17&gt; v = {{'\"', 'a', 'a', 'a', 'a', 'a', 'a', '\\', 'u', '1', '1', '1', '1', '1', '1', '1', '1'}};
		        json _;
		        CHECK_THROWS_AS(_ = json::parse(std::begin(v), std::end(v)), json::parse_error&);
		        CHECK(!json::accept(std::begin(v), std::end(v)));
		
		        json j_error;
		        CHECK_NOTHROW(j_error = json::parse(std::begin(v), std::end(v), nullptr, false));
		        CHECK(j_error.is_discarded());
		
		        SaxEventLogger l;
		        CHECK(!json::sax_parse(std::begin(v), std::end(v), &l));
		        CHECK(l.events.size() == 1);
		        CHECK(l.events == std::vector&lt;std::string&gt;({"parse_error(18)"}));
		    }
		
		    SECTION("case 4")
		    {
		        std::array&lt;std::uint8_t, 17&gt; v = {{'\"', 'a', 'a', 'a', 'a', 'a', 'a', 'u', '1', '1', '1', '1', '1', '1', '1', '1', '\\'}};
		        json _;
		        CHECK_THROWS_AS(_ = json::parse(std::begin(v), std::end(v)), json::parse_error&);
		        CHECK(!json::accept(std::begin(v), std::end(v)));
		
		        json j_error;
		        CHECK_NOTHROW(j_error = json::parse(std::begin(v), std::end(v), nullptr, false));
		        CHECK(j_error.is_discarded());
		
		        SaxEventLogger l;
		        CHECK(!json::sax_parse(std::begin(v), std::end(v), &l));
		        CHECK(l.events.size() == 1);
		        CHECK(l.events == std::vector&lt;std::string&gt;({"parse_error(18)"}));
		    }
		
		    SECTION("case 5")
		    {
		        std::array&lt;std::uint8_t, 3&gt; v = {{'\"', 0x7F, 0xC1}};
		        json _;
		        CHECK_THROWS_AS(_ = json::parse(std::begin(v), std::end(v)), json::parse_error&);
		        CHECK(!json::accept(std::begin(v), std::end(v)));
		
		        json j_error;
		        CHECK_NOTHROW(j_error = json::parse(std::begin(v), std::end(v), nullptr, false));
		        CHECK(j_error.is_discarded());
		
		        SaxEventLogger l;
		        CHECK(!json::sax_parse(std::begin(v), std::end(v), &l));
		        CHECK(l.events.size() == 1);
		        CHECK(l.events == std::vector&lt;std::string&gt;({"parse_error(3)"}));
		    }
		
		    SECTION("case 6")
		    {
		        std::array&lt;std::uint8_t, 4&gt; v = {{'\"', 0x7F, 0xDF, 0x7F}};
		        json _;
		        CHECK_THROWS_WITH_AS(_ = json::parse(std::begin(v), std::end(v)), "[json.exception.parse_error.101] parse error at line 1, column 4; syntax error while parsing value - invalid string; ill-formed UTF-8 byte; last read; '\"\x7f\xdf\x7f'", json::parse_error&);
		        CHECK(!json::accept(std::begin(v), std::end(v)));
		
		        json j_error;
		        CHECK_NOTHROW(j_error = json::parse(std::begin(v), std::end(v), nullptr, false));
		        CHECK(j_error.is_discarded());
		
		        SaxEventLogger l;
		        CHECK(!json::sax_parse(std::begin(v), std::end(v), &l));
		        CHECK(l.events.size() == 1);
		        CHECK(l.events == std::vector&lt;std::string&gt;({"parse_error(4)"}));
		    }
		
		    SECTION("case 7")
		    {
		        std::array&lt;std::uint8_t, 4&gt; v = {{'\"', 0x7F, 0xDF, 0xC0}};
		        json _;
		        CHECK_THROWS_AS(_ = json::parse(std::begin(v), std::end(v)), json::parse_error&);
		        CHECK(!json::accept(std::begin(v), std::end(v)));
		
		        json j_error;
		        CHECK_NOTHROW(j_error = json::parse(std::begin(v), std::end(v), nullptr, false));
		        CHECK(j_error.is_discarded());
		
		        SaxEventLogger l;
		        CHECK(!json::sax_parse(std::begin(v), std::end(v), &l));
		        CHECK(l.events.size() == 1);
		        CHECK(l.events == std::vector&lt;std::string&gt;({"parse_error(4)"}));
		    }
		
		    SECTION("case 8")
		    {
		        std::array&lt;std::uint8_t, 4&gt; v = {{'\"', 0x7F, 0xE0, 0x9F}};
		        json _;
		        CHECK_THROWS_AS(_ = json::parse(std::begin(v), std::end(v)), json::parse_error&);
		        CHECK(!json::accept(std::begin(v), std::end(v)));
		
		        json j_error;
		        CHECK_NOTHROW(j_error = json::parse(std::begin(v), std::end(v), nullptr, false));
		        CHECK(j_error.is_discarded());
		
		        SaxEventLogger l;
		        CHECK(!json::sax_parse(std::begin(v), std::end(v), &l));
		        CHECK(l.events.size() == 1);
		        CHECK(l.events == std::vector&lt;std::string&gt;({"parse_error(4)"}));
		    }
		
		    SECTION("case 9")
		    {
		        std::array&lt;std::uint8_t, 4&gt; v = {{'\"', 0x7F, 0xEF, 0xC0}};
		        json _;
		        CHECK_THROWS_AS(_ = json::parse(std::begin(v), std::end(v)), json::parse_error&);
		        CHECK(!json::accept(std::begin(v), std::end(v)));
		
		        json j_error;
		        CHECK_NOTHROW(j_error = json::parse(std::begin(v), std::end(v), nullptr, false));
		        CHECK(j_error.is_discarded());
		
		        SaxEventLogger l;
		        CHECK(!json::sax_parse(std::begin(v), std::end(v), &l));
		        CHECK(l.events.size() == 1);
		        CHECK(l.events == std::vector&lt;std::string&gt;({"parse_error(4)"}));
		    }
		
		    SECTION("case 10")
		    {
		        std::array&lt;std::uint8_t, 4&gt; v = {{'\"', 0x7F, 0xED, 0x7F}};
		        json _;
		        CHECK_THROWS_AS(_ = json::parse(std::begin(v), std::end(v)), json::parse_error&);
		        CHECK(!json::accept(std::begin(v), std::end(v)));
		
		        json j_error;
		        CHECK_NOTHROW(j_error = json::parse(std::begin(v), std::end(v), nullptr, false));
		        CHECK(j_error.is_discarded());
		
		        SaxEventLogger l;
		        CHECK(!json::sax_parse(std::begin(v), std::end(v), &l));
		        CHECK(l.events.size() == 1);
		        CHECK(l.events == std::vector&lt;std::string&gt;({"parse_error(4)"}));
		    }
		
		    SECTION("case 11")
		    {
		        std::array&lt;std::uint8_t, 4&gt; v = {{'\"', 0x7F, 0xF0, 0x8F}};
		        json _;
		        CHECK_THROWS_AS(_ = json::parse(std::begin(v), std::end(v)), json::parse_error&);
		        CHECK(!json::accept(std::begin(v), std::end(v)));
		
		        json j_error;
		        CHECK_NOTHROW(j_error = json::parse(std::begin(v), std::end(v), nullptr, false));
		        CHECK(j_error.is_discarded());
		
		        SaxEventLogger l;
		        CHECK(!json::sax_parse(std::begin(v), std::end(v), &l));
		        CHECK(l.events.size() == 1);
		        CHECK(l.events == std::vector&lt;std::string&gt;({"parse_error(4)"}));
		    }
		
		    SECTION("case 12")
		    {
		        std::array&lt;std::uint8_t, 4&gt; v = {{'\"', 0x7F, 0xF0, 0xC0}};
		        json _;
		        CHECK_THROWS_AS(_ = json::parse(std::begin(v), std::end(v)), json::parse_error&);
		        CHECK(!json::accept(std::begin(v), std::end(v)));
		
		        json j_error;
		        CHECK_NOTHROW(j_error = json::parse(std::begin(v), std::end(v), nullptr, false));
		        CHECK(j_error.is_discarded());
		
		        SaxEventLogger l;
		        CHECK(!json::sax_parse(std::begin(v), std::end(v), &l));
		        CHECK(l.events.size() == 1);
		        CHECK(l.events == std::vector&lt;std::string&gt;({"parse_error(4)"}));
		    }
		
		    SECTION("case 13")
		    {
		        std::array&lt;std::uint8_t, 4&gt; v = {{'\"', 0x7F, 0xF3, 0x7F}};
		        json _;
		        CHECK_THROWS_AS(_ = json::parse(std::begin(v), std::end(v)), json::parse_error&);
		        CHECK(!json::accept(std::begin(v), std::end(v)));
		
		        json j_error;
		        CHECK_NOTHROW(j_error = json::parse(std::begin(v), std::end(v), nullptr, false));
		        CHECK(j_error.is_discarded());
		
		        SaxEventLogger l;
		        CHECK(!json::sax_parse(std::begin(v), std::end(v), &l));
		        CHECK(l.events.size() == 1);
		        CHECK(l.events == std::vector&lt;std::string&gt;({"parse_error(4)"}));
		    }
		
		    SECTION("case 14")
		    {
		        std::array&lt;std::uint8_t, 4&gt; v = {{'\"', 0x7F, 0xF3, 0xC0}};
		        json _;
		        CHECK_THROWS_AS(_ = json::parse(std::begin(v), std::end(v)), json::parse_error&);
		        CHECK(!json::accept(std::begin(v), std::end(v)));
		
		        json j_error;
		        CHECK_NOTHROW(j_error = json::parse(std::begin(v), std::end(v), nullptr, false));
		        CHECK(j_error.is_discarded());
		
		        SaxEventLogger l;
		        CHECK(!json::sax_parse(std::begin(v), std::end(v), &l));
		        CHECK(l.events.size() == 1);
		        CHECK(l.events == std::vector&lt;std::string&gt;({"parse_error(4)"}));
		    }
		
		    SECTION("case 15")
		    {
		        std::array&lt;std::uint8_t, 4&gt; v = {{'\"', 0x7F, 0xF4, 0x7F}};
		        json _;
		        CHECK_THROWS_AS(_ = json::parse(std::begin(v), std::end(v)), json::parse_error&);
		        CHECK(!json::accept(std::begin(v), std::end(v)));
		
		        json j_error;
		        CHECK_NOTHROW(j_error = json::parse(std::begin(v), std::end(v), nullptr, false));
		        CHECK(j_error.is_discarded());
		
		        SaxEventLogger l;
		        CHECK(!json::sax_parse(std::begin(v), std::end(v), &l));
		        CHECK(l.events.size() == 1);
		        CHECK(l.events == std::vector&lt;std::string&gt;({"parse_error(4)"}));
		    }
		
		    SECTION("case 16")
		    {
		        std::array&lt;std::uint8_t, 6&gt; v = {{'{', '\"', '\"', ';', '1', '1'}};
		        json _;
		        CHECK_THROWS_AS(_ = json::parse(std::begin(v), std::end(v)), json::parse_error&);
		        CHECK(!json::accept(std::begin(v), std::end(v)));
		
		        json j_error;
		        CHECK_NOTHROW(j_error = json::parse(std::begin(v), std::end(v), nullptr, false));
		        CHECK(j_error.is_discarded());
		
		        SaxEventLogger l;
		        CHECK(!json::sax_parse(std::begin(v), std::end(v), &l));
		        CHECK(l.events.size() == 4);
		        CHECK(l.events == std::vector&lt;std::string&gt;(
		        {
		            "start_object()", "key()", "number_unsigned(11)",
		            "parse_error(7)"
		        }));
		    }
		}
		
		```


- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/n_string_no_quotes_with_bad_escape.json, /nst_json_testsuite2/test_parsing/n_string_single_doublequote.json, /nst_json_testsuite2/test_parsing/n_string_single_quote.json, /nst_json_testsuite2/test_parsing/n_string_single_string_no_double_quotes.json]`


			- Description; 
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_string_no_quotes_with_bad_escape.json
			
			
			 ```json
			[\n]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_string_single_doublequote.json
			
			
			 ```json
			"
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_string_single_quote.json
			
			
			 ```json
			['single quote']
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_string_single_string_no_double_quotes.json
			
			
			 ```json
			abc
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;n]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("n")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_no_quotes_with_bad_escape.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_single_doublequote.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_single_quote.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_single_string_no_double_quotes.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_THROWS_AS(_ = json::parse(f), json::parse_error&);
			        std::ifstream f2(filename);
			        CHECK(!json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			




**Fallacies;**

_None_


---

### NJF-07.3 

The service does not accept unescaped control characters.


**Supported Requests;**

- [NJF-07](NJF.md#njf-07)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [parser class;accept;string;errors]
(/workspaces/json/tests/src/unit-class_parser.cpp)`


		```cpp
		SECTION("errors")
		{
		    // error; tab in string
		    CHECK(accept_helper("\"\t\"") == false);
		    // error; newline in string
		    CHECK(accept_helper("\"\n\"") == false);
		    CHECK(accept_helper("\"\r\"") == false);
		    // error; backspace in string
		    CHECK(accept_helper("\"\b\"") == false);
		    // improve code coverage
		    CHECK(accept_helper("\uFF01") == false);
		    CHECK(accept_helper("[-4;1,]") == false);
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
		
		```





**Fallacies;**

_None_


---

### NJF-07.4 

The service does accept escaped control characters.


**Supported Requests;**

- [NJF-07](NJF.md#njf-07)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [parser class;accept;string;escaped]
(/workspaces/json/tests/src/unit-class_parser.cpp)`


		```cpp
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
		
		```


- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/y_string_1_2_3_bytes_UTF-8_sequences.json, /nst_json_testsuite2/test_parsing/y_string_accepted_surrogate_pair.json, /nst_json_testsuite2/test_parsing/y_string_accepted_surrogate_pairs.json, /nst_json_testsuite2/test_parsing/y_string_allowed_escapes.json, /nst_json_testsuite2/test_parsing/y_string_backslash_and_u_escaped_zero.json, /nst_json_testsuite2/test_parsing/y_string_backslash_doublequotes.json, /nst_json_testsuite2/test_parsing/y_string_comments.json, /nst_json_testsuite2/test_parsing/y_string_double_escape_a.json, /nst_json_testsuite2/test_parsing/y_string_double_escape_n.json, /nst_json_testsuite2/test_parsing/y_string_escaped_control_character.json, /nst_json_testsuite2/test_parsing/y_string_escaped_noncharacter.json]`


			- Description; Checks that various escaped control and unicode characters are accepted.
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_string_1_2_3_bytes_UTF-8_sequences.json
			
			
			 ```json
			["\u0060\u012a\u12AB"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_string_accepted_surrogate_pair.json
			
			
			 ```json
			["\uD801\udc37"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_string_accepted_surrogate_pairs.json
			
			
			 ```json
			["\ud83d\ude39\ud83d\udc8d"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_string_allowed_escapes.json
			
			
			 ```json
			["\"\\\/\b\f\n\r\t"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_string_backslash_and_u_escaped_zero.json
			
			
			 ```json
			["\\u0000"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_string_backslash_doublequotes.json
			
			
			 ```json
			["\""]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_string_comments.json
			
			
			 ```json
			["a/*b*/c/*d//e"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_string_double_escape_a.json
			
			
			 ```json
			["\\a"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_string_double_escape_n.json
			
			
			 ```json
			["\\n"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_string_escaped_control_character.json
			
			
			 ```json
			["\u0012"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_string_escaped_noncharacter.json
			
			
			 ```json
			["\uFFFF"]
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;y]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("y")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_string_1_2_3_bytes_UTF-8_sequences.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_string_accepted_surrogate_pair.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_string_accepted_surrogate_pairs.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_string_allowed_escapes.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_string_backslash_and_u_escaped_zero.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_string_backslash_doublequotes.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_string_comments.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_string_double_escape_a.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_string_double_escape_n.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_string_escaped_control_character.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_string_escaped_noncharacter.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f));
			        std::ifstream f2(filename);
			        CHECK(json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			

- `cpp-test; [Unicode (1/5);\\uxxxx sequences;correct sequences]
(/workspaces/json/tests/src/unit-unicode1.cpp)`


		```cpp
		SECTION("correct sequences")
		{
		    // generate all UTF-8 code points; in total, 1112064 code points are
		    // generated; 0x1FFFFF code points - 2048 invalid values between
		    // 0xD800 and 0xDFFF.
		    for (std::size_t cp = 0; cp &lt;= 0x10FFFFu; ++cp)
		    {
		        // string to store the code point as in \uxxxx format
		        std::string json_text = "\"";
		
		        // decide whether to use one or two \uxxxx sequences
		        if (cp &lt; 0x10000u)
		        {
		            // The Unicode standard permanently reserves these code point
		            // values for UTF-16 encoding of the high and low surrogates, and
		            // they will never be assigned a character, so there should be no
		            // reason to encode them. The official Unicode standard says that
		            // no UTF forms, including UTF-16, can encode these code points.
		            if (cp &gt;= 0xD800u && cp &lt;= 0xDFFFu)
		            {
		                // if we would not skip these code points, we would get a
		                // "missing low surrogate" exception
		                continue;
		            }
		
		            // code points in the Basic Multilingual Plane can be
		            // represented with one \uxxxx sequence
		            json_text += codepoint_to_unicode(cp);
		        }
		        else
		        {
		            // To escape an extended character that is not in the Basic
		            // Multilingual Plane, the character is represented as a
		            // 12-character sequence, encoding the UTF-16 surrogate pair
		            const auto codepoint1 = 0xd800u + (((cp - 0x10000u) &gt;&gt; 10) & 0x3ffu);
		            const auto codepoint2 = 0xdc00u + ((cp - 0x10000u) & 0x3ffu);
		            json_text += codepoint_to_unicode(codepoint1) + codepoint_to_unicode(codepoint2);
		        }
		
		        json_text += "\"";
		        CAPTURE(json_text)
		        json _;
		        CHECK_NOTHROW(_ = json::parse(json_text));
		    }
		}
		
		```


- `cpp-test; [accept;basic multilingual plane]
(/workspaces/json/TSF/tests/unit-strings.cpp)`


		```cpp
		SECTION("basic multilingual plane")
		{
		    for (uint32_t i = 0x0000; i&lt;=0xFFFF; i++)
		    {
		        if (i&gt;=0xD800 && i&lt;=0xDFFF)
		        {
		            // skip the utf-16 surrogates
		            continue;
		        }
		        std::ostringstream temp;
		        temp &lt;&lt; "\"\\u" &lt;&lt; std::hex &lt;&lt; std::uppercase &lt;&lt; std::setfill('0') &lt;&lt; std::setw(4) &lt;&lt; i &lt;&lt; "\"";
		        CHECK(json::accept(temp.str()));
		    }
		}
		
		```





**Fallacies;**

_None_


---

### NJF-07.5 

The service does accept UTF-16 surrogate pairs.


**Supported Requests;**

- [NJF-07](NJF.md#njf-07)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [parser class;accept;string;escaped]
(/workspaces/json/tests/src/unit-class_parser.cpp)`


		```cpp
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
		
		```


- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/y_string_accepted_surrogate_pair.json, /nst_json_testsuite2/test_parsing/y_string_accepted_surrogate_pairs.json]`


			- Description; Checks that single and multiple surrogates are accepted.
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_string_accepted_surrogate_pair.json
			
			
			 ```json
			["\uD801\udc37"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_string_accepted_surrogate_pairs.json
			
			
			 ```json
			["\ud83d\ude39\ud83d\udc8d"]
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;y]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("y")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_string_accepted_surrogate_pair.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_string_accepted_surrogate_pairs.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f));
			        std::ifstream f2(filename);
			        CHECK(json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			




**Fallacies;**

_None_


---

### NJF-07.6 

The service does accept non-empty strings.


**Supported Requests;**

- [NJF-07](NJF.md#njf-07)

**Supporting Items;**

_None_



**References;**

_None_



**Fallacies;**

_None_


---

### NJF-07.7 

The service does not accept escaped invalid characters.


**Supported Requests;**

- [NJF-07](NJF.md#njf-07)

**Supporting Items;**

_None_



**References;**

- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape.json, /nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape_u.json, /nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape_u1.json, /nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape_u1x.json, /nst_json_testsuite2/test_parsing/n_string_accentuated_char_no_quotes.json, /nst_json_testsuite2/test_parsing/n_string_backslash_00.json, /nst_json_testsuite2/test_parsing/n_string_escape_x.json, /nst_json_testsuite2/test_parsing/n_string_escaped_backslash_bad.json, /nst_json_testsuite2/test_parsing/n_string_escaped_ctrl_char_tab.json, /nst_json_testsuite2/test_parsing/n_string_escaped_emoji.json, /nst_json_testsuite2/test_parsing/n_string_incomplete_escape.json, /nst_json_testsuite2/test_parsing/n_string_incomplete_escaped_character.json, /nst_json_testsuite2/test_parsing/n_string_incomplete_surrogate.json, /nst_json_testsuite2/test_parsing/n_string_incomplete_surrogate_escape_invalid.json, /nst_json_testsuite2/test_parsing/n_string_invalid-utf-8-in-escape.json, /nst_json_testsuite2/test_parsing/n_string_invalid_backslash_esc.json, /nst_json_testsuite2/test_parsing/n_string_invalid_unicode_escape.json, /nst_json_testsuite2/test_parsing/n_string_invalid_utf8_after_escape.json]`


			- Description; Checks that various illegal control characters and utf-8 characters are rejected.
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape.json
			
			
			 ```json
			["\uD800\"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape_u.json
			
			
			 ```json
			["\uD800\u"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape_u1.json
			
			
			 ```json
			["\uD800\u1"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape_u1x.json
			
			
			 ```json
			["\uD800\u1x"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_string_accentuated_char_no_quotes.json
			
			
			 ```json
			[é]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_string_backslash_00.json
			
			
			 ```json
			["\ "]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_string_escape_x.json
			
			
			 ```json
			["\x00"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_string_escaped_backslash_bad.json
			
			
			 ```json
			["\\\"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_string_escaped_ctrl_char_tab.json
			
			
			 ```json
			["\	"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_string_escaped_emoji.json
			
			
			 ```json
			["\🌀"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_string_incomplete_escape.json
			
			
			 ```json
			["\"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_string_incomplete_escaped_character.json
			
			
			 ```json
			["\u00A"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_string_incomplete_surrogate.json
			
			
			 ```json
			["\uD834\uDd"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_string_incomplete_surrogate_escape_invalid.json
			
			
			 ```json
			["\uD800\uD800\x"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_string_invalid-utf-8-in-escape.json
			
			
			 ```json
			["\uﮒ"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_string_invalid_backslash_esc.json
			
			
			 ```json
			["\a"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_string_invalid_unicode_escape.json
			
			
			 ```json
			["\uqqqq"]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_string_invalid_utf8_after_escape.json
			
			
			 ```json
			["\ﮒ"]
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;n]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("n")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape_u.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape_u1.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape_u1x.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_accentuated_char_no_quotes.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_backslash_00.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_escape_x.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_escaped_backslash_bad.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_escaped_ctrl_char_tab.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_escaped_emoji.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_incomplete_escape.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_incomplete_escaped_character.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_incomplete_surrogate.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_incomplete_surrogate_escape_invalid.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_invalid-utf-8-in-escape.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_invalid_backslash_esc.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_invalid_unicode_escape.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_invalid_utf8_after_escape.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_THROWS_AS(_ = json::parse(f), json::parse_error&);
			        std::ifstream f2(filename);
			        CHECK(!json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			




**Fallacies;**

_None_


---

### NJF-08 

The service accepts numbers according to RFC8259 §6.


**Supported Requests;**

- [WFJ-03](WFJ.md#wfj-03)

**Supporting Items;**

- [NJF-08.1](NJF.md#njf-08.1)
- [NJF-08.2](NJF.md#njf-08.2)
- [NJF-08.3](NJF.md#njf-08.3)
- [NJF-08.4](NJF.md#njf-08.4)
- [NJF-08.5](NJF.md#njf-08.5)
- [NJF-08.6](NJF.md#njf-08.6)
- [NJF-08.7](NJF.md#njf-08.7)
- [NJF-08.8](NJF.md#njf-08.8)
- [NJF-08.9](NJF.md#njf-08.9)



**References;**

_None_



**Fallacies;**

_None_


---

### NJF-08.1 

The service does accept integers.


**Supported Requests;**

- [NJF-08](NJF.md#njf-08)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [parser class;accept;number;integers]
(/workspaces/json/tests/src/unit-class_parser.cpp)`


		```cpp
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
		        // From RFC8259, Section 6;
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
		        // i.e. -(2**63) -&gt; (2**64)-1.
		
		        // -(2**63)    ** Note; compilers see negative literals as negated positive numbers (hence the -1))
		        CHECK(accept_helper("-9223372036854775808"));
		        // (2**63)-1
		        CHECK(accept_helper("9223372036854775807"));
		        // (2**64)-1
		        CHECK(accept_helper("18446744073709551615"));
		    }
		}
		
		```





**Fallacies;**

_None_


---

### NJF-08.2 

The service does accept integers according to IEEE 754 binary64.


**Supported Requests;**

- [NJF-08](NJF.md#njf-08)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [parser class;accept;number;integers;edge cases]
(/workspaces/json/tests/src/unit-class_parser.cpp)`


		```cpp
		SECTION("edge cases")
		{
		    // From RFC8259, Section 6;
		    // Note that when such software is used, numbers that are
		    // integers and are in the range [-(2**53)+1, (2**53)-1]
		    // are interoperable in the sense that implementations will
		    // agree exactly on their numeric values.
		
		    // -(2**53)+1
		    CHECK(accept_helper("-9007199254740991"));
		    // (2**53)-1
		    CHECK(accept_helper("9007199254740991"));
		}
		
		```





**Fallacies;**

_None_


---

### NJF-08.3 

The service does not accept NaN, infinity. (Could be added)


**Supported Requests;**

- [NJF-08](NJF.md#njf-08)

**Supporting Items;**

_None_



**References;**

_None_



**Fallacies;**

_None_


---

### NJF-08.4 

The service does accept e or E.


**Supported Requests;**

- [NJF-08](NJF.md#njf-08)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [parser class;accept;number;integers;with exponent]
(/workspaces/json/tests/src/unit-class_parser.cpp)`


		```cpp
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
		
		```


- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/y_number_real_capital_e.json, /nst_json_testsuite2/test_parsing/y_number_real_capital_e_neg_exp.json, /nst_json_testsuite2/test_parsing/y_number_real_capital_e_pos_exp.json, /nst_json_testsuite2/test_parsing/y_number_real_exponent.json, /nst_json_testsuite2/test_parsing/y_number_real_fraction_exponent.json, /nst_json_testsuite2/test_parsing/y_number_real_neg_exp.json, /nst_json_testsuite2/test_parsing/y_number_real_pos_exponent.json]`


			- Description; Checks that various numbers with exponent are accepted.
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_number_real_capital_e.json
			
			
			 ```json
			[1E22]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_number_real_capital_e_neg_exp.json
			
			
			 ```json
			[1E-2]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_number_real_capital_e_pos_exp.json
			
			
			 ```json
			[1E+2]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_number_real_exponent.json
			
			
			 ```json
			[123e45]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_number_real_fraction_exponent.json
			
			
			 ```json
			[123.456e78]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_number_real_neg_exp.json
			
			
			 ```json
			[1e-2]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/y_number_real_pos_exponent.json
			
			
			 ```json
			[1e+2]
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;y]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("y")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_number_real_capital_e.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_number_real_capital_e_neg_exp.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_number_real_capital_e_pos_exp.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_number_real_exponent.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_number_real_fraction_exponent.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_number_real_neg_exp.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_number_real_pos_exponent.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_NOTHROW(_ = json::parse(f));
			        std::ifstream f2(filename);
			        CHECK(json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			




**Fallacies;**

_None_


---

### NJF-08.5 

The service does not accept cyrillic e u0415, u0436, nor exp. (could be added)


**Supported Requests;**

- [NJF-08](NJF.md#njf-08)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [accept;exponents;U+0425]
(/workspaces/json/TSF/tests/unit-numbers.cpp)`


		```cpp
		SECTION("U+0425")
		{            
		    CHECK(!json::accept("0\u0425123"));
		    CHECK(!json::accept("123\u04250"));
		    CHECK(!json::accept("0.123\u0425123"));
		    CHECK(!json::accept("1.23\u0425123"));
		    CHECK(!json::accept("1.23\u04250"));
		}
		
		```


- `cpp-test; [accept;exponents;U+0436]
(/workspaces/json/TSF/tests/unit-numbers.cpp)`


		```cpp
		SECTION("U+0436")
		{            
		    CHECK(!json::accept("0\u0436123"));
		    CHECK(!json::accept("123\u04360"));
		    CHECK(!json::accept("0.123\u0436123"));
		    CHECK(!json::accept("1.23\u0436123"));
		    CHECK(!json::accept("1.23\u04360"));
		}
		
		```





**Fallacies;**

_None_


---

### NJF-08.6 

The service does not accept invalid syntax for numbers.


**Supported Requests;**

- [NJF-08](NJF.md#njf-08)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [parser class;accept;number;invalid numbers]
(/workspaces/json/tests/src/unit-class_parser.cpp)`


		```cpp
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
		    CHECK(accept_helper("-0.0;") == false);
		    CHECK(accept_helper("-0.0Z") == false);
		    CHECK(accept_helper("-0E123;") == false);
		    CHECK(accept_helper("-0e0-;") == false);
		    CHECK(accept_helper("-0e-;") == false);
		    CHECK(accept_helper("-0f") == false);
		
		    // numbers must not begin with "+"
		    CHECK(accept_helper("+1") == false);
		    CHECK(accept_helper("+0") == false);
		}
		
		```


- `cpp-test; [nst's JSONTestSuite (2);test_parsing;n]
(/workspaces/json/tests/src/unit-testsuites.cpp)`


		```cpp
		SECTION("n")
		{
		    for (const auto* filename ;
		            {
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_1_true_without_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_a_invalid_utf8.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_colon_instead_of_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_comma_after_close.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_comma_and_number.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_double_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_double_extra_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_extra_close.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_extra_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_incomplete.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_incomplete_invalid_value.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_inner_array_no_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_invalid_utf8.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_items_separated_by_semicolon.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_just_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_just_minus.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_missing_value.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_newlines_unclosed.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_number_and_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_number_and_several_commas.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_spaces_vertical_tab_formfeed.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_star_inside.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_unclosed.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_unclosed_trailing_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_unclosed_with_new_lines.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_unclosed_with_object_inside.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_incomplete_false.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_incomplete_null.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_incomplete_true.json",
		                //TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_multidigit_number_then_00.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_++.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_+1.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_+Inf.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_-01.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_-1.0..json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_-2..json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_-NaN.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_.-1.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_.2e-3.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_0.1.2.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_0.3e+.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_0.3e.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_0.e1.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_0_capital_E+.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_0_capital_E.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_0e+.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_0e.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_1.0e+.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_1.0e-.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_1.0e.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_1_000.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_1eE2.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_2.e+3.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_2.e-3.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_2.e3.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_9.e+.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_Inf.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_NaN.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_U+FF11_fullwidth_digit_one.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_expression.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_hex_1_digit.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_hex_2_digits.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_infinity.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_invalid+-.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_invalid-negative-real.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_invalid-utf-8-in-bigger-int.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_invalid-utf-8-in-exponent.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_invalid-utf-8-in-int.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_minus_infinity.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_minus_sign_with_trailing_garbage.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_minus_space_1.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_neg_int_starting_with_zero.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_neg_real_without_int_part.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_neg_with_garbage_at_end.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_real_garbage_after_e.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_real_with_invalid_utf8_after_e.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_real_without_fractional_part.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_starting_with_dot.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_with_alpha.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_with_alpha_char.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_with_leading_zero.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_bad_value.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_bracket_key.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_comma_instead_of_colon.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_double_colon.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_emoji.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_garbage_at_end.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_key_with_single_quotes.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_lone_continuation_byte_in_key_and_trailing_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_missing_colon.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_missing_key.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_missing_semicolon.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_missing_value.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_no-colon.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_non_string_key.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_non_string_key_but_huge_number_instead.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_repeated_null_null.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_several_trailing_commas.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_single_quote.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_trailing_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_trailing_comment.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_trailing_comment_open.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_trailing_comment_slash_open.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_trailing_comment_slash_open_incomplete.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_two_commas_in_a_row.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_unquoted_key.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_unterminated-value.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_with_single_string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_with_trailing_garbage.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_single_space.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape_u.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape_u1.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape_u1x.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_accentuated_char_no_quotes.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_backslash_00.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_escape_x.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_escaped_backslash_bad.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_escaped_ctrl_char_tab.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_escaped_emoji.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_incomplete_escape.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_incomplete_escaped_character.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_incomplete_surrogate.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_incomplete_surrogate_escape_invalid.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_invalid-utf-8-in-escape.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_invalid_backslash_esc.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_invalid_unicode_escape.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_invalid_utf8_after_escape.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_leading_uescaped_thinspace.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_no_quotes_with_bad_escape.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_single_doublequote.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_single_quote.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_single_string_no_double_quotes.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_start_escape_unclosed.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_unescaped_crtl_char.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_unescaped_newline.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_unescaped_tab.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_unicode_CapitalU.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_with_trailing_garbage.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_U+2060_word_joined.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_UTF8_BOM_no_data.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_angle_bracket_..json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_angle_bracket_null.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_array_trailing_garbage.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_array_with_extra_array_close.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_array_with_unclosed_string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_ascii-unicode-identifier.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_capitalized_True.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_close_unopened_array.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_comma_instead_of_closing_brace.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_double_array.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_end_array.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_incomplete_UTF8_BOM.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_lone-invalid-utf-8.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_lone-open-bracket.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_no_data.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_null-byte-outside-string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_number_with_trailing_garbage.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_object_followed_by_closing_object.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_object_unclosed_no_value.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_object_with_comment.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_object_with_trailing_garbage.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_array_apostrophe.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_array_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_array_open_object.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_array_open_string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_array_string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_object.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_object_close_array.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_object_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_object_open_array.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_object_open_string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_object_string_with_apostrophes.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_open.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_single_eacute.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_single_star.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_trailing_#.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_uescaped_LF_before_string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_unclosed_array.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_unclosed_array_partial_null.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_unclosed_array_unfinished_false.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_unclosed_array_unfinished_true.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_unclosed_object.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_unicode-identifier.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_whitespace_U+2060_word_joiner.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_whitespace_formfeed.json"
		            }
		        )
		    {
		        CAPTURE(filename)
		        std::ifstream f(filename);
		        json _;
		        CHECK_THROWS_AS(_ = json::parse(f), json::parse_error&);
		        std::ifstream f2(filename);
		        CHECK(!json::accept(f2));
		    }
		}
		
		```


- `cpp-test; [accept;operators]
(/workspaces/json/TSF/tests/unit-numbers.cpp)`


		```cpp
		SECTION("operators")
		{
		    SECTION("plus")
		    {
		        CHECK(!json::accept("1+1"));
		        CHECK(!json::accept("0.1+1"));
		        CHECK(!json::accept("0.1+1.0"));
		        CHECK(!json::accept("0+0.1"));
		        CHECK(!json::accept("0.1\u00452+1"));
		        CHECK(!json::accept("0.1\u00652+1"));
		        CHECK(!json::accept("1+0.1\u00652"));
		        CHECK(!json::accept("3.5+0.1\u00652"));
		    }
		    SECTION("minus")
		    {
		
		        CHECK(!json::accept("1-1"));
		        CHECK(!json::accept("0.1-1"));
		        CHECK(!json::accept("0.1-1.0"));
		        CHECK(!json::accept("0-0.1"));
		        CHECK(!json::accept("0.1\u00452-1"));
		        CHECK(!json::accept("0.1\u00652-1"));
		        CHECK(!json::accept("1-0.1\u00652"));
		        CHECK(!json::accept("3.5-0.1\u00652"));
		    }
		    SECTION("brackets")
		    {
		
		        CHECK(!json::accept("(145)"));
		        CHECK(!json::accept("(34.32874)"));
		        CHECK(!json::accept("42\u0045(134)"));
		        CHECK(!json::accept("42\u0065(134)"));
		    }
		    SECTION("factorial")
		    {
		
		        CHECK(!json::accept("13!"));
		    }
		    SECTION("multiplication")
		    {
		
		        CHECK(!json::accept("1*1"));
		        CHECK(!json::accept("1.45*5"));
		        CHECK(!json::accept("154*23.76"));
		        CHECK(!json::accept("1\u004545*3"));
		        CHECK(!json::accept("1\u006545*3"));
		        CHECK(!json::accept("3*6\u004512"));
		        CHECK(!json::accept("3*6\u006512"));
		    }
		    SECTION("division")
		    {
		
		        CHECK(!json::accept("0/0"));
		        CHECK(!json::accept("1.45/5"));
		        CHECK(!json::accept("154/23.76"));
		        CHECK(!json::accept("1\u004545/3"));
		        CHECK(!json::accept("1\u006545/3"));
		        CHECK(!json::accept("7/6\u004512"));
		        CHECK(!json::accept("7/6\u006512"));
		    }
		    SECTION("comma")
		    {
		
		        CHECK(!json::accept("0,0"));
		        CHECK(!json::accept("100,000"));
		        CHECK(!json::accept("1,000.23"));
		    }
		}
		
		```





**Fallacies;**

_None_


---

### NJF-08.7 

The service does accept decimal points.


**Supported Requests;**

- [NJF-08](NJF.md#njf-08)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [parser class;accept;number;floating-point]
(/workspaces/json/tests/src/unit-class_parser.cpp)`


		```cpp
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
		
		```





**Fallacies;**

_None_


---

### NJF-08.8 

The service does not accept leading zeroes.


**Supported Requests;**

- [NJF-08](NJF.md#njf-08)

**Supporting Items;**

_None_



**References;**

- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/n_number_-01.json, /nst_json_testsuite2/test_parsing/n_number_neg_int_starting_with_zero.json]`


			- Description; Checks that -01 is rejected.
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_number_-01.json
			
			
			 ```json
			[-01]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_number_neg_int_starting_with_zero.json
			
			
			 ```json
			[-012]
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;n]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("n")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_-01.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_neg_int_starting_with_zero.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_THROWS_AS(_ = json::parse(f), json::parse_error&);
			        std::ifstream f2(filename);
			        CHECK(!json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			

- `cpp-test; [parser class;accept;number;invalid numbers]
(/workspaces/json/tests/src/unit-class_parser.cpp)`


		```cpp
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
		    CHECK(accept_helper("-0.0;") == false);
		    CHECK(accept_helper("-0.0Z") == false);
		    CHECK(accept_helper("-0E123;") == false);
		    CHECK(accept_helper("-0e0-;") == false);
		    CHECK(accept_helper("-0e-;") == false);
		    CHECK(accept_helper("-0f") == false);
		
		    // numbers must not begin with "+"
		    CHECK(accept_helper("+1") == false);
		    CHECK(accept_helper("+0") == false);
		}
		
		```


- `cpp-test; [accept;Leading zeroes]
(/workspaces/json/TSF/tests/unit-numbers.cpp)`


		```cpp
		SECTION("Leading zeroes")
		{
		    CHECK(!json::accept("01.0"));
		    CHECK(!json::accept("05\u004542"));
		    CHECK(!json::accept("05\u006542"));
		    CHECK(!json::accept("00"));
		    CHECK(!json::accept("000000000000000000000000000000000000000000000000"));
		    CHECK(!json::accept("0000000000000000000000000000000000042"));
		    CHECK(!json::accept("-01.0"));
		    CHECK(!json::accept("-05\u004542"));
		    CHECK(!json::accept("-05\u006542"));
		    CHECK(!json::accept("-00"));
		    CHECK(!json::accept("-000000000000000000000000000000000000000000000000"));
		    CHECK(!json::accept("-0000000000000000000000000000000000042"));
		}
		
		```





**Fallacies;**

_None_


---

### NJF-08.9 

The service does not accept any base exceeding 10 in ist standard representation. (could be added)


**Supported Requests;**

- [NJF-08](NJF.md#njf-08)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [parser class;accept;number;integers]
(/workspaces/json/tests/src/unit-class_parser.cpp)`


		```cpp
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
		        // From RFC8259, Section 6;
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
		        // i.e. -(2**63) -&gt; (2**64)-1.
		
		        // -(2**63)    ** Note; compilers see negative literals as negated positive numbers (hence the -1))
		        CHECK(accept_helper("-9223372036854775808"));
		        // (2**63)-1
		        CHECK(accept_helper("9223372036854775807"));
		        // (2**64)-1
		        CHECK(accept_helper("18446744073709551615"));
		    }
		}
		
		```


- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/n_number_hex_1_digit.json, /nst_json_testsuite2/test_parsing/n_number_hex_2_digits.json, /nst_json_testsuite2/test_parsing/n_number_hex_2_digits.json]`


			- Description; Rejects Hexadecimals
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_number_hex_1_digit.json
			
			
			 ```json
			[0x1]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_number_hex_2_digits.json
			
			
			 ```json
			[0x42]
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_number_hex_2_digits.json
			
			
			 ```json
			[0x42]
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;n]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("n")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_hex_1_digit.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_hex_2_digits.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_THROWS_AS(_ = json::parse(f), json::parse_error&);
			        std::ifstream f2(filename);
			        CHECK(!json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			

- `cpp-test; [accept;bases]
(/workspaces/json/TSF/tests/unit-numbers.cpp)`


		```cpp
		SECTION("bases")
		{
		    SECTION("Octal")
		    {
		        CHECK(!json::accept("o42"));
		        CHECK(!json::accept("q42"));
		        CHECK(!json::accept("0o42"));
		        CHECK(!json::accept("\\42"));
		        CHECK(!json::accept("@42"));
		        CHECK(!json::accept("&42"));
		        CHECK(!json::accept("$42"));
		        CHECK(!json::accept("42o"));
		    }
		    // Recall that hexadecimal is also checked in nst_json_testsuite2/test_parsing/n_number_hex_1_digit.json
		    // and nst_json_testsuite2/test_parsing/n_number_hex_2_digits.json
		    SECTION("Hexadecimal")
		    {
		        CHECK(!json::accept("0x42"));
		        CHECK(!json::accept("42h"));
		        CHECK(!json::accept("42H"));
		        CHECK(!json::accept("0F42h"));
		        CHECK(!json::accept("0F42H"));
		        CHECK(!json::accept("$4A2"));
		        CHECK(!json::accept("16r42"));
		        CHECK(!json::accept("0h42"));
		        CHECK(!json::accept("#42"));
		        CHECK(!json::accept("#16r42"));
		        CHECK(!json::accept("42F3"));
		    }
		}
		
		```





**Fallacies;**

_None_


---

### NJF-09 

The service does accept the six structural characters.


**Supported Requests;**


**Supporting Items;**

_None_



**References;**

_None_



**Fallacies;**

_None_


---

### NJF-10 

The service does not accept any other structural characters.


**Supported Requests;**


**Supporting Items;**

_None_



**References;**

- `cpp-test; [nst's JSONTestSuite (2);test_parsing;n]
(/workspaces/json/tests/src/unit-testsuites.cpp)`


		```cpp
		SECTION("n")
		{
		    for (const auto* filename ;
		            {
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_1_true_without_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_a_invalid_utf8.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_colon_instead_of_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_comma_after_close.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_comma_and_number.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_double_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_double_extra_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_extra_close.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_extra_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_incomplete.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_incomplete_invalid_value.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_inner_array_no_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_invalid_utf8.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_items_separated_by_semicolon.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_just_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_just_minus.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_missing_value.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_newlines_unclosed.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_number_and_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_number_and_several_commas.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_spaces_vertical_tab_formfeed.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_star_inside.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_unclosed.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_unclosed_trailing_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_unclosed_with_new_lines.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_array_unclosed_with_object_inside.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_incomplete_false.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_incomplete_null.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_incomplete_true.json",
		                //TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_multidigit_number_then_00.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_++.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_+1.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_+Inf.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_-01.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_-1.0..json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_-2..json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_-NaN.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_.-1.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_.2e-3.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_0.1.2.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_0.3e+.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_0.3e.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_0.e1.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_0_capital_E+.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_0_capital_E.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_0e+.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_0e.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_1.0e+.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_1.0e-.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_1.0e.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_1_000.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_1eE2.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_2.e+3.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_2.e-3.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_2.e3.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_9.e+.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_Inf.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_NaN.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_U+FF11_fullwidth_digit_one.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_expression.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_hex_1_digit.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_hex_2_digits.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_infinity.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_invalid+-.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_invalid-negative-real.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_invalid-utf-8-in-bigger-int.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_invalid-utf-8-in-exponent.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_invalid-utf-8-in-int.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_minus_infinity.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_minus_sign_with_trailing_garbage.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_minus_space_1.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_neg_int_starting_with_zero.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_neg_real_without_int_part.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_neg_with_garbage_at_end.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_real_garbage_after_e.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_real_with_invalid_utf8_after_e.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_real_without_fractional_part.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_starting_with_dot.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_with_alpha.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_with_alpha_char.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_number_with_leading_zero.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_bad_value.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_bracket_key.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_comma_instead_of_colon.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_double_colon.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_emoji.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_garbage_at_end.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_key_with_single_quotes.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_lone_continuation_byte_in_key_and_trailing_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_missing_colon.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_missing_key.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_missing_semicolon.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_missing_value.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_no-colon.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_non_string_key.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_non_string_key_but_huge_number_instead.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_repeated_null_null.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_several_trailing_commas.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_single_quote.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_trailing_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_trailing_comment.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_trailing_comment_open.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_trailing_comment_slash_open.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_trailing_comment_slash_open_incomplete.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_two_commas_in_a_row.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_unquoted_key.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_unterminated-value.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_with_single_string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_object_with_trailing_garbage.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_single_space.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape_u.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape_u1.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_1_surrogate_then_escape_u1x.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_accentuated_char_no_quotes.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_backslash_00.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_escape_x.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_escaped_backslash_bad.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_escaped_ctrl_char_tab.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_escaped_emoji.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_incomplete_escape.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_incomplete_escaped_character.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_incomplete_surrogate.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_incomplete_surrogate_escape_invalid.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_invalid-utf-8-in-escape.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_invalid_backslash_esc.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_invalid_unicode_escape.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_invalid_utf8_after_escape.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_leading_uescaped_thinspace.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_no_quotes_with_bad_escape.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_single_doublequote.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_single_quote.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_single_string_no_double_quotes.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_start_escape_unclosed.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_unescaped_crtl_char.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_unescaped_newline.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_unescaped_tab.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_unicode_CapitalU.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_string_with_trailing_garbage.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_U+2060_word_joined.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_UTF8_BOM_no_data.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_angle_bracket_..json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_angle_bracket_null.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_array_trailing_garbage.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_array_with_extra_array_close.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_array_with_unclosed_string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_ascii-unicode-identifier.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_capitalized_True.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_close_unopened_array.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_comma_instead_of_closing_brace.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_double_array.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_end_array.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_incomplete_UTF8_BOM.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_lone-invalid-utf-8.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_lone-open-bracket.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_no_data.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_null-byte-outside-string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_number_with_trailing_garbage.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_object_followed_by_closing_object.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_object_unclosed_no_value.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_object_with_comment.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_object_with_trailing_garbage.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_array_apostrophe.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_array_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_array_open_object.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_array_open_string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_array_string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_object.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_object_close_array.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_object_comma.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_object_open_array.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_object_open_string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_object_string_with_apostrophes.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_open_open.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_single_eacute.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_single_star.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_trailing_#.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_uescaped_LF_before_string.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_unclosed_array.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_unclosed_array_partial_null.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_unclosed_array_unfinished_false.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_unclosed_array_unfinished_true.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_unclosed_object.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_unicode-identifier.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_whitespace_U+2060_word_joiner.json",
		                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_whitespace_formfeed.json"
		            }
		        )
		    {
		        CAPTURE(filename)
		        std::ifstream f(filename);
		        json _;
		        CHECK_THROWS_AS(_ = json::parse(f), json::parse_error&);
		        std::ifstream f2(filename);
		        CHECK(!json::accept(f2));
		    }
		}
		
		```





**Fallacies;**

_None_


---

### NJF-11 

The service accepts leading and closing whitespaces.


**Supported Requests;**


**Supporting Items;**

_None_



**References;**

_None_



**Fallacies;**

_None_


---

### NJF-12 

The service decodes UTF-8 data.


**Supported Requests;**

- [WFJ-07](WFJ.md#wfj-07)

**Supporting Items;**

- [NJF-12.1](NJF.md#njf-12.1)
- [NJF-12.2](NJF.md#njf-12.2)
- [NJF-12.3](NJF.md#njf-12.3)
- [NJF-12.5](NJF.md#njf-12.5)
- [NJF-12.6](NJF.md#njf-12.6)



**References;**

_None_



**Fallacies;**

_None_


---

### NJF-12.1 

The service rejects malformed UTF-8 data.


**Supported Requests;**

- [NJF-12](NJF.md#njf-12)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [Markus Kuhn's UTF-8 decoder capability and stress test;3  Malformed sequences]
(/workspaces/json/tests/src/unit-unicode1.cpp)`


		```cpp
		SECTION("3  Malformed sequences")
		{
		    SECTION("3.1  Unexpected continuation bytes")
		    {
		        // Each unexpected continuation byte should be separately signalled as a
		        // malformed sequence of its own.
		
		        // 3.1.1  First continuation byte 0x80
		        roundtrip(false, "\x80");
		        // 3.1.2  Last  continuation byte 0xbf
		        roundtrip(false, "\xbf");
		
		        // 3.1.3  2 continuation bytes
		        roundtrip(false, "\x80\xbf");
		        // 3.1.4  3 continuation bytes
		        roundtrip(false, "\x80\xbf\x80");
		        // 3.1.5  4 continuation bytes
		        roundtrip(false, "\x80\xbf\x80\xbf");
		        // 3.1.6  5 continuation bytes
		        roundtrip(false, "\x80\xbf\x80\xbf\x80");
		        // 3.1.7  6 continuation bytes
		        roundtrip(false, "\x80\xbf\x80\xbf\x80\xbf");
		        // 3.1.8  7 continuation bytes
		        roundtrip(false, "\x80\xbf\x80\xbf\x80\xbf\x80");
		
		        // 3.1.9  Sequence of all 64 possible continuation bytes (0x80-0xbf)
		        roundtrip(false, "\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf");
		    }
		
		    SECTION("3.2  Lonely start characters")
		    {
		        // 3.2.1  All 32 first bytes of 2-byte sequences (0xc0-0xdf)
		        roundtrip(false, "\xc0 \xc1 \xc2 \xc3 \xc4 \xc5 \xc6 \xc7 \xc8 \xc9 \xca \xcb \xcc \xcd \xce \xcf \xd0 \xd1 \xd2 \xd3 \xd4 \xd5 \xd6 \xd7 \xd8 \xd9 \xda \xdb \xdc \xdd \xde \xdf");
		        // 3.2.2  All 16 first bytes of 3-byte sequences (0xe0-0xef)
		        roundtrip(false, "\xe0 \xe1 \xe2 \xe3 \xe4 \xe5 \xe6 \xe7 \xe8 \xe9 \xea \xeb \xec \xed \xee \xef");
		        // 3.2.3  All 8 first bytes of 4-byte sequences (0xf0-0xf7)
		        roundtrip(false, "\xf0 \xf1 \xf2 \xf3 \xf4 \xf5 \xf6 \xf7");
		        // 3.2.4  All 4 first bytes of 5-byte sequences (0xf8-0xfb)
		        roundtrip(false, "\xf8 \xf9 \xfa \xfb");
		        // 3.2.5  All 2 first bytes of 6-byte sequences (0xfc-0xfd)
		        roundtrip(false, "\xfc \xfd");
		    }
		
		    SECTION("3.3  Sequences with last continuation byte missing")
		    {
		        // All bytes of an incomplete sequence should be signalled as a single
		        // malformed sequence, i.e., you should see only a single replacement
		        // character in each of the next 10 tests. (Characters as in section 2)
		
		        // 3.3.1  2-byte sequence with last byte missing (U+0000)
		        roundtrip(false, "\xc0");
		        // 3.3.2  3-byte sequence with last byte missing (U+0000)
		        roundtrip(false, "\xe0\x80");
		        // 3.3.3  4-byte sequence with last byte missing (U+0000)
		        roundtrip(false, "\xf0\x80\x80");
		        // 3.3.4  5-byte sequence with last byte missing (U+0000)
		        roundtrip(false, "\xf8\x80\x80\x80");
		        // 3.3.5  6-byte sequence with last byte missing (U+0000)
		        roundtrip(false, "\xfc\x80\x80\x80\x80");
		        // 3.3.6  2-byte sequence with last byte missing (U-000007FF)
		        roundtrip(false, "\xdf");
		        // 3.3.7  3-byte sequence with last byte missing (U-0000FFFF)
		        roundtrip(false, "\xef\xbf");
		        // 3.3.8  4-byte sequence with last byte missing (U-001FFFFF)
		        roundtrip(false, "\xf7\xbf\xbf");
		        // 3.3.9  5-byte sequence with last byte missing (U-03FFFFFF)
		        roundtrip(false, "\xfb\xbf\xbf\xbf");
		        // 3.3.10 6-byte sequence with last byte missing (U-7FFFFFFF)
		        roundtrip(false, "\xfd\xbf\xbf\xbf\xbf");
		    }
		
		    SECTION("3.4  Concatenation of incomplete sequences")
		    {
		        // All the 10 sequences of 3.3 concatenated, you should see 10 malformed
		        // sequences being signalled;
		        roundtrip(false, "\xc0\xe0\x80\xf0\x80\x80\xf8\x80\x80\x80\xfc\x80\x80\x80\x80\xdf\xef\xbf\xf7\xbf\xbf\xfb\xbf\xbf\xbf\xfd\xbf\xbf\xbf\xbf");
		    }
		
		    SECTION("3.5  Impossible bytes")
		    {
		        // The following two bytes cannot appear in a correct UTF-8 string
		
		        // 3.5.1  fe
		        roundtrip(false, "\xfe");
		        // 3.5.2  ff
		        roundtrip(false, "\xff");
		        // 3.5.3  fe fe ff ff
		        roundtrip(false, "\xfe\xfe\xff\xff");
		    }
		}
		
		```





**Fallacies;**

_None_


---

### NJF-12.2 

The service rejects "overlong sequences".


**Supported Requests;**

- [NJF-12](NJF.md#njf-12)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [Markus Kuhn's UTF-8 decoder capability and stress test;4  Overlong sequences]
(/workspaces/json/tests/src/unit-unicode1.cpp)`


		```cpp
		SECTION("4  Overlong sequences")
		{
		    // The following sequences are not malformed according to the letter of
		    // the Unicode 2.0 standard. However, they are longer then necessary and
		    // a correct UTF-8 encoder is not allowed to produce them. A "safe UTF-8
		    // decoder" should reject them just like malformed sequences for two
		    // reasons; (1) It helps to debug applications if overlong sequences are
		    // not treated as valid representations of characters, because this helps
		    // to spot problems more quickly. (2) Overlong sequences provide
		    // alternative representations of characters, that could maliciously be
		    // used to bypass filters that check only for ASCII characters. For
		    // instance, a 2-byte encoded line feed (LF) would not be caught by a
		    // line counter that counts only 0x0a bytes, but it would still be
		    // processed as a line feed by an unsafe UTF-8 decoder later in the
		    // pipeline. From a security point of view, ASCII compatibility of UTF-8
		    // sequences means also, that ASCII characters are *only* allowed to be
		    // represented by ASCII bytes in the range 0x00-0x7f. To ensure this
		    // aspect of ASCII compatibility, use only "safe UTF-8 decoders" that
		    // reject overlong UTF-8 sequences for which a shorter encoding exists.
		
		    SECTION("4.1  Examples of an overlong ASCII character")
		    {
		        // With a safe UTF-8 decoder, all the following five overlong
		        // representations of the ASCII character slash ("/") should be rejected
		        // like a malformed UTF-8 sequence, for instance by substituting it with
		        // a replacement character. If you see a slash below, you do not have a
		        // safe UTF-8 decoder!
		
		        // 4.1.1 U+002F = c0 af
		        roundtrip(false, "\xc0\xaf");
		        // 4.1.2 U+002F = e0 80 af
		        roundtrip(false, "\xe0\x80\xaf");
		        // 4.1.3 U+002F = f0 80 80 af
		        roundtrip(false, "\xf0\x80\x80\xaf");
		        // 4.1.4 U+002F = f8 80 80 80 af
		        roundtrip(false, "\xf8\x80\x80\x80\xaf");
		        // 4.1.5 U+002F = fc 80 80 80 80 af
		        roundtrip(false, "\xfc\x80\x80\x80\x80\xaf");
		    }
		
		    SECTION("4.2  Maximum overlong sequences")
		    {
		        // Below you see the highest Unicode value that is still resulting in an
		        // overlong sequence if represented with the given number of bytes. This
		        // is a boundary test for safe UTF-8 decoders. All five characters should
		        // be rejected like malformed UTF-8 sequences.
		
		        // 4.2.1  U-0000007F = c1 bf
		        roundtrip(false, "\xc1\xbf");
		        // 4.2.2  U-000007FF = e0 9f bf
		        roundtrip(false, "\xe0\x9f\xbf");
		        // 4.2.3  U-0000FFFF = f0 8f bf bf
		        roundtrip(false, "\xf0\x8f\xbf\xbf");
		        // 4.2.4  U-001FFFFF = f8 87 bf bf bf
		        roundtrip(false, "\xf8\x87\xbf\xbf\xbf");
		        // 4.2.5  U-03FFFFFF = fc 83 bf bf bf bf
		        roundtrip(false, "\xfc\x83\xbf\xbf\xbf\xbf");
		    }
		
		    SECTION("4.3  Overlong representation of the NUL character")
		    {
		        // The following five sequences should also be rejected like malformed
		        // UTF-8 sequences and should not be treated like the ASCII NUL
		        // character.
		
		        // 4.3.1  U+0000 = c0 80
		        roundtrip(false, "\xc0\x80");
		        // 4.3.2  U+0000 = e0 80 80
		        roundtrip(false, "\xe0\x80\x80");
		        // 4.3.3  U+0000 = f0 80 80 80
		        roundtrip(false, "\xf0\x80\x80\x80");
		        // 4.3.4  U+0000 = f8 80 80 80 80
		        roundtrip(false, "\xf8\x80\x80\x80\x80");
		        // 4.3.5  U+0000 = fc 80 80 80 80 80
		        roundtrip(false, "\xfc\x80\x80\x80\x80\x80");
		    }
		}
		
		```





**Fallacies;**

_None_


---

### NJF-12.3 

The service rejects single and paired UTF-16 surrogates.


**Supported Requests;**

- [NJF-12](NJF.md#njf-12)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [Markus Kuhn's UTF-8 decoder capability and stress test;5  Illegal code positions]
(/workspaces/json/tests/src/unit-unicode1.cpp)`


		```cpp
		SECTION("5  Illegal code positions")
		{
		    // The following UTF-8 sequences should be rejected like malformed
		    // sequences, because they never represent valid ISO 10646 characters and
		    // a UTF-8 decoder that accepts them might introduce security problems
		    // comparable to overlong UTF-8 sequences.
		
		    SECTION("5.1 Single UTF-16 surrogates")
		    {
		        // 5.1.1  U+D800 = ed a0 80
		        roundtrip(false, "\xed\xa0\x80");
		        // 5.1.2  U+DB7F = ed ad bf
		        roundtrip(false, "\xed\xad\xbf");
		        // 5.1.3  U+DB80 = ed ae 80
		        roundtrip(false, "\xed\xae\x80");
		        // 5.1.4  U+DBFF = ed af bf
		        roundtrip(false, "\xed\xaf\xbf");
		        // 5.1.5  U+DC00 = ed b0 80
		        roundtrip(false, "\xed\xb0\x80");
		        // 5.1.6  U+DF80 = ed be 80
		        roundtrip(false, "\xed\xbe\x80");
		        // 5.1.7  U+DFFF = ed bf bf
		        roundtrip(false, "\xed\xbf\xbf");
		    }
		
		    SECTION("5.2 Paired UTF-16 surrogates")
		    {
		        // 5.2.1  U+D800 U+DC00 = ed a0 80 ed b0 80
		        roundtrip(false, "\xed\xa0\x80\xed\xb0\x80");
		        // 5.2.2  U+D800 U+DFFF = ed a0 80 ed bf bf
		        roundtrip(false, "\xed\xa0\x80\xed\xbf\xbf");
		        // 5.2.3  U+DB7F U+DC00 = ed ad bf ed b0 80
		        roundtrip(false, "\xed\xad\xbf\xed\xb0\x80");
		        // 5.2.4  U+DB7F U+DFFF = ed ad bf ed bf bf
		        roundtrip(false, "\xed\xad\xbf\xed\xbf\xbf");
		        // 5.2.5  U+DB80 U+DC00 = ed ae 80 ed b0 80
		        roundtrip(false, "\xed\xae\x80\xed\xb0\x80");
		        // 5.2.6  U+DB80 U+DFFF = ed ae 80 ed bf bf
		        roundtrip(false, "\xed\xae\x80\xed\xbf\xbf");
		        // 5.2.7  U+DBFF U+DC00 = ed af bf ed b0 80
		        roundtrip(false, "\xed\xaf\xbf\xed\xb0\x80");
		        // 5.2.8  U+DBFF U+DFFF = ed af bf ed bf bf
		        roundtrip(false, "\xed\xaf\xbf\xed\xbf\xbf");
		    }
		
		    SECTION("5.3 Noncharacter code positions")
		    {
		        // The following "noncharacters" are "reserved for internal use" by
		        // applications, and according to older versions of the Unicode Standard
		        // "should never be interchanged". Unicode Corrigendum #9 dropped the
		        // latter restriction. Nevertheless, their presence in incoming UTF-8 data
		        // can remain a potential security risk, depending on what use is made of
		        // these codes subsequently. Examples of such internal use;
		        //
		        //  - Some file APIs with 16-bit characters may use the integer value -1
		        //    = U+FFFF to signal an end-of-file (EOF) or error condition.
		        //
		        //  - In some UTF-16 receivers, code point U+FFFE might trigger a
		        //    byte-swap operation (to convert between UTF-16LE and UTF-16BE).
		        //
		        // With such internal use of noncharacters, it may be desirable and safer
		        // to block those code points in UTF-8 decoders, as they should never
		        // occur legitimately in incoming UTF-8 data, and could trigger unsafe
		        // behaviour in subsequent processing.
		
		        // Particularly problematic noncharacters in 16-bit applications;
		
		        // 5.3.1  U+FFFE = ef bf be
		        roundtrip(true, "\xef\xbf\xbe");
		        // 5.3.2  U+FFFF = ef bf bf
		        roundtrip(true, "\xef\xbf\xbf");
		
		        // 5.3.3  U+FDD0 .. U+FDEF
		        roundtrip(true, "\xEF\xB7\x90");
		        roundtrip(true, "\xEF\xB7\x91");
		        roundtrip(true, "\xEF\xB7\x92");
		        roundtrip(true, "\xEF\xB7\x93");
		        roundtrip(true, "\xEF\xB7\x94");
		        roundtrip(true, "\xEF\xB7\x95");
		        roundtrip(true, "\xEF\xB7\x96");
		        roundtrip(true, "\xEF\xB7\x97");
		        roundtrip(true, "\xEF\xB7\x98");
		        roundtrip(true, "\xEF\xB7\x99");
		        roundtrip(true, "\xEF\xB7\x9A");
		        roundtrip(true, "\xEF\xB7\x9B");
		        roundtrip(true, "\xEF\xB7\x9C");
		        roundtrip(true, "\xEF\xB7\x9D");
		        roundtrip(true, "\xEF\xB7\x9E");
		        roundtrip(true, "\xEF\xB7\x9F");
		        roundtrip(true, "\xEF\xB7\xA0");
		        roundtrip(true, "\xEF\xB7\xA1");
		        roundtrip(true, "\xEF\xB7\xA2");
		        roundtrip(true, "\xEF\xB7\xA3");
		        roundtrip(true, "\xEF\xB7\xA4");
		        roundtrip(true, "\xEF\xB7\xA5");
		        roundtrip(true, "\xEF\xB7\xA6");
		        roundtrip(true, "\xEF\xB7\xA7");
		        roundtrip(true, "\xEF\xB7\xA8");
		        roundtrip(true, "\xEF\xB7\xA9");
		        roundtrip(true, "\xEF\xB7\xAA");
		        roundtrip(true, "\xEF\xB7\xAB");
		        roundtrip(true, "\xEF\xB7\xAC");
		        roundtrip(true, "\xEF\xB7\xAD");
		        roundtrip(true, "\xEF\xB7\xAE");
		        roundtrip(true, "\xEF\xB7\xAF");
		
		        // 5.3.4  U+nFFFE U+nFFFF (for n = 1..10)
		        roundtrip(true, "\xF0\x9F\xBF\xBF");
		        roundtrip(true, "\xF0\xAF\xBF\xBF");
		        roundtrip(true, "\xF0\xBF\xBF\xBF");
		        roundtrip(true, "\xF1\x8F\xBF\xBF");
		        roundtrip(true, "\xF1\x9F\xBF\xBF");
		        roundtrip(true, "\xF1\xAF\xBF\xBF");
		        roundtrip(true, "\xF1\xBF\xBF\xBF");
		        roundtrip(true, "\xF2\x8F\xBF\xBF");
		        roundtrip(true, "\xF2\x9F\xBF\xBF");
		        roundtrip(true, "\xF2\xAF\xBF\xBF");
		    }
		}
		
		```


- `cpp-testsuite; [/nst_json_testsuite2/test_parsing/n_structure_incomplete_UTF8_BOM.json, /nst_json_testsuite2/test_parsing/n_structure_lone-invalid-utf-8.json]`


			- Description; 
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_structure_incomplete_UTF8_BOM.json
			
			
			 ```json
			믯絻
			```
			
			
			
			
			- JSON Testsuite; /nst_json_testsuite2/test_parsing/n_structure_lone-invalid-utf-8.json
			
			
			 ```json
			V
			```
			
			
			- cpp-test; [nst's JSONTestSuite (2);test_parsing;n]
			(/workspaces/json/tests/src/unit-testsuites.cpp)
			
			
			```cpp
			SECTION("n")
			{
			    for (const auto* filename ;
			            {
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_incomplete_UTF8_BOM.json",
			                TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/n_structure_lone-invalid-utf-8.json",
			            }
			        )
			    {
			        CAPTURE(filename)
			        std::ifstream f(filename);
			        json _;
			        CHECK_THROWS_AS(_ = json::parse(f), json::parse_error&);
			        std::ifstream f2(filename);
			        CHECK(!json::accept(f2));
			    }
			}
			
			
			 // Note; Other test data lines have been filtered out for conciseness.
			```
			




**Fallacies;**

_None_


---

### NJF-12.5 

The service accepts Non-Characters


**Supported Requests;**

- [NJF-12](NJF.md#njf-12)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [Markus Kuhn's UTF-8 decoder capability and stress test;5.3 Noncharacter code positions]
(/workspaces/json/tests/src/unit-unicode1.cpp)`


		```cpp
		SECTION("5.3 Noncharacter code positions")
		{
		    // The following "noncharacters" are "reserved for internal use" by
		    // applications, and according to older versions of the Unicode Standard
		    // "should never be interchanged". Unicode Corrigendum #9 dropped the
		    // latter restriction. Nevertheless, their presence in incoming UTF-8 data
		    // can remain a potential security risk, depending on what use is made of
		    // these codes subsequently. Examples of such internal use;
		    //
		    //  - Some file APIs with 16-bit characters may use the integer value -1
		    //    = U+FFFF to signal an end-of-file (EOF) or error condition.
		    //
		    //  - In some UTF-16 receivers, code point U+FFFE might trigger a
		    //    byte-swap operation (to convert between UTF-16LE and UTF-16BE).
		    //
		    // With such internal use of noncharacters, it may be desirable and safer
		    // to block those code points in UTF-8 decoders, as they should never
		    // occur legitimately in incoming UTF-8 data, and could trigger unsafe
		    // behaviour in subsequent processing.
		
		    // Particularly problematic noncharacters in 16-bit applications;
		
		    // 5.3.1  U+FFFE = ef bf be
		    roundtrip(true, "\xef\xbf\xbe");
		    // 5.3.2  U+FFFF = ef bf bf
		    roundtrip(true, "\xef\xbf\xbf");
		
		    // 5.3.3  U+FDD0 .. U+FDEF
		    roundtrip(true, "\xEF\xB7\x90");
		    roundtrip(true, "\xEF\xB7\x91");
		    roundtrip(true, "\xEF\xB7\x92");
		    roundtrip(true, "\xEF\xB7\x93");
		    roundtrip(true, "\xEF\xB7\x94");
		    roundtrip(true, "\xEF\xB7\x95");
		    roundtrip(true, "\xEF\xB7\x96");
		    roundtrip(true, "\xEF\xB7\x97");
		    roundtrip(true, "\xEF\xB7\x98");
		    roundtrip(true, "\xEF\xB7\x99");
		    roundtrip(true, "\xEF\xB7\x9A");
		    roundtrip(true, "\xEF\xB7\x9B");
		    roundtrip(true, "\xEF\xB7\x9C");
		    roundtrip(true, "\xEF\xB7\x9D");
		    roundtrip(true, "\xEF\xB7\x9E");
		    roundtrip(true, "\xEF\xB7\x9F");
		    roundtrip(true, "\xEF\xB7\xA0");
		    roundtrip(true, "\xEF\xB7\xA1");
		    roundtrip(true, "\xEF\xB7\xA2");
		    roundtrip(true, "\xEF\xB7\xA3");
		    roundtrip(true, "\xEF\xB7\xA4");
		    roundtrip(true, "\xEF\xB7\xA5");
		    roundtrip(true, "\xEF\xB7\xA6");
		    roundtrip(true, "\xEF\xB7\xA7");
		    roundtrip(true, "\xEF\xB7\xA8");
		    roundtrip(true, "\xEF\xB7\xA9");
		    roundtrip(true, "\xEF\xB7\xAA");
		    roundtrip(true, "\xEF\xB7\xAB");
		    roundtrip(true, "\xEF\xB7\xAC");
		    roundtrip(true, "\xEF\xB7\xAD");
		    roundtrip(true, "\xEF\xB7\xAE");
		    roundtrip(true, "\xEF\xB7\xAF");
		
		    // 5.3.4  U+nFFFE U+nFFFF (for n = 1..10)
		    roundtrip(true, "\xF0\x9F\xBF\xBF");
		    roundtrip(true, "\xF0\xAF\xBF\xBF");
		    roundtrip(true, "\xF0\xBF\xBF\xBF");
		    roundtrip(true, "\xF1\x8F\xBF\xBF");
		    roundtrip(true, "\xF1\x9F\xBF\xBF");
		    roundtrip(true, "\xF1\xAF\xBF\xBF");
		    roundtrip(true, "\xF1\xBF\xBF\xBF");
		    roundtrip(true, "\xF2\x8F\xBF\xBF");
		    roundtrip(true, "\xF2\x9F\xBF\xBF");
		    roundtrip(true, "\xF2\xAF\xBF\xBF");
		}
		
		```





**Fallacies;**

_None_


---

### NJF-12.6 

The service accepts well-formed UTF-8 data.


**Supported Requests;**

- [NJF-12](NJF.md#njf-12)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [Markus Kuhn's UTF-8 decoder capability and stress test;2  Boundary condition test cases]
(/workspaces/json/tests/src/unit-unicode1.cpp)`


		```cpp
		SECTION("2  Boundary condition test cases")
		{
		    SECTION("2.1  First possible sequence of a certain length")
		    {
		        // 2.1.1  1 byte  (U-00000000)
		        roundtrip(true, std::string("\0", 1));
		        // 2.1.2  2 bytes (U-00000080)
		        roundtrip(true, "\xc2\x80");
		        // 2.1.3  3 bytes (U-00000800)
		        roundtrip(true, "\xe0\xa0\x80");
		        // 2.1.4  4 bytes (U-00010000)
		        roundtrip(true, "\xf0\x90\x80\x80");
		
		        // 2.1.5  5 bytes (U-00200000)
		        roundtrip(false, "\xF8\x88\x80\x80\x80");
		        // 2.1.6  6 bytes (U-04000000)
		        roundtrip(false, "\xFC\x84\x80\x80\x80\x80");
		    }
		
		    SECTION("2.2  Last possible sequence of a certain length")
		    {
		        // 2.2.1  1 byte  (U-0000007F)
		        roundtrip(true, "\x7f");
		        // 2.2.2  2 bytes (U-000007FF)
		        roundtrip(true, "\xdf\xbf");
		        // 2.2.3  3 bytes (U-0000FFFF)
		        roundtrip(true, "\xef\xbf\xbf");
		
		        // 2.2.4  4 bytes (U-001FFFFF)
		        roundtrip(false, "\xF7\xBF\xBF\xBF");
		        // 2.2.5  5 bytes (U-03FFFFFF)
		        roundtrip(false, "\xFB\xBF\xBF\xBF\xBF");
		        // 2.2.6  6 bytes (U-7FFFFFFF)
		        roundtrip(false, "\xFD\xBF\xBF\xBF\xBF\xBF");
		    }
		
		    SECTION("2.3  Other boundary conditions")
		    {
		        // 2.3.1  U-0000D7FF = ed 9f bf
		        roundtrip(true, "\xed\x9f\xbf");
		        // 2.3.2  U-0000E000 = ee 80 80
		        roundtrip(true, "\xee\x80\x80");
		        // 2.3.3  U-0000FFFD = ef bf bd
		        roundtrip(true, "\xef\xbf\xbd");
		        // 2.3.4  U-0010FFFF = f4 8f bf bf
		        roundtrip(true, "\xf4\x8f\xbf\xbf");
		
		        // 2.3.5  U-00110000 = f4 90 80 80
		        roundtrip(false, "\xf4\x90\x80\x80");
		    }
		}
		
		```





**Fallacies;**

_None_


---

### NJF-13 

The service accepts JSON data consisting of combinations of the data types.


**Supported Requests;**

- [WFJ-05](WFJ.md#wfj-05)

**Supporting Items;**

_None_



**References;**

- `cpp-test; [compliance tests from json.org;expected passes]
(/workspaces/json/tests/src/unit-testsuites.cpp)`


		```cpp
		SECTION("expected passes")
		{
		    for (const auto* filename ;
		            {
		                TEST_DATA_DIRECTORY "/json_tests/pass1.json",
		                TEST_DATA_DIRECTORY "/json_tests/pass2.json",
		                TEST_DATA_DIRECTORY "/json_tests/pass3.json"
		            })
		    {
		        CAPTURE(filename)
		        std::ifstream f(filename);
		        json j;
		        CHECK_NOTHROW(f &gt;&gt; j);
		    }
		}
		
		```





**Fallacies;**

_None_

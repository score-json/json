
#include "doctest_compatibility.h"

#include <nlohmann/json.hpp>
using nlohmann::json;

TEST_CASE("accept")
{
    SECTION("exponents")
    {
        // The only valid exponents are U+0065 and U+0045.
        // Their look-alikes, in particular U+0425 and U+0436 are forbidden.
        SECTION("U+0425")
        {            
            CHECK(!json::accept("0\u0425123"));
            CHECK(!json::accept("123\u04250"));
            CHECK(!json::accept("0.123\u0425123"));
            CHECK(!json::accept("1.23\u0425123"));
            CHECK(!json::accept("1.23\u04250"));
        }
        SECTION("U+0436")
        {            
            CHECK(!json::accept("0\u0436123"));
            CHECK(!json::accept("123\u04360"));
            CHECK(!json::accept("0.123\u0436123"));
            CHECK(!json::accept("1.23\u0436123"));
            CHECK(!json::accept("1.23\u04360"));
        }
        // Leading zeroes for exponents are allowed.
        SECTION("leading zeroes")
        {
            CHECK(json::accept("42\u004507"));
            CHECK(json::accept("42\u004500000000000007"));
            CHECK(json::accept("42\u00450000000000"));
            CHECK(json::accept("42\u006507"));
            CHECK(json::accept("42\u006500000000000007"));
            CHECK(json::accept("42\u00650000000000"));
        }
    }
    // The only valid operators are plus and minus at the beginning of a number.
    // All other operators, i.e. brackets, *, /, +, -, !, comma are illegal.
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
    // Leading and tailing whitespace are ignored; whitespace in between a number is illegal.
    // see also nst_json_testsuite2/test_parsing/n_number_1_000.json for a single test of this
    // circumstance.
    SECTION("whitespace")
    {
        SECTION("space")
        {
            CHECK(!json::accept("0 1"));
            CHECK(!json::accept("1234 567"));
            CHECK(!json::accept("123.456 789"));
            CHECK(!json::accept("123\u00450 0"));
            CHECK(!json::accept("123\u0045132 94"));
            CHECK(!json::accept("1.23\u00450 0"));
            CHECK(!json::accept("1.23\u0045132 94"));
            CHECK(!json::accept("123\u00650 0"));
            CHECK(!json::accept("123\u0065132 94"));
            CHECK(!json::accept("1.23\u00650 0"));
            CHECK(!json::accept("1.23\u0065132 94"));
        }
        SECTION("tab")
        {
            CHECK(!json::accept("0\t1"));
            CHECK(!json::accept("1234\t567"));
            CHECK(!json::accept("123.456\t789"));
            CHECK(!json::accept("123\u00450\t0"));
            CHECK(!json::accept("123\u0045132\t94"));
            CHECK(!json::accept("1.23\u00450\t0"));
            CHECK(!json::accept("1.23\u0045132\t94"));
            CHECK(!json::accept("123\u00650\t0"));
            CHECK(!json::accept("123\u0065132\t94"));
            CHECK(!json::accept("1.23\u00650\t0"));
            CHECK(!json::accept("1.23\u0065132\t94"));
        }
        SECTION("new line")
        {
            CHECK(!json::accept("0\n1"));
            CHECK(!json::accept("1234\n567"));
            CHECK(!json::accept("123.456\n789"));
            CHECK(!json::accept("123\u00450\n0"));
            CHECK(!json::accept("123\u0045132\n94"));
            CHECK(!json::accept("1.23\u00450\n0"));
            CHECK(!json::accept("1.23\u0045132\n94"));
            CHECK(!json::accept("123\u00650\n0"));
            CHECK(!json::accept("123\u0065132\n94"));
            CHECK(!json::accept("1.23\u00650\n0"));
            CHECK(!json::accept("1.23\u0065132\n94"));
        }
        SECTION("Carriage return")
        {
            CHECK(!json::accept("0\u000d1"));
            CHECK(!json::accept("1234\u000d567"));
            CHECK(!json::accept("123.456\u000d789"));
            CHECK(!json::accept("123\u00450\u000d0"));
            CHECK(!json::accept("123\u0045132\u000d94"));
            CHECK(!json::accept("1.23\u00450\u000d0"));
            CHECK(!json::accept("1.23\u0045132\u000d94"));
            CHECK(!json::accept("123\u00650\u000d0"));
            CHECK(!json::accept("123\u0065132\u000d94"));
            CHECK(!json::accept("1.23\u00650\u000d0"));
            CHECK(!json::accept("1.23\u0065132\u000d94"));
        }
        // See also nst_json_testsuite2/test_parsing/y_number_after_space.json
        SECTION("Leading and tailing")
        {
            SECTION("space")
            {
                CHECK(json::accept(" 123"));
                CHECK(json::accept(" 123.23672"));
                CHECK(json::accept(" 12\u004523"));
                CHECK(json::accept(" 92\u006532"));
                CHECK(json::accept("              123"));
                CHECK(json::accept("            123.23672"));
                CHECK(json::accept("     12\u004523"));
                CHECK(json::accept("           92\u006532"));
                CHECK(json::accept("123 "));
                CHECK(json::accept("123.23672 "));
                CHECK(json::accept("12\u004523 "));
                CHECK(json::accept("92\u006532 "));
                CHECK(json::accept("123                 "));
                CHECK(json::accept("123.23672               "));
                CHECK(json::accept("12\u004523                "));
                CHECK(json::accept("92\u006532              "));
            }
            SECTION("tab")
            {
                CHECK(json::accept("\t123"));
                CHECK(json::accept("\t123.23672"));
                CHECK(json::accept("\t12\u004523"));
                CHECK(json::accept("\t92\u006532"));
                CHECK(json::accept("123\t"));
                CHECK(json::accept("123.23672\t"));
                CHECK(json::accept("12\u004523\t"));
                CHECK(json::accept("92\u006532\t"));
                CHECK(json::accept("\t\t\t\t\t\t\t123"));
                CHECK(json::accept("\t\t\t\t\t\t\t\t123.23672"));
                CHECK(json::accept("\t\t\t\t\t\t\t\t\t12\u004523"));
                CHECK(json::accept("\t\t\t\t\t\t92\u006532"));
                CHECK(json::accept("123\t\t\t\t\t\t"));
                CHECK(json::accept("123.23672\t\t\t\t\t"));
                CHECK(json::accept("12\u004523\t\t\t\t"));
                CHECK(json::accept("92\u006532\t\t\t\t\t\t"));
            }
            SECTION("newline")
            {
                CHECK(json::accept("\n123"));
                CHECK(json::accept("\n123.23672"));
                CHECK(json::accept("\n12\u004523"));
                CHECK(json::accept("\n92\u006532"));
                CHECK(json::accept("123\n"));
                CHECK(json::accept("123.23672\n"));
                CHECK(json::accept("12\u004523\n"));
                CHECK(json::accept("92\u006532\n"));
                CHECK(json::accept("\n\n\n\n\n\n\n123"));
                CHECK(json::accept("\n\n\n\n\n\n\n\n123.23672"));
                CHECK(json::accept("\n\n\n\n\n\n\n\n12\u004523"));
                CHECK(json::accept("\n\n\n\n\n\n92\u006532"));
                CHECK(json::accept("123\n\n\n\n\n\n"));
                CHECK(json::accept("123.23672\n\n\n\n\n"));
                CHECK(json::accept("12\u004523\n\n\n\n"));
                CHECK(json::accept("92\u006532\n\n\n\n\n\n"));
            }
            SECTION("Carriage return")
            {
                CHECK(json::accept("\u000d123"));
                CHECK(json::accept("\u000d123.23672"));
                CHECK(json::accept("\u000d12\u004523"));
                CHECK(json::accept("\u000d92\u006532"));
                CHECK(json::accept("123\u000d"));
                CHECK(json::accept("123.23672\u000d"));
                CHECK(json::accept("12\u004523\u000d"));
                CHECK(json::accept("92\u006532\u000d"));
                CHECK(json::accept("\u000d\u000d\u000d\u000d\u000d\u000d\u000d123"));
                CHECK(json::accept("\u000d\u000d\u000d\u000d\u000d\u000d\u000d\u000d123.23672"));
                CHECK(json::accept("\u000d\u000d\u000d\u000d\u000d\u000d\u000d\u000d\u000d12\u004523"));
                CHECK(json::accept("\u000d\u000d\u000d\u000d\u000d\u000d92\u006532"));
                CHECK(json::accept("123\u000d\u000d\u000d\u000d\u000d\u000d"));
                CHECK(json::accept("123.23672\u000d\u000d\u000d\u000d\u000d"));
                CHECK(json::accept("12\u004523\u000d\u000d\u000d\u000d"));
                CHECK(json::accept("92\u006532\u000d\u000d\u000d\u000d\u000d\u000d"));
            }
            SECTION("Mixed")
            {
                CHECK(json::accept("\u000d\t\n  \t\n \u000d\u000d\t\t124234   \n\n\n\n\u000d\u000d\t\t"));
                CHECK(json::accept("\u000d\t\n  \t\n \u000d\u000d\t\t1242.34   \n\n\n\n\u000d\u000d\t\t"));
                CHECK(json::accept("\u000d\t\n  \t\n \u000d\u000d\t\t1242\u004534   \n\n\n\n\u000d\u000d\t\t"));
                CHECK(json::accept("\u000d\t\n  \t\n \u000d\u000d\t\t1242\u006534   \n\n\n\n\u000d\u000d\t\t"));
            }
        }
    }
    // Recall that unit-class_parser.cpp parser class:accept:number:invalid numbers checks 01;
    // nst_json_testsuite2/test_parsing/n_number_-01.json checks -01.
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
    // According to RFC8259, only numbers in base ten are allowed. For bases lower than ten, this can
    // not be checked using the numerical representation and checking the grammar, assuming that the 
    // standard digits are used; instead, this is the job of the parser.
    // For bases exceeding ten, this can be checked. In particular hexadecimal can be tested for.
    // For base eight, this can also be tested assuming that one of the conventions for the
    // representation is used.
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
}

TEST_CASE("parse")
{
    // While leading zeroes are forbidden according to RFC8259, 
    // leading zeroes in the exponent are allowed and ignored in the parsing.
    SECTION("exponents")
    {
        SECTION("leading zeroes")
        {
            CHECK(json::parse("1\u00451")==json::parse("1\u004501"));
            CHECK(json::parse("0.1\u00451")==json::parse("0.1\u004501"));
            CHECK(json::parse("1\u004545")==json::parse("1\u004500000000000000000000000045"));
            CHECK(json::parse("12415\u004516")==json::parse("12415\u00450016"));
            CHECK(json::parse("12.415\u004516")==json::parse("12.415\u00450016"));
            CHECK(json::parse("1\u00651")==json::parse("1\u006501"));
            CHECK(json::parse("0.1\u00651")==json::parse("0.1\u006501"));
            CHECK(json::parse("1\u006545")==json::parse("1\u006500000000000000000000000045"));
            CHECK(json::parse("12415\u006516")==json::parse("12415\u00650016"));
            CHECK(json::parse("12.415\u006516")==json::parse("12.415\u00650016"));
        }
        SECTION("leading plus")
        {
            CHECK(json::parse("1\u0045+1")==json::parse("1\u00451"));
            CHECK(json::parse("1\u0065+1")==json::parse("1\u00651"));
            CHECK(json::parse("1.0034\u0045+23")==json::parse("1.0034\u004523"));
            CHECK(json::parse("1.0034\u0065+23")==json::parse("1.0034\u006523"));
        }
        SECTION("Capitalisation")
        {
            CHECK(json::parse("3.1415\u00454")==json::parse("3.1415\u00654"));
        }
    }
    SECTION("trailing zeroes")
    {   
        // Trailing zeroes after the decimal point do not influence the parsing
        CHECK(json::parse("3.1415000000000000000000000")==json::parse("3.1415"));
        CHECK(json::parse("3.1415000000000\u004515")==json::parse("3.1415\u004515"));
        CHECK(json::parse("3.1415926000000000\u006515")==json::parse("3.1415926\u006515"));
        // This also works for numbers that are not parsed correctly anyway
        CHECK(json::parse("2.2250738585072011360574097967091319759348195463516456400000000e-308")==json::parse("2.22507385850720113605740979670913197593481954635164564e-308"));
        CHECK(json::parse("0.999999999999999944488848768742172978818416595458984374")==json::parse("0.999999999999999944488848768742172978818416595458984374000000"));
    }
    SECTION("Whitespace")
    {
        // Leading and trailing whitespace is ignored.
        CHECK(json::parse("\n\n\t 123\n\t\t  \u000d")==json::parse("123"));
        CHECK(json::parse(" 123 ")==json::parse("123"));
        CHECK(json::parse(" 123\t")==json::parse("123"));
        CHECK(json::parse(" 123\n")==json::parse("123"));
        CHECK(json::parse(" 123\u000d")==json::parse("123"));
        CHECK(json::parse("\t123 ")==json::parse("123"));
        CHECK(json::parse("\t123\t")==json::parse("123"));
        CHECK(json::parse("\t123\n")==json::parse("123"));
        CHECK(json::parse("\t123\u000d")==json::parse("123"));
        CHECK(json::parse("\n123 ")==json::parse("123"));
        CHECK(json::parse("\n123\t")==json::parse("123"));
        CHECK(json::parse("\n123\n")==json::parse("123"));
        CHECK(json::parse("\n123\u000d")==json::parse("123"));
        CHECK(json::parse("\u000d123 ")==json::parse("123"));
        CHECK(json::parse("\u000d123\t")==json::parse("123"));
        CHECK(json::parse("\u000d123\n")==json::parse("123"));
        CHECK(json::parse("\u000d123\u000d")==json::parse("123"));
    }
}
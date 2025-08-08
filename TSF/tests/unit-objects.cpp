#include <fstream>
#include "doctest_compatibility.h"

#include <nlohmann/json.hpp>
using nlohmann::json;

namespace
{
void parser_helper(const std::string& input);

void parser_helper(const std::string& input){
    const json temp = json::parse(input);
}
} //namespace

TEST_CASE("accept")
{
    // A name (or key) is a string. No other token is a valid name
    // See also n_object_missing_key.json, n_object_non_string_key.json, 
    // n_object_non_string_key_but_huge_number_instead.json, n_object_repeated_null_null
    // n_object_unquoted_key for some non-exhaustive tests
    SECTION("names")
    {
        SECTION("numbers")
        {
            // cf. n_object_non_string_key.json, n_object_non_string_key_but_huge_number_instead.json, for some integers
            CHECK(!json::accept("{0.1:\"foo\"}"));
            CHECK(!json::accept("{3\u004542:\"foo\"}"));
            CHECK(!json::accept("{3.1415\u006542:\"foo\"}"));
            CHECK(!json::accept("{-15:\"foo\"}"));
        }
        SECTION("arrays")
        {
            CHECK(!json::accept("{[]:\"foo\"}"));
            CHECK(!json::accept("{[1]:\"foo\"}"));
            CHECK(!json::accept("{[1,\"foo\"]:\"bar\"}"));
        }
        SECTION("objects")
        {
            CHECK(!json::accept("{{}:\"foo\"}"));
            CHECK(!json::accept("{{\"a\":1}:\"foo\"}"));
            CHECK(!json::accept("{{\"a\":1,\"b\":\"foo\"}:\"bar\"}"));
        }
        SECTION("literals")
        {
            CHECK(!json::accept("true:\"foo\""));
            CHECK(!json::accept("false:\"foo\""));
            CHECK(!json::accept("null:\"foo\""));
        }
        // Various valid strings are tests for in unit-testsuites.cpp
        // However, these do not include unicode utf-8 and utf-16 surrogate characters,
        // or control characters.
        SECTION("strings")
        {
            SECTION("control characters")
            {
                CHECK(json::accept("{\"foo\\u0000bar\":123}"));
                CHECK(json::accept("{\"foo\\u0001bar\":123}"));
                CHECK(json::accept("{\"foo\\u0002bar\":123}"));
                CHECK(json::accept("{\"foo\\u0003bar\":123}"));
                CHECK(json::accept("{\"foo\\u0004bar\":123}"));
                CHECK(json::accept("{\"foo\\u0005bar\":123}"));
                CHECK(json::accept("{\"foo\\u0006bar\":123}"));
                CHECK(json::accept("{\"foo\\u0007bar\":123}"));
                CHECK(json::accept("{\"foo\\u0008bar\":123}"));
                CHECK(json::accept("{\"foo\\u0009bar\":123}"));
                CHECK(json::accept("{\"foo\\u000abar\":123}"));
                CHECK(json::accept("{\"foo\\u000bbar\":123}"));
                CHECK(json::accept("{\"foo\\u000cbar\":123}"));
                CHECK(json::accept("{\"foo\\u000dbar\":123}"));
                CHECK(json::accept("{\"foo\\u000ebar\":123}"));
                CHECK(json::accept("{\"foo\\u000fbar\":123}"));
                CHECK(json::accept("{\"foo\\u0010bar\":123}"));
                CHECK(json::accept("{\"foo\\u0011bar\":123}"));
                CHECK(json::accept("{\"foo\\u0012bar\":123}"));
                CHECK(json::accept("{\"foo\\u0013bar\":123}"));
                CHECK(json::accept("{\"foo\\u0014bar\":123}"));
                CHECK(json::accept("{\"foo\\u0015bar\":123}"));
                CHECK(json::accept("{\"foo\\u0016bar\":123}"));
                CHECK(json::accept("{\"foo\\u0017bar\":123}"));
                CHECK(json::accept("{\"foo\\u0018bar\":123}"));
                CHECK(json::accept("{\"foo\\u0019bar\":123}"));
                CHECK(json::accept("{\"foo\\u001abar\":123}"));
                CHECK(json::accept("{\"foo\\u001bbar\":123}"));
                CHECK(json::accept("{\"foo\\u001cbar\":123}"));
                CHECK(json::accept("{\"foo\\u001dbar\":123}"));
                CHECK(json::accept("{\"foo\\u001ebar\":123}"));
                CHECK(json::accept("{\"foo\\u001fbar\":123}"));
            }
            SECTION("unicode")
            {  
                // escaped
                CHECK(json::accept("{\"\\u0066\\u006f\\u006f\\u0062\\u0061\\u0072\":123}"));
                // unescaped
                CHECK(json::accept("{\"\u0066\u006f\u006f\u0062\u0061\u0072\":123}"));
            }
            SECTION("escaped UTF-16 surrogates")
            {
                CHECK(json::accept("{\"\\ud834\\udd1e\":123}"));
                CHECK(json::accept("{\"\\ud83d\\ude00\":123}"));
                CHECK(json::accept("{\"\\ud83d\\udca9\":123}"));
                CHECK(json::accept("{\"\\ud83e\\udda5\":123}"));
                CHECK(json::accept("{\"\\ud83d\\ude80\":123}"));
                CHECK(json::accept("{\"\\ud840\\udc00\":123}"));
                CHECK(json::accept("{\"\\udbff\\udfff\":123}"));
                CHECK(json::accept("{\"\\ud83c\\udfc3\":123}"));
                CHECK(json::accept("{\"\\ud801\\udc37\":123}"));
                CHECK(json::accept("{\"\\ud83d\\udcbb\":123}"));
            }
        }
    }
    // Name/key and value of an array are treated as any other token. 
    // In particular, leading and trailing whitespace are ignored
    SECTION("whitespace")
    {
        SECTION("empty object")
        {
            CHECK(json::accept("{          }"));
            CHECK(json::accept("{\t}"));
            CHECK(json::accept("{\n}"));
            CHECK(json::accept("{\u000d}"));
            CHECK(json::accept("{\u000d\u000d\u000d  \t\t\t\n\n   \u000d \n\t  \t \u000d}"));
        }
        SECTION("non-empty object")
        {
            CHECK(json::accept("{ \"foo\" : \"bar\" }"));
            CHECK(json::accept("{\t\"foo\"\t:\t\"bar\"\t}"));
            CHECK(json::accept("{\n\"foo\"\n:\n\"bar\"\n}"));
            CHECK(json::accept("{\u000d\"foo\"\u000d:\u000d\"bar\"\u000d}"));
            CHECK(json::accept("{ \"foo\"\t:\n\"bar\"\n}"));
            CHECK(json::accept("{\t\t\t\t\t\n\n\u000d\"foo\"\t \t\t  \n\n  \u000d:\"bar\"}"));
        }   
    }
    // The colon U+003A is the only valid member separator.
    // Look-alikes are illegal.
    // All other valid structural characters are illegal.
    SECTION("member separator")
    {
        CHECK(json::accept("{\"foo\"\u003a\"bar\"}"));      //:
        CHECK(!json::accept("{\"foo\"\uff1a\"bar\"}"));     
        CHECK(!json::accept("{\"foo\"\ua789\"bar\"}"));
        CHECK(!json::accept("{\"foo\"\u005b\"bar\"}"));     //[
        CHECK(!json::accept("{\"foo\"\u007b\"bar\"}"));     //{
        CHECK(!json::accept("{\"foo\"\u005d\"bar\"}"));     //]
        CHECK(!json::accept("{\"foo\"\u007d\"bar\"}"));     //}
        CHECK(!json::accept("{\"foo\"\u002c\"bar\"}"));     //,
        CHECK(!json::accept("{\"foo\"\u003b\"bar\"}"));     //;
    }
}

TEST_CASE("parse")
{
    SECTION("whitespace")
    {
        SECTION("empty object")
        {
            CHECK(json::parse("{          }")==json({}));
            CHECK(json::parse("{\t}")==json({}));
            CHECK(json::parse("{\n}")==json({}));
            CHECK(json::parse("{\u000d}")==json({}));
            CHECK(json::parse("{\u000d\u000d\u000d  \t\t\t\n\n   \u000d \n\t  \t \u000d}")==json({}));
        }
        SECTION("non-empty object")
        {
            CHECK(json::parse("{ \"foo\" : \"bar\" }")==json::parse("{\"foo\":\"bar\"}"));
            CHECK(json::parse("{\t\"foo\"\t:\t\"bar\"\t}")==json::parse("{\"foo\":\"bar\"}"));
            CHECK(json::parse("{\n\"foo\"\n:\n\"bar\"\n}")==json::parse("{\"foo\":\"bar\"}"));
            CHECK(json::parse("{\u000d\"foo\"\u000d:\u000d\"bar\"\u000d}")==json::parse("{\"foo\":\"bar\"}"));
            CHECK(json::parse("{ \"foo\"\t:\n\"bar\"\n}")==json::parse("{\"foo\":\"bar\"}"));
            CHECK(json::parse("{\t\t\t\t\t\n\n\u000d\"foo\"\t \t\t  \n\n  \u000d:\"bar\"}")==json::parse("{\"foo\":\"bar\"}"));
        }
    }    
    // The colon U+003A is the only valid member separator.
    // Look-alikes are illegal.
    // All other valid structural characters are illegal.
    SECTION("member separator")
    {
        CHECK_NOTHROW(parser_helper("{\"foo\"\u003a\"bar\"}"));      //:
        CHECK_THROWS_AS(parser_helper("{\"foo\"\uff1a\"bar\"}"),json::parse_error&);     
        CHECK_THROWS_AS(parser_helper("{\"foo\"\ua789\"bar\"}"),json::parse_error&);
        CHECK_THROWS_AS(parser_helper("{\"foo\"\u005b\"bar\"}"),json::parse_error&);     //[
        CHECK_THROWS_AS(parser_helper("{\"foo\"\u007b\"bar\"}"),json::parse_error&);     //{
        CHECK_THROWS_AS(parser_helper("{\"foo\"\u005d\"bar\"}"),json::parse_error&);     //]
        CHECK_THROWS_AS(parser_helper("{\"foo\"\u007d\"bar\"}"),json::parse_error&);     //}
        CHECK_THROWS_AS(parser_helper("{\"foo\"\u002c\"bar\"}"),json::parse_error&);     //,
        CHECK_THROWS_AS(parser_helper("{\"foo\"\u003b\"bar\"}"),json::parse_error&);     //;
    }
    SECTION("names")
    {
        SECTION("numbers")
        {
            // cf. n_object_non_string_key.json, n_object_non_string_key_but_huge_number_instead.json, for some integers
            CHECK_THROWS_AS(parser_helper("{0.1:\"foo\"}"),json::parse_error&);
            CHECK_THROWS_AS(parser_helper("{3\u004542:\"foo\"}"),json::parse_error&);
            CHECK_THROWS_AS(parser_helper("{3.1415\u006542:\"foo\"}"),json::parse_error&);
            CHECK_THROWS_AS(parser_helper("{-15:\"foo\"}"),json::parse_error&);
        }
        SECTION("arrays")
        {
            CHECK_THROWS_AS(parser_helper("{[]:\"foo\"}"),json::parse_error&);
            CHECK_THROWS_AS(parser_helper("{[1]:\"foo\"}"),json::parse_error&);
            CHECK_THROWS_AS(parser_helper("{[1,\"foo\"]:\"bar\"}"),json::parse_error&);
        }
        SECTION("objects")
        {
            CHECK_THROWS_AS(parser_helper("{{}:\"foo\"}"),json::parse_error&);
            CHECK_THROWS_AS(parser_helper("{{\"a\":1}:\"foo\"}"),json::parse_error&);
            CHECK_THROWS_AS(parser_helper("{{\"a\":1,\"b\":\"foo\"}:\"bar\"}"),json::parse_error&);
        }
        SECTION("literals")
        {
            CHECK_THROWS_AS(parser_helper("true:\"foo\""),json::parse_error&);
            CHECK_THROWS_AS(parser_helper("false:\"foo\""),json::parse_error&);
            CHECK_THROWS_AS(parser_helper("null:\"foo\""),json::parse_error&);
        }
    }
    // It is checked in unit-testsuites that duplicate values are parsed without error.
    // The exact behaviour, however, appears to be not tested for yet.
    SECTION("duplicate names")
    {
        // object containing 100,000 members with the same name and different values.
        //std::ifstream f("duplicate_objects.json");
        //json _1 = json::parse(f);
        //CHECK(_1 == "{\"name\":\"value\"}"); 
        // object containing 100,000 members with only first and last member of the same name
        //std::ifstream f2("100000_members_one_duplicate_name.json");
        //std::ifstream f3("100000_members_without_duplicate_name.json");
        //json _2 = json::parse(f2);
        //json _3 = json::parse(f3);
        //CHECK(_2==_3);
    }
}

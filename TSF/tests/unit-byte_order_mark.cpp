
#include "doctest_compatibility.h"

#include <nlohmann/json.hpp>
using nlohmann::json;


// build throws a warning when json::parse(foo) is used without output.
// The parser_helper prevents this.
void parser_helper(std::string input)
{
    json temp = json::parse(input);
}

TEST_CASE("accept")
{
    SECTION("UTF-8")
    {
        SECTION("multiple BOM")
        {
            CHECK(!json::accept("\xEF\xBB\xBF\xEF\xBB\xBF"));
            CHECK(!json::accept("\xEF\xBB\xBF\xEF\xBB\xBF\xEF\xBB\xBF"));
            CHECK(!json::accept("\xEF\xBB\xBF\xEF\xBB\xBF\xEF\xBB\xBF\xEF\xBB\xBF"));
            CHECK(!json::accept("\xEF\xBB\xBF\xEF\xBB"));
            CHECK(!json::accept("\xEF\xBB\xBF foo"));
        }
        SECTION("unexpected BOM")
        {
            CHECK(!json::accept(" \xEF\xBB\xBF"));
            CHECK(!json::accept("\t\xEF\xBB\xBF"));
            CHECK(!json::accept("\n\xEF\xBB\xBF"));
            CHECK(!json::accept("\xEF\xBB\xBF"));
            CHECK(!json::accept("\u000d\xEF\xBB\xBF"));
            CHECK(!json::accept("1\xEF\xBB\xBF"));
            CHECK(!json::accept("\"foo\"\xEF\xBB\xBF"));
            CHECK(!json::accept("[42]\xEF\xBB\xBF"));
            CHECK(!json::accept("{\"foo\":\"bar\"}\xEF\xBB\xBF"));
        }
    }
    SECTION("Other byte-order marks")
    {
        SECTION("UTF-16")
        {
            CHECK(!json::accept("\xFE\xFF"));
            CHECK(!json::accept("\xFF\xFE"));
        }
        SECTION("UTF-32")
        {
            CHECK(!json::accept("\x00\x00\xFE\xFF"));
            CHECK(!json::accept("\xFF\xFE\x00\x00"));
        }
    }
}

TEST_CASE("parse")
{
    SECTION("UTF-8")
    {
        SECTION("multiple BOM")
        {
            // Whenever a fourth character of a BOM-candidate is read, an error is thrown. 
            // This error does not depend on any trailing garbage.
            CHECK_THROWS_WITH_AS(parser_helper("\xEF\xBB\xBF\xEF\xBB\xBF"),"[json.exception.parse_error.101] parse error at line 1, column 4: syntax error while parsing value - invalid literal; last read: '\xEF\xBB\xBF\xEF'", json::parse_error&);
            CHECK_THROWS_WITH_AS(parser_helper("\xEF\xBB\xBF\xEF\xBB\xBF\xEF\xBB\xBF"),"[json.exception.parse_error.101] parse error at line 1, column 4: syntax error while parsing value - invalid literal; last read: '\xEF\xBB\xBF\xEF'", json::parse_error&);
            CHECK_THROWS_WITH_AS(parser_helper("\xEF\xBB\xBF\xEF\xBB\xBF\xEF\xBB\xBF\xEF\xBB\xBF"),"[json.exception.parse_error.101] parse error at line 1, column 4: syntax error while parsing value - invalid literal; last read: '\xEF\xBB\xBF\xEF'", json::parse_error&);
            CHECK_THROWS_WITH_AS(parser_helper("\xEF\xBB\xBF\xEF\xBB"),"[json.exception.parse_error.101] parse error at line 1, column 4: syntax error while parsing value - invalid literal; last read: '\xEF\xBB\xBF\xEF'", json::parse_error&);
            CHECK_THROWS_WITH_AS(parser_helper("\xEF\xBB\xBF\xEF foo"),"[json.exception.parse_error.101] parse error at line 1, column 4: syntax error while parsing value - invalid literal; last read: '\xEF\xBB\xBF\xEF'", json::parse_error&);
        }
        SECTION("unexpected BOM")
        {
            // A byte order mark at any other position than the very first character is illegal and an error is thrown.
            CHECK_THROWS_AS(parser_helper(" \xEF\xBB\xBF"), json::parse_error&);
            CHECK_THROWS_AS(parser_helper("\t\xEF\xBB\xBF"), json::parse_error&);
            CHECK_THROWS_AS(parser_helper("\n\xEF\xBB\xBF"), json::parse_error&);
            CHECK_THROWS_AS(parser_helper("\xEF\xBB\xBF"), json::parse_error&);
            CHECK_THROWS_AS(parser_helper("\u000d\xEF\xBB\xBF"), json::parse_error&);
            CHECK_THROWS_AS(parser_helper("1\xEF\xBB\xBF"), json::parse_error&);
            CHECK_THROWS_AS(parser_helper("\"foo\"\xEF\xBB\xBF"), json::parse_error&);
            CHECK_THROWS_AS(parser_helper("[42]\xEF\xBB\xBF"), json::parse_error&);
            CHECK_THROWS_AS(parser_helper("{\"foo\":\"bar\"}\xEF\xBB\xBF"), json::parse_error&);
        }
    }
    SECTION("other BOM")
    {
        SECTION("UTF-16")
        {
            CHECK_THROWS_AS(parser_helper("\xFE\xFF"),json::parse_error&);
            CHECK_THROWS_AS(parser_helper("\xFF\xFE"),json::parse_error&);
        }
        SECTION("UTF-32")
        {
            CHECK_THROWS_AS(parser_helper("\x00\x00\xFE\xFF"),json::parse_error&);
            CHECK_THROWS_AS(parser_helper("\xFF\xFE\x00\x00"),json::parse_error&);
        }
    }
}
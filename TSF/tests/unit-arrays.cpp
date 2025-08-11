
#include "doctest_compatibility.h"

#include <nlohmann/json.hpp>
#include <fstream>
#include <sstream>
using nlohmann::json;

// The pipeline complains if json::parse is called without an output.
// Masking this call within a helper function suppresses this complaint.
json parser_helper(std::string input);

json parser_helper(std::string input){
    return json::parse(input);
}

TEST_CASE("accept")
{
    // An interval accepts only [ and ] as left and right boundary, resp.
    // everything else, in particular invalid tokens, are illegal.
    SECTION("boundaries")
    {
        CHECK(!json::accept("[}"));
        CHECK(!json::accept("[\"foobar\"}"));
        CHECK(!json::accept("[1.23\u004513}"));
        CHECK(!json::accept("[[1,32,5,\"foo\"]}"));
        CHECK(!json::accept("{]"));
        CHECK(!json::accept("{\"foobar\"]"));
        CHECK(!json::accept("{1.23\u004513]"));
        CHECK(!json::accept("{[1,32,5,\"foo\"]]"));
        CHECK(!json::accept("(]"));
        CHECK(!json::accept("(\"foobar\"]"));
        CHECK(!json::accept("(1.23\u004513]"));
        CHECK(!json::accept("([1,32,5,\"foo\"]]"));

        // Test whether 100,000 opening brackets with "Moin!" and 99,999 closing brackets are rejected.
        std::stringstream faulty_array;
        for (int i = 0; i < 100000; i++){
            faulty_array << "[";
        }
        faulty_array << "\"Moin!\"";
        for (int i = 1; i < 100000; i++){
            faulty_array << "]";
        }
        CHECK(!json::accept(faulty_array.str()));
        // double check if rejection is not due to overflow
        CHECK_THROWS_AS(parser_helper(faulty_array.str()),json::parse_error&);
    }
}

TEST_CASE("parse")
{
    SECTION("whitespace")
    {
        json j = json::parse(R"(["1","2","test","foo","bar"])");
        CHECK(parser_helper("[ \"1\" , \"2\" , \"test\" , \"foo\" , \"bar\" ]")==j);
        CHECK(parser_helper("[ \"1\"\t, \"2\"\t, \"test\"\t, \"foo\"\t, \"bar\"\t]")==j);
        CHECK(parser_helper("[ \"1\"\n, \"2\"\n, \"test\"\n, \"foo\"\n, \"bar\"\n]")==j);
        CHECK(parser_helper("[ \"1\"\u000d, \"2\"\u000d, \"test\"\u000d, \"foo\"\u000d, \"bar\"\u000d]")==j);
        CHECK(parser_helper("[\t\"1\" ,\t\"2\" ,\t\"test\" ,\t\"foo\" ,\t\"bar\" ]")==j);
        CHECK(parser_helper("[\t\"1\"\t,\t\"2\"\t,\t\"test\"\t,\t\"foo\"\t,\t\"bar\"\t]")==j);
        CHECK(parser_helper("[\t\"1\"\n,\t\"2\"\n,\t\"test\"\n,\t\"foo\"\n,\t\"bar\"\n]")==j);
        CHECK(parser_helper("[\t\"1\"\u000d,\t\"2\"\u000d,\t\"test\"\u000d,\t\"foo\"\u000d,\t\"bar\"\u000d]")==j);
        CHECK(parser_helper("[\n\"1\" ,\n\"2\" ,\n\"test\" ,\n\"foo\" ,\n\"bar\" ]")==j);
        CHECK(parser_helper("[\n\"1\"\t,\n\"2\"\t,\n\"test\"\t,\n\"foo\"\t,\n\"bar\"\t]")==j);
        CHECK(parser_helper("[\n\"1\"\n,\n\"2\"\n,\n\"test\"\n,\n\"foo\"\n,\n\"bar\"\n]")==j);
        CHECK(parser_helper("[\n\"1\"\u000d,\n\"2\"\u000d,\n\"test\"\u000d,\n\"foo\"\u000d,\n\"bar\"\u000d]")==j);
        CHECK(parser_helper("[\u000d\"1\" ,\u000d\"2\" ,\u000d\"test\" ,\u000d\"foo\" ,\u000d\"bar\" ]")==j);
        CHECK(parser_helper("[\u000d\"1\"\t,\u000d\"2\"\t,\u000d\"test\"\t,\u000d\"foo\"\t,\u000d\"bar\"\t]")==j);
        CHECK(parser_helper("[\u000d\"1\"\n,\u000d\"2\"\n,\u000d\"test\"\n,\u000d\"foo\"\n,\u000d\"bar\"\n]")==j);
        CHECK(parser_helper("[\u000d\"1\"\u000d,\u000d\"2\"\u000d,\u000d\"test\"\u000d,\u000d\"foo\"\u000d,\u000d\"bar\"\u000d]")==j);
    }
}

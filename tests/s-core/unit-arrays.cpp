
#include "doctest_compatibility.h"

#include <nlohmann/json.hpp>
#include <fstream>
using nlohmann::json;


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
        std::ifstream fs("faulty_arrays.json");
        CHECK(!json::accept(fs));
    }
}
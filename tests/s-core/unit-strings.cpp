#include <string>
#include <sstream>
#include <iomanip>

#include "doctest_compatibility.h"

#include <nlohmann/json.hpp>
using nlohmann::json;

TEST_CASE("accept")
{
    SECTION("basic multilingual plane")
    {
        for (uint32_t i = 0x0000; i<=0xFFFF; i++)
        {
            if (i>=0xD800 && i<=0xDFFF)
            {
                // skip the utf-16 surrogates
                continue;
            }
            std::ostringstream temp;
            temp << "\"\\u" << std::hex << std::uppercase << std::setfill('0') << std::setw(4) << i << "\"";
            CHECK(json::accept(temp.str()));
        }
    }
}
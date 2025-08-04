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
            std::ostringstream temp;
            temp << "\"\\u" << std::hex << std::uppercase << std::setfill('0') << std::setw(4) << i << "\"";
            if (i>=0xD800 && i<=0xDFFF)
            {
                // Unpaired utf-16 surrogates are illegal.
                // Observe that this verbatim not what RFC8259 §7 prescribes; 
                // it appears, however, to be in the spirit of RFC8259, cf. §8.2 
                CHECK(!json::accept(temp.str()));
            } else { 
                // all other characters of the basic multilingual plane are accepted.
                CHECK(json::accept(temp.str()));
            }
        }
    }
    SECTION("utf-16 surrogates")
    {
        for (uint16_t i = 0xD800; i <= 0xDBFF; i++){
            for (uint16_t j = 0xDC00; j <= 0xDFFF; j++){
                std::ostringstream temp;
                temp << "\"\\u" << std::hex << std::uppercase << std::setfill('0') << std::setw(4) << i\
                << "\\u" << std::hex << std::uppercase << std::setfill('0') << std::setw(4) << j\
                << "\"" ;
                CHECK(json::accept(temp.str()));
            }
        }
    }
}
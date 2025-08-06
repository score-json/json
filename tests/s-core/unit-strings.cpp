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
    // escaped utf-16 surrogate pairs are accepted.
    SECTION("escaped utf-16 surrogates")
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
    // unescaped utf-16 surrogates are rejected.
    SECTION("unescaped utf-16 surrogates")
    {
        for (uint16_t i = 0xD800; i <= 0xDBFF; i++){
            for (uint16_t j = 0xDC00; j <= 0xDFFF; j++){
                std::string temp;
                temp += static_cast<char>(0xED);
                temp += static_cast<char>(i>>8);
                temp += static_cast<char>(i&0xFF);
                temp += static_cast<char>(0xED);
                temp += static_cast<char>(j>>8);
                temp += static_cast<char>(j&0xFF);
                CHECK(!json::accept(temp));
            }
        }
    }
    // noncharacters
    // The parsing of these is tested in unit-unicode.cpp;
    // here: replace roundtrip() (i.e. test for parse() and dump()) with accept.
    SECTION("noncharacter code positions")
    {
        // 5.3.1  U+FFFE = ef bf be
        CHECK(!json::accept("\xef\xbf\xbe"));
        // 5.3.2  U+FFFF = ef bf bf
        CHECK(!json::accept("\xef\xbf\xbf"));

        // 5.3.3  U+FDD0 .. U+FDEF
        CHECK(!json::accept("\xEF\xB7\x90"));
        CHECK(!json::accept("\xEF\xB7\x91"));
        CHECK(!json::accept("\xEF\xB7\x92"));
        CHECK(!json::accept("\xEF\xB7\x93"));
        CHECK(!json::accept("\xEF\xB7\x94"));
        CHECK(!json::accept("\xEF\xB7\x95"));
        CHECK(!json::accept("\xEF\xB7\x96"));
        CHECK(!json::accept("\xEF\xB7\x97"));
        CHECK(!json::accept("\xEF\xB7\x98"));
        CHECK(!json::accept("\xEF\xB7\x99"));
        CHECK(!json::accept("\xEF\xB7\x9A"));
        CHECK(!json::accept("\xEF\xB7\x9B"));
        CHECK(!json::accept("\xEF\xB7\x9C"));
        CHECK(!json::accept("\xEF\xB7\x9D"));
        CHECK(!json::accept("\xEF\xB7\x9E"));
        CHECK(!json::accept("\xEF\xB7\x9F"));
        CHECK(!json::accept("\xEF\xB7\xA0"));
        CHECK(!json::accept("\xEF\xB7\xA1"));
        CHECK(!json::accept("\xEF\xB7\xA2"));
        CHECK(!json::accept("\xEF\xB7\xA3"));
        CHECK(!json::accept("\xEF\xB7\xA4"));
        CHECK(!json::accept("\xEF\xB7\xA5"));
        CHECK(!json::accept("\xEF\xB7\xA6"));
        CHECK(!json::accept("\xEF\xB7\xA7"));
        CHECK(!json::accept("\xEF\xB7\xA8"));
        CHECK(!json::accept("\xEF\xB7\xA9"));
        CHECK(!json::accept("\xEF\xB7\xAA"));
        CHECK(!json::accept("\xEF\xB7\xAB"));
        CHECK(!json::accept("\xEF\xB7\xAC"));
        CHECK(!json::accept("\xEF\xB7\xAD"));
        CHECK(!json::accept("\xEF\xB7\xAE"));
        CHECK(!json::accept("\xEF\xB7\xAF"));

        // 5.3.4  U+nFFFE U+nFFFF (for n = 1..10)
        CHECK(!json::accept("\xF0\x9F\xBF\xBF"));
        CHECK(!json::accept("\xF0\xAF\xBF\xBF"));
        CHECK(!json::accept("\xF0\xBF\xBF\xBF"));
        CHECK(!json::accept("\xF1\x8F\xBF\xBF"));
        CHECK(!json::accept("\xF1\x9F\xBF\xBF"));
        CHECK(!json::accept("\xF1\xAF\xBF\xBF"));
        CHECK(!json::accept("\xF1\xBF\xBF\xBF"));
        CHECK(!json::accept("\xF2\x8F\xBF\xBF"));
        CHECK(!json::accept("\xF2\x9F\xBF\xBF"));
        CHECK(!json::accept("\xF2\xAF\xBF\xBF"));
    }
    // also copied from unit-unicode.cpp with replaced roundtrip()
    SECTION("overlong sequences")
    {
        SECTION("Examples of an overlong ASCII character")
        {
            // 4.1.1 U+002F = c0 af
            CHECK(!json::accept("\xc0\xaf"));
            // 4.1.2 U+002F = e0 80 af
            CHECK(!json::accept("\xe0\x80\xaf"));
            // 4.1.3 U+002F = f0 80 80 af
            CHECK(!json::accept("\xf0\x80\x80\xaf"));
            // 4.1.4 U+002F = f8 80 80 80 af
            CHECK(!json::accept("\xf8\x80\x80\x80\xaf"));
            // 4.1.5 U+002F = fc 80 80 80 80 af
            CHECK(!json::accept("\xfc\x80\x80\x80\x80\xaf"));
        }

        SECTION("Maximum overlong sequences")
        {
            // Below you see the highest Unicode value that is still resulting in an
            // overlong sequence if represented with the given number of bytes. This
            // is a boundary test for safe UTF-8 decoders. All five characters should
            // be rejected like malformed UTF-8 sequences.

            // 4.2.1  U-0000007F = c1 bf
            CHECK(!json::accept("\xc1\xbf"));
            // 4.2.2  U-000007FF = e0 9f bf
            CHECK(!json::accept("\xe0\x9f\xbf"));
            // 4.2.3  U-0000FFFF = f0 8f bf bf
            CHECK(!json::accept("\xf0\x8f\xbf\xbf"));
            // 4.2.4  U-001FFFFF = f8 87 bf bf bf
            CHECK(!json::accept("\xf8\x87\xbf\xbf\xbf"));
            // 4.2.5  U-03FFFFFF = fc 83 bf bf bf bf
            CHECK(!json::accept("\xfc\x83\xbf\xbf\xbf\xbf"));
        }

        SECTION("Overlong representation of the NUL character")
        {
            // The following five sequences should also be rejected like malformed
            // UTF-8 sequences and should not be treated like the ASCII NUL
            // character.

            // 4.3.1  U+0000 = c0 80
            CHECK(!json::accept("\xc0\x80"));
            // 4.3.2  U+0000 = e0 80 80
            CHECK(!json::accept("\xe0\x80\x80"));
            // 4.3.3  U+0000 = f0 80 80 80
            CHECK(!json::accept("\xf0\x80\x80\x80"));
            // 4.3.4  U+0000 = f8 80 80 80 80
            CHECK(!json::accept("\xf8\x80\x80\x80\x80"));
            // 4.3.5  U+0000 = fc 80 80 80 80 80
            CHECK(!json::accept("\xfc\x80\x80\x80\x80\x80"));
        }
    }
    // also copied from unit-unicode.cpp with replaced roundtrip()
    SECTION("malformed sequences")
    {
        SECTION("Unexpected continuation bytes")
        {
            // Each unexpected continuation byte should be separately signalled as a
            // malformed sequence of its own.

            // 3.1.1  First continuation byte 0x80
            CHECK(!json::accept("\x80"));
            // 3.1.2  Last  continuation byte 0xbf
            CHECK(!json::accept("\xbf"));

            // 3.1.3  2 continuation bytes
            CHECK(!json::accept("\x80\xbf"));
            // 3.1.4  3 continuation bytes
            CHECK(!json::accept("\x80\xbf\x80"));
            // 3.1.5  4 continuation bytes
            CHECK(!json::accept("\x80\xbf\x80\xbf"));
            // 3.1.6  5 continuation bytes
            CHECK(!json::accept("\x80\xbf\x80\xbf\x80"));
            // 3.1.7  6 continuation bytes
            CHECK(!json::accept("\x80\xbf\x80\xbf\x80\xbf"));
            // 3.1.8  7 continuation bytes
            CHECK(!json::accept("\x80\xbf\x80\xbf\x80\xbf\x80"));

            // 3.1.9  Sequence of all 64 possible continuation bytes (0x80-0xbf)
            CHECK(!json::accept("\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf"));
        }

        SECTION("Lonely start characters")
        {
            // 3.2.1  All 32 first bytes of 2-byte sequences (0xc0-0xdf)
            CHECK(!json::accept("\xc0 \xc1 \xc2 \xc3 \xc4 \xc5 \xc6 \xc7 \xc8 \xc9 \xca \xcb \xcc \xcd \xce \xcf \xd0 \xd1 \xd2 \xd3 \xd4 \xd5 \xd6 \xd7 \xd8 \xd9 \xda \xdb \xdc \xdd \xde \xdf"));
            // 3.2.2  All 16 first bytes of 3-byte sequences (0xe0-0xef)
            CHECK(!json::accept("\xe0 \xe1 \xe2 \xe3 \xe4 \xe5 \xe6 \xe7 \xe8 \xe9 \xea \xeb \xec \xed \xee \xef"));
            // 3.2.3  All 8 first bytes of 4-byte sequences (0xf0-0xf7)
            CHECK(!json::accept("\xf0 \xf1 \xf2 \xf3 \xf4 \xf5 \xf6 \xf7"));
            // 3.2.4  All 4 first bytes of 5-byte sequences (0xf8-0xfb)
            CHECK(!json::accept("\xf8 \xf9 \xfa \xfb"));
            // 3.2.5  All 2 first bytes of 6-byte sequences (0xfc-0xfd)
            CHECK(!json::accept("\xfc \xfd"));
        }

        SECTION("Sequences with last continuation byte missing")
        {
            // All bytes of an incomplete sequence should be signalled as a single
            // malformed sequence, i.e., you should see only a single replacement
            // character in each of the next 10 tests. (Characters as in section 2)

            // 3.3.1  2-byte sequence with last byte missing (U+0000)
            CHECK(!json::accept("\xc0"));
            // 3.3.2  3-byte sequence with last byte missing (U+0000)
            CHECK(!json::accept("\xe0\x80"));
            // 3.3.3  4-byte sequence with last byte missing (U+0000)
            CHECK(!json::accept("\xf0\x80\x80"));
            // 3.3.4  5-byte sequence with last byte missing (U+0000)
            CHECK(!json::accept("\xf8\x80\x80\x80"));
            // 3.3.5  6-byte sequence with last byte missing (U+0000)
            CHECK(!json::accept("\xfc\x80\x80\x80\x80"));
            // 3.3.6  2-byte sequence with last byte missing (U-000007FF)
            CHECK(!json::accept("\xdf"));
            // 3.3.7  3-byte sequence with last byte missing (U-0000FFFF)
            CHECK(!json::accept("\xef\xbf"));
            // 3.3.8  4-byte sequence with last byte missing (U-001FFFFF)
            CHECK(!json::accept("\xf7\xbf\xbf"));
            // 3.3.9  5-byte sequence with last byte missing (U-03FFFFFF)
            CHECK(!json::accept("\xfb\xbf\xbf\xbf"));
            // 3.3.10 6-byte sequence with last byte missing (U-7FFFFFFF)
            CHECK(!json::accept("\xfd\xbf\xbf\xbf\xbf"));
        }

        SECTION("Concatenation of incomplete sequences")
        {
            // All the 10 sequences of 3.3 concatenated, you should see 10 malformed
            // sequences being signalled:
            CHECK(!json::accept("\xc0\xe0\x80\xf0\x80\x80\xf8\x80\x80\x80\xfc\x80\x80\x80\x80\xdf\xef\xbf\xf7\xbf\xbf\xfb\xbf\xbf\xbf\xfd\xbf\xbf\xbf\xbf"));
        }

        SECTION("Impossible bytes")
        {
            // The following two bytes cannot appear in a correct UTF-8 string

            // 3.5.1  fe
            CHECK(!json::accept("\xfe"));
            // 3.5.2  ff
            CHECK(!json::accept("\xff"));
            // 3.5.3  fe fe ff ff
            CHECK(!json::accept("\xfe\xfe\xff\xff"));
        }
    }
}

TEST_CASE("parse")
{
    SECTION("escaped unicode")
    {
        for (uint32_t i = 0x0000; i<=0xFFFF; i++)
        {
            std::ostringstream temp;
            std::ostringstream temp2;
            temp << "\"\\u" << std::hex << std::uppercase << std::setfill('0') << std::setw(4) << i << "\"";
            temp2 << "\"\\u" << std::hex << std::nouppercase << std::setfill('0') << std::setw(4) << i << "\"";
            if (i>=0xD800 && i<=0xDFFF)
            {
                // Unpaired utf-16 surrogates are illegal.
                // Observe that this verbatim not what RFC8259 §7 prescribes; 
                // it appears, however, to be in the spirit of RFC8259, cf. §8.2 
                // Illegal characters are not parsed anyway.
                continue;
            } else { 
                // all other characters of the basic multilingual plane are accepted.
                CHECK(json::parse(temp.str())==json::parse(temp2.str()));
            }
        }
    }
    SECTION("unescaped unicode")
    {
        for (uint32_t i = 0x0000; i<=0x10FFFF; i++)
        {
            if (i>=0xD800 && i<=0xDFFF)
            {
                // Unpaired utf-16 surrogates are illegal.
                // Observe that this verbatim not what RFC8259 §7 prescribes; 
                // it appears, however, to be in the spirit of RFC8259, cf. §8.2 
                // Illegal characters are not parsed anyway.
                continue;
            } else if (i<0x0020||i==0x0022||i==0x005c) { 
                // These characters are illegal if unescaped.
            } else {
                // All other characters are valid according to RFC8259
                std::string temp = "\"";
                // evil chat-gpt magic transforms i into utf-8 encoded unescaped character
                if (i <= 0x7F) {
                    temp += static_cast<char>(i); // 1-byte (ASCII)
                } else if (i <= 0x7FF) {
                    temp += static_cast<char>(0xC0 | ((i >> 6) & 0x1F)); // 2-byte sequence
                    temp += static_cast<char>(0x80 | (i & 0x3F));
                } else if (i <= 0xFFFF) {
                    temp += static_cast<char>(0xE0 | ((i >> 12) & 0x0F)); // 3-byte sequence
                    temp += static_cast<char>(0x80 | ((i >> 6) & 0x3F));
                    temp += static_cast<char>(0x80 | (i & 0x3F));
                } else if (i <= 0x10FFFF) {
                    temp += static_cast<char>(0xF0 | ((i >> 18) & 0x07)); // 4-byte sequence
                    temp += static_cast<char>(0x80 | ((i >> 12) & 0x3F));
                    temp += static_cast<char>(0x80 | ((i >> 6) & 0x3F));
                    temp += static_cast<char>(0x80 | (i & 0x3F));
                }
                temp += "\"";
                CHECK_NOTHROW(json::parse(temp));
            }
        }
    }
}
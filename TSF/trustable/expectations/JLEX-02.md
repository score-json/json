---
level: 1.1
normative: true
references:
        - type: function_reference
          name: "basic_json::parse"
          path: "include/nlohmann/json.hpp"
          description: "the public interface of the `parse`-functionality of nlohmann/json for single inputs"
          overload: 1
        - type: function_reference
          name: "basic_json::parse"
          path: "include/nlohmann/json.hpp"
          description: "the public interface of the `parse`-functionality of nlohmann/json for iterator inputs"
          overload: 2
        - type: function_reference
          name: "basic_json::parse"
          path: "include/nlohmann/json.hpp"
          description: "the public interface of the `parse`-functionality of nlohmann/json for input buffer"
          overload: 3
        - type: function_reference
          name: "parser::parse"
          path: "include/nlohmann/detail/input/parser.hpp"
          description: "the internal `parse`-functionality called by basic_json::parse"
        - type: function_reference
          name: "parser::sax_parse"
          path: "include/nlohmann/detail/input/parser.hpp"
          description: "called by parser::parse"
        - type: function_reference
          name: "parser::sax_parse_internal"
          path: "include/nlohmann/detail/input/parser.hpp"
          description: "called by parser::sax_parse"
        - type: function_reference
          name: "lexer::scan"
          path: "include/nlohmann/detail/input/lexer.hpp"
          description: "scans input, called in parser::sax_parse_internal"
---

The requirement regarding [JSON Deserialization](https://eclipse-score.github.io/score/main/modules/baselibs/json/docs/requirements/index.html#comp_req__json__deserialization) is fulfilled.
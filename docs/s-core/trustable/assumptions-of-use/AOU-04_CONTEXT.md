---
level: 1.1
normative: false
---

All exceptions (json::parse_error, json::invalid_iterator, json::type_error, json::out_of_range, json::other_error) inherit from json::exception. 

The nlohman_json library uses JSON_TRY, JSON_CATCH, etc.,  marcos instead of the exception keywords try, catch, etc., which may be overwritten to suppress exceptions. Each keyword can be individually overwritten (e.g. #define JSON_THROW(exception) std::abort()) or you can set (#define JSON_NOEXCEPTION) which leads to suppressing exceptions.

Alternatively, the accept function may first be used to check if the JSON is valid since the accept function only throws an exception for an empty input. In case of invalid JSON, false is returned and no exception. The parse function also has a parameter allow_exceptions to turn off parse error exceptions.
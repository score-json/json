This file collects and comments the open known misbehaviours as identified in the [issues](https://github.com/nlohmann/json/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22kind%3A%20bug%22) on nlohmann/json.

issue-id | comment
---------|--------
4925 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. Optimized binary arrays have to be explicitly enabled when parsing from BJdata; otherwise an exception is thrown.
4916 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. Version 3.12.0 of nlohmann::json does not contain a constructor accepting std::views.
4903 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. Defining the namespace "nlohmann" multiple times within the same project leads to an error.
4901 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. Using json::from_ubjson() (cf. [here](https://json.nlohmann.me/api/basic_json/from_ubjson/)) on long nested inputs can lead to stack overflow.
4898 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. Brace initialisation yields array, cf. [here](https://json.nlohmann.me/home/faq/#brace-initialization-yields-arrays).
4864 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. Using std::optional with nlohmann::json is broken in version 3.12.0, but shall be fixed in version 3.12.1.
4842 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. Instead of the provided allocator, the standard allocator is used in the non-recursive destructor.
4813 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. This issue is observed under specific circumstances only; in particular, basic_json is not affected.
4810 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. nlohmann::json currently does not allow selecting a custom allocator.
4714 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. Binary formats are creating broken outputs when discarded values are included in arrays/objects.
4621 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. Deprecation warning when using the .at or .value functions on a ordered_json object with a parameter type of json_pointer; this issue is still open in version 3.12.0.
4552 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. Invalid UTF-8 characters are not ignored when passing  error_handler_t::ignore to dump(); this issue is still open in version 3.12.0.
4104 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. This bug was observed in version 3.11.2; in version 3.12.0 it appears that the minimal code example does not trigger an error.
4041 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. This issue was observed in version 3.11.2; it is fixed in version 3.12.0.
3970 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. The use of C++20 modules with nlohmann/json may lead to errors; this issue still exists in version 3.12.0
3912 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. There is currently no way to query object keys via std::string_view; this issue still exists in version 3.12.0.
3907 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. Using CUDA with gcc as host compiler can lead to compiler errors. This issue still exists in version 3.12.0.
3885 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. Using meson instead of cmake to build the library does not work; use cmake to guarantee the expected outcome.
3868 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. This issue regards the compatibility with the latest C++ standard.
3859 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. json.value() with optional fallback value does not compile; this issue is still open in version 3.12.0.
3732 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. Using iteration_proxy_value with ordered_json as shown below fails to compile due to an incomplete type error in iterator set_parents(iterator it, typename iterator::difference_type count_set_parents); this issue still exists in version 3.12.0.
3669 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. This issue was observed in version 3.10.3; it appears fixed in version 3.12.0.
3659 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. Moving a directory into or out of the serve_header.py root is not detected; this is not an issue if the release version 3.12.0 is used without any changes.
3583 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. The performance of destroy() is quite slow.
3578 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. Custom number types with non-trivial destructors and move-constructors are not permitted.
3425 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. This issue is fixed in version 3.12.0 with the corresponding test in line 323 of unit-alt-string.cpp
3381 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. Keys of objects are required to be strings; and the literal null is not a string.
3106 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. Setting JSON_DIAGNOSTICS was broken in version 3.10.4.
2649 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. This issue was observed in version 3.9.1; it appears fixed in version 3.12.0.
2226 | This issue does not apply to the use of nlohmann/json in Eclipse S-CORE. std::tuple<const nlohmann::json&>::tuple(std::tuple<nlohmann::json&>&&) constructor creates a temporary object and a dangling reference. This issue still exists in version 3.12.0.

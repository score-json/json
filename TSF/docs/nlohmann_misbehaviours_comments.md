This file collects and comments the open known misbehaviours as identified in the [issues](https://github.com/nlohmann/json/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22kind%3A%20bug%22) on nlohmann/json.

issue-id | applies to S-CORE | comment
---------|-------------------|--------
4946 | No | Compatibility with CMake < 3.5 has been removed from CMake as of [CMake 4.0+](https://cmake.org/cmake/help/latest/command/cmake_minimum_required.html)
4925 | No | Optimized binary arrays have to be explicitly enabled when parsing from BJdata; otherwise an exception is thrown.
4916 | No | Version 3.12.0 of nlohmann::json does not contain a constructor accepting std::views.
4903 | No | Defining the namespace "nlohmann" multiple times within the same project leads to an error.
4901 | No | Using json::from_ubjson() (cf. [here](https://json.nlohmann.me/api/basic_json/from_ubjson/)) on long nested inputs can lead to stack overflow.
4898 | No | Brace initialisation yields array, cf. [here](https://json.nlohmann.me/home/faq/#brace-initialization-yields-arrays).
4864 | No | Using std::optional with nlohmann::json is broken in version 3.12.0, but shall be fixed in version 3.12.1.
4842 | No | Instead of the provided allocator, the standard allocator is used in the non-recursive destructor.
4813 | No | This issue is observed under specific circumstances only; in particular, basic_json is not affected.
4810 | No | nlohmann::json currently does not allow selecting a custom allocator.
4714 | No | Binary formats are creating broken outputs when discarded values are included in arrays/objects.
4621 | No | Deprecation warning when using the .at or .value functions on a ordered_json object with a parameter type of json_pointer; this issue is still open in version 3.12.0.
4552 | No | Invalid UTF-8 characters are not ignored when passing  error_handler_t::ignore to dump(); this issue is still open in version 3.12.0.
4104 | No | This bug was observed in version 3.11.2; in version 3.12.0 it appears that the minimal code example does not trigger an error.
4041 | No | This issue was observed in version 3.11.2; it is fixed in version 3.12.0.
3970 | No | The use of C++20 modules with nlohmann/json may lead to errors; this issue still exists in version 3.12.0
3912 | No | There is currently no way to query object keys via std::string_view; this issue still exists in version 3.12.0.
3907 | No | Using CUDA with gcc as host compiler can lead to compiler errors. This issue still exists in version 3.12.0.
3885 | No | Using meson instead of cmake to build the library does not work; use cmake to guarantee the expected outcome.
3868 | No | This issue regards the compatibility with the latest C++ standard.
3859 | No | json.value() with optional fallback value does not compile; this issue is still open in version 3.12.0.
3732 | No | Using iteration_proxy_value with ordered_json as shown below fails to compile due to an incomplete type error in iterator set_parents(iterator it, typename iterator::difference_type count_set_parents); this issue still exists in version 3.12.0.
3669 | No | This issue was observed in version 3.10.3; it appears fixed in version 3.12.0.
3659 | No | Moving a directory into or out of the serve_header.py root is not detected; this is not an issue if the release version 3.12.0 is used without any changes.
3583 | No | The performance of destroy() is quite slow.
3578 | No | Custom number types with non-trivial destructors and move-constructors are not permitted.
3425 | No | This issue is fixed in version 3.12.0 with the corresponding test in line 323 of unit-alt-string.cpp
3381 | No | Keys of objects are required to be strings; and the literal null is not a string.
3106 | No | Setting JSON_DIAGNOSTICS was broken in version 3.10.4.
2649 | No | This issue was observed in version 3.9.1; it appears fixed in version 3.12.0.
2226 | No | std::tuple<const nlohmann::json&>::tuple(std::tuple<nlohmann::json&>&&) constructor creates a temporary object and a dangling reference. This issue still exists in version 3.12.0.

# List of known misbehaviours

This file collects and comments the known misbehaviours opened after the release of version 3.12.0 as identified in the [issues](https://github.com/nlohmann/json/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22kind%3A%20bug%22) on nlohmann/json.

## known open misbehaviours

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

## known misbehaviours closed since being opened

issue-id | applies to S-CORE | comment
---------|-------------------|--------
4733 | No | Clang 11.0.x with libc++ fails to compile tests in C++20 mode due to incomplete char8_t support in std::filesystem::path. 
4740 | No | Using std::optional with nlohmann::json is broken in version 3.12.0, but shall be fixed in version 3.12.1.
4745 | No | Compiling version 3.12.0 with /std:c++ latest in Visual Studio 2022 17.12.7 raises compiler errors.
4746 | No | If you do not use the single_include json.hpp as intended, then the library may not quite work as intended.
4755 | No | The serialization of floating-point numbers is handled in two code paths. If number_float_t is double or long_double, then no issue arises.
4756 | No | nlohmann::ordered_json::from_msgpack() does not work with buffer of type std::vector\<std::byte\> using Xcode 16.3 and C++20.
4759 | No | Wrapping the library into a module fails due to `static` in lines 9832 and 3132.
4762 | No | Default return value for type_name() is number, which makes some error messages more than cryptic.
4778 | No | std::is_trivial is deprecated in C++26, using GCC 15.1.1 produces a deprecation warning.
4780 | No | The conversion from JSON to std::optional does not work.
4792 | No | C++20 support of NVHPC 25.5 is broken.
4798 | No | The float value is encoded to msgpack as double if it contains float NaN or infinity.
4804 | No | Trying to use json::from_cbor with a binary_t set to std::vector\<std::byte> will fail.
4812 | No | Only binary formats like CBOR or MessagePack allow writing and reading binary values; no misbehaviour.
4819 | No | This is a bug in gcc 14.2, which will not be suppressed by the library.
4821 | No | Cf. https://json.nlohmann.me/home/faq/#brace-initialization-yields-arrays
4825 | No | template class nlohmann::basic_json<>; leads to a compilation error "ambigious static_caststd::string" inside binary_writer::write_bjdata_ndarray.
4826 | No | Issue closed due to inactivity.
4828 | No | Cryptic issue with joining objects on keys, no minimal working example provided.
4834 | No | Using std::optional with nlohmann::json is broken in version 3.12.0, but shall be fixed in version 3.12.1.
4842 | No | The vector used to track nested objects and arrays is allocated with the standard allocators, but the issue expects a different allocator. This issue is not a critical bug.
4852 | No | CONTRIBUTING.md does not mention the code style that is enforced for this project.
4854 | No | nullptr as SAX handler is not explicitly handled, shall be fixed in 3.12.1.
4863 | No | Shall be fixed in 3.12.1.
4869 | No | The linkage of this [link](https://raw.githubusercontent.com/nlohmann/json/v3.11.3/single_include/nlohmann/json.hpp) pointed erroneously to version 3.12.0 for some time.
4890 | No | If the coveralls service website is down, then the CI-pipeline fails by default.
4892 | No | This feature request is obsolete.





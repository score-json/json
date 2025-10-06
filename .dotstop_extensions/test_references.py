import pytest
import tempfile
from pathlib import Path
from unittest.mock import patch
from validators import file_exists
from references import CPPTestReference, JSONTestsuiteReference, FunctionReference, ListOfTestCases, ItemReference


@pytest.fixture
def sample_cpp_content():
    """Sample C++ test file content for testing."""
    return '''#include "test.h"

TEST_CASE("basic_test")
{
    SECTION("section1")
    {
        CHECK(true);
        
        SECTION("nested_section")
        {
            CHECK(1 == 1);
        }
    }
    
    SECTION("section2")
    {
        CHECK(false);
    }
}

TEST_CASE("another_test")
{
    CHECK(2 == 2);
}
'''

@pytest.fixture
def sample_testsuite_test():
    """Sample JSON testsuite content for testing."""
    return '''TEST_CASE("compliance tests from json.org")
{
    // test cases are from https://json.org/JSON_checker/

    SECTION("expected failures")
    {
        for (const auto* filename :
                {
                    TEST_DATA_DIRECTORY "/json_tests/fail1.json",
                    TEST_DATA_DIRECTORY "/json_tests/fail2.json",
                    TEST_DATA_DIRECTORY "/json_tests/fail3.json",
                    \\ TEST_DATA_DIRECTORY "/json_tests/fail4.json",
                })
        {
            CAPTURE(filename)
            std::ifstream f(filename);
            json _;
            CHECK_THROWS_AS(_ = json::parse(f), json::parse_error&);
        }
    }
}
'''

@pytest.fixture
def sample_hpp_content():
    """Sample content in the style of lexer.hpp"""
    return '''template<typename BasicJsonType>
class lexer_base
{
    // class body
};

template<typename BasicJsonType, typename InputAdapterType>
class lexer : public lexer_base<BasicJsonType>
{

  private
    bool dummy_function()
    {
        return my_function();
    }

    bool my_function()
    {
        // function body 
    }
};
'''

def create_temp_file(content, suffix='.txt'):
    """Helper method to create temporary files for testing."""
    with tempfile.NamedTemporaryFile(mode='w', suffix=suffix, delete=False) as f:
        f.write(content)
        f.flush()
        return Path(f.name)

@pytest.fixture
def temp_cpp_file(sample_cpp_content):
    """Create a temporary C++ file for testing."""
    temp_file = create_temp_file(sample_cpp_content, '.cpp')
    yield temp_file
    temp_file.unlink()

@pytest.fixture
def temp_cpp_file_with_testsuite(sample_testsuite_test):
    """Create a temporary C++ file with testsuite content."""
    temp_file = create_temp_file(sample_testsuite_test, '.cpp')
    yield temp_file
    temp_file.unlink()

@pytest.fixture
def temp_hpp_file(sample_hpp_content):
    """Create a temporary .hpp file for testing."""
    temp_file = create_temp_file(sample_hpp_content, '.hpp')
    yield temp_file
    temp_file.unlink()

def test_init():
    """Test CPPTestReference initialization."""
    ref = CPPTestReference("test_section", "test.cpp")
    assert ref._name == "test_section"
    assert ref._path == Path("test.cpp")

def test_type_classmethod():
    """Test the type class method."""
    assert CPPTestReference.type() == "cpp_test"

def test_find_section_start_single_section():
    """Test finding a single section start."""
    lines = [
        '#include "test.h"\n',
        '\n',
        'TEST_CASE("basic_test")\n',
        '{\n',
        '    SECTION("section1")\n',
        '    {\n',
        '        CHECK(true);\n',
        '    }\n',
        '}\n'
    ]
    ref = CPPTestReference("basic_test", "test.cpp")
    start_index = ref.find_section_start(lines)
    assert start_index == 2

def test_find_section_start_nested_section():
    """Test finding nested section start."""
    lines = [
        'TEST_CASE("basic_test")\n',
        '{\n',
        '    SECTION("section1")\n',
        '    {\n',
        '        SECTION("nested")\n',
        '        {\n',
        '            CHECK(true);\n',
        '        }\n',
        '    }\n',
        '}\n'
    ]
    ref = CPPTestReference("basic_test;section1", "test.cpp")
    start_index = ref.find_section_start(lines)
    assert start_index == 2

def test_find_section_start_no_bracket_following_quote():
    """Test finding section start in case of no section start."""
    lines = [
        'TEST_CASE("basic_test"* doctest::skip())\n',
        '{\n',
        '    SECTION("section1")\n',
        '    {\n',
        '        CHECK(true);\n',
        '    }\n',
        '}\n'
    ]
    ref = CPPTestReference("basic_test", "test.cpp")
    start_index = ref.find_section_start(lines)
    assert start_index == 0

def test_find_section_start_not_found():
    """Test exception when section is not found."""
    lines = [
        'TEST_CASE("basic_test")\n',
        '{\n',
        '    CHECK(true);\n',
        '}\n'
    ]
    ref = CPPTestReference("nonexistent_section", "test.cpp")
    with pytest.raises(ValueError, match="Start of section nonexistent_section not found"):
        ref.find_section_start(lines)

def test_find_section_end():
    """Test finding section end with matching braces."""
    lines = [
        'SECTION("test")\n',
        '{\n',
        '    CHECK(true);\n',
        '}\n',
        'other code\n'
    ]
    ref = CPPTestReference("test", "test.cpp")
    end_index = ref.find_section_end(lines, 0)
    assert end_index == 4

def test_find_section_end_indented_braces():
    """Test finding section end with indented braces."""
    lines = [
        '    SECTION("test")\n',
        '    {\n',
        '        CHECK(true);\n',
        '    }\n',
        'other code\n'
    ]
    ref = CPPTestReference("test", "test.cpp")
    end_index = ref.find_section_end(lines, 0)
    assert end_index == 4

def test_find_section_end_no_opening_brace():
    """Test exception when no opening brace is found."""
    lines = [
        'SECTION("test")\n'
    ]
    ref = CPPTestReference("test", "test.cpp")
    with pytest.raises(ValueError, match="Section declaration is on the last line"):
        ref.find_section_end(lines, 0)

def test_find_section_end_invalid_pattern():
    """Test exception when opening brace pattern is invalid."""
    lines = [
        'SECTION("test")\n',
        'invalid line\n'
    ]
    ref = CPPTestReference("test", "test.cpp")
    with pytest.raises(ValueError, match="Section start line does not match expected pattern"):
        ref.find_section_end(lines, 0)

def test_find_section_end_no_closing_brace():
    """Test exception when no matching closing brace is found."""
    lines = [
        'SECTION("test")\n',
        '{\n',
        '    CHECK(true);\n'
    ]
    ref = CPPTestReference("test", "test.cpp")
    with pytest.raises(ValueError, match="Section end not found"):
        ref.find_section_end(lines, 0)

def test_remove_leading_whitespace_preserve_indentation():
    """Test whitespace removal while preserving indentation."""
    ref = CPPTestReference("test", "test.cpp")
    # 4 - (tab+4) - 4 spaces here
    text = "    line1\n\t    line2\n    line3\n"
    # 0 - 4 - 0 spaces here
    expected = "line1\n    line2\nline3\n"
    result = ref.remove_leading_whitespace_preserve_indentation(text)
    assert result == expected

def test_remove_leading_whitespace_preserve_indentation_tabs():
    test_input = '''\t\t\tSECTION("empty object")
\t\t\t{
\t\t\t\tCHECK(parser_helper("{}") == json(json::value_t::object));
\t\t\t}
'''

    expected_output = '''SECTION("empty object")
{
    CHECK(parser_helper("{}") == json(json::value_t::object));
}
'''
    ref = CPPTestReference("test", "test.cpp")
    result = ref.remove_leading_whitespace_preserve_indentation(test_input)
    assert result == expected_output

def test_get_section_integration(temp_cpp_file):
    """Test complete section extraction."""
    ref = CPPTestReference("basic_test;section1", str(temp_cpp_file))
    section = ref.get_section()
    assert 'TEST_CASE("basic_test")' not in section
    assert 'SECTION("section1")' in section
    assert 'CHECK(true)' in section
    assert 'SECTION("nested_section")' in section
    assert 'SECTION("section2")' not in section

def test_get_section_file_not_found():
    """Test exception when file is not found."""
    ref = CPPTestReference("test", "nonexistent.cpp")
    with pytest.raises(FileNotFoundError):
        ref.get_section()

def test_content_property(temp_cpp_file):
    """Test content property returns bytes."""
    ref = CPPTestReference("basic_test", str(temp_cpp_file))
    content = ref.content
    assert isinstance(content, bytes)
    assert b'TEST_CASE("basic_test")' in content
    assert b'SECTION("section2")' in content
    assert b'TEST_CASE("another_test")' not in content

def test_as_markdown(temp_cpp_file):
    """Test markdown formatting."""
    ref = CPPTestReference("basic_test", str(temp_cpp_file))
    markdown = ref.as_markdown()
    assert isinstance(markdown, str)
    assert 'TEST_CASE("basic_test")' in markdown

@pytest.mark.parametrize("section_name,expected_line", [
    ("basic_test", 2),
    ("another_test", 20)
])
def test_find_different_sections(sample_cpp_content, section_name, expected_line):
    """Test finding different sections in the same file."""
    lines = sample_cpp_content.split('\n')
    lines = [line + '\n' for line in lines]  # Add back newlines
    ref = CPPTestReference(section_name, "test.cpp")
    start_index = ref.find_section_start(lines)
    assert start_index == expected_line

def test_nested_section_extraction(temp_cpp_file):
    """Test extracting nested sections."""
    ref = CPPTestReference("basic_test;section1;nested_section", temp_cpp_file)
    section = ref.get_section()
    assert 'nested_section' in section

def test_testsuite_json_loading():
    """Test TestsuiteReference initialization and type."""
    with patch.object(JSONTestsuiteReference, 'check_testsuite_file_is_used_by_cpp_test') as mock_check, \
         patch.object(JSONTestsuiteReference, 'get_testsuite_content') as mock_get_content:
        
        mock_check.return_value = None  # Mock the validation check
        mock_get_content.return_value = '["Unclosed array"'
        
        suite_ref = JSONTestsuiteReference("name", "path", ["/json_tests/fail2.json"], "description")
        json = suite_ref.get_testsuite_content("/json_tests/fail2.json")
        assert json == '["Unclosed array"'

def test_json_testsuite_reference_content(temp_cpp_file_with_testsuite, sample_testsuite_test):
    """Test JSONTestsuiteReference content property."""
    suite_ref = JSONTestsuiteReference("compliance tests from json.org;expected failures", str(temp_cpp_file_with_testsuite), ["/json_tests/fail2.json", "/json_tests/fail3.json"], "description")
    
    content = suite_ref.content
    assert isinstance(content, bytes)

    decoded_content = content.decode('utf-8')

    relevant_section = '\n'.join(sample_testsuite_test.split('\n')[4:-2])

    # content should include the section from the C++ test file and the JSON files
    assert relevant_section in decoded_content
    # "/json_tests/fail2.json"
    assert '["Unclosed array"' in decoded_content
    # "/json_tests/fail3.json"
    assert '{unquoted_key: "keys must be quoted"}' in decoded_content

def test_json_testsuite_reference_init_valid():
    """Test JSONTestsuiteReference initialization with valid parameters."""
    test_suite_paths = ["tests/data/json_tests/pass1.json", "tests/data/json_tests/pass2.json"]
    description = "Test suite for valid JSON parsing"
    
    with patch.object(JSONTestsuiteReference, 'get_testsuite_content') as mock_get_content, \
         patch.object(JSONTestsuiteReference, 'check_testsuite_file_is_used_by_cpp_test') as mock_check:
        
        mock_get_content.side_effect = lambda path: f"content of {path}"
        mock_check.return_value = None  # Mock the validation check
        
        ref = JSONTestsuiteReference("test_section", "test.cpp", test_suite_paths, description)
        
        # Test initialization
        assert ref._name == "test_section"
        assert ref._path == Path("test.cpp")
        assert ref._test_suite_paths == test_suite_paths
        assert ref._description == description
        
        # Test that content was loaded for each path
        assert len(ref._loaded_json_map) == 2
        assert ref._loaded_json_map["tests/data/json_tests/pass1.json"] == "content of tests/data/json_tests/pass1.json"
        assert ref._loaded_json_map["tests/data/json_tests/pass2.json"] == "content of tests/data/json_tests/pass2.json"
        
        # Verify get_testsuite_content was called for each path
        assert mock_get_content.call_count == 2

def test_json_testsuite_reference_init_invalid_paths_type():
    """Test JSONTestsuiteReference initialization with invalid test_suite_paths type."""
    with pytest.raises(ValueError, match="test_suite_paths must be a list of strings"):
        JSONTestsuiteReference("test_section", "test.cpp", "not_a_list", "description")

def test_type_classmethod_JSON_testsuite():
    """Test the type class method."""
    assert JSONTestsuiteReference.type() == "JSON_testsuite"

def test_is_json_test_line_valid_cases():
    """Test is_json_test_line with valid JSON test lines."""
    # line from "json.org examples"
    assert JSONTestsuiteReference.is_json_test_line('    std::ifstream f(TEST_DATA_DIRECTORY "/json.org/5.json");')
    # line from "compliance tests from json.org"
    assert JSONTestsuiteReference.is_json_test_line('    TEST_DATA_DIRECTORY "/json_tests/fail2.json",')
    # line from "nst's JSONTestSuite (2)"
    assert JSONTestsuiteReference.is_json_test_line('TEST_DATA_DIRECTORY "/nst_json_testsuite2/test_parsing/y_string_surrogates_U+1D11E_MUSICAL_SYMBOL_G_CLEF.json",')


def test_filter_other_test_data_lines_keeps_relevant_lines():
    """Test filter_other_test_data_lines keeps lines with relevant test suite paths."""
    test_suite_paths = ["json_tests/pass1.json", "json_tests/pass2.json"]
    
    with patch.object(JSONTestsuiteReference, 'get_testsuite_content') as mock_get_content, \
         patch.object(JSONTestsuiteReference, 'check_testsuite_file_is_used_by_cpp_test') as mock_check:
        
        mock_get_content.return_value = "sample json content"
        mock_check.return_value = None  # Mock the validation check

        ref = JSONTestsuiteReference("test_section", "test.cpp", test_suite_paths, "Test description")
        
        input_text = '''TEST_CASE("test")
{
    // TEST_DATA_DIRECTORY "/json_tests/pass1.json",
    // TEST_DATA_DIRECTORY "/json_tests/fail1.json",
    TEST_DATA_DIRECTORY "/json_tests/pass2.json",
    TEST_DATA_DIRECTORY "/json_tests/other.json",
    CHECK(true);
}'''

def test_get_single_json_as_markdown_small_content():
    """Test get_single_json_as_markdown with small JSON content for two files."""
    test_suite_paths = ["json_tests/small.json", "json_tests/large.json"]

    def mock_content_side_effect(path):
        if path == "json_tests/small.json":
            return '{"test": "value1"}'
        elif path == "json_tests/large.json":
            return 'test\n'*500
        return ""
    
    with patch.object(JSONTestsuiteReference, 'get_testsuite_content') as mock_get_content, \
        patch.object(JSONTestsuiteReference, 'check_testsuite_file_is_used_by_cpp_test') as mock_check:
        
        mock_get_content.side_effect = mock_content_side_effect
        mock_check.return_value = None  # Mock the validation check
        
       
        ref = JSONTestsuiteReference("test_section", "test.cpp", test_suite_paths, "Test description")
        
        result1 = ref.get_single_json_as_markdown("json_tests/small.json")
        assert "- JSON Testsuite: json_tests/small.json" in result1
        assert "```json" in result1
        assert '{"test": "value1"}' in result1
        
        result2 = ref.get_single_json_as_markdown("json_tests/large.json")
        assert "- JSON Testsuite: json_tests/large.json" in result2
        assert '[Link to file]' in result2

def test_get_all_json_as_markdown():
    """Test get_all_json_as_markdown with multiple JSON files."""
    test_suite_paths = ["json_tests/file1.json", "json_tests/file2.json"]
    
    def mock_content_side_effect(path):
        if path == "json_tests/file1.json":
            return '{"name": "test1"}'
        elif path == "json_tests/file2.json":
            return '{"name": "test2"}'
        return ""
    
    with patch.object(JSONTestsuiteReference, 'get_testsuite_content') as mock_get_content, \
        patch.object(JSONTestsuiteReference, 'check_testsuite_file_is_used_by_cpp_test') as mock_check:
        
        mock_get_content.side_effect = mock_content_side_effect
        mock_check.return_value = None  # Mock the validation check
      
        
        ref = JSONTestsuiteReference("test_section", "test.cpp", test_suite_paths, "Test description")
        
        result = ref.get_all_json_as_markdown()
        
        # Should contain both JSON files
        assert "- JSON Testsuite: json_tests/file1.json" in result
        assert "- JSON Testsuite: json_tests/file2.json" in result
        
        # Should contain both JSON contents
        assert '{"name": "test1"}' in result
        assert '{"name": "test2"}' in result
        
        # Should have proper separation between files
        assert result.count("```json") == 2

def test_as_markdown():
    """Test as_markdown method with complete output structure."""
    test_suite_paths = ["json_tests/test1.json", "json_tests/test2.json"]
    
    def mock_content_side_effect(path):
        if path == "json_tests/test1.json":
            return '{"test": "value1"}'
        elif path == "json_tests/test2.json":
            return '{"test": "value2"}'
        return ""
    
    with patch.object(JSONTestsuiteReference, 'get_testsuite_content') as mock_get_content, \
         patch.object(JSONTestsuiteReference, 'get_section') as mock_get_section:
        
        mock_get_content.side_effect = mock_content_side_effect
        mock_get_section.return_value = '''TEST_CASE("test")
{
    TEST_DATA_DIRECTORY "/json_tests/test1.json",
    TEST_DATA_DIRECTORY "/json_tests/test2.json",
    CHECK(true);
}'''
        
        ref = JSONTestsuiteReference("test_section", "test.cpp", test_suite_paths, "Test JSON files")
        
        result = ref.as_markdown()
        
        # Should contain description
        assert "Description: Test JSON files" in result
        
        # Should contain JSON content
        assert "JSON Testsuite: json_tests/test1.json" in result
        assert "JSON Testsuite: json_tests/test2.json" in result
        assert '{"test": "value1"}' in result
        assert '{"test": "value2"}' in result
        
        # Should contain C++ test content
        assert "cpp-test:" in result
        assert "```cpp" in result
        assert "CHECK(true);" in result
        
        # Should be indented (starts with tab)
        assert result.startswith('\t')


def test_check_testsuite_file_is_used_by_cpp_test_valid():
    """Test check_testsuite_file_is_used_by_cpp_test with valid usage."""
    test_suite_paths = ["json_tests/pass1.json", "json_tests/pass2.json"]
    
    with patch.object(JSONTestsuiteReference, 'get_testsuite_content') as mock_get_content, \
         patch.object(JSONTestsuiteReference, 'get_section') as mock_get_section:
        
        mock_get_content.return_value = "sample json content"
        mock_get_section.return_value = '''TEST_CASE("test")
{
    for (const auto* filename :
        {
            TEST_DATA_DIRECTORY "/json_tests/pass1.json",
            TEST_DATA_DIRECTORY "/json_tests/pass2.json",
        })
    {
        CHECK(true);
    }
}'''
        
        # Should not raise any exception
        ref = JSONTestsuiteReference("test_section", "test.cpp", test_suite_paths, "Test description")
        assert ref._test_suite_paths == test_suite_paths

def test_check_testsuite_file_is_used_by_cpp_test_missing_file():
    """Test check_testsuite_file_is_used_by_cpp_test with missing file reference."""
    test_suite_paths = ["json_tests/missing.json", "json_tests/pass1.json"]
    
    with patch.object(JSONTestsuiteReference, 'get_testsuite_content') as mock_get_content, \
         patch.object(JSONTestsuiteReference, 'get_section') as mock_get_section:
        
        mock_get_content.return_value = "sample json content"
        mock_get_section.return_value = '''TEST_CASE("test")
{
    TEST_DATA_DIRECTORY "/json_tests/pass1.json",
    CHECK(true);
}'''
        
        # Should raise ValueError for missing file
        with pytest.raises(ValueError, match="JSON testsuite json_tests/missing.json is not used in the C\\+\\+ test file"):
            JSONTestsuiteReference("test_section", "test.cpp", test_suite_paths, "Test description")
    
def test_get_function_boundaries():
    lines = [
        'template<typename BasicJsonType>\n',
        'class lexer_base\n',
        '{\n',
        '    // class body\n',
        '};\n',
        '\n',
        'template<typename BasicJsonType, typename InputAdapterType>\n',
        'class lexer : public lexer_base<BasicJsonType>\n',
        '{\n',
        '\n',
        '  private\n',
        '    bool dummy_function()\n',
        '    {\n',
        '        return my_function();\n',
        '    }\n',
        '\n',
        '    bool my_function()\n',
        '    {\n',
        '        // function body \n',
        '    }\n',
        '};\n'
    ]
    assert FunctionReference.get_function_boundaries("foo","lexer::my_function",lines,1) == [16,19]
    
def test_get_function_boundaries_with_multiline_declaration():
    lines = [
        'template<typename BasicJsonType>\n',
        'class lexer_base\n',
        '{\n',
        '    // class body\n',
        '};\n',
        '\n',
        'template<typename BasicJsonType, typename InputAdapterType>\n',
        'class lexer : public lexer_base<BasicJsonType>\n',
        '{\n',
        '\n',
        '  private\n',
        '    bool dummy_function()\n',
        '    {\n',
        '        return my_function();\n',
        '    }\n',
        '\n',
        '    bool my_function(int: foo,',
        '                       bool: bar)\n',
        '    {\n',
        '        // function body \n',
        '    }\n',
        '};\n'
    ]
    assert FunctionReference.get_function_boundaries("foo","lexer::my_function",lines,1) == [16,20]
    
def test_get_function_boundaries_with_multiple_overloads():
    lines = [
        'template<typename BasicJsonType>\n',
        'class lexer_base\n',
        '{\n',
        '    // class body\n',
        '};\n',
        '\n',
        'template<typename BasicJsonType, typename InputAdapterType>\n',
        'class lexer : public lexer_base<BasicJsonType>\n',
        '{\n',
        '\n',
        '  private\n',
        '    bool dummy_function()\n',
        '    {\n',
        '        return my_function();\n',
        '    }\n',
        '\n',
        '    bool my_function()\n',
        '    {\n',
        '        // function body \n',
        '    }\n',
        '\n',
        '    void my_function()\n',
        '    {\n',
        '        // function body \n',
        '    }\n',
        '\n',
        '    int my_function()\n',
        '    {\n',
        '        // function body \n',
        '    }\n',
        '};\n'
    ]
    assert FunctionReference.get_function_boundaries("foo","lexer::my_function",lines,1) == [16,19]
    assert FunctionReference.get_function_boundaries("foo","lexer::my_function",lines,2) == [21,24]
    assert FunctionReference.get_function_boundaries("foo","lexer::my_function",lines,3) == [26,29]
    with pytest.raises(ValueError, match="Could not locate 4th implementation of lexer::my_function in file foo."):
        FunctionReference.get_function_boundaries("foo","lexer::my_function",lines,4)
    with pytest.raises(ValueError, match="Could not locate 123rd implementation of lexer::my_function in file foo."):
        FunctionReference.get_function_boundaries("foo","lexer::my_function",lines,123)
    with pytest.raises(ValueError, match="Could not locate 11th implementation of lexer::my_function in file foo."):
        FunctionReference.get_function_boundaries("foo","lexer::my_function",lines,11)

def test_get_function_line_numbers(temp_hpp_file):
    [a,b] = FunctionReference.get_function_line_numbers(str(temp_hpp_file),"lexer::my_function")
    assert a == 16
    assert b == 19

def test_init_function_reference(temp_hpp_file):
    ref = FunctionReference("lexer::my_function",str(temp_hpp_file))
    assert ref.code == b"    bool my_function()\n    {\n        // function body \n    }\n"
    assert ref._name == "lexer::my_function"
    assert ref.path == temp_hpp_file
    assert ref._overload == 1

def test_default_init_ListOfTestCases():
    ref = ListOfTestCases(["file_1","file_2"])
    assert ref._test_files == ["file_1","file_2"]
    assert ref._database == "artifacts/MemoryEfficientTestResults.db"
    assert ref._table == "test_results"

def test_non_default_init_ListOfTestCases():
    ref = ListOfTestCases(["file_1","file_2"],"my_database.db","my_fancy_table")
    assert ref._test_files == ["file_1","file_2"]
    assert ref._database == "my_database.db"
    assert ref._table == "my_fancy_table"

def test_compile_string():
    with pytest.raises(RuntimeError):
        ListOfTestCases.compile_string([])

def test_remove_and_count_indent():
    assert ListOfTestCases.remove_and_count_indent("Hallo")== (0,"Hallo")
    assert ListOfTestCases.remove_and_count_indent(" Hallo") == (1,"Hallo")
    assert ListOfTestCases.remove_and_count_indent("\t Hallo Welt \t\t") == (5,"Hallo Welt \t\t")

def test_extract_quotation():
    assert ListOfTestCases.extract_quotation("\"Hallo\" Welt") == "Hallo"
    assert ListOfTestCases.extract_quotation("This is quite \"exciting\", isn't it.") == "exciting"
    assert ListOfTestCases.extract_quotation("\"Hallo\" \"Welt\"") == "Hallo"

def test_extract_faulty_quotation():
    with pytest.raises(RuntimeError, match=r"Expected quotation mark; none were detected."):
        ListOfTestCases.extract_quotation("Hallo Welt")
    with pytest.raises(RuntimeError, match=r"Expected quotation marks; only one was detected."):
        ListOfTestCases.extract_quotation("Hallo \"Welt")

def test_transform_test_file_to_test_name():
    assert ListOfTestCases.transform_test_file_to_test_name("unit-dummy-test.cpp") == "test-dummy-test"
    assert ListOfTestCases.transform_test_file_to_test_name("unit-dummy_test.cpp") == "test-dummy_test"

def test_file_exists(tmp_path):
    root = tmp_path / "direx"
    root.mkdir()
    path_1 = root / "subfolder"
    path_1.mkdir()
    path_1_1 = path_1 / "test.yml"
    path_1_1.write_text("test")
    path_2 = root / "script.py"
    path_2.write_text("print(\"Hallo, Welt\")")
    files = [str(path_1),str(path_1_1),"foo.bar",str(path_2)]

    score, exceptions = file_exists({"files": files})

    assert score == 2/4
    assert any(isinstance(exception,Warning) for exception in exceptions)
    assert any(isinstance(exception,RuntimeError) for exception in exceptions)
def test_faulty_init_ItemReference():
    with pytest.raises(RuntimeError, match = r"Error: Can't initialise empty ItemReference."):
        item_reference = ItemReference([])

def test_init_ItemReference():
    item_reference = ItemReference(["Hallo","Welt"])
    assert item_reference._items == ["Hallo","Welt"]

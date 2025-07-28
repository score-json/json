import pytest
import tempfile
from pathlib import Path
from unittest.mock import patch, mock_open
from references import CPPTestReference


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
def temp_cpp_file(sample_cpp_content):
    """Create a temporary C++ file for testing."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.cpp', delete=False) as f:
        f.write(sample_cpp_content)
        f.flush()
        yield Path(f.name)
    Path(f.name).unlink()

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
    ref = CPPTestReference("basic_test:section1", "test.cpp")
    start_index = ref.find_section_start(lines)
    assert start_index == 2

def test_find_section_start_not_found():
    """Test exception when section is not found."""
    lines = [
        'TEST_CASE("basic_test")\n',
        '{\n',
        '    CHECK(true);\n',
        '}\n'
    ]
    ref = CPPTestReference("nonexistent_section", "test.cpp")
    with pytest.raises(ValueError, match="Section start not found"):
        ref.find_section_start(lines)

def test_find_section_end_valid():
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
    text = "    line1\n        line2\n    line3\n"
    expected = "line1\n    line2\nline3\n"
    result = ref.remove_leading_whitespace_preserve_indentation(text)
    assert result == expected

def test_remove_leading_whitespace_preserve_indentation_tabs():
    test_input = '''            SECTION("empty object")
            {
                CHECK(parser_helper("{}") == json(json::value_t::object));
            }
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
    ref = CPPTestReference("basic_test", str(temp_cpp_file))
    section = ref.get_section()
    assert 'TEST_CASE("basic_test")' in section
    assert 'SECTION("section1")' in section
    assert 'CHECK(true)' in section

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
    ref = CPPTestReference("basic_test:section1:nested_section", temp_cpp_file)
    section = ref.get_section()
    assert 'nested_section' in section

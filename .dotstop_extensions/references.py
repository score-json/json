from pathlib import Path
from trudag.dotstop.core.reference.references import BaseReference

class CPPTestReference(BaseReference):
    """
    Represents a reference to a specific section within a C++ test file. The class
    assumes that the C++ test sections are defined using `SECTION("name")` or
    `TEST_CASE("name")` syntax, where the section name can be nested using
    colon-separated names (e.g., "testcase1:section1:section2"). 
    
    Additionally, the opening brace `{` must be on the line immediately after the 
    section declaration, and the closing brace `}` must have the same indentation 
    as the opening brace. This is the case for the tests from nlohmann_json.
    """
    def __init__(self, name: str, path: str) -> None:
        """
        Initialize CPPTestReference.
        
        Args:
            name: Section name, use colon-separated for nested sections (e.g., "testcase1:section1:section2")
            path: Relative path from project root to the file
        """
        self._name = name
        self._path = Path(path)

    @classmethod
    def type(cls) -> str:
        return "cpp_test"

    def get_section(self) -> str:
        """Extract the specified section from the C++ test file."""
        with open(self._path, 'r') as file:
            lines = file.readlines()
            start_index = self.find_section_start(lines)
            end_index = self.find_section_end(lines, start_index)
            test_section = ''.join(lines[start_index:end_index])
        return test_section
    
    def find_section_start(self, file_lines: list[str]) -> int:
        """Find the starting line index of the section in the file."""

        # section names are colon-separated, e.g., "section1:section2"
        section_names = self._name.split(':')
        for line_number, line in enumerate(file_lines):
            # Check if current line contains a SECTION or TEST_CASE declaration matching the current first section name
            section_pattern = f'SECTION("{section_names[0]}")'
            test_case_pattern = f'TEST_CASE("{section_names[0]}")'
            if section_pattern in line or test_case_pattern in line:
                if len(section_names) == 1:
                    # If we only have one section name, we found our target
                    return line_number
                else:
                    # Remove the found section from the list and continue searching for nested sections
                    section_names.pop(0)


        raise ValueError("Section start not found")
    
    def find_section_end(self, file_lines: list[str], start_index: int):
        """
        Find the ending line index of a C++ test section.
        
        This method expects C++ test sections to follow the pattern:
        SECTION("name")
        {
            // section content
        }
        
        The opening brace must be on the line immediately after the section declaration,
        and the closing brace must have the same indentation as the opening brace. This
        is the case for the tests from nlohmann_json.
        
        Args:
            file_lines: List of lines from the C++ test file
            start_index: Line index where the section declaration was found
            
        Returns:
            Line index immediately after the closing brace of the section
            
        Raises:
            ValueError: If the section doesn't follow expected brace pattern or
                    if matching closing brace is not found
        """
        # Verify we have a valid line after the section declaration
        if start_index + 1 >= len(file_lines):
            raise ValueError("Section declaration is on the last line - no opening brace found")
            
        # The line after the section starts is " "*n + "{" and the section ends with " "*n + "}"
        # Check that the pattern matches the expected format
        line_after_start_line = file_lines[start_index + 1]
        if not line_after_start_line.strip().endswith('{'):
            raise ValueError("Section start line does not match expected pattern (*{)")
        
        # Create the expected closing line by replacing '{' with '}'
        end_line = line_after_start_line.replace('{', '}')
        
        # Search for the matching closing brace with same indentation
        for line_number in range(start_index + 1, len(file_lines)):
            if file_lines[line_number].rstrip() == end_line.rstrip():
                return line_number + 1
        
        raise ValueError("Section end not found")
    
    def remove_leading_whitespace_preserve_indentation(self, text: str) -> str:
        """Remove leading whitespace from all lines while preserving relative indentation."""
        lines = text.split('\n')
        ident_to_remove = len(lines[0]) - len(lines[0].lstrip())
        
        # Remove the baseline indentation from all lines
        adjusted_lines = []
        for line in lines:
            if line.strip():  # Non-empty line
                if not line.startswith(lines[0][:ident_to_remove]):
                    # If the indentation is not >= than for the baseline, return the original text
                    return text
                adjusted_lines.append(line[ident_to_remove:] if len(line) >= ident_to_remove else line)
            else:  # Empty line
                adjusted_lines.append('')
        
        return '\n'.join(adjusted_lines)

    @property
    def content(self) -> bytes:
        # encoding is necessary since content will be hashed
        return self.get_section().encode('utf-8')
  

    def as_markdown(self, filepath: None | str = None) -> str:
        content = self.content.decode('utf-8')
        return self.remove_leading_whitespace_preserve_indentation(content)
    
    def __str__(self) -> str:
        # this is used as a title in the trudag report
        return f"cpp-test: [{self._name}]\n({self._path})"

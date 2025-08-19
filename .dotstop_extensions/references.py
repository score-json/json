from pathlib import Path
from trudag.dotstop.core.reference.references import BaseReference
from trudag.dotstop.core.reference.references import SourceSpanReference
import requests
import subprocess

# Constants
MAX_JSON_LINES_FOR_DISPLAY = 25
TEST_DATA_REPO_URL = "https://raw.githubusercontent.com/nlohmann/json_test_data/master/"
NUM_WHITESPACE_FOR_TAB = 4

def format_cpp_code_as_markdown(code: str) -> str:
    return f"```cpp\n{code}\n```\n"

def format_json_as_markdown(json_content: str) -> str:
    return f"```json\n{json_content}\n```\n"

def make_md_bullet_point(text: str, indent_level: int = 0) -> str:
    indent = '\t' * indent_level
    return f"{indent}- {text}\n"

def add_indentation(text: str, indent_level: int) -> str:
    indent = '\t' * indent_level
    return indent + text.replace('\n', '\n' + indent)

class CPPTestReference(BaseReference):
    """
    Represents a reference to a specific section within a C++ test file. The class
    assumes that the C++ test sections are defined using `SECTION("name")` or
    # `TEST_CASE("name")` syntax, where the section name can be nested using
    colon-separated names (e.g., "testcase1:section1:section2"). We assume that the 
    section path is unique within the file.
    
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
            section_start_line = self.find_section_start(lines)
            section_end_line = self.find_section_end(lines, section_start_line)
            test_section = ''.join(lines[section_start_line:section_end_line])
        return test_section
    
    def find_section_start(self, file_lines: list[str]) -> int:
        """ 
        This method finds the starting line index of the section in the file. It expects 
        the section name to be in the format "section1" or "section1:section2". It searches 
        for the first occurrence of a line containing either SECTION("section1")
        or TEST_CASE("section1") where section1 matches the first part of the section name. 
        This is done iteratively for nested sections until the full section name sequence 
        is matched. This implicitly assumes that the section paths are unique within the file.

        Args:
            file_lines: List of lines from the C++ test file

        Returns:
            Line index where the section starts (i.e. the line containing SECTION or TEST_CASE)
        """
        section_names = self._name.split(';')
        for line_number, line in enumerate(file_lines):
            # Check if current line contains a SECTION or TEST_CASE declaration matching the current first section name
            section_pattern = f'SECTION("{section_names[0]}"'
            test_case_pattern = f'TEST_CASE("{section_names[0]}"'
            if section_pattern in line or test_case_pattern in line:
                if len(section_names) == 1:
                    # If we only have one section name left, we found our target
                    return line_number
                else:
                    # Remove the found section from the list and continue searching for nested sections
                    section_names.pop(0)

        raise ValueError("Start of section "+self._name+" not found.")
    
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
        
        # replace in every line tabs with spaces to ensure consistency
        file_lines_whitespaces = [line.replace('\t', ' ' * NUM_WHITESPACE_FOR_TAB) for line in file_lines]

        # The line after the section starts with " "*n + "{"  and the section ends with " "*n + "}"
        # We assume that there are only whitespace characters after the opening/ending brace
        # Check that the pattern matches the expected format
        line_after_start_line = file_lines_whitespaces[start_index + 1]
        if not line_after_start_line.strip() == '{':
            raise ValueError("Section start line does not match expected pattern (' '*n + '{')")
        
        # Create the expected closing line by replacing '{' with '}'
        end_line = line_after_start_line.replace('{', '}').rstrip()
        
        # Search for the matching closing brace with same indentation
        for line_number in range(start_index + 1, len(file_lines)):
            if file_lines[line_number].rstrip() == end_line:
                return line_number + 1
        
        raise ValueError("Section end not found")
    
    def remove_leading_whitespace_preserve_indentation(self, text: str) -> str:
        """Remove leading whitespace from all lines while preserving relative indentation."""
        lines = text.split('\n')
        lines = [line.replace('\t', ' ' * NUM_WHITESPACE_FOR_TAB) for line in lines]
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
        content = self.remove_leading_whitespace_preserve_indentation(content)
        return format_cpp_code_as_markdown(content)

    def __str__(self) -> str:
        # this is used as a title in the trudag report
        return f"cpp-test: [{self._name}]\n({self._path})"


class JSONTestsuiteReference(CPPTestReference):
    """
    Represents a reference to one or more JSON testsuite files, where the CPP test 
    structure is assumed to be as in tests/src/unit-testsuites.cpp and the JSON testsuite 
    files are assumed to be hosted in the nlohmann/json_test_data repository on github. 
    
    The referenced JSON files are displayed (using the as_markdown function) as well as 
    the relevant part of the C++ test section that uses them. Both the C++ test file and 
    the JSON files are included in the content property that is used for hashing.
    """

    def __init__(self, name: str, path, test_suite_paths: str, description: str, remove_other_test_data_lines: bool = True) -> None:
        """
        Initialize JSONTestsuiteReference.
        
        Args:
            name: Section name in the C++ test file, use colon-separated for nested sections
            path: Relative path from project root to the C++ test file
            test_suite_paths: List of relative paths to JSON test files in the nlohmann test data repository
            description: Human-readable description of what this test suite covers
            remove_other_test_data_lines: If True, removes lines from the markdown (not the content used for hashing) that include 'TEST_DATA_DIRECTORY' and '.json"'

        Raises:
            ValueError: If test_suite_paths is not a list of strings
        """
        super().__init__(name, path)
        self._path = Path(path)
        if not isinstance(test_suite_paths, list):
            raise ValueError(f"test_suite_paths must be a list of strings: {test_suite_paths}")
        
        self._description = description
        self._test_suite_paths = test_suite_paths
        self.check_testsuite_file_is_used_by_cpp_test()
        self._remove_other_test_data_lines = remove_other_test_data_lines
        self._loaded_json_cache = {}
    
    @property
    def _loaded_json_map(self) -> dict[str, str]:
        """Lazy-load JSON content for all test suite paths."""
        for path in self._test_suite_paths:
            if path not in self._loaded_json_cache:
                self._loaded_json_cache[path] = self.get_testsuite_content(path)
        return self._loaded_json_cache

    def check_testsuite_file_is_used_by_cpp_test(self) -> None:
        """Check if the C++ test file uses the JSON testsuite files."""
        cpp_test_content = self.get_section()
        for test_suite_path in self._test_suite_paths:
            if test_suite_path not in cpp_test_content:
                raise ValueError(f"JSON testsuite {test_suite_path} is not used in the C++ test file {self._path}")

    @classmethod
    def type(cls) -> str:
        return "JSON_testsuite"

    def get_testsuite_content(self, test_suite_path: str) -> str:
        url = TEST_DATA_REPO_URL + str(test_suite_path)
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            raise ValueError(f"Failed to fetch testsuite content from {url}: {e}")
    
    @property
    def content(self) -> bytes:
        all_json_content = "\n".join(self._loaded_json_map.values())
        content = self.get_section() + "\n" + all_json_content
        return content.encode('utf-8')
    
    @staticmethod
    def is_json_test_line(line: str) -> bool:
        return 'TEST_DATA_DIRECTORY' in line and '.json"' in line
    
    def filter_other_test_data_lines(self, text: str) -> str:
        """Remove lines that only contain other test data references."""
        lines = text.split('\n')
        filtered_lines = []
        
        for line in lines:
            if any(test_suite_path in line for test_suite_path in self._test_suite_paths) or not self.is_json_test_line(line):
                filtered_lines.append(line)

        if len(filtered_lines) < len(lines):
            filtered_lines.append('\n // Note: Other test data lines have been filtered out for conciseness.') 
        
        return '\n'.join(filtered_lines)

    def get_single_json_as_markdown(self, test_suite_path: str) -> str:
        num_json_lines = len(self._loaded_json_map[test_suite_path].split('\n'))
        if num_json_lines > MAX_JSON_LINES_FOR_DISPLAY:
            link_to_file = TEST_DATA_REPO_URL + str(test_suite_path)
            json_for_display = f"[Link to file]({link_to_file}) [Content too large - {num_json_lines} lines]\n\n"
        else:
            json_for_display = format_json_as_markdown(self._loaded_json_map[test_suite_path])

        markdown_bullet_point = make_md_bullet_point(f"JSON Testsuite: {test_suite_path}")
        return f"{markdown_bullet_point}\n\n {json_for_display}\n\n"
        
    def get_all_json_as_markdown(self) -> str:
        """Get all JSON test files as markdown."""
        return "\n\n".join(
            self.get_single_json_as_markdown(test_suite_path) for test_suite_path in self._test_suite_paths
        )

    def as_markdown(self, filepath: None | str = None) -> str:
        description = ""
        if self._description!="": 
            description = "Description: {self._description}\n\n"

        # we can not simply use the parent class's as_markdown method, because it does not filter out
        # the other test data lines, which are not relevant for the trudag report
        cpp_test_content = self.remove_leading_whitespace_preserve_indentation(self.get_section())
        if self._remove_other_test_data_lines:
            cpp_test_content = self.filter_other_test_data_lines(cpp_test_content)
        cpp_test_content = format_cpp_code_as_markdown(cpp_test_content)

        cpp_test_title = super().__str__() + '\n\n'

        markdown_content = (
            make_md_bullet_point(description) + 
            self.get_all_json_as_markdown() + 
            make_md_bullet_point(cpp_test_title) + 
            cpp_test_content
        )
        # the markdown content is indented by one level to fit into the report markdown structure
        return add_indentation(markdown_content, 1)

    def __str__(self) -> str:
        # this is used as a title in the trudag report
        return f"cpp-testsuite: [{', '.join(self._test_suite_paths)}]"
    
class WebReference(BaseReference):
    """
    Represents a reference to a website. 
    This custom reference type is included as an example on https://codethinklabs.gitlab.io/trustable/trustable/trudag/references.html
    and, for the most part, copied from there
    """
    def __init__(self, url: str, description: str = "") -> None:
        self._url = url
        self._description = description
    
    @classmethod
    def type(cls) -> str:
        return "website"
    
    @property
    def content(self) -> bytes:
        # In the example, the text on the website is used.
        # This does not work for constantly changing websites.
        # Would the text be used, then the statement could never be reviewed.
        # Therefore, the url is returned, which is sufficient for our purposes.
        return self._url.encode('utf-8')
    
    def as_markdown(self, filepath: None | str = None) -> str:
        # If we did not add a description, nothing is printed
        if (self._description == ""):
            return f"`{self._url}`"
        # else, we print the description below the url
        return f"`{self._url}`\n"+make_md_bullet_point(self._description,1)    
    
    def __str__(self) -> str:
        # this is used as a title in the trudag report
        return f"website: {self._url}"
    
class WebContentReference(WebReference):
    def __init__(self, url, description = ""):
        super().__init__(url, description)
    
    @classmethod
    def type(cls):
        return "web_content"

    @property
    def content(self) -> bytes:
        return requests.get(self._url).text.encode('utf-8')
    
    def as_markdown(self, filepath: None | str = None) -> str:
        return super().as_markdown(filepath)
    
    def __str__(self) -> str:
        return super().__str__

class TimeVaryingWebReference(WebReference):
    def __init__(self, url, description = "", changelog = "ChangeLog.md"):
        super().__init__(url, description)
        self._changelog = changelog
    
    @classmethod
    def type(cls) -> str:
        return "project_website"

    @property
    def content(self) -> bytes:    
        with open(self._changelog, 'r') as file:
            lines = file.readlines()
        lines.insert(0,self._url)
        return '\n'.join(lines)
    
    def as_markdown(self, filepath: None | str = None) -> str:
        return super().as_markdown(filepath)
    
    def __str__(self) -> str:
        return super().__str__()
    
class FunctionReference(SourceSpanReference):
    """
    Represents a reference to a function within a class in a hpp-file. This class assumes that
    the hpp-file has the form 
    ...
    class xyz
    {
        ...
        output function_name(input)
        {
            ...
        }
        ...
    };
    This is the layout that is followed by the hpp-files of nlohmann/json.

    A specific function is identified by 
        1. the hpp-file
        2. the name of the class, whithin which our function is defined
        3. (optionally) the number of prior definitions within the same class in case of overloaded functions;
            by default, the first definition is used.
    Since classes are in hpp-files of nlohmann/json uniquely identified by their name, this uniquely identifies a function.
    """

    def __init__(self, name: str, path: str, overload: str = "1") -> None:
        [start_line,end_line] = FunctionReference.get_function_line_numbers(Path(path),name,int(overload))
        # SourceSpanReference copies code from a start-character in a start-line 
        # up to an end-character in an end-line.
        # Here, we want every character in all lines between start- and end-line.
        # Therefore, we set the end-character to 1000, which could fail, if ever a
        # line with more than 1000 characters is copied.
        # In nlohmann/json, no hpp-file has such a line, so that the following works fine.
        super().__init__(Path(path),[[start_line,0],[end_line,1000]])
        self._name = name
        self._overload = int(overload)

    def language(self):
        return "C++" 
    
    @classmethod
    def type(cls) -> str:
        return "function_reference"
    
    def remove_leading_whitespace_preserve_indentation(self, text: str) -> str:
        """
        Remove leading whitespace from all lines while preserving relative indentation.
        This is identical to CPPTestReference.remove_leading_whitespace_preserve_indentation
        """
        lines = text.split('\n')
        lines = [line.replace('\t', ' ' * NUM_WHITESPACE_FOR_TAB) for line in lines]
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
    
    @staticmethod
    def get_function_line_numbers(path: Path, name: str, overload = 1) -> tuple[int, int]:
        with open(path, 'r') as file:
            lines = file.readlines()
        function_start_line = FunctionReference.get_function_start(path, name, lines, overload)
        function_end_line = FunctionReference.get_function_end(path, name, function_start_line, lines)
        return (function_start_line, function_end_line)
        

    def get_function_start(path: Path, name: str, lines: list[str], overload: int) -> int:
        # Split name in class_name and function_name, 
        # and check that both, and only both, parts of the name are found.
        name_parts = name.split("::")
        if len(name_parts) != 2:
            raise ValueError(f"Name {name} does not have the form class_name::function_name")
        # name_parts[0] is interpreted as class_name, 
        # name_parts[1] is interpreted as function_name
        in_class = False
        sections = []
        instance = 0
        amopen = []
        for line_number, line in enumerate(lines):
            # first task: find literal string "class class_name " within a line
            if not in_class:
                if f"class {name_parts[0]} " in line or f"class {name_parts[0]}\n" in line:
                    in_class = True
                    continue
                continue
            # now we are within the class
            # time to search for our function
            if "};" in line and len(sections)==0:
                # then, we have reached the end of the class
                break
            # ignore all commented out lines
            if line.strip().startswith("//"):
                continue
            if '{' in line or '}' in line:
                for c in line:
                    if c == '{':
                        sections.append(1)
                    if c == '}':
                        try:
                            sections.pop()
                        except IndexError:
                            raise ValueError(f"Fatal error: Could not resolve {name} in file {path}.")
            # A function-declaration always contains the literal string " function_name("
            # When this string is found within the indentation of the class itself,
            # then it can be assumed that we have a function declaration.
            # This is true in case of the hpp-files of nlohmann/json. 
            if f" {name_parts[1]}(" in line and len(sections) == 1:
                instance += 1
                if instance == overload:
                    return line_number
        if not in_class:
            raise ValueError(f"Could not find class {name_parts[0]} in file {path}")
        if overload%10 == 1 and overload != 11:
            raise ValueError(f"Could not locate {overload}st implementation of {name_parts[1]} in file {path}.")
        elif overload%10 == 2 and overload != 12:
            raise ValueError(f"Could not locate {overload}nd implementation of {name} in file {path}.")
        elif overload%10 == 3 and overload != 13:
            raise ValueError(f"Could not locate {overload}rd implementation of {name} in file {path}.")
        else:
            raise ValueError(f"Could not locate {overload}th implementation of {name} in file {path}.")
    
    def get_function_end(path: Path, name: str, function_start: int, lines: list[str]) -> int:
        found_start = False
        sections = []
        for line_number, line in enumerate(lines):
            if line_number<function_start:
                # skip ahead
                continue
            # Now, we have found the line, where the function declaration
            # In nlohmann/json, the function body is written between a lonely { and a lonely }.
            # First, we should search for the first lonely {
            if '{' in line or '}' in line:
                for c in line:
                    if c == '{':
                        sections.append(1)
                    if c == '}':
                        try:
                            sections.pop()
                        except IndexError:
                            raise ValueError(f"Fatal error: Could not resolve {name} in file {path}.")
            if not found_start and len(sections)>0:
                found_start = True
            if found_start and len(sections)==0:
                return line_number
        raise ValueError(f"Could not find end of function-body of {name} in file {path}.")

    @property
    def content(self) -> bytes:
        # I don't think this needs to be further encoded, since it is encoded by super()
        return self.code
  

    def as_markdown(self, filepath: None | str = None) -> str:
        content = self.code.decode('utf-8')
        content = self.remove_leading_whitespace_preserve_indentation(content)
        return format_cpp_code_as_markdown(content)

    def __str__(self) -> str:
        # this is used as a title in the trudag report
        return f"function: [{self._name}]\n({str(self.path)})"
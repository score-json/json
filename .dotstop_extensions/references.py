from pathlib import Path
from trudag.dotstop.core.reference.references import BaseReference
from trudag.dotstop.core.reference.references import SourceSpanReference
import requests
import sqlite3
import re

# Constants
MAX_JSON_LINES_FOR_DISPLAY = 25
TEST_DATA_REPO_URL = "https://raw.githubusercontent.com/eclipse-score/inc_nlohmann_json/refs/heads/json_test_data_version_3_1_0_mirror/"
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
            description = f"Description: {self._description}\n\n"

        # we can not simply use the parent class's as_markdown method, because it does not filter out
        # the other test data lines, which are not relevant for the trudag report
        cpp_test_content = self.remove_leading_whitespace_preserve_indentation(self.get_section())
        if self._remove_other_test_data_lines:
            cpp_test_content = self.filter_other_test_data_lines(cpp_test_content)
        cpp_test_content = format_cpp_code_as_markdown(cpp_test_content)

        cpp_test_title = super().__str__() + '\n\n'

        markdown_content = (
            self.get_all_json_as_markdown() + 
            make_md_bullet_point(cpp_test_title) + 
            cpp_test_content
        )
        if description != "":
            markdown_content = make_md_bullet_point(description) + markdown_content
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
    def __init__(self, url: str, description: str = "") -> None:
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
        return super().__str__()

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
        return '\n'.join(lines).encode('utf-8')
    
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

    def __init__(self, name: str, path: str, description: str = "", overload: str = "1") -> None:
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
        self._description = description

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
        return FunctionReference.get_function_boundaries(path, name, lines, overload)
        

    def get_function_boundaries(path: Path, name: str, lines: list[str], overload: int) -> list[int]:
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
        start_line = 0
        found_start = False
        in_body = False
        for line_number, line in enumerate(lines):
            # first task: find literal string "class class_name " within a line
            if not in_class:
                if f"class {name_parts[0]} " in line or f"class {name_parts[0]}\n" in line:
                    in_class = True
                continue
            # now we are within the class
            # time to search for our function
            # ignore all commented out lines
            if line.strip().startswith("//"):
                continue
            if "};" in line and len(sections)==0:
                # then, we have reached the end of the class
                break
            if not found_start:
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
                        start_line = line_number
                        found_start = True
                        sections.pop()
            else:
                if '{' in line or '}' in line:
                    for c in line:
                        if c == '{':
                            sections.append(1)
                        if c == '}':
                            try:
                                sections.pop()
                            except IndexError:
                                raise ValueError(f"Fatal error: Could not resolve {name} in file {path}.")
                if not in_body and len(sections)>0:
                    in_body = True
                if in_body and len(sections)==0:
                    return [start_line,line_number]
        if not in_class:
            raise ValueError(f"Could not find class {name_parts[0]} in file {path}")
        if not found_start and overload%10 == 1 and overload%100 != 11:
            raise ValueError(f"Could not locate {overload}st implementation of {name_parts[1]} in file {path}.")
        elif not found_start and overload%10 == 2 and overload%100 != 12:
            raise ValueError(f"Could not locate {overload}nd implementation of {name} in file {path}.")
        elif not found_start and overload%10 == 3 and overload%100 != 13:
            raise ValueError(f"Could not locate {overload}rd implementation of {name} in file {path}.")
        elif not found_start:
            raise ValueError(f"Could not locate {overload}th implementation of {name} in file {path}.")
        else:
            raise ValueError(f"Could not find end of function-body of {name} in file {path}.")

    @property
    def content(self) -> bytes:
        # I don't think this needs to be further encoded, since it is encoded by super()
        return self.code
  

    def as_markdown(self, filepath: None | str = None) -> str:
        content = self.code.decode('utf-8')
        content = self.remove_leading_whitespace_preserve_indentation(content)
        content = format_cpp_code_as_markdown(content)
        if self._description != "":
            content = make_md_bullet_point(f"Description: {self._description}",1) + "\n\n" + add_indentation(content,1)
        return content

    def __str__(self) -> str:
        # this is used as a title in the trudag report
        return f"function: [{self._name}]\n({str(self.path)})"
    
class ListOfTestCases(BaseReference):

    def __init__(self, test_files: list[str], recent_result_database: str = "artifacts/MemoryEfficientTestResults.db", recent_result_table: str = "test_results") -> None:
        self._test_files = test_files
        self._database = recent_result_database
        self._table =  recent_result_table

    @staticmethod    
    def compile_string(items: list[str]) -> str:
        # input: list of strings representing the structure of TEST_CASE, SECTION etc.,
        # e.g. items = ["lexer class", "scan", "literal names"]
        # output: the last item of the list, representing the most recent SECTION,
        # indented as in the source code 
        # throws error if input is empty
        if len(items) == 0:
            raise RuntimeError("Received empty structural list; nonempty list expected.")
        result = ""
        for _ in range(1, len(items)):
            result += "    "
        if items:
            result += "* " + items[-1]
        return result

    @staticmethod    
    def extract_quotation(s: str) -> str:
        # input: string containing at least one quoted substring, e.g. s = "my \"input\""
        # output: the first quoted substring of the input
        # throws error if no quoted substring can be found.
        first = s.find('"')
        if first == -1:
            raise RuntimeError("Expected quotation mark; none were detected.")
        second = s.find('"', first + 1)
        if second == -1:
            raise RuntimeError("Expected quotation marks; only one was detected.")
        return s[first + 1 : second]
    
    @staticmethod
    def remove_and_count_indent(s: str) -> tuple[int, str]:
        # input: string with possibly leading whitespace (space of horizontal tab)
        # output: the number of leading spaces and the string with leading whitespace removed;
        # tab counted as four spaces
        cnt = 0
        i = 0
        n = len(s)
        while i < n and (s[i] == " " or s[i] == "\t"):
            if s[i] == " ":
                cnt += 1
            elif s[i] == "\t":
                cnt += 4
            i += 1
        return (cnt, s[i:])

    @staticmethod
    def head_of_list() -> str:
        return """## List of all unit-tests with test environments

This list contains all unit-tests possibly running in this project.
These tests are compiled from the source-code, where the individual unit-tests are arranged in TEST_CASEs containing possibly nested SECTIONs.
To reflect the structure of the nested sections, nested lists are utilised, where the top-level list represents the list of TEST_CASEs. 

It should be noted that not all unit-tests in a test-file are executed with every compiler-configuration.
"""
    
    @staticmethod
    def transform_test_file_to_test_name(test_file: str) -> str:
        return "test-"+"-".join((test_file.split('.')[0]).split('-')[1:])

    @classmethod
    def type(cls) -> str:
        return "list_of_test_cases"

    def extract_test_structure(self, file_path: Path) -> str:
        # input: path to a file potentially containing unit-tests
        # output: the extracted arrangement of TEST_CASE and SECTION
        # in the form of nested markdown lists

        indent = 0 # the indent of the currently read line
        current_indent = 0 # the indent of the last TEST_CASE or SECTION
        current_path = [] # the current path
        lines_out = [] # the collection of lines to be outputted

        # open file_path as read-only, and process line by line
        with file_path.open("r", encoding="utf-8", errors="replace") as source:
            for line in source:
                # count and remove leading whitespace
                indent, trimmed = self.remove_and_count_indent(str(line))
                
                # check whether we have found a TEST_CASE
                if trimmed.startswith("TEST_CASE(") or trimmed.startswith("TEST_CASE_TEMPLATE(") or trimmed.startswith("TEST_CASE_TEMPLATE_DEFINE("):
                    # remember the current indent
                    current_indent = indent
                    # TEST_CASE is always the head of a new arrangement-structure
                    # remove stored structure
                    current_path.clear()
                    # extract name of TEST_CASE and append path
                    current_path.append(self.extract_quotation(trimmed))
                    lines_out.append(self.compile_string(current_path))
                
                # check whether we have found a SECTION
                if trimmed.startswith("SECTION("):
                    # update path to reflect arrangement of current section
                    while indent <= current_indent and current_path:
                        current_path.pop()
                        current_indent -= 4
                    # remember the current indent
                    current_indent = indent
                    # extract name of SECTION and append path
                    current_path.append(self.extract_quotation(trimmed))
                    lines_out.append(self.compile_string(current_path))

        # process extracted lines
        return ("\n".join(lines_out) + "\n") if lines_out else ""

    def extract_recent_test_environments(self) -> dict:
        fetched_data = dict()
        try:    
            # initialise connection to test result database
            connector = sqlite3.connect(self._database)
            cursor = connector.cursor()
            # verify that the expected table does exist
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name = ?;",(self._table,))
            if cursor.fetchone() is None: 
                raise RuntimeError(f"Fatal Error: Could not find table {self._table} in database {self._database}.")
        except sqlite3.Error as e:
            raise RuntimeError(f"Fatal Error accessing database {self._database}: {e}")
        # get all test-files from recent test executions
        command = f"SELECT name FROM {self._table};"
        cursor.execute(command)
        raw_cases = cursor.fetchall()
        cases = set([raw_case[0] for raw_case in raw_cases])
        # for each test-file
        for case in cases:
            case_data = dict()
            # get the test-environments
            command = f"SELECT compiler, cpp_standard FROM {self._table} WHERE name = ? and skipped_cases == 0"
            cursor.execute(command,(case,))
            results = cursor.fetchall()
            case_data["noskip"] = [{"compiler":result[0], "standard":result[1]} for result in results]
            # some test-cases are skipped with certain environments
            # It is unclear from the log, which cases are skipped;
            # we leave this to the interested reader
            command = f"SELECT compiler, cpp_standard, skipped_cases FROM {self._table} WHERE name = ? and skipped_cases != 0"
            cursor.execute(command, (case,))
            results = cursor.fetchall()
            case_data["skip"] = [{"compiler": result[0], "standard": result[1], "skipped": result[2]} for result in results]
            fetched_data[case] = case_data
        return fetched_data

    def fetch_all_test_data(self, input: list[str]):
        # inputs: path(s) to directory potentially containing some test-data
        extracted_test_data = []
        recent_test_data = self.extract_recent_test_environments()
        for arg in input:
            p = Path(arg)
            if p.is_file() and p.suffix == ".cpp" and p.name.startswith("unit-"):
                extracted_test_data.append((p.name,self.extract_test_structure(p)))
            elif p.is_dir():
                for entry in p.rglob("*"):
                    if entry.is_file() and entry.suffix == ".cpp" and entry.name.startswith("unit-"):
                        extracted_test_data.append((entry.name,self.extract_test_structure(entry)))
        extracted_test_data.sort(key= lambda x: x[0])
        result = self.head_of_list()
        for test_file, list_of_tests in extracted_test_data:
            result += f"\n\n### List of tests in file {test_file}\n\n"
            result += list_of_tests
            result += "\n\n"
            if recent_test_data.get(self.transform_test_file_to_test_name(test_file), None) is None:
                result += "Unfortunately, none of the following tests seems to have been executed. Very strange indeed!\n\n"
            else:
                if recent_test_data.get(self.transform_test_file_to_test_name(test_file)).get("noskip",None) is not None:
                    if len(recent_test_data.get(self.transform_test_file_to_test_name(test_file)).get("noskip")) != 0:
                        result  += "\nAll tests in this file were run in the following configurations:\n\n"
                        for datum in recent_test_data.get(self.transform_test_file_to_test_name(test_file)).get("noskip"):
                            result += "* "
                            result += datum.get("compiler",None)
                            result += " with standard "
                            result += datum.get("standard",None)
                            result += "\n"
                if recent_test_data.get(self.transform_test_file_to_test_name(test_file)).get("skip",None) is not None:
                    if len(recent_test_data.get(self.transform_test_file_to_test_name(test_file)).get("skip")) != 0:
                        result += "\nIn the following configuration, however, some test-cases were skipped:\n\n"
                        for datum in recent_test_data.get(self.transform_test_file_to_test_name(test_file)).get("skip"):
                            result += "* "
                            how_many = datum.get("skipped",None)
                            result += str(how_many)
                            if how_many == 1:
                                result += " test case was skipped when using "
                            else:
                                result += " test cases were skipped when using "
                            result += datum.get("compiler",None)
                            result += " with standard "
                            result += datum.get("standard",None)
                            result += "\n"
        return result
    
    @property
    def content(self) -> bytes:
        # encoding is necessary since content will be hashed
        return self.fetch_all_test_data(self._test_files).encode('utf-8')
    
    def as_markdown(self, filepath: None | str = None) -> str:
        return self.content.decode('utf-8')

    def __str__(self) -> str:
        # this is used as a title in the trudag report
        return "List of all unit-tests"

from trudag.dotstop.core.reference.references import LocalFileReference as LFR    

class VerboseFileReference(LFR):
    def __init__(self, path: str, description: str = "", **kwargs) -> None:
        self._path = Path(path)
        self._description = description
   
    @classmethod
    def type(cls) -> str:
        return "verbose_file"
 
    @property    
    def content(self) -> bytes:
        if not self._path.is_file():
            raise ReferenceError(
                f"Cannot get non-existent or non-regular file {self._path}"
            )
        with self._path.open("rb") as reference_content:
            return reference_content.read()
       
    def as_markdown(self, filepath: None | str = None) -> str:
        result = super().as_markdown()
        if self._description != "":
            result += make_md_bullet_point(f"Description: {self._description}\n\n")
        return result
   
    def __str__(self) -> str:
        return str(self._path)  

class Checklist(LFR):
    def __init__(self, path: str, **kwargs) -> None:
        self._path = Path(path)
   
    @classmethod
    def type(cls) -> str:
        return "checklist"
 
    @property    
    def content(self) -> bytes:
        if not self._path.is_file():
            raise ReferenceError(
                f"Cannot get non-existent or non-regular file {self._path}"
            )
        with self._path.open("rb") as reference_content:
            return reference_content.read()
       
    def as_markdown(self, filepath: None | str = None) -> str:
        return self.content.decode('utf-8')
   
    def __str__(self) -> str:
        return str(self._path)  

del LFR

class NumberOfFailures(BaseReference):
    def __init__(self, owner: str, repo: str, branch: str | None = None) -> None:
        self._owner = owner
        self._repo = repo
        self._branch = branch
    
    @classmethod
    def type(cls) -> str:
        return "workflow_failures"
    
    @property
    def content(self) -> bytes:
        # build the url
        url = f"https://github.com/{self._owner}/{self._repo}/actions?query=is%3Afailure"
        if self._branch is not None:
            url += "+branch%3A{self._branch}"
        # ask the website
        res = requests.get(url)
        # if call is not successful, raise an error
        if res.status_code != 200:
            candidate = f"The url {url} is not reachable, so that the number of failed workflows can not be fetched!"
            raise RuntimeError(candidate)
        # otherwise fetch the number printed in the head of the table
        m = re.search(r'(\d+)\s+workflow run results', res.text, flags=re.I)
        if m is None:
            candidate = f"The number of failed workflows can not be found, please check that the table head contains \"XX workflow run results\"!"
            raise RuntimeError(candidate)
        return m.group(1).encode('utf-8')
    
    def as_markdown(self, filepath: None | str = None) -> str:
        if self._branch is not None:
            return f"{self.content.decode('utf-8')} workflows failed on {self._owner}/{self._repo}"
        else:
            return f"{self.content.decode('utf-8')} workflows failed on branch {self._branch} of {self._owner}/{self._repo}"
    
    def __str__(self) -> str:
        # this is used as a title in the trudag report
        if self._branch is not None:
            result = f"failures on branch {self._branch} of {self._owner}/{self._repo}"
        else:
            result = f"failures on {self._owner}/{self._repo}"
        return result
    
class ItemReference(BaseReference):
    def __init__(self, items: list[str]) -> None:
        if len(items) == 0:
            raise RuntimeError("Error: Can't initialise empty ItemReference.")
        self._items = items
    
    @classmethod
    def type(cls) -> str:
        return "item"
    
    @staticmethod
    def get_markdown_link(item: str) -> str:
        first_part = item.split("-")[0]
        return f"see [here]({first_part}.md#{item.lower()}) to find {item}"
    
    @staticmethod
    def get_reference_contents(items: list[str]) -> bytes:
        lines = open(".dotstop.dot","r").read().split("\n")
        contents = []
        for item in items:
            # check whether the item is valid
            content = [line for line in lines if line.startswith(f"\"{item}\" [")]
            if len(content) != 1:
                raise RuntimeError(f"Error: The item {item} is not contained in the trustable graph")
            contents.append(content[0].encode("utf-8"))
        return b"".join(contents) if len(contents)!=0 else b"No external references"

    @property
    def content(self) -> bytes:
        return ItemReference.get_reference_contents(self._items)
    
    def as_markdown(self, filepath: None | str = None) -> str:
        result = ""
        for item in self._items:
            result += make_md_bullet_point(ItemReference.get_markdown_link(item),1)
        return result
    
    def __str__(self):
        title = "this item also refers to the references of "
        if len(self._items) == 1:
            title += "item "
        else:
            title += "items "
        title += ", ".join(self._items)
        return title

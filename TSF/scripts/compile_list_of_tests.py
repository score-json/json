import sys
from pathlib import Path

# This is a script to compile a list of all unit-tests out of a given source.
# It is assumed that every file containing unit-tests is called unit-xxx.cpp,
# and that, within these files, the test are arranged as
#
# TEST_CASE("my test-case")
# { 
#   ...
#   SECTION("my section within my test-case")
#   {
#       ...
#   } 
# }
# The aim of this program is to compile a list, which reflects the arrangement
# as nesting of lists.

FILE_OF_TEST_DATA = "TSF/List_of_all_tests.md"
DIRECTORY_OF_NLOHMANN_TESTS = "tests/src"
DIRECTORY_OF_TSF_CUSTOM_TESTS = "TSF/tests"

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


def extract_test_structure(file_path: Path) -> str:
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
            indent, trimmed = remove_and_count_indent(line)

            # check whether we have found a TEST_CASE
            if trimmed.startswith("TEST_CASE(") or trimmed.startswith("TEST_CASE_TEMPLATE(") or trimmed.startswith("TEST_CASE_TEMPLATE_DEFINE("):
                # remember the current indent
                current_indent = indent
                # TEST_CASE is always the head of a new arrangement-structure
                # remove stored structure
                current_path.clear()
                # extract name of TEST_CASE and append path
                current_path.append(extract_quotation(trimmed))
                lines_out.append(compile_string(current_path))
            
            # check whether we have found a SECTION
            if trimmed.startswith("SECTION("):
                # update path to reflect arrangement of current section
                while indent <= current_indent and current_path:
                    current_path.pop()
                    current_indent -= 4
                # remember the current indent
                current_indent = indent
                # extract name of SECTION and append path
                current_path.append(extract_quotation(trimmed))
                lines_out.append(compile_string(current_path))

    # process extracted lines
    return ("\n".join(lines_out) + "\n") if lines_out else ""


def head_of_list() -> str:
    return """# List of all unit-tests

This file contains the list of all unit-tests possibly running in this project.
These tests are compiled from the source-code, where the individual unit-tests are arranged in TEST_CASEs containing possibly nested SECTIONs.
To reflect the structure of the nested sections, nested lists are utilised, where the top-level list represents the list of TEST_CASEs. 

It should be noted that not all unit-tests in a test-file are executed with every compiler-configuration.
"""

def main(input: list[str]):
    # inputs: path to file, and path(s) to directory potentially containing some test-data
    target_path = input[0]
    args = input[1:]
    extracted_test_data = []
    for arg in args:
        p = Path(arg)
        if p.is_file() and p.suffix == ".cpp" and p.name.startswith("unit-"):
            extracted_test_data.append((p.name,extract_test_structure(p)))
        elif p.is_dir():
            for entry in p.rglob("*"):
                if entry.is_file() and entry.suffix == ".cpp" and entry.name.startswith("unit-"):
                    extracted_test_data.append((entry.name,extract_test_structure(entry)))
    extracted_test_data.sort(key= lambda x: x[0])
    try: 
        with open(target_path, "w", encoding="utf-8") as target:
            target.write(head_of_list())
            for test_file, list_of_tests in extracted_test_data:
                target.write(f"\n\n# List of tests in file {test_file}\n\n")
                target.write(list_of_tests)
    except:
        raise RuntimeError(f"Critical Error: unable to open target file {target_path}.")

    return 0


if __name__ == "__main__":
    sys.exit(main([FILE_OF_TEST_DATA, DIRECTORY_OF_NLOHMANN_TESTS, DIRECTORY_OF_TSF_CUSTOM_TESTS]))
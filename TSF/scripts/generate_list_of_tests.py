from pathlib import Path
import sqlite3

class ListOfTestsGenerator:

    def __init__(self):
        self._database = "./artifacts/MemoryEfficientTestResults.db"
        self._table = "test_results"
        self._test_files = ["./tests/src", "./TSF/tests"]
    
    def set_database(self,db:str):
        self._database = db
        
    def set_table(self,table:str):
        self._table = table
        
    def set_sources(self,sources:list):
        self._test_files = sources

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
    def transform_test_file_to_test_name(test_file: str) -> str:
        return "test-"+"-".join((test_file.split('.')[0]).split('-')[1:])

    @staticmethod
    def head_of_list() -> str:
        return """## List of all unit-tests with test environments

    This list contains all unit-tests possibly running in this project.
    These tests are compiled from the source-code, where the individual unit-tests are arranged in TEST_CASEs containing possibly nested SECTIONs.
    To reflect the structure of the nested sections, nested lists are utilised, where the top-level list represents the list of TEST_CASEs. 

    It should be noted that not all unit-tests in a test-file are executed with every compiler-configuration.
    """

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
                indent, trimmed = ListOfTestsGenerator.remove_and_count_indent(str(line))
                
                # check whether we have found a TEST_CASE
                if trimmed.startswith("TEST_CASE(") or trimmed.startswith("TEST_CASE_TEMPLATE(") or trimmed.startswith("TEST_CASE_TEMPLATE_DEFINE("):
                    # remember the current indent
                    current_indent = indent
                    # TEST_CASE is always the head of a new arrangement-structure
                    # remove stored structure
                    current_path.clear()
                    # extract name of TEST_CASE and append path
                    current_path.append(ListOfTestsGenerator.extract_quotation(trimmed))
                    lines_out.append(ListOfTestsGenerator.compile_string(current_path))
                
                # check whether we have found a SECTION
                if trimmed.startswith("SECTION("):
                    # update path to reflect arrangement of current section
                    while indent <= current_indent and current_path:
                        current_path.pop()
                        current_indent -= 4
                    # remember the current indent
                    current_indent = indent
                    # extract name of SECTION and append path
                    current_path.append(ListOfTestsGenerator.extract_quotation(trimmed))
                    lines_out.append(ListOfTestsGenerator.compile_string(current_path))

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

    def fetch_all_test_data(self):
        # inputs: path(s) to directory potentially containing some test-data
        extracted_test_data = []
        recent_test_data = self.extract_recent_test_environments()
        for arg in self._test_files:
            p = Path(arg)
            if p.is_file() and p.suffix == ".cpp" and p.name.startswith("unit-"):
                extracted_test_data.append((p.name,ListOfTestsGenerator.extract_test_structure(p)))
            elif p.is_dir():
                for entry in p.rglob("*"):
                    if entry.is_file() and entry.suffix == ".cpp" and entry.name.startswith("unit-"):
                        extracted_test_data.append((entry.name,ListOfTestsGenerator.extract_test_structure(entry)))
        extracted_test_data.sort(key= lambda x: x[0])
        result = ListOfTestsGenerator.head_of_list()
        for test_file, list_of_tests in extracted_test_data:
            result += f"\n\n### List of tests in file {test_file}\n\n"
            result += list_of_tests
            result += "\n\n"
            if recent_test_data.get(ListOfTestsGenerator.transform_test_file_to_test_name(test_file), None) is None:
                result += "Unfortunately, none of the following tests seems to have been executed. Very strange indeed!\n\n"
            else:
                if recent_test_data.get(ListOfTestsGenerator.transform_test_file_to_test_name(test_file)).get("noskip",None) is not None:
                    if len(recent_test_data.get(ListOfTestsGenerator.transform_test_file_to_test_name(test_file)).get("noskip")) != 0:
                        result  += "\nAll tests in this file were run in the following configurations:\n\n"
                        for datum in recent_test_data.get(ListOfTestsGenerator.transform_test_file_to_test_name(test_file)).get("noskip"):
                            result += "* "
                            result += datum.get("compiler",None)
                            result += " with standard "
                            result += datum.get("standard",None)
                            result += "\n"
                if recent_test_data.get(ListOfTestsGenerator.transform_test_file_to_test_name(test_file)).get("skip",None) is not None:
                    if len(recent_test_data.get(ListOfTestsGenerator.transform_test_file_to_test_name(test_file)).get("skip")) != 0:
                        result += "\nIn the following configuration, however, some test-cases were skipped:\n\n"
                        for datum in recent_test_data.get(ListOfTestsGenerator.transform_test_file_to_test_name(test_file)).get("skip"):
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
    
if __name__ == "__main__":
    generator = ListOfTestsGenerator()
    with open("./TSF/docs/list_of_test_environments.md",'w') as f:
        print(generator.fetch_all_test_data(),file=f)
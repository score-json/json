import os
import re
import sys

# The trudag report is not in standard markdown format, so we need to clean it up.
# This script will remove specific patterns from the markdown files in the current directory and its subdirectories
# It requires 1 command line argument which is the root folder we want to be processed

# List of regex patterns to remove only the matched part, not the whole line
replace_by_empty_string_patterns = [
    r"\{class[:=][^}]*\}",           # {class:...} or {class=...} with any attributes inside
    r"\{\%[\s]*raw[\s]*\%\}",        # {% raw %}
    r"\{\%[\s]*endraw[\s]*\%\}",     # {% endraw %}
    r"#{1,3}\s*\{[^}]*\}",           # one to three # followed by {: ... }
    r"\{\.[^}]*\}",                  # {.something ... }
    r"\{ \.[^}]*\}",                 # { .something ... }
    r"\{: [^}]*\}",                  # {: ... }
]

remove_line_patterns = [
    r"localplugins\.CPPTestReference",  # Lines containing localplugins.CPPTestReference
    r'"Click to view reference"',       # "Click to view reference" lines
]


compiled_patterns_replace_by_empty_string = [re.compile(p) for p in replace_by_empty_string_patterns]
compiled_patterns_remove_line = [re.compile(p) for p in remove_line_patterns]

def clean_line(line):
    while any((re.search(pat,line) is not None) for pat in compiled_patterns_replace_by_empty_string):
        for pat in compiled_patterns_replace_by_empty_string:
            line = pat.sub("", line)
    return line

def remove_line(line):
    return any((re.search(pat,line) is not None) for pat in compiled_patterns_remove_line)

def remove_invalid_markdown_start(lines: list[str]) -> list[str]:
    """
    Remove file start of the form:
    '

    ---
    ' as this leads to errors in doc-as-code
    """
    if len(lines) > 2:
        first_two_lines_empty = not lines[0].strip() and not lines[1].strip() 
        if first_two_lines_empty and lines[2].startswith("---"):
            return lines[3:]
    return lines

def insert_line(filepath):
    """Insert a new line explaining the abbreviation ABBR in '## Compliance for ABBR' in the trustable report."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    modified = False
    updated_lines = []
    for line in lines:
        updated_lines.append(line)
        stripped_line = line.strip()
        if stripped_line.startswith("## Compliance for"):
            if stripped_line == '## Compliance for AOU':
                updated_lines.append("This presents the compliance for the _Assumptions of Use_ (AOU) in tabular form.\n")
            elif stripped_line == '## Compliance for JLEX':
                updated_lines.append("This presents the compliance for the _JSON-Library Expectations_ (JLEX) in tabular form.\n")
            elif stripped_line == '## Compliance for JLS':
                updated_lines.append("This presents the compliance for the _JSON-Library Statements_ (JLS) in tabular form.\n")
            elif stripped_line == '## Compliance for NJF':
                updated_lines.append("This presents the compliance for the _No JSON Faults_ (NJF) in tabular form.\n")
            elif stripped_line == '## Compliance for NPF':
                updated_lines.append("This presents the compliance for the _No Parsing Faults_ (NPF) in tabular form.\n")
            elif stripped_line == '## Compliance for PJD':
                updated_lines.append("This presents the compliance for the _Parse JSON Data_ (PJD) in tabular form.\n")
            elif stripped_line == '## Compliance for TA':
                updated_lines.append("This presents the compliance for the _Trustable Assertions_ (TA) in tabular form.\n")
            elif stripped_line == '## Compliance for TIJ':
                updated_lines.append("This presents the compliance for the _Throw Ill-Formed JSON_ (TIJ) in tabular form.\n")
            elif stripped_line == '## Compliance for TRUSTABLE':
                updated_lines.append("This presents the ultimate trustability score for nlohmann/json.\n")
            elif stripped_line == '## Compliance for TT':
                updated_lines.append("This presents the compliance for the _Trustable Tenets_ (TT) in tabular form.\n")
            elif stripped_line == '## Compliance for WFJ':
                updated_lines.append("This presents the compliance for _Well Formed JSON_ (WFJ) in tabular form.\n")
            modified = True
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(updated_lines)

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    lines = remove_invalid_markdown_start(lines)
    new_lines = [clean_line(line) for line in lines]
    new_lines = [line for line in new_lines if not remove_line(line)]  # Remove empty lines
    new_lines = [line[2:] if line.startswith('\t\t') else line for line in new_lines]
    if new_lines != lines:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"Cleaned: {filepath}")

def main():
    input_path = '.'
    if(len(sys.argv) != 2):
       sys.exit('ERROR:' + sys.argv[0] + ' expects 1 command line argument which is the processing path. Instead ' + str(len(sys.argv) - 1) + ' arguments were passed.')
    else:
        input_path = sys.argv[1]

    for root, _, files in os.walk(input_path):
        for file in files:
            # all .md files are potentially ill-formatted
            if file.endswith('.md'):
                clean_file(os.path.join(root, file))
            # abbreviations are only explained in the main report
            if file == "trustable_report_for_software.md":
                insert_line(os.path.join(root, file))

if __name__ == "__main__":
    main()
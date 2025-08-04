import os
import re

# The trudag report is not in standard markdown format, so we need to clean it up.
# This script will remove specific patterns from the markdown files in the current directory and its subdirectories


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
    for pat in compiled_patterns_replace_by_empty_string:
        line = pat.sub("", line)
    return line

def remove_line(line):
    for pat in compiled_patterns_remove_line:
        if re.search(pat, line):
            return True
    return False

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
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.md'):
                clean_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
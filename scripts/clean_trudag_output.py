import os
import re

# The trudag report is not in standard markdown format, so we need to clean it up.
# This script will remove specific patterns from the markdown files in the current directory and its subdirectories


# List of regex patterns to remove only the matched part, not the whole line
patterns = [
    r"\{class[:=][^}]*\}",           # {class:...} or {class=...} with any attributes inside
    r"\{\%[\s]*raw[\s]*\%\}",        # {% raw %}
    r"\{\%[\s]*endraw[\s]*\%\}",     # {% endraw %}
    r"#{1,3}\s*\{[^}]*\}",           # one to three # followed by {: ... }
    r"\{\.[^}]*\}",                  # {.something ... }
    r"\{ \.[^}]*\}",                 # { .something ... }
    r"\{: [^}]*\}",                  # {: ... }
]

compiled_patterns = [re.compile(p) for p in patterns]

def clean_line(line):
    for pat in compiled_patterns:
        line = pat.sub("", line)
    return line

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    new_lines = [clean_line(line) for line in lines]
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
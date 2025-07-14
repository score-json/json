import os
import re
import subprocess
import shutil

# Path to the folder containing the Python file
DIRECTORY = os.path.dirname(os.path.abspath(__file__))


# Convert all .md files in the input directory to .rst files using m2r2
# and move them to the output directory.
# Args:
#     input_dir (str): Directory containing the .md files.
#     output_dir (str): Directory to move the converted .rst files to.
def convert_and_move_md_files(input_dir, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Iterate over all .md files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".md"):  # Process only .md files
            md_file_path = os.path.join(input_dir, filename)

            # Call m2r2 to convert the file
            print(f"Converting: {md_file_path}")
            subprocess.run(["m2r2", md_file_path], check=True)

            # Determine the base name (without extension)
            basename = os.path.splitext(filename)[0]
            rst_file_name = f"{basename}.rst"
            rst_file_path = os.path.join(input_dir, rst_file_name)

            # Move the .rst file to the output directory
            if os.path.exists(rst_file_path):
                shutil.move(rst_file_path, os.path.join(output_dir, rst_file_name))
                print(
                    f"Converted and moved: {md_file_path} -> {os.path.join(output_dir, rst_file_name)}"
                )
            else:
                print(f"Error: Expected .rst file not found for {md_file_path}")


# Function to clean ".item-element" lines and remove content between {...}
def clean_item_element_references(directory):
    print("Cleaning .item-element references...")
    for filename in os.listdir(directory):
        if filename.endswith(".rst"):  # Process only .rst files
            file_path = os.path.join(directory, filename)
            print(f"Processing file: {file_path}")

            # Read the file content
            with open(file_path, "r") as file:
                lines = file.readlines()

            # Process each line and remove content between {...} for ".item-element" lines
            processed_lines = []
            for line in lines:
                if ".item-element" in line:
                    line = re.sub(r"{.*?}", "", line)  # Remove content between { and }
                processed_lines.append(line)

            # Write the cleaned lines back to the file
            with open(file_path, "w") as file:
                file.writelines(processed_lines)
            print(f"File cleaned and saved: {file_path}")


def add_sections_and_headers(directory):
    print("Adding sections and rearranging headers...")
    for filename in os.listdir(directory):
        if filename.endswith(".rst"):  # Process only .rst files
            file_path = os.path.join(directory, filename)
            print(f"Processing file: {file_path}")

            # Read the file content
            with open(file_path, "r") as file:
                lines = file.readlines()

            # Collect all existing section references (e.g., .. _ta-analysis:)
            existing_references = set()
            for line in lines:
                match = re.match(r"^\.\.\s*_(.+?):\s*$", line.strip())
                if match:
                    existing_references.add(match.group(1).strip().lower())

            # Process the file line by line
            processed_lines = []
            i = 0
            while i < len(lines):
                line = lines[i]

                # Match lines containing uppercase words with optional ### and symbols like _
                # E.g., TA-ANALYSIS ###, TT-CHANGES ###, TA-SUPPLY_CHAIN ###, etc.
                match = re.match(r"^([A-Z0-9\-_]+)(\s*###)?$", line.strip())
                # Verify the next line exists for the ^^^ line
                if match and i + 1 < len(lines):
                    next_line = lines[i + 1].strip()

                    # Check if the next line is all ^^^ (or longer)
                    if re.match(r"^\^{5,}$", next_line):  # Line with `^^^^` or longer
                        section_name = match.group(1).strip()
                        section_reference = section_name.lower()

                        # Only add a new reference if it doesn't already exist
                        if section_reference not in existing_references:
                            # Add two blank lines and a section declaration above the line
                            processed_lines.append("\n\n")  # Two blank lines
                            processed_lines.append(f".. _{section_reference}:\n")
                            processed_lines.append("\n")  # Additional blank line

                        # Add the original title without the ###
                        processed_lines.append(f"{section_name}\n")
                        processed_lines.append(next_line + "\n")

                        # Skip to the line after the ^^^ line
                        i += 2
                        continue  # Skip further processing of this section

                # Append unmodified lines if no match
                processed_lines.append(line)
                i += 1

            # Write the updated content back to the file
            with open(file_path, "w") as file:
                file.writelines(processed_lines)
            print(f"Sections and headers updated: {file_path}")


# Function to replace markdown-style references with :ref: (remove full links)
def replace_markdown_references(directory):
    print("Replacing markdown-style references with :ref:...")
    for filename in os.listdir(directory):
        if filename.endswith(".rst"):  # Process only .rst files
            file_path = os.path.join(directory, filename)
            print(f"Processing file: {file_path}")

            # Read the file content
            with open(file_path, "r") as file:
                lines = file.readlines()

            # Replace all markdown-structured references with proper Sphinx :ref: format
            processed_lines = []
            for line in lines:
                # Match lines like `TA-ANALYSIS <TA.md#ta-analysis>`_
                line = re.sub(
                    r"`.*?<.*?#([\w\-_.]+)>`_",  # Match the structure, including backticks and trailing _
                    r":ref:`\1`",  # Replace it with the Sphinx :ref: format
                    line,
                )
                processed_lines.append(line)

            # Write the updated lines back to the file
            with open(file_path, "w") as file:
                file.writelines(processed_lines)
            print(f"Markdown references replaced in: {file_path}")


def rewrite_trudag_report(nav_file_path, trudag_report_path):
    print(f"Rewriting file: {trudag_report_path} based on: {nav_file_path}")
    # Read the content of nav.rst
    try:
        with open(nav_file_path, "r") as nav_file:
            nav_lines = nav_file.readlines()
    except FileNotFoundError:
        print(f"Error: {nav_file_path} not found.")
        return

    # Extract references from nav.rst and convert them to Sphinx-compatible paths
    new_toc_entries = []
    for line in nav_lines:
        # Match lines like `* `Compliance report <trustable_report_for_json_library.md>`_`
        match = re.match(r"\*\s*`.+? <(.+?)\.md>`_", line.strip())
        if match:
            # Extract the file name without `.md` and convert to the Sphinx path
            reference = match.group(1)
            sphinx_path = f"   trudag/m2r2_test/{reference}"
            new_toc_entries.append(sphinx_path)
    if not new_toc_entries:
        print("No valid entries found in nav.rst.")
        return

    # Construct the content of the new trudag_report.rst file
    new_content = """..
   # *******************************************************************************
   # Copyright (c) 2025 Contributors to the Eclipse Foundation
   #
   # See the NOTICE file(s) distributed with this work for additional
   # information regarding copyright ownership.
   #
   # This program and the accompanying materials are made available under the
   # terms of the Apache License Version 2.0 which is available at
   # https://www.apache.org/licenses/LICENSE-2.0
   #
   # SPDX-License-Identifier: Apache-2.0
   # *******************************************************************************

.. _trudag_report:

Trudag Report
=================

.. toctree::
   :maxdepth: 2
   :caption: Trudag Report
   :glob:

"""
    new_content += "\n".join(new_toc_entries) + "\n"

    # Write the new content to trudag_report.rst
    try:
        with open(trudag_report_path, "w") as trudag_report_file:
            trudag_report_file.write(new_content)
        print(f"File {trudag_report_path} has been successfully rewritten.")
    except Exception as e:
        print(f"Error writing to file {trudag_report_path}: {e}")


def add_missing_headers(directory):
    print("Adding headers to .rst files where missing...")
    # Process each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".rst"):  # Only process .rst files
            file_path = os.path.join(directory, filename)
            print(f"Processing file: {file_path}")

            # Read the file content
            with open(file_path, "r") as file:
                lines = file.readlines()

            # Check if the file already has a header with `=` underline
            has_header = False
            for i in range(len(lines) - 1):  # Iterate through lines and check pairs
                current_line = lines[i].strip()
                next_line = lines[i + 1].strip()

                # Check if the current line is text and the next line is `=` with the same length
                if current_line and next_line == "=" * len(current_line):
                    has_header = True
                    break

            # Skip the file if it already has a header
            if has_header:
                print(f"Header already exists in: {filename}")
                continue

            # Generate the header from the filename (strip the .rst extension)
            document_name = os.path.splitext(filename)[0]
            header = f"{document_name}\n{'=' * len(document_name)}\n\n"

            # Add the header at the top of the file
            updated_lines = [header] + lines

            # Write the updated content back to the file
            with open(file_path, "w") as file:
                file.writelines(updated_lines)
            print(f"Header added to: {filename}")


# Run all functions
if __name__ == "__main__":
    # Convert .md files to .rst and move them
    convert_and_move_md_files(os.path.join(DIRECTORY, ".."), DIRECTORY)

    # Clean ".item-element" references
    clean_item_element_references(DIRECTORY)

    # Add sections and headers
    add_sections_and_headers(DIRECTORY)

    # Replace markdown-style references with :ref:
    replace_markdown_references(DIRECTORY)

    # Update trudag_report.rst based on nav.rst
    nav_file_path = rewrite_trudag_report(
        DIRECTORY + "/nav.rst", "/workspaces/inc_json/docs/trustable/trudag_report.rst"
    )

    # Add missing headers to .rst files
    add_missing_headers(DIRECTORY)

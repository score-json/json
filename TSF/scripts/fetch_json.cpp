#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <regex>
#include <stdexcept>

using namespace std;

/*
This is a command line tool that fetches the .json file-names from the file unit-testsuites.cpp and
prints the result into a file using the desired format for use in the items in the trustable graph.

User inputs are asked from the command line and are
    - relative path to file from which names are read (i.e. unit-testsuites.cpp)
    - relative path to output file
    - name of the test
    - description of the test
    - whether a single line at a time is to be read or all lines from a starting line until an ending line
    - these lines

Assumptions:
    - A .json filename is the only value within quotation marks in a line containing "TEST_DATA_DIRECTORY".
    - The provided lines are valid.

Dangers:
    - output file is overwritten by default.

*/

string replace_tab_with_spaces(const string& input, const int num_of_spaces = 4);
string wrapper_for_trudag(string evidence, string wrap_left = "\t\t\t- \"", string wrap_right = "\"\n");
bool get_json_from_line(int line, ifstream& source, ofstream& target);
bool read_line_by_line(ifstream& source, ofstream& target);
bool read_region(ifstream& source, ofstream& target);


// Horizontal tabs are automatically replaced by four spaces in VSCode except if a '\t' is pasted into the file.
// This function does the same.
string replace_tab_with_spaces(const string& input, const int num_of_spaces){
    string output = input;
    string spaces = "    ";
    regex tab("\t");
    if (num_of_spaces!=4){
        spaces = "";
        for (int i = 0; i<num_of_spaces; i++){
            spaces += " ";
        }
    }
    return regex_replace(output,tab,spaces);
}

// This function brings a filename in the format which can be directly pasted in the item of the trustable graph.
string wrapper_for_trudag(string evidence, string wrap_left, string wrap_right){
    stringstream res;
    res << wrap_left << evidence << wrap_right;
    return res.str();
}

// This function attempts to extract the filename.json from a candidate line.
// On error, an exception is thrown.
string get_json_from_candidate(string candidate){
    regex pattern("\"([^\"]*)\"");
    smatch m;
    if (candidate.find("TEST_DATA_DIRECTORY")!=string::npos && regex_search(candidate,m,pattern)){
        return replace_tab_with_spaces(wrapper_for_trudag(m[1]));
    } else {
        throw out_of_range("No TEST_DATA_DIRECTORY in candidate");
    }
}

// Attempts to extract filename.json from a specified line in the source file and writes it into the target file.
// If filename.json could be located, true is returned, and false otherwise.
bool get_json_from_line(int line, ifstream& source, ofstream& target){
    if (line<=0){
        throw invalid_argument("Can not read negative lines.");
    }
    // reset getline()
    source.clear();
    source.seekg(0,source.beg);
    // initialise counter
    int cnt = 1;
    // read until
    string candidate;
    while (cnt <= line){
        if (!getline(source, candidate)){
            throw out_of_range("Only "+to_string(cnt-1)+" lines to be found.");
        }
        cnt++;
    }
    string res;
    try {
        res = get_json_from_candidate(candidate);
    } catch (const out_of_range& e) {
        return false;
    }
    target << res;
    return true;
}

// Reads the filename.json line by line.
// Asks the user to input the line-numbers.
bool read_line_by_line(ifstream& source, ofstream& target){
    int line = -1;
    string ans;
    while (true){
        cout << "Please specify line: ";
        getline(std::cin, ans);
        try {
            line = stoi(ans);
        } catch (...) {
            cout << "Error: couldn't convert " << ans << " to integer!\n";
            continue;
        }
        if (line<=0){
            cout << "Invalid line, please try again.\n";
            continue;
        }
        cout << "Reading line " << line << "\n";
        bool success;
            try {
                success = get_json_from_line(line,source,target);
            } catch (const invalid_argument& ia){
                cout << ia.what();
            } catch (const out_of_range& oor) {
                cout << oor.what();
            }
        if (!success) {
            cout << "Could not find json reference in line " << line << " !\n";
        }
        cout << "Add another line? y/n? ";
        getline(std::cin, ans);
        if (ans!="y"&&ans!="Y"&&ans!="") {
            break;
        }
    }
    return true;
}

// Reads the filename.json beginning from a starting line until (inclusively) an ending line.
// Asks the reader to input these line-numbers. 
bool read_region(ifstream& source, ofstream& target){
    int start_line;
    int end_line;
    string ans;
    while (true){
        cout << "Line to start: ";
        getline(std::cin, ans);
        try {
            start_line = stoi(ans);
        } catch (...) {
            cout << "Error: couldn't convert " << ans << " to integer!\n";
            continue;
        }
        cout << "Line to end on: ";
        getline(std::cin, ans);
        try {
            end_line = stoi(ans);
        } catch (...) {
            cout << "Error: couldn't convert " << ans << " to integer!\n";
            continue;
        }
        if (start_line>end_line) {
            cout << "Invalid configuration: start-line is after end-line.\n";
            return false;
        }
        for (int line = start_line; line <= end_line; line++){
            cout << "Reading line " << line << "\n";
            bool success;
            try {
                success = get_json_from_line(line,source,target);
            } catch (const invalid_argument& ia){
                cout << ia.what();
                return false;
            } catch (const out_of_range& oor) {
                cout << oor.what();
                return false;
            }
            if (!success) {
                cout << "Could not find json reference in line " << line << " !\n";
            }
        }
        cout << "Add another region? y/n? ";
        getline(std::cin, ans);
        if (ans != "" && ans != "y" && ans != "Y"){
            break;
        }
    }
    return true;
}

int main(){
    // define standard paths
    string path_to_testsuite = "../../tests/src/unit-testsuites.cpp";
    string path_to_evidence = "temp.md";
    
    // Setup source
    cout << "Read from standard file " << path_to_testsuite << " y/n? ";
    string ans;
    getline(std::cin, ans);
    if (ans!="y" && ans!="Y" && ans!=""){
        cout << "Please insert file to read from: ";
        getline(std::cin, path_to_testsuite);
    }
    cout << "Attempting to read from " << path_to_testsuite << "..." << "\n";
    ifstream testsuite;
    try {
        testsuite.open(path_to_testsuite);
    } catch (const ifstream::failure& e) {
        cout << "Could not open file " << path_to_testsuite << "\n";
        return -1;
    }
    if (testsuite.fail()||!testsuite.is_open()){
        cout << "Could not open file " << path_to_testsuite << "\n";
        testsuite.close();
        return -1;
    } else {
        cout << "Reading successful\n\n";
    }

    // Setup target
    cout << "Write to standard file " << path_to_evidence << " y/n? "; 
    getline(std::cin, ans);
    if (ans!="y" && ans!="Y" && ans!=""){
        cout << "Please specify where to write results: ";
        getline(std::cin, path_to_evidence);
    }
    cout << "Opening " << path_to_evidence << "..." << "\n";
    ofstream evidence;
    try {
        evidence.open(path_to_evidence);
    } catch (const ifstream::failure& e) {
        cout << "Could not open file " << path_to_evidence;
        testsuite.close();
        evidence.close();
        return -1;
    }
    cout << "Done!\n\n";

    // initialise target
    
    // get name
    string description;
    while (true){
        evidence << replace_tab_with_spaces("\t\t- type: JSON_testsuite\n");
        cout << "Testname ";
        getline(std::cin, ans);
        cout << "Initialising collection of evidence for " << ans << "\n";
        evidence << replace_tab_with_spaces("\t\t  name: \"") << ans << "\"\n";
        evidence << replace_tab_with_spaces("\t\t  path: \"");
        if (path_to_testsuite.substr(0,3)=="../") {
            evidence << "/workspaces/json/" << path_to_testsuite.substr(3);
        } else {
            evidence << "/workspaces/json/scripts/" << path_to_testsuite;
        }
        evidence << replace_tab_with_spaces("\"\n\t\t  test_suite_paths:\n");
        cout << "Description of the test: ";
        getline(std::cin, description);

        cout << "Read single lines? y/n? ";
        getline(std::cin, ans);
        if (ans!="y"&&ans!="Y"&&ans!="") {
            cout << "Read region? y/n? ";
            getline(std::cin, ans);
            if (ans!="y"&&ans!="Y"&&ans!="") {
                testsuite.close();
                evidence.close();
                return -1;
            }
            if (!read_region(testsuite, evidence)){
                testsuite.close();
                evidence.close();
                return -1;
            }
        } else {
            if (!read_line_by_line(testsuite, evidence)){
                testsuite.close();
                evidence.close();
                return -1;
            }
        }
        evidence << replace_tab_with_spaces("\t\t  description: \"") << description << "\"\n";
        cout << "Add another test? y/n? ";
        getline(std::cin, ans);
        if (ans!="y"&&ans!="Y"&&ans!="") {
            break;
        }
    }
    testsuite.close();
    evidence.close();
    return 0;
}
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <regex>

using namespace std;

string replace_tab_with_spaces(const string& input, int num_of_spaces = 4){
    string output = input;
    string spaces = "    ";
    regex tab("\t");
    if (num_of_spaces==4){
        spaces = "";
        for (int i = 0; i<num_of_spaces; i++){
            spaces += " ";
        }
    }
    regex_replace(output,tab,spaces);
    return output;
}

string wrapper_for_trudag(string evidence, string wrap_left = "\t\t\t- \"", string wrap_right = "\"\n"){
    stringstream res;
    res << wrap_left << evidence << wrap_right;
    return res.str();
}

string get_json_from_candidate(string candidate){
    regex pattern("\"([^\"]*)\"");
    smatch m;
    if (candidate.find("TEST_DATA_DIRECTORY")!=string::npos && regex_search(candidate,m,pattern)){
        return replace_tab_with_spaces(wrapper_for_trudag(m[1]));
    } else {
        throw 0;
    }
}

bool get_json_from_line(int line, ifstream& source, ofstream& target){
    if (line<=0){
        throw;
    }
    // reset getline()
    source.clear();
    source.seekg(0,source.beg);
    // initialise counter
    int cnt = 1;
    // read until
    string candidate;
    while (cnt <= line){
        getline(source, candidate);
        cnt++;
    }
    string res;
    try {
        res = get_json_from_candidate(candidate);
    } catch (int i) {
        return false;
    }
    target << res;
    return true;
}

void replace(ifstream& source, ofstream& target){}

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
        if (!get_json_from_line(line,source,target)) {
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
            if (!get_json_from_line(line,source,target)) {
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

int main(int arg_num, char* args[]){
    if (arg_num>2){
        cout << "Error: illegal number of options\n" << arg_num << "\n";
        return -1;
    }
    bool overwrite = true;
    if (arg_num == 2){
        if (args[0]=="--append"){
            overwrite = false;
            cout << "Modus: append\n\n";
        } else if (args[0] == "--replace"){
            cout << "Modus: replace\n\n";
        } else {
            cout << "Un-known option " << args[0] << "\nModus: replace\n\n";
        }
    }
    // define standard paths
    string path_to_testsuite = "../tests/src/unit-testsuites.cpp";
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
            evidence << path_to_testsuite.substr(3);
        } else {
            evidence << path_to_testsuite;
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
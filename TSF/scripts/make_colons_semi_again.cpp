#include <iostream>
#include <fstream>
#include <sstream>
#include <regex>
#include <filesystem>

using namespace std;

/*
This is a program to replace names of the form "test_case:section1:section2:etc." by "test_case;section1;section2;etc".

The change of the separator was necessary because the colon is used in section names of unit-unicode2.cpp. 
*/

string semi_colon(const string& input);
string restore_args(const string& input);
void replace_colons(const filesystem::path& file);

// replaces every colon in a string by a semi-colon
string semi_colon(const string& input){
    string output;
    for (char c: input){
        if (c==':'){
            output += ';';
        } else {
            output += c;
        }
    }
    return output;
}

// Some colons are not to be replaced, so that we change back.
string restore_args(const string& input){
    string output = input;
    output = regex_replace(output, regex("level;"), "level:");
    output = regex_replace(output, regex("normative;"), "normative:");
    output = regex_replace(output, regex("references;"), "references:");
    output = regex_replace(output, regex("type;"), "type:");
    output = regex_replace(output, regex("name;"), "name:");
    output = regex_replace(output, regex("path;"), "path:");
    output = regex_replace(output, regex("test_suite_paths;"), "test_suite_paths:");
    output = regex_replace(output, regex("description;"), "description:");
    output = regex_replace(output, regex("references;"), "references:");
    output = regex_replace(output, regex("reference;"), "reference:");
    output = regex_replace(output, regex("reference:"), "references:");
    output = regex_replace(output, regex("https;//"), "https://");
    output = regex_replace(output, regex("json;;"), "json::");
    output = regex_replace(output, regex("std;;"), "std::");
    output = regex_replace(output, regex("ill-formed;"), "ill-formed:");
    output = regex_replace(output, regex("miloyip/nativejson-benchmark;"), "miloyip/nativejson-benchmark:");
    return output;
}

/*
This method replaces every single colon within a file by a semi-colon, and reverts the changes
as described by restore_args.
It is assumed that the input is a file, and not a path; and this is not tested for.
*/
void replace_colons(const filesystem::path& file){
    ifstream source(file);
    stringstream buffer;
    buffer << source.rdbuf();
    source.close();
    string temp = buffer.str();
    temp = semi_colon(temp);
    temp = restore_args(temp);
    ofstream  target(file);
    target << temp;
    target.close();
}

/*
The program gets the relative path of a directory as input. 
Within this directory, replace_colons is applied to every single mark-down file.
*/
int main(int argnum, char* args[]){
    for (int arg = 1; arg<argnum; arg++){
        for (const auto& entry: filesystem::recursive_directory_iterator(args[arg])){
            if (filesystem::is_regular_file(entry) && entry.path().extension()==".md"){
                replace_colons(entry.path());
            }            
        }
    }
    return 0;
}
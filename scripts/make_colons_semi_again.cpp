#include <iostream>
#include <fstream>
#include <sstream>
#include <regex>
#include <filesystem>

using namespace std;

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
    return output;
}

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
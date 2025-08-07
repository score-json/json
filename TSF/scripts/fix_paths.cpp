#include <iostream>
#include <fstream>
#include <sstream>
#include <regex>
#include <filesystem>

using namespace std;

/*
This is a program to replace the path "/workspaces/json/tests/s-core/" by "/workspaces/json/TSF/tests/".

This change was necessary because the folders of the project have been restructured. 
*/

/*
This method replaces every single path within a file.
It is assumed that the input is a file, and not a path; and this is not tested for.
*/
void fix_paths(const filesystem::path& file){
    ifstream source(file);
    stringstream buffer;
    buffer << source.rdbuf();
    source.close();
    string temp = buffer.str();
    temp = regex_replace(temp, regex("/workspaces/json/tests/s-core/"), "/workspaces/json/TSF/tests/");
    ofstream  target(file);
    target << temp;
    target.close();
}

/*
The program gets the relative path of a directory as input. 
Within this directory, fix_paths is applied to every single mark-down file.
*/
int main(int argnum, char* args[]){
    for (int arg = 1; arg<argnum; arg++){
        for (const auto& entry: filesystem::recursive_directory_iterator(args[arg])){
            if (filesystem::is_regular_file(entry) && entry.path().extension()==".md"){
                fix_paths(entry.path());
            }            
        }
    }
    return 0;
}
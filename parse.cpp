#include <fstream>
#include <iostream>

#include <string>
#include <vector>
#include <algorithm>
#include <optional>

const std::string base_url = "https://babbage.cs.niu.edu:16710";

auto clean_anchors(std::vector<std::string>& files) -> void;
auto get_path(std::string &anchor) -> std::optional<std::string>;

auto get_file_name(std::string &anchor) -> std::string;

int main(int argc, char **argv) {
    
    if (argc == 0) {
        std::cerr << "USAGE: ./parse.o assignment_url";
    }

    std::ifstream input_file(argv[0]);

    if (input_file.fail()) {
        std::cerr << "Failed to open file.";
    }

    bool found_list{false}, start_collecting_links{false};
    std::string line;
    std::string match = "Handouts";
    std::vector<std::pair<std::string, std::string>> files;

    
    while (std::getline(input_file, line)) {
        if (std::search(line.begin(), line.end(), match.begin(), match.end()) != line.end()) {
            found_list = true;
        } 
        if (line.substr(0,4) == "<li>" && found_list) {
           start_collecting_links = true;  
           break;
        }

    }
    if (start_collecting_links) {
        do { 
            auto path = get_path(line);
            auto file_name = get_file_name(line);

            if (path != std::nullopt && !file_name.empty()) files.push_back({*path, file_name});
        } while (std::getline(input_file, line) && line.substr(0,4) == "<li>");
    }

    std::ofstream output_file("files.txt");


    for (const auto &i : files) {
            output_file << i.first << ":"<< i.second << '\n';
    }


    return 0;
}
auto get_path(std::string &anchor) -> std::optional<std::string> {
    
    size_t first = anchor.find("/assets");
    size_t last = first;
    for (; anchor[last + 1] != ' ' && last < anchor.length(); ++last);

    if (first != std::string::npos && last < anchor.length()) {
        return anchor.substr(first,last - first);
    }
    return std::nullopt;
}
auto get_file_name(std::string &anchor) -> std::string {
    auto last = anchor.rbegin(); 
    for(; *last != '<';) {++last;}; 
    auto first = ++last;
    for(; *first != '>';) {++first;}
    return std::string(first.base(), last.base());
}




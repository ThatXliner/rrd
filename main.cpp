#include <iostream>
#include <regex>

#include "cpr/cpr.h"

std::regex REGEX(R"((rick\s*roll)|(never\s*gonna\s*(give\s*you\s*up)?)|(dQw4w9WgXcQ))");
std::smatch match;

int main(int argc, char const *argv[]) {
    if (argc < 2) {
        std::cout << "Usage: rrd URL" << std::endl;
        return 1;
    }
    cpr::Response r = cpr::Get(cpr::Url{argv[1]});

    if (std::regex_search(r.text, match, REGEX)) {
        std::cout << "Possible rickroll detected" << std::endl;
    } else {
        std::cout << "No rickroll detected" << std::endl;
    }
    return 0;
}

/*
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

:)
*/

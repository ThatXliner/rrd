cmake_minimum_required(VERSION 3.20)  # Version of CMake required to run `cmake .`

# Tell CMake we're making a project named 'Rrd'
# and that it's on version 1.0 (optional)
project(Rrd VERSION 1.0)

# Make sure the C++ compiler supports C++11 (optional)
set(CMAKE_CXX_STANDARD 11)

# IDK: this is magic from https://github.com/whoshuu/cpr#cmake
# I modified the mumbo jumbo after 'GIT_TAG' to
# the git commit hash of the latest release (https://github.com/whoshuu/cpr/releases/latest)
include(FetchContent)
FetchContent_Declare(cpr GIT_REPOSITORY https://github.com/whoshuu/cpr.git GIT_TAG f4622efcb59d84071ae11404ae61bd821c1c344b) # the commit hash for 1.5.0
FetchContent_MakeAvailable(cpr)

# Tell CMake we're making an executable named 'rrd'
# from the source file(s) 'main.cpp'
add_executable(rrd main.cpp)

# Link CPR to our executable
target_link_libraries(rrd PRIVATE cpr::cpr)

# Now we're finished! :pogchamp:

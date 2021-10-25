cmake_minimum_required(VERSION 3.20)  # Version of CMake required to run `cmake .`

# Tell CMake we're making a project named 'Rrd'
# and that it's on version 1.0 (optional)
project(Rrd VERSION 1.0)

# Make sure the C++ compiler supports at least C++11 (optional)
set(CMAKE_CXX_STANDARD 11)  # Other options: 98, 11, 14, 17, 20, 23

# IDK: this is magic from https://github.com/whoshuu/cpr#cmake
# I guess this just downloads the library and uses it...
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

# There's PRIVATE linking, PUBLIC linking, and INTERFACE linking
# TL;DR:
#     PRIVATE: implementation-only
#     PUBLIC: implementation and interface
#     INTERFACE: interface only

# See also https://cmake.org/cmake/help/latest/command/target_link_libraries.html#libraries-for-a-target-and-or-its-dependents:

# > Libraries and targets following PUBLIC are linked to, and are made part of the link interface.
# > Libraries and targets following PRIVATE are linked to, but are not made part of the link interface.
# > Libraries following INTERFACE are appended to the link interface and are not used for linking <target>.

# Or https://cmake.org/pipermail/cmake/2016-May/063400.html:

# > - When A links in B as *PRIVATE*, it is saying that A uses B in its
# >   implementation, but B is not used in any part of A's public API. Any code
# >   that makes calls into A would not need to refer directly to anything from
# >   B. An example of this could be a networking library A which can be built to
# >   use one of a number of different SSL libraries internally (which B
# >   represents). A presents a unified interface for client code which does not
# >   reference any of the internal SSL data structures or functions. Client code
# >   would have no idea what SSL implementation (B) is being used by A, nor does
# >   that client code need to care.
# > - When A links in B as *INTERFACE*, it is saying that A does not use B
# >   in its implementation, but B is used in A's public API. Code that calls
# >   into A may need to refer to things from B in order to make such calls. One
# >   example of this is an interface library which simply forwards calls along
# >   to another library but doesn't actually reference the objects on the way
# >   through other than by a pointer or reference. Another example is where A is
# >   defined in CMake as an interface library, meaning it has no actual
# >   implementation itself, it is effectively just a collection of other
# >   libraries (I'm probably over-simplifying here, but you get the picture).
# > - When A links in B as *PUBLIC*, it is essentially a combination of
# >   PRIVATE and INTERFACE. It says that A uses B in its implementation and B is
# >   also used in A's public API.


# Now we're finished! :pogchamp:

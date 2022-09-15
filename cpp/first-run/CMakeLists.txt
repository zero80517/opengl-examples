# setup CMake
cmake_minimum_required(VERSION 3.10)

# set the project name and version
project(first-run)

# add the executable
add_executable(${PROJECT_NAME} main.cpp)

# add glfw3 lib
## include path for target
target_include_directories(${PROJECT_NAME} PUBLIC "${PROJECT_SOURCE_DIR}/../3rdparty/include")
## add lib directory
target_link_directories(${PROJECT_NAME} PUBLIC "${PROJECT_SOURCE_DIR}/../3rdparty/libs")

# check OpenGL
find_package(OpenGL REQUIRED)

# Put all libraries into a variable
set(LIBS glfw3 opengl32)

# link libs
target_link_libraries(${PROJECT_NAME} ${LIBS})

# specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# setup CMake
cmake_minimum_required(VERSION 3.10)

# set the project name and version
project(00_hello_window)

# add GLAD sources
set(GLAD_SOURCES "${PROJECT_SOURCE_DIR}/../3rdparty/src/glad.c")

# add the executable
add_executable(${PROJECT_NAME} main.cpp ${GLAD_SOURCES})

# add glfw3 lib
## include path for target
target_include_directories(${PROJECT_NAME} PUBLIC "${PROJECT_SOURCE_DIR}/../3rdparty/include")
## add lib directory
target_link_directories(${PROJECT_NAME} PUBLIC "${PROJECT_SOURCE_DIR}/../3rdparty/libs")

# check OpenGL
find_package(OpenGL REQUIRED)

# Put all libraries into a variable
# NOTE pthread and dl libs are required for linux
set(THREADS_PREFER_PTHREAD_FLAG ON)
find_package(Threads REQUIRED)
set(LIBS glfw3 OpenGL::GL ${CMAKE_DL_LIBS} Threads::Threads)

# link libs
target_link_libraries(${PROJECT_NAME} ${LIBS})

# specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# setup CMake
cmake_minimum_required(VERSION 3.10)

# set the project name and version
project(3rdparty)

# add libs
add_subdirectory(glfw)

# copy headers from libs
add_custom_target(
    CopyTarget ALL
    COMMAND ${CMAKE_COMMAND} -E copy_directory
            ${CMAKE_SOURCE_DIR}/glfw/include
            ${CMAKE_SOURCE_DIR}/glad/include
            ${CMAKE_SOURCE_DIR}/include
    COMMENT "Copy headers to ${CMAKE_SOURCE_DIR}/include"
    COMMAND ${CMAKE_COMMAND} -E copy_directory
            ${CMAKE_SOURCE_DIR}/glad/src
            ${CMAKE_SOURCE_DIR}/src
    COMMENT "Copy sources ${CMAKE_SOURCE_DIR}/include"
)

# set where builded entities should be dropped
set_target_properties( 
    glfw
    PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/libs
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/libs
)

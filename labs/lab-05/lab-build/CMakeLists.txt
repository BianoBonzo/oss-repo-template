cmake_minimum_required(VERSION 3.0)
project(Program)

add_library(dblock SHARED block.c ../headers/block.h)
add_library(sblock STATIC block.c ../headers/block.h)

add_executable(dynamic_block ../program.c)
target_link_libraries(dynamic_block dblock)

add_executable(static_block ../program.c)
target_link_libraries(static_block sblock)

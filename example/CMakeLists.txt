cmake_minimum_required (VERSION 2.6)

project(vplot_example)

file(GLOB src *.cpp *.cc *.h)

set( CMAKE_CXX_FLAGS "-std=c++1y -stdlib=libc++ -g" )

add_executable(vplot_example ${src} )


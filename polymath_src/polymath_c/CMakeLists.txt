cmake_minimum_required(VERSION 3.8)
project(polymath_c)

set(CMAKE_C_STANDARD 99)

set(SOURCE_FILES libpolymath.h uint64_to_poly_array.c poly_array_to_uint64.c print_poly_array.c shift_lfsr.c polynomial_multiplication.c polynomial_modulo_padding.c)
add_library(polymath_c ${SOURCE_FILES})
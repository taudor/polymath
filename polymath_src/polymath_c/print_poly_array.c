/*
 * This file implements the function print_Poly_Array from libpolymath.h
 */

#include "libpolymath.h"

void print_Poly_Array(Poly_Array* poly)
{
    printf("Degree: %llu\n", poly->deg);
    printf("Used uint64 numbers: %llu\n", poly->len);
    for (size_t i = 0; i < poly->len; i++) {
        printf("0x%0llX ", *(poly->poly + i));
    }
    printf("\n");
}
/*
 * author: Mahmud Ahsan
 * https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * http://banglaprogramming.com
 * License: MIT License
 */
 
/* 
 * Pointer
 * syntax:
 * TYPE *variable_name;
 */

#include <stdio.h>

int main(){
    int value = 100;
    int another_value = 10000;

    // integer pointer
    int *value_pointer;

    // assigning memory address to a pointer
    value_pointer = &value;

    // accessing value by pointer indirectly
    printf("Indirect Accessing Value: %d\n", *value_pointer);

    // changing value
    *value_pointer = 200;

    printf("Changed Value via Pointer: %d\n", *value_pointer);
    printf("Original Value: %d\n", value);

    // accessing another integer value
    value_pointer = &another_value;
    printf("Another value via pointer: %d\n", *value_pointer);

    return 0;
}

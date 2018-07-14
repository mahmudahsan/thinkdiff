/*
 * author: Mahmud Ahsan
 * github: https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * Web: http://banglaprogramming.com
 * youtube: https://www.youtube.com/c/banglaprogramming
 * License: MIT License
 * https://github.com/mahmudahsan/thinkdiff/blob/master/LICENSE 
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

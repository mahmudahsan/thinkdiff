/*
 * author: Mahmud Ahsan
 * github: https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * Web: http://banglaprogramming.com
 * youtube: https://www.youtube.com/c/banglaprogramming
 * License: MIT License
 * https://github.com/mahmudahsan/thinkdiff/blob/master/LICENSE 
 */
 
 /* Variable
 * a variable is like a container which holds a value
 * an expression replace the variable by value
 * 5 common variables types
 * int : integer variable eg. 100
 * float: floating point variable eg. 103.33
 * double: floating point variable twice precision eg. 333.33
 * char: character variable eg. 'w'
 * _Bool: can holds 0 or 1 
 */

#include <stdio.h>

int main(){
    int integerValue = 100;
    float floatingValue = 101.11;
    double doubleValue = 4004.444;
    char characterValue = 'S';
    _Bool isTrue = 1;

    printf("Integer: %d and size: %lu bytes\n", integerValue, 
            sizeof(integerValue));
    printf("Float: %f and size: %lu bytes\n", floatingValue, 
            sizeof(floatingValue));
    printf("Double: %f and size: %lu bytes\n", doubleValue, 
            sizeof(doubleValue));
    printf("Char: %c and size: %lu byte\n", characterValue, 
            sizeof(characterValue));
    printf("Bool: %i and size: %lu byte\n", isTrue, 
            sizeof(isTrue));
    return 0;
}
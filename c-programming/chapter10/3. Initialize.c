/*
 * author: Mahmud Ahsan
 * https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * http://banglaprogramming.com
 * License: MIT License
 */
 
/* 
 * String
 * \0 is auto assigned
 */

#include <stdio.h>

int main(){
    char name[] = {"Steve Jobs"};
    char anotherName[] = "Bill Gates"; // curly braces are optional

    printf("%s\n", name);
    printf("%s\n", anotherName);

    return 0;
}

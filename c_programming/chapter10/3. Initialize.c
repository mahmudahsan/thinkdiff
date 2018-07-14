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

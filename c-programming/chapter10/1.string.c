/*
 * author: Mahmud Ahsan
 * https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * http://banglaprogramming.com
 * License: MIT License
 */
 
/* 
 * String
 * It is a sequence of charcters in an array
 */

#include <stdio.h>

int main(){
    char vowel[] = {'a', 'e', 'i', 'o', 'u'};

    for (int i = 0; i < 5; ++i){
        printf("%c", vowel[i]);
    }
    printf("\nTHIS IS A STRING\n");

    printf("%s\n", vowel);

    return 0;
}

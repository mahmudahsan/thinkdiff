/*
 * author: Mahmud Ahsan
 * https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * http://banglaprogramming.com
 * License: MIT License
 */
 
/* 
 * String
 * Variable length character string
 * NULL '\0' character
 */

#include <stdio.h>

int stringLength(const char str[]);

int main(){
    char vowel[] = {'a', 'e', 'i', 'o', 'u', '\0'};

    int vowelLength = stringLength(vowel);

    for (int i = 0; i < vowelLength; ++i){
        printf("%c", vowel[i]);
    }
    printf("\n");

    return 0;
}

int stringLength(const char str[]){
    int pos = 0;
    char c = str[pos];
    int length = 0;

    while (c != '\0'){
        length += 1;
        pos += 1;
        c = str[pos];
    }
    return length;
}

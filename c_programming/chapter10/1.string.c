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

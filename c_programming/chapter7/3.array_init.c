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
 * Array Initialization
 */

#include <stdio.h>

int main(){
    // initialization while declaring array
    float points[5] = {0.0, 0.1, 1.5, 11.48, 90.44};

    // OR skipping number of elements inside braces
    // float points[] = {0.0, 0.1, 1.5, 11.48, 90.44};

    for (int i = 0; i < 5; ++i){
        printf("points[%d] is: %f\n", i, points[i]);
    }
    printf("\n");

    char vowel[5] = {'a', 'e', 'i', 'o', 'u'};
    for (int i = 0; i < 5; ++i){
        printf("%c", vowel[i]);
    }
    printf("\n\n");
        
    // index based initialization
    int numbers[3] = { [1] = 4, [0] = 1, [2] = 100 };

    for (int i = 0; i < 3; ++i){
        printf("Numbers[%d] = %d\n", i, numbers[i]);
    }

    return 0;
}
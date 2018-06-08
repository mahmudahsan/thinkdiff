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
 * Type Casting
 */

#include <stdio.h>

int main(){
    int a = 100;
    int b = 7;
    float c = 23.0F;
    
    int resultInt = (int) c + a;
    printf("(int) c + a: %i\n", resultInt);

    float resultF = a / b; // after decimal point truncated
    printf("a / b: %.2f\n", resultF);

    resultF = a / (float) b;
    printf("a / b: %f\n", resultF);

    resultF = (float) a / b;
    printf("a / b: %f\n", resultF);

    resultF = (float) a / (float) b;
    printf("a / b: %f\n", resultF);

    resultInt = (int) resultF;
    printf("a / b: %i\n", resultInt);

    return 0;
}
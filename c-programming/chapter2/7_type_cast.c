/*
 * author: Mahmud Ahsan
 * https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * http://banglaprogramming.com
 * License: MIT License
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
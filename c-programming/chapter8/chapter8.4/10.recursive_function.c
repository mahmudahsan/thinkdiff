/*
 * author: Mahmud Ahsan
 * https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * http://banglaprogramming.com
 * License: MIT License
 */
 
/* 
 * Recursive Function
 * A function that calls itself
 */

#include <stdio.h>

int factorial(int num);

int main(){
    printf("!%d => %d\n", 0, factorial(0));
    printf("!%d => %d\n", 5, factorial(5));
    printf("!%d => %d\n", 6, factorial(6));
    printf("!%d => %d\n", 7, factorial(7));
    printf("!%d => %d\n", 8, factorial(8));
    return 0;
}

// !5 = 5 * 4 * 3 * 2 * 1 => 120
int factorial(int num){
    // base case
    if (num <= 1) return 1;

    // recursive case
    return num * factorial(num - 1);
}
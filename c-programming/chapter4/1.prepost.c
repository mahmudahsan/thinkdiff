/*
 * author: Mahmud Ahsan
 * https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * http://banglaprogramming.com
 * License: MIT License
 */
 
/* 
 * Difference between ++i and i++
 */

#include <stdio.h>

int main(){
    printf("\nDifference between ++i and i++\n");
    
    int i = 100;
    printf("i: %d\n", i);
    
    int num1 = ++i;
    printf("num1: %d i: %d\n", num1, i);
    
    int num2 = i++;
    printf("num2: %d i: %d\n", num2, i);

    
    int j = 0;
    printf("%d\n", j);
    ++j;
    printf("%d\n", j);
    j++;
    printf("%d\n", j);
    
}
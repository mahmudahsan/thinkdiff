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
 * Fibonacci Number Series
 * In this series, a number is the sum of previous two numbers   
 * other than first and second positions which is 0 and 1
 * Example: 0, 1, 1, 2, 3, 5, 8
 * Problem: Write a program that can show a fibonacci number for a * given position within 20. 
 * Input: 1 to 20, 0 for exit
 * Output: Fibonacci number for the position
 */

#include <stdio.h>
#define MAX_FIB 20 // Defining a Constant value

int main(){
    int fibs[MAX_FIB];
    fibs[0] = 0;
    fibs[1] = 1;


    for (int i = 2; i < MAX_FIB; ++i){
        fibs[i] = fibs[i-1] + fibs[i-2];
    }

    int pos;
    do {
        printf("Enter a positive number within (1-20) or 0 to Exit: ");
        scanf("%d", &pos);

        if (pos >= 1 && pos <= MAX_FIB){
            printf("\nFibonacci number for position %d is %d\n", pos, fibs[pos-1]);
        }
    } while(pos != 0);
        
    return 0;
}
/*
 * author: Mahmud Ahsan
 * https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * http://banglaprogramming.com
 * License: MIT License
 */
 
/* 
 * Static Variable
 * value exists entire time of the program execution
 * automatically initialized to 0
 */

#include <stdio.h>

void incrementalSum(int num);

int main(){
    incrementalSum(100);
    incrementalSum(50);
    incrementalSum(400);

    return 0;
}

void incrementalSum(int num){
    auto int aSum = 0; // auto optional
    static int sum; // initialized only once and remain in memory

    sum += num;
    aSum += num;

    printf("Static Sum: %d, auto Sum: %d\n", sum, aSum);
}
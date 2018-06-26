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
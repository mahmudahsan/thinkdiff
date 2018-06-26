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
 * GCD Function
 * Greatest common divisor of 2 integers which are not all zeros is the largest number that divides both integers.
 */

#include <stdio.h>

void gcd(int num1, int num2);

int main(){
    gcd(2, 4);
    gcd(5, 10);
    gcd(10, 25);
    gcd(2, 7);

    return 0;
}

void gcd(int num1, int num2){
    int orgNum1 = num1;
    int orgNum2 = num2;
    int temp;
    while (num2 != 0) {
        temp = num1 % num2;
        num1 = num2;
        num2 = temp;
    }

    printf("GCD(%d, %d) = %d\n", orgNum1, orgNum2, num1);
}

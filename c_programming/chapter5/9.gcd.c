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
 * Greatest Common Divisor or GCD(10, 15) = 5
 * GCD of 2 integer is the largest integer evenly divides the two integers
 */

#include <stdio.h>

int main(){
        int num1, num2;
        printf("Enter two numbers: ");
        scanf("%d %d", &num1, &num2);
        
        while (num2 != 0){
            int temp = num1 % num2;
            num1 = num2;
            num2 = temp;
        }
        
        printf("GCD is: %d\n", num1);
        
        return 0;
}
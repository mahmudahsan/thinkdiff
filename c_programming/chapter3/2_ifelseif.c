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
 * if syntax
 * if (expression) {
 *     statements 
 * } 
 * else if (expression2) {
 *     statements
 * } 
 * else {
 *     statements
 * }
 * one line statement { } braces are optional
 */

#include <stdio.h>

int main(){
    int number;
    
    printf("Please enter a number: ");
    scanf("%d", &number);
    if (number < 10) {
        printf("Input number is less than 10\n");
    }
    else if (number < 50){
        printf("Input number is less than 50\n");
    }
    else {
        printf("Input number is greater than or equal to 50\n");
    }
        
    return 0;
}
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
 * scanf
 * if syntax
 * if (expression) {
       statements 
   } 
 * one line statement { } braces are optional
 */

#include <stdio.h>

int main(){
    int number;
    
    printf("Please enter a number: ");
    scanf("%d", &number);
    if (number < 10)
        printf("Input number is less than 10\n");
        
    /* or with braces but for multiline statements braces is must
    if (number < 10) {
        printf("Input number is less than 10\n");
    }
    */
        
    return 0;
}
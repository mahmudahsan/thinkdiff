/*
 * author: Mahmud Ahsan
 * https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * http://banglaprogramming.com
 * License: MIT License
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
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
 * Function
 * A sequence of statements can be defined as function
 * Syntax:
 * return_type function_name(arguments){
 *    statements;
 * }
 */

#include <stdio.h>

void welcomeMessage(){
    printf("Welcome in my world!\n");
}

int square(int number){
    int result = number * number;
    return result;
}

double squareDouble(double number){
    return number * number;
}

// built in function
int main(){
    welcomeMessage();
    printf("Square number of 2 is %d\n", square(2));
    printf("Square number of 2.2 is %.2f\n", squareDouble(2.2));

    printf("\n");

    // Multiplication table for 2
    for (int i = 1; i <= 10; ++i){
        printf("2 x %d = %d\n", i, square(i));
    }    
    
    return 0;
}
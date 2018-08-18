/*
 * author: Mahmud Ahsan
 * https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * http://banglaprogramming.com
 * License: MIT License
 */

/* 
 * Leap Year
 * year % 4 == 0 && year % 100 != 0
 * or 
 * year % 400 == 0
 */

#include <stdio.h>

int main(){
    int year;
    
    printf("Please enter a year: ");
    scanf("%d", &year);
    if ( (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0) ) {
        printf("%d is a leap year\n", year);
    }
    else {
        printf("%d is not a leap year\n", year);
    }
        
    return 0;
}
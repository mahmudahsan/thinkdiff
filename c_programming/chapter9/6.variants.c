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
 * Structure
 * Variants
 * Declaring variable at the definition 
 */

#include <stdio.h>

struct date{
    int day;
    int month;
    int year;
} today, tomorrow;

void printDate(struct date _date);

int main(){
    today = (struct date) {02, 07, 2018};
    tomorrow = (struct date) {.year = 2018, .day = 03, .month = 07};
    

    printDate(today);
    printDate(tomorrow);

    return 0;
}

void printDate(struct date _date){
    printf("Day: %d | Month: %d | Year: %d\n", _date.day, _date.month, _date.year);
}
/*
 * author: Mahmud Ahsan
 * https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * http://banglaprogramming.com
 * License: MIT License
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
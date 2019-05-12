/*
 * author: Mahmud Ahsan
 * https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * http://banglaprogramming.com
 * License: MIT License
 */
 
/* 
 * Structure
 * Grouping data to make a new custom data type
 * Syntax:
 * struct name {
 *     types;
 * };
 */

#include <stdio.h>

// creating a structure type
// date is a new structure type
// date contains 3 members
struct date{
    int day;
    int month;
    int year;
};

void printDate(struct date _date);

int main(){
    struct date today;
    struct date yesterday, tomorrow;

    today.day = 25;
    today.month = 06;
    today.year = 2018;

    yesterday.day = 24;
    yesterday.month = 06;
    yesterday.year = 2018;

    tomorrow.day = 26;
    tomorrow.month = 06;
    tomorrow.year = 2018;
    
    printDate(today);
    printDate(yesterday);
    printDate(tomorrow);

    return 0;
}

void printDate(struct date _date){
    printf("Day: %d | Month: %d | Year: %d\n", _date.day, _date.month, _date.year);
}
/*
 * author: Mahmud Ahsan
 * https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * http://banglaprogramming.com
 * License: MIT License
 */
 
/* 
 * Structure
 * initialize 
 */

#include <stdio.h>

typedef struct date{
    int day;
    int month;
    int year;
} Date;

void printDate(Date _date);

int main(){
    Date today = {2, 7, 2018};
    Date tomorrow = {3, 7};

    printDate(today);
    printDate(tomorrow);

    return 0;
}

void printDate(Date _date){
    printf("Day: %d | Month: %d | Year: %d\n", _date.day, _date.month, _date.year);
}
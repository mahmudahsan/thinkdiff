/*
 * author: Mahmud Ahsan
 * https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * http://banglaprogramming.com
 * License: MIT License
 */
 
/* 
 * Structure
 * Array 
 */

#include <stdio.h>

typedef struct date{
    int day;
    int month;
    int year;
} Date;

void printDate(Date _date);

int main(){
    const int DATES_LENGTH = 2;

    Date dates[DATES_LENGTH];
    dates[0].day = 02;
    dates[0].month = 07;
    dates[0].year = 2018;

    dates[1].day = 03;
    dates[1].month = 07;
    dates[1].year = 2018;
    

    for (int i = 0; i < DATES_LENGTH; ++i){
        printDate(dates[i]);
    }

    return 0;
}

void printDate(Date _date){
    printf("Day: %d | Month: %d | Year: %d\n", _date.day, _date.month, _date.year);
}
/*
 * author: Mahmud Ahsan
 * https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * http://banglaprogramming.com
 * License: MIT License
 */
 
/* 
 * Structure
 * Compound Literals 
 */

#include <stdio.h>

typedef struct date{
    int day;
    int month;
    int year;
} Date;

void printDate(Date _date);

int main(){
    Date today;
    Date tomorrow;
    /* error occurs must need type cast for init
        today = {02, 07, 2018};
    */
    today = (Date) {02, 07, 2018};

    // OR by accessing members
    tomorrow = (Date) {.year = 2018, .day = 03, .month = 07};
    

    printDate(today);
    printDate(tomorrow);

    return 0;
}

void printDate(Date _date){
    printf("Day: %d | Month: %d | Year: %d\n", _date.day, _date.month, _date.year);
}
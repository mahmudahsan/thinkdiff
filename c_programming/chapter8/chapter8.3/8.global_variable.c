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
 * Global Variable
 */

#include <stdio.h>

// global variable
int number;

void changeNumber(int newValue);
void printNumber();

int main(){
    number = 100;
    printNumber();

    changeNumber(-500);
    printNumber();

    return 0;
}

void changeNumber(int newValue){
    number = newValue;
}

void printNumber(){
    printf("%d\n", number);
}
/*
 * author: Mahmud Ahsan
 * https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * http://banglaprogramming.com
 * License: MIT License
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
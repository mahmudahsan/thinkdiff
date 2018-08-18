/*
 * author: Mahmud Ahsan
 * https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * http://banglaprogramming.com
 * License: MIT License
 */

/* 
 * Function and Array as parameter
 */

#include <stdio.h>

int sum(int numbers[], int length);

int main(){
    int arr1[] = {1, 2, 3, 4, 5};
    printf("Sum of arr1 values is: %d\n", sum(arr1, 5));

    return 0;
}

int sum(int numbers[], int length){
    int sum = 0;
    for (int i = 0; i < length; ++i){
        sum += numbers[i];
    }
    return sum;
}
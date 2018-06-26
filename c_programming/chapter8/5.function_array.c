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
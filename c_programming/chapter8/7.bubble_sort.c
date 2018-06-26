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
 * Bubble Sort Function Ascending
 * input an integer array sort it and print it
 */

#include <stdio.h>

void bubbleSort(int arr[], int length);
void printArr(int arr[], int length);

int main(){
    int arr[] = {4, 1, 3, 2, 5};
    printArr(arr, 5);

    printf("after sorting");
    bubbleSort(arr, 5);
    printArr(arr, 5);

    return 0;
}

void bubbleSort(int arr[], int length) {
    for (int i = 0; i < length - 1; ++i){
        for (int j = i + 1; j < length; ++j){
            if (arr[i] > arr[j]){
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

void printArr(int arr[], int length){
    printf("\n");
    for (int i = 0; i < length; ++i){
        printf("arr[%d] = %d\n", i, arr[i]);
    }
    printf("\n");
}
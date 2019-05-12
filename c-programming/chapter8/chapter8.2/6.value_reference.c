/*
 * author: Mahmud Ahsan
 * https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * http://banglaprogramming.com
 * License: MIT License
 */
 
/* 
 * Argument by value 
 * Argument by reference 
 */

#include <stdio.h>

void swap(int n1, int n2);
void swapArrayValues(int array[], int pos1, int pos2);
void printArr(int arr[], int length);

int main(){
    // values type passed by value
    int a = 5;
    int b = 10;

    printf("a = %d, b = %d\n", a, b);
    swap(a, b);
    printf("a = %d, b = %d\n", a, b);

    // array passed by reference
    int arr[] = {1, 2, 3, 4, 5};
    printArr(arr, 5);
    swapArrayValues(arr, 0, 4);
    printArr(arr, 5);

    return 0;
}

void swap(int n1, int n2){
    int temp = n1;
    n1 = n2;
    n2 = temp;
}

void swapArrayValues(int array[], int pos1, int pos2){
    int temp = array[pos1];
    array[pos1] = array[pos2];
    array[pos2] = temp;
}

void printArr(int arr[], int length){
    printf("\n");
    for (int i = 0; i < length; ++i){
        printf("arr[%d] = %d\n", i, arr[i]);
    }
    printf("\n");
}
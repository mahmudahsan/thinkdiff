/*
 * author: Mahmud Ahsan
 * https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * http://banglaprogramming.com
 * License: MIT License
 */
 
/* 
 * Multidimensional Array
 * Array of Array
 * Type array[ROW][COL];
 */

#include <stdio.h>

int main(){
    // A 2 dimensional or 2D matrix array
    int graph[4][3] = {
                        {1, 2, 3},
                        {4, 5, 6},
                        {7, 8, 9},
                        {1, 1, 1},
                    };
        
    for (int row = 0; row < 4; ++row){
        for (int col = 0; col < 3; ++col){
            printf("%d ", graph[row][col]);
        }
        printf("\n");
    }

    return 0;
}
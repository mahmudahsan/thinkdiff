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
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
 * Array
 * Array is an ordered collection of values 
 * Syntax:
 * TYPE array_variable_name[max_element];
 * float price[10];
 * int scores[10];
 */

#include <stdio.h>

int main(){
    // creating array
    int scores[10]; // 10 integer elements array

    // Indexing or Subscripting
    // array index start from 0 Zero
    // to access last element number_of_elements - 1
    scores[0] = 10;
    scores[1] = 100;
    scores[2] = 200;

    for (int i = 3; i < 8; ++i){
        scores[i] = 0;
    }

    scores[8] = -(10 / 2);
    scores[9] = 300;

    for (int i = 0; i < 10; ++i){
        printf("Scores[%d] => %d\n", i, scores[i]);
    }
        
    return 0;
}
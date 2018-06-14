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
 * Inner For loop
  *
  ** 
  ***
  ****
  *****
 */

#include <stdio.h>

int main(){
    for (int i = 1; i <= 5; ++i){
        for (int j = 1; j <= i; ++j){
            printf("*");
        }
        printf("\n");
    }
    
    printf("\n\n");
    
    return 0;
}
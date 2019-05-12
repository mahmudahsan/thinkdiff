/*
 * author: Mahmud Ahsan
 * https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * http://banglaprogramming.com
 * License: MIT License
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
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
 * do While loop
 * do {
 *    statement
 * }while(condition)
 */

#include <stdio.h>

int main(){
        int i = 1;
        
        do {
            printf("%d\n", i);
            ++i;
        }while(i <= 10);
        
        return 0;
}
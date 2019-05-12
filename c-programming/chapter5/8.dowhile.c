/*
 * author: Mahmud Ahsan
 * https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * http://banglaprogramming.com
 * License: MIT License
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
/*
 * author: Mahmud Ahsan
 * https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * http://banglaprogramming.com
 * License: MIT License
 */
 
/* 
 * for (initialization; condition; expression){
 *     statements;   
 * } 
 */

#include <stdio.h>

int main(){
    int number;
    printf("Enter a number: ");
    scanf("%d", &number);
    
    int i = 0;
    for ( ;i < number; ){
        printf("%d\n", i);
        ++i;
    }
    
    return 0;
}
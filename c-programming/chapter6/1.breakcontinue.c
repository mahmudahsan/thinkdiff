/*
 * author: Mahmud Ahsan
 * https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * http://banglaprogramming.com
 * License: MIT License
 */
 
/* 
 * break
 * continue
 */

#include <stdio.h>

int main(){
        for (int i = 1; i <= 1000; ++i){
            if (i > 10){
                break;
            }
            printf("%d\n", i);
        }
        
        printf("\nPrinting odd numbers\n");
        for (int i = 1; i <= 10; ++i){
            if (i % 2 == 0){
               continue;
            }
            
            printf("%d\n", i);
        }
        
        return 0;
}
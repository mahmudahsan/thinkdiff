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
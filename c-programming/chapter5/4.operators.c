/*
 * author: Mahmud Ahsan
 * https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * http://banglaprogramming.com
 * License: MIT License
 */
 
/* 
 * == Equal to
 * != Not equal to
 * < Less than
 * > Greater than
 * <= Less than or equal to
 * >= Greater than or equal to
 */

#include <stdio.h>

int main(){
    for (int i = 0; i < 10; ++i){
        if (i == 0){ // be careful about =
            printf("i == 0\n");
        }
        else if (i <= 1 && i != 0){
            printf("i less than or equal to 1 and i is not zero\n");
        }
        else if (i < 5){
            printf("i less than 5\n");
        }
        else if (i >= 6){
            printf("i greater than or equal to 6\n");
        }
    }
    
    return 0;
}
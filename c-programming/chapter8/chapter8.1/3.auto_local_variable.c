/*
 * author: Mahmud Ahsan
 * https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * http://banglaprogramming.com
 * License: MIT License
 */
 
/* 
 * Function 
 * Auto local variable
 * Variable declared inside a function is called automatic local variable. 
 * Each time the function called, variables inside function are automatically created.
 * Values inside function are local in that function
 * auto keyword before variable inside function is optional
 */

#include <stdio.h>

// function prototype
void square (int n);

int main(){
    square(2);
    square(5);
    square(10);
    
    return 0;
}

void square (int n){
    auto int result = n * n; //auto is optional
    printf("%d x %d = %d\n", n, n, result);
}

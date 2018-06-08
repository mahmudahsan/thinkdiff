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
 * Operators: Binary and Unary
 * = Assignment
 * + Plus
 * - Minus
 * * Multiplication
 * / Division
 * % Module
 * - Unary minus
 * ++ Unary plus
 * -- Unary minus
 */

#include <stdio.h>

int main(){
    int a = 100;
    int b = 2;
    int c = 25;
    int d = 4;
    int result;
    
    result = a - b;
    printf ("a - b = %i\n", result);

    result = b * c;
    printf ("b * c = %i\n", result);

    result = a / c;
    printf ("a / c = %i\n", result);

    result = a + b * c;
    printf ("a + b * c = %i\n", result);

    printf ("a * b + c * d = %i\n", a * b + c * d);

    result = (a + b) * c;
    printf ("(a + b) * c = %i\n", result);

    result = (a + b) % c;
    printf ("(a + b) %% c = %i\n", result);

    printf ("\nresult: %i\n", result);
    printf ("result: %i\n\n", -result);

    ++result;
    printf ("++result = %i\n", result);

    result++;
    printf ("result++ = %i\n", result);

    --result;
    printf ("--result = %i\n", result);

    result--;
    printf ("result-- = %i\n", result);

    return 0;
}
/*
 * author: Mahmud Ahsan
 * github: https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * Web: http://banglaprogramming.com
 * youtube: https://www.youtube.com/c/banglaprogramming
 * License: MIT License
 * https://github.com/mahmudahsan/thinkdiff/blob/master/LICENSE 
 */
 
 /* Variable Modifiers
 * short
 * long
 * signed    +/-
 * unsigned
 * value range n=bits: -2^n-1 to (+2^n-1)-1
 */

#include <stdio.h>

int main(){
    // n=32, -2^31 to (+2^31)-1
    // -2147483648 to 2147483647
    int intNum = 2147483647; 

    signed int sIntNum = -2147483648;
    unsigned int uIntNum = 4147483647;
    short int shortIntNum = 32767;
    long int longIntNum = 10147483647;
    long long int llIntNum = 11147483647;

    // shorten
    short _shortInNum;
    long _longIntNum;
    unsigned _uIntNum;

    printf("\n");
    printf("int num %i | size: %lu bytes\n", 
        intNum, sizeof(intNum));
    printf("signed int num %i | size: %lu bytes\n", 
        sIntNum, sizeof(sIntNum));
    printf("unsigned int num %u | size: %lu bytes\n", 
        uIntNum, sizeof(uIntNum));
    printf("short int num %hi | size: %lu bytes\n", 
        shortIntNum, sizeof(shortIntNum));
    printf("long int num %li | size: %lu bytes\n", 
        longIntNum, sizeof(longIntNum));
    printf("long long int num %lli | size: %lu bytes\n", 
        llIntNum, sizeof(llIntNum));

    // Long constant by L or l
    // Float constant by F or f
    long longNum = 404L;
    float floatNum = 40.40F;

    printf("\nLong Number: %li\n", longNum);
    printf("\nFloat Number: %f\n", floatNum);

    return 0;
}
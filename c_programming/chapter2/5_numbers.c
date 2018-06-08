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
 * Numbers
 * Base 10 or Decimal
 * Base 2 or Binary
 * Base 16 or Hexadecimal
 * Base 8 or Octal
 */

#include <stdio.h>

int main(){
    int number = 500;
    int binaryNumber = 101; // 5 (base 10)
    int hexaNumber = 0x1F4; // 500 (base 10)
    int octNumber = 0764; // 500 (base 10)

    printf("Number: %d | %#o | %#x \n", 
        number, number, number);
    printf("binary number: %d \n", binaryNumber);
    printf("hexa number: %d | %#o | %#x  \n", 
        hexaNumber, hexaNumber, hexaNumber);
    printf("octal number: %d | %#o | %#x  \n", 
        octNumber, octNumber, octNumber);

    return 0;

}
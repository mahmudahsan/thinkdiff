/*
 * author: Mahmud Ahsan
 * https://github.com/mahmudahsan
 * blog: http://thinkdiff.net
 * http://banglaprogramming.com
 * License: MIT License
 */
 
/* 
 * Challenge 2
 */

 #include <stdio.h>

 int main(){
     int integer = 45;
     float floating = 3030.33;
     double doubleNum = 4.335;
     char character = 'C';

     printf("Integer: %i and Size: %lu bytes\n", 
        integer, sizeof(integer));
     printf("Float: %f and Size: %lu bytes\n", 
        floating, sizeof(floating));
     printf("Double: %f and Size: %lu bytes\n", 
        doubleNum, sizeof(doubleNum));
     printf("Character: %c and Size: %lu bytes\n", 
        character, sizeof(character));
     return 0;
 }
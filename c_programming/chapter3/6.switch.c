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
 * switch (expression) {
 *    case value1:
        statement;
        break;
      default:
        statement;
 * }
 */

#include <stdio.h>

int main(){
    float num1, num2;
    char operator;
    
    printf("Please enter first number operator second number: ");
    scanf("%f %c %f", &num1, &operator, &num2);
    
    float result;
    switch(operator){
        case '+':
            result = num1 + num2;
            printf("Result is: %.2f\n", result);
            break;
        case '-':
            result = num1 - num2;
            printf("Result is: %.2f\n", result);
            break;
        case '*':
            result = num1 * num2;
            printf("Result is: %.2f\n", result);
            break;
        case '/':
            result = num1 / num2;
            if (num2 == 0){
                printf("Can not divide by Zero\n");
            }
            else {
                printf("Result is: %.2f\n", result);
            }
            break;
        default:
            printf("Unknown Operator\n");
            break;
            
    }
    
        
    return 0;
}
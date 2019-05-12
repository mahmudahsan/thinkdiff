/**
 * JavaScript fundamentals includes comments, variable and operator
 * JavaScript is a duck type language.
 * @author Mahmud Ahsan 
 * {@link https://github.com/mahmudahsan/javascript}
 */

 // Single line comment

/**
 * Multiline
 * comment
 */

/**
 * Variable and Data Type
 * 1. Number
 * 2. String
 */

var number1 = 200; // number: integer
let number2 = 300.50; // number: floating-point
const name = "Aladin"; // string
const boolean = true; // true | false
const nothing = null; // absent of object
const undef = undefined; // absent of value

// const means constant. It can not be modifed once defined

console.log(number1, typeof number1);
console.log(number2, typeof number2);
console.log(name, typeof name);
console.log(boolean, typeof boolean);
console.log(nothing, typeof nothing);
console.log(undef, typeof undef);

console.log();
// var exist in function scope
{
  var str = "Hello World";
  console.log(str);
}
console.log(str); // Okay no error

console.log();
// let and const is in block scope
{
  let localStr1 = "Life is Cool";
  const localStr2 = "Nothing is impossible";

  console.log(localStr1);
  console.log(localStr2);
}

//console.log(localStr1); // ReferenceError: localStr1 is not defined
//console.log(localStr2); // ReferenceError: localStr2 is not defined


console.log();
/**
 * null vs undefined
 * you can use any to describe absent of value
 */

const absent1 = null;
const absent2 = undefined;
console.log(absent1 == absent2); // true
console.log(absent1 === absent2); // value and identity check false

console.log();
/**
 * Spcial Numbers
 */
const sp1 = Infinity;
const sp2 = -Infinity;
const sp3 = NaN; // Not a number
console.log(sp1, typeof sp1);
console.log(sp2, typeof sp2);
console.log(sp3, typeof sp3);
console.log((0/0)); // output: Nan

console.log();
/**
 * String
 * Single Quote, Double Quote and Backtick 
 */
const strType1 = "Life is good";
const strType2 = 'Let\'s do it';
const strType3 = `Sum of 2+2=${2+2}`; // template literal

// Template literal ${} inside value computed and converted to string

console.log(strType1);
console.log(strType2);
console.log(strType3);

/**
 * Expression
 * In computer programming expression part of code that generates value
 */
console.log(2+2); // 2+2 is expression

console.log();
/**
 * Operators
 */

// Unary Operator
let uVal = 10;
console.log(-uVal); 

++uVal; // --uVal => pre-increment, pre-decrement
console.log(uVal); // 11

uVal++; // uVal-- => post-increment, post-decrement
console.log(uVal); // 12

// Difference between ++uVal and uVal++
uVal = 100;
console.log(++uVal);
console.log(uVal);
console.log(uVal++);
console.log(uVal);

console.log();
// Binary Operator
let bNum1 = 20;
let bNum2 = 40;
let resultBN = bNum1 + bNum2; // bNum1 - bNum2
console.log(`${bNum1}+${bNum2}=${bNum1 + bNum2}`);

resultBN = resultBN + 10;
console.log(resultBN);
resultBN += 1; // ++resultBN or resultBN++
console.log(resultBN);

console.log();
resultBN = 100;
console.log(resultBN); 
resultBN = resultBN - 10;
console.log(resultBN); 
resultBN = resultBN * 2;
console.log(resultBN);
resultBN = resultBN / 7;
console.log(resultBN); // 25.714285714285715
console.log(Math.floor(resultBN)); // 25

console.log();
// Remainder operator
let x = 10;
let y = 3;
console.log(x % y);

// Exponential function
let aNum = 2;
console.log("Exponential: " + Math.pow(aNum, 8));
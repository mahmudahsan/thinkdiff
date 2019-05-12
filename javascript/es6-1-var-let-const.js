/**
 * ES6/ES2015
 * var vs let and const
 * @author Mahmud Ahsan 
 * {@link https://github.com/mahmudahsan/javascript}
 */

// var exist in outside of scope
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

  localStr1 = "Malaysia";
  console.log(localStr1);

  // localStr2 = "hi";  // error
}

//console.log(localStr1); // ReferenceError: localStr1 is not defined
//console.log(localStr2); // ReferenceError: localStr2 is not defined

// Object, Array can updated
const numbers = [1, 2, 3];
numbers.push(4);
console.log(numbers);
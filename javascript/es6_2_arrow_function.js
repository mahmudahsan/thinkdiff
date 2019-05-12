/**
 * ES6/ES2015
 * Arrow function
 * An arrow function is shorter than a regular function expression
 * @author Mahmud Ahsan 
 * {@link https://github.com/mahmudahsan/javascript}
 */

const squareRegular = function(n){
  return n * n;
};
console.log(squareRegular(5));

// Arrow function 1
const squareArrow1 = (n) => {
  return n * n;
};
console.log("Arrow1: " + squareArrow1(7));

// Arrow function 2
const squareArrow2 = n => {
  return n * n;
};
console.log("Arrow2: " + squareArrow1(9));

// Arrow function 3
const squareArrow3 = n => n * n;
console.log("Arrow3: " + squareArrow1(11));

// Invalid 
//const addArrow = a, b => a + b; // ERROR

// Valid
const addArrow = (a, b) => a + b; 

// Empty parameter
const helloWorld = () => {
  console.log("Hello World");
}
helloWorld();

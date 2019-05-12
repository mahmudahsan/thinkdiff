/**
 * ES6/ES2015
 * Spread Operator

 * @author Mahmud Ahsan 
 * {@link https://github.com/mahmudahsan/javascript}
 */

// arr1 and arr2 are same this is not the right way
const arr1 = [1, 2, 3, 4];
const arr2 = arr1;
console.log(arr1 === arr2);

arr2.push(5);
console.log(arr1);

// ...arrayName return each element of an array
const arr3 = [...arr1, 6];
console.log(arr3);
console.log(arr1 === arr3);

/**
 * Spread operator for object is proposal feature
 * ...object proposal feature
 * works with babel
 */
const obj1 = {
  name: 'rice',
  price: 20
};

const type = 'groceries';

const obj2 = {...obj1, type}
console.log(obj2);
/**
 * ES6/ES2015
 * Object Initializer

 * @author Mahmud Ahsan 
 * {@link https://github.com/mahmudahsan/javascript}
 */

 /**
  * Shorthand property name in object
  * When object property name and initializing variable name are same we can use shorthand syntax
  */

const name = "Ahsan";

// ES5
var person = {
  name: name
};
console.log(person.name);

// ES6
const personSame = {
  name,
};

console.log(personSame.name);

/**
 * Concise Method name in object
 */

// ES5
var person = {
  name: 'Mahmud',
  getName: function(){
    return this.name;
  }
};

console.log(person.getName());

// ES6
const personAgain = {
  name: 'Mahmud Ahsan',
  getName(){
    return this.name;
  }
};

console.log(personAgain.getName());

/**
 * Computed property name
 */

const key = 'key' + 1;
const obj = {
  [key]: 'data',
};

console.log(obj[key]);

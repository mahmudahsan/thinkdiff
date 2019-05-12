/**
 * ES6/ES2015
 * Destructuring

 * @author Mahmud Ahsan 
 * {@link https://github.com/mahmudahsan/javascript}
 */

/**
 * Destructuring is an easier way to access properties in objects and arrays
 */

const person = {
  name: "Mahmud",
  country: "Bangladesh",
};

// individual variable
// const { name } = person;
// console.log(name);

// be careful to use actual property name
// here if i use nameAgain it will not work
// const { nameAgain, country } = person;
// console.log(nameAgain, " " + country);

// fix
const { name, country } = person;
console.log(name, " " + country);

// in function call common destructuring scenario
const personName = ( {name} ) => {
  console.log(name.toUpperCase());
};

personName(person);

/**
 * destructuring array
 * In this case use [] square brackets instead of {}
 */

const arrNumbers = [1, 2, 3, 4, 5];

const [ one, two, three ] = arrNumbers;
console.log(one, two, three);
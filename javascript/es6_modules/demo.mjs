/**
 * ES6/ES2015
 * Modules import / export

 * @author Mahmud Ahsan 
 * {@link https://github.com/mahmudahsan/javascript}
 */

/**
 * ES6/ES2015 are experimental feature in node.js
 * file extension must be .mjs
 * node --experimental-modules demo.mjs
 */

// named import
import { firstName, lastName } from './person';
import { print } from './person';

console.log("my name: " + firstName, lastName);
print();

// default import
import Person from './person';

const p1 = new Person("Donald", 40);
p1.print();

console.log();
import * as p from './person';
console.log(p.firstName, p.lastName);
p.print();

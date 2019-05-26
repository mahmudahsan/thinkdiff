/**
 * ES6/ES2015
 * Default value in function parameter
 * @author Mahmud Ahsan 
 * {@link https://github.com/mahmudahsan/javascript}
 */

const personDetails = (name, country='Bangladesh') => {
  console.log(name + " " + country);
}

personDetails("mahmud");
personDetails('mark', 'Malaysia');

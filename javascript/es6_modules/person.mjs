const firstName = 'Mahmud';
const lastName = 'Ahsan';

const print = () => {
  console.log(firstName, lastName);
};

// named export
export { firstName, lastName };
export { print };

// default export
class Person {
  constructor(name, age){
    this.name = name;
    this.age = age
  }

  print(){
    console.log(this.name, this.age);
  }
}

export default Person;
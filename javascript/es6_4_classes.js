/**
 * ES6/ES2015
 * Classes
 * JavaScript classes are syntactic sugar over existing prototype based inheritance.
 * @author Mahmud Ahsan 
 * {@link https://github.com/mahmudahsan/javascript}
 */

/**
 * constructor is a special method to initialize class object while initiating.
 */
class Address {
  constructor(city, country){
    this.city = city;
    this.country = country;
  }

  print(){
    console.log(this.city);
    console.log(this.country);
  }
}

// initiating instance of class
const myAddress = new Address('dhaka', 'bangladesh');
myAddress.print();


/**
 * static method
 * can be called with the class name
 */
class Point {
  constructor(x, y){
    this.x = x;
    this.y = y;
  }

  static distance(pointA, pointB){
    const ptX = Math.pow((pointB.x - pointA.x), 2);
    const ptY = Math.pow((pointB.y - pointA.y), 2);
    const dt  = Math.sqrt(ptX + ptY);
    return dt;
  }
}

const pt1 = new Point(5, 2);
const pt2 = new Point(10, 3);
const distanceOfPt = Point.distance(pt1, pt2);
console.log(distanceOfPt);

/**
 * Subclass
 */

class Car {
  constructor(brand, type){
    this.brand = brand;
    this.type = type;
  }

  print(){
    console.log('Brand: ' + this.brand);
    console.log('Type: ' + this.type);
  }
}

// if subclass has constructor it needs to call
// super before using this
class Honda extends Car {
  constructor(brand, type, model){
    super(brand, type);
    this.model = model;
  }

  print(){
    super.print();
    console.log('Model: ' + this.model);
  }
}

const honda = new Honda('honda', 'sedan', 'accord');
honda.print();
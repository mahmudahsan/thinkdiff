mixin CanFly {
  void fly(String name) {
    print('$name flying');
  }
}

mixin CanDrive {
  void drive(String name) {
    print('$name driving');
  }
}

class Car with CanDrive {

}

class Helicopter with CanFly, CanDrive {
  void perform(String name) {
    fly(name);
    drive(name);
  }
}

void main() {
  Car car = Car();
  car.drive('car');

  Helicopter helicopter = Helicopter();
  helicopter.perform('helicopter');
}
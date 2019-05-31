void main() {
  print(isAdult(1));
  print(isAdult());
}

bool isAdult([int age = 18]) => age >= 18;
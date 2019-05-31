void main() {
  print(sum(2, 2));
  print(sum(2));
}

dynamic sum(var num1, [var num2]) => num1 + ( num2 ?? 0 );
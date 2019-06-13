void task1() {
  print('Task 1 Done.');
}

Future <String> task2() async {
  Duration duration = Duration(seconds: 2);
  
  String result;

  await Future.delayed(duration, () {
    print('Task 2 Done.');
    result = ' Task 2 Data';
  });

  return result;
}

void task3(String result) {
  print('Task 3 Done. $result');
}

void main() async {
  task1();
  String result = await task2();
  task3(result);
}
Future delayedPrint(int seconds, String msg) {
  final duration = Duration(seconds: seconds);
  return Future.delayed(duration).then((value) => msg);
}

main() {
  print('Life');
  delayedPrint(2, "Is").then((status) {
    print(status);
  }).catchError((err) => print(err));
  print('Good');
}

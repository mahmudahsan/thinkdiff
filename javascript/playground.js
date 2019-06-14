function task1() {
  console.log('Task 1');
}

function task2() {
  console.log('Task 2');
  return new Promise((resolve, reject) => {
    setTimeout(() => resolve('Task 2'), 2000);
  });
}

function task3(data) {
  console.log(`Task 3 with ${data}`);
}

function main() {
  task1();
  task2().then(data => task3(data));
}

main();
/**
 * ES2017
 * async/Await
 * async/await functions are built onto promise. A function starts with async keyword means, it will must return a promise either implicitly or explicitly.
 * @author Mahmud Ahsan 
 * {@link https://github.com/mahmudahsan/javascript}
 */

 // Example 1
 const sum = async (a, b) => {
   return a + b;
 };
 console.log(sum); // [AsyncFunction: sum]
 console.log(sum(1, 2)); // Promise { 3 }
 const result = sum(100, 200);
 result.then(value => {
  console.log(value);
 });

 // Example 2 
 const pow = async (num, pow) => {
  return new Promise((resolve, reject)=>{
    const r = Math.pow(num, pow);
    resolve(r);
  });
 };

 pow(2, 2).then(val => {console.log(val)});

 /**
  * The keyword await makes JavaScript wait until the promise settled and return the result
  */
 // Example 3
 const getData = async () => {
    const data = new Promise((resolve, reject) => {
      setTimeout(()=>{
        resolve("data received");
      }, 2000);
    });

    console.log('test 1');
    let result = await data;
    console.log('test 2');
    return result;
 };

 getData().then(result => {
   console.log(result);
 });

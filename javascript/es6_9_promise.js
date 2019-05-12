/**
 * ES6/ES2015
 * Promise
 * A promise object represents an eventual completion or failure for an asynchronous operation.
 * @author Mahmud Ahsan 
 * {@link https://github.com/mahmudahsan/javascript}
 */

 const getData = () => {
  return new Promise((resolve, reject) => {
    setTimeout(()=>{
      resolve('data received');
    }, 1000);

    // reject example 
    setTimeout(()=>{
      reject('network disconnected');
    }, 500);
  });
 };

 const dataFromServer = getData();
 
 dataFromServer.then(
    (value)=>{
      console.log(value);
    }, 
    (error)=>{
      console.log(error);
    }
 ); 

 /*
  //catch to redetect reject
   dataFromServer.then(
    (value)=>{
      console.log(value);
    })
    .catch((error)=>{
      console.log(error);
    }  
 );
 */


 /**
  * Promise has 3 states
  * pending | fulfilled | rejected
  */

  /**
   * When a pending promise either fulfilled or rejected and if a corresponding handler is attached by 'then' method, the handler will be called.  
   */
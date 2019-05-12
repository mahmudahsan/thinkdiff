**Problem: Given a sorted array of integers, return the index of the given key. Return -1 if not found.**

**Runtime Complexity: O(logn)** 

**Memory Complexity: O(1)**
 

`Python`
```python
def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = int(( low + high ) / 2) 
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1
    
if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    assert binary_search(arr1, 10) == -1
    assert binary_search(arr1, 5) == 4
    assert binary_search(arr1, 1) == 0
    
```

`JavaScript`
```javascript
var assert = require('assert')

function binary_search(arr, item) {
    let low = 0;
    let high = arr.length - 1;
    
    while (low <= high) {
        let mid = Math.floor((low + high) / 2); 
        
        if (arr[mid] == item) return mid;
        else if (arr[mid] < item) low = mid + 1;
        else high = mid - 1
    }
    
    return -1;
}

// test

const arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9];

assert(binary_search(arr1, 10) === -1);
assert(binary_search(arr1, 5) === 4);
assert(binary_search(arr1, 1) === 0);
```
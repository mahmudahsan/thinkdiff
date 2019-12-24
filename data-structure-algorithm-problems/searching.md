### Contents
1. [Binary Search](#binary-search)

### Binary Search

```
// Time: O(logN), Space: O(1)
```

```js
// JavaScript
const binarySearch = (nums, target) => {
    let low = 0;
    let high = nums.length - 1;
    
    while (low <= high) {
        let mid = parseInt( (low + high) / 2 );
        
        if (target == nums[mid]) {
            return mid;
        } else if (target < nums[mid]) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    
    return -1;
}

console.log(binarySearch([1, 2, 3, 4, 5], 4));
console.log(binarySearch([1, 2, 3, 4, 5], 10));
```

```dart
// Dart
int binarySearch(List<dynamic> nums, dynamic target) {
    int low = 0;
    int high = nums.length - 1;

    while (low <= high) {
        int mid = ((low + high) / 2).toInt();

        if (target == nums[mid]) {
            return mid;
        } else if (target < nums[mid]) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    return -1;
}

main() {
    List<int> arr = [1, 2, 3, 4, 5];
    print(binarySearch(arr, 4));
    print(binarySearch(arr, 10));
}
```
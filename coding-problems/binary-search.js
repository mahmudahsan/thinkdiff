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
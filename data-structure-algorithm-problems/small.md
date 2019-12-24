### Contents
1. [Reverse a String](#reverse-a-string)
2. [Palindrome](#palindrome)
3. [Reverse an Integer](#reverse-an-integer)
4. [Most used Character](#most-used-character)
5. [Two Sum](#two-sum)

### Reverse a String

```javascript
// Time: O(n), Space: O(n)
function reverse(str) {
    let revStrArr = [];
    for (let i = str.length - 1; i >= 0; --i) {
        revStrArr.push(str[i]);
    }
    return revStrArr.join('');
}

// OR
// Using reduce function
// reduce(function(total, currentValue, currentIndex, arr), initialValue)

// Time: O(n), Space: O(n)
function reverse(str) {
    return str.split('').reduce((reversed, char) => char + reversed, '');
}


console.log(reverse('Apple'));
console.log(reverse(""));
console.log(reverse('Life is Good'));
```

Output:
```
elppA

dooG si efiL
```

### Palindrome
> Given a string return true if the string is palindrome and false if not.
> // palindrome('abba') is true
> // palindrome('bcecb') is true

```javascript
// Solution 1
// Time: O(n), Space: O(n)
function isPalindrome(str) {
    let strRev = str.split('').reverse().join('');
    
    if (str === strRev){
        return true;
    }
    return false;
}

// Solution 2
// Time: O(n), Space: O(1)
function isPalindrome(str) {
    let mid = parseInt(str.length / 2)
    
    for (let i = 0; i < mid; ++i) {
        let firstChar = str[i];
        let compareChar = str[str.length-i-1];
        
        if (firstChar !== compareChar){
            return false;
        }
    }
    
    return true;
}

console.log(isPalindrome('abba')); // true
console.log(isPalindrome('bcecb')); // true 
console.log(isPalindrome('abxhkbba')); // false
```

### Reverse an Integer

```javascript
function reverseInt(num) {
    let mNum = parseInt(num.toString()
                            .split('')
                            .reverse()
                            .join(''));
    
    if (num < 0) {
        return -mNum;
    }
    return mNum;
}

console.log(reverseInt(100)); // 1
console.log(reverseInt(12345)); // 54321
console.log(reverseInt(-577490)) // -94775
```

### Most used Character

```javascript
// Time: O(n), Space: O(n)
function maxChar(str) {
    let dict = {};
    
    for (let char of str) {
        dict[char] = dict[char] + 1 || 1
    }
    
    let mChar = '';
    let temp = 0;
    
    for (let key in dict) {
        if (dict[key] > temp) {
            temp = dict[key];
            mChar = key;
        }
    }
    
    return mChar;
}

console.log(maxChar('abcdeeeeeeeefjg')); // e
console.log(maxChar('orange 135244')); // 4
```

### Two Sum
> Given an array of integers, return indices of the two numbers such that they add up to a specific target.
> You may assume that each input would have exactly one solution, and you may not use the same element twice.

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

```js
// Time: O(n), Space: O(1)
var twoSum = function(nums, target) {
  const length = nums.length;
  for (let i = 0; i < length; ++i){
    const remain = target - nums.shift();
    if (nums.includes(remain)) {
      return [i, nums.indexOf(remain) + i + 1];
    }
  }
}
```

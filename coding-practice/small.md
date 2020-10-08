### Contents
1. [Reverse a String](#reverse-a-string)
2. [Palindrome](#palindrome)
3. [Reverse an Integer](#reverse-an-integer)
4. [Most used Character](#most-used-character)
5. [Two Sum](#two-sum)
6. [Convert integer to Binary](#integer-to-binary)

### Reverse a String

#### `javascript`
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
#### `Swift`
```swift
func reverseStr(_ str: String) -> String {
    let arr = Array(str)
    var result = ""
    
    var i = arr.count - 1
    while i >= 0 {
        result += String(arr[i])
        i -= 1
    }
    
    return result
}

assert(reverseStr("love") == "evol")
assert(reverseStr("a") == "a")
assert(reverseStr("loKe") == "eKol")
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

#### `javascript`
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

#### `Swift`
```swift
func palindrome(_ str: String) -> Bool {
    let arrStr = Array(str)
    let mid = arrStr.count / 2
    var i = 0
    
    while i < mid {
        if arrStr[i] != arrStr[arrStr.count - i - 1] {
            return false
        }
        i += 1
    }
    
    return true
}

assert(palindrome("love") == false)
assert(palindrome("a") == true)
assert(palindrome("aba") == true)
assert(palindrome("abba") == true)
assert(palindrome("abcba") == true)
```

### Reverse an Integer

#### `javascript`
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

#### `Swift`
```swift
func revInt(_ n: Int) -> Int {
    var N = abs(n)
    var rev = 0
    
    while N > 0 {
        let lastDigit = N % 10
        N = N / 10
        rev = rev * 10 + lastDigit
    }
    return n < 0 ? -rev : rev
}

assert(revInt(10) == 1)
assert(revInt(102) == 201)
assert(revInt(-123) == -321)
```

### Most used Character

#### `javascript`
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

#### `Swift`
> For same value it prefers the character alphabetically comes before.

```swift
func maxChar(_ str: String) -> String {
    let strArr = Array(str)
    var dict = [String: Int]()
    
    for x in strArr {
        let key = String(x)
        dict[key] = (dict[key] ?? 0 ) + 1
    }
    
    var mostUsedChar = ""
    var mostUsedVal = 0
    
    for (k, v) in dict {
        if v > mostUsedVal {
            mostUsedChar = k
            mostUsedVal = v
        }
        else if v == mostUsedVal && k < mostUsedChar {
            mostUsedChar = k
        }
    }
    return mostUsedChar
}

assert(maxChar("abccccd") == "c")
assert(maxChar("abcde") == "a")
```

### Two Sum
> Given an array of integers, return indices of the two numbers such that they add up to a specific target.
> You may assume that each input would have exactly one solution, and you may not use the same element twice.

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

#### `JavaScript`
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

#### `Swift`
```swift
// Time: O(nLog(n)) | Space O(n)
func twoNumberSum(array: [Int], targetSum: Int) -> [Int] {
    let sortedArray = array.sorted(by: <)
    
    var left = 0
    var right = sortedArray.count - 1
    
    while left < right {
        let sum = sortedArray[left] + sortedArray[right]
        
        if sum == targetSum {
            return [left, right]
        }
        else if sum < targetSum {
            left += 1
        }
        else if sum > targetSum {
            right -= 1
        }
    }
    
    return []
}
```

### Integer To Binary
> Given an integer number returns a binary String

Swift Implementation
```swift
func intToBinary(_ N: Int) -> String {
    return String(N, radix: 2)
}

assert(intToBinary(2) == "10")
```

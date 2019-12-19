### Contents
1. [Reverse a String](#1.-reverse-a-string)

#### 1. Reverse a String

```javascript
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

function reverse(str) {
    return str.split('').reduce((reversed, char) => char + reversed, '');
}


console.log(reverse('Apple'));
console.log(reverse(""));
console.log(reverse('Life is Good'));
```
Time: O(n), Space: O(n)

Output:
```
elppA

dooG si efiL
```


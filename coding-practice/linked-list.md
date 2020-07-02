### What is Linked List
> Linked List data structure is a collection of nodes, where each node points to each other.

**Two types of Linked List**
1. [Singly Linked List](#singly-linked-list)
2. Doubly Linked List

#### Singly Linked List

```js
class Node {
    constructor(item) {
        this.item = item
        this.next = null
    }
}

class SinglyLinkedList {
    constructor() {
        this.head = null
        this.size = 0
    }
    
    isEmpty() {
        return this.size == 0
    }
    
    traverse() {
        let curr = this.head
        while (curr) {
            console.log(curr.item)
            curr = curr.next
        }
    }
    
    add(item) {
        if (this.head == null) {
            this.head = new Node(item)
        }
        else {
            const temp = this.head 
            this.head = new Node(item)
            this.head.next = temp
        }
        this.size += 1
    }
    
    search(item) {
        let curr = this.head 
        while(curr) {
            if (curr.item == item) {
                return true
            }
            else {
                curr = curr.next
            }
        }
        return false
    }
    
    remove(item) {
        if (this.head.item === item) {
            this.head = this.head.next
            this.size -= 1
        }
        else {
            let prev = this.head
            let curr = this.head.next 
            
            while (curr) {
                if (curr.item === item) {
                    prev.next = curr.next
                    this.size -= 1
                    break
                }
                else {
                    prev = curr
                    curr = curr.next
                }
            }
        }
    }
}

```
> Testing

```js
const list = new SinglyLinkedList()
console.log(`Is Empty: ${list.isEmpty()}`)

// Adding items
list.add(1)
list.add(2)
list.add(3)

console.log(`List Size: ${list.size}`)
console.log(`Is Empty: ${list.isEmpty()}`)

// Traversering
list.traverse()

// Searching 
console.log(`Find Item 2: ${list.search(2)}`)
console.log(`Find Item 5: ${list.search(5)}`)

// Remove
list.remove(2)
list.traverse()
console.log(`Size: ${list.size}`)
```

> Output
```
Is Empty: true
List Size: 3
Is Empty: false
3
2
1
Find Item 2: true
Find Item 5: false
3
1
Size: 2

```
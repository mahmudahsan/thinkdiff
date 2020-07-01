### What is Linked List
> Linked List data structure is a collection of nodes, where each node points to each other.

**Two types of Linked List**
1. [Singly Linked List](#singly-linked-list)
2. Doubly Linked List

#### Singly Linked List

```js
class Node {
    constructor(data) {
        this.data = data
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
    
    insert(data) {
        if (this.isEmpty()) {
            this.head = new Node(data)
        }
        else {
            const temp = this.head
            this.head = new Node(data)
            this.head.next = temp
        }
        ++this.size
    }
}

```
> Testing

```js
const singlyLinkedList = new SinglyLinkedList()
console.log(singlyLinkedList.isEmpty())
singlyLinkedList.insert(2)
singlyLinkedList.insert(4)
console.log(singlyLinkedList)
```

> Output
```
true
SinglyLinkedList {
    head: Node { data: 4, next: Node { data: 2, next: null } },
    size: 2
}
```
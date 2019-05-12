/**
 * LinkedinList
 * @author Mahmud Ahsan
 */

class Node {
  constructor(data) {
    this.data = data;
    this.nextElement = null;
  }
}

class LinkedinList {
  constructor(){
    this.head = new Node(-1);
    this.length = 0;
  }

  isEmpty() {
    return this.length === 0;
  }

  // insert at head O(1)
  insertAtHead(dt) {
    let tempNode = new Node(dt);
    tempNode.nextElement = this.head.nextElement;
    this.head.nextElement = tempNode;
    this.length += 1;
    return this;
  }

  // insert at tail O(n)
  insertAtTail(dt){
    const node = new Node(dt);
    let temp = this.head;
    while (temp.nextElement != null){
      temp = temp.nextElement;
    }
    temp.nextElement = node;
    this.length += 1;
    return this;
  }

  // Search O(n)
  search(data){
    let tip = this.head.nextElement;

    while (tip.nextElement != null){
      if (tip.data == data){
        return true;
      }
      tip = tip.nextElement;
    }
    return false;
  }

  // Delete at head O(1)
  deleteAtHead(){
    const head = this.head;
    let tip = head.nextElement;

    if (tip.nextElement != null){
      head.nextElement = tip.nextElement;
    }
    return this;
  }

  // delete by data O(n)
  delete(data){
    let tip = this.head.nextElement;
    let tipPrev = this.head;

    while (tip != null){
      if (tip.data === data){
        tipPrev.nextElement = tip.nextElement;
        return true;
      }
      tipPrev = tip;
      tip = tip.nextElement;
    }
    return false;
  }

  // print O(n)
  printList() {
    if (this.isEmpty()){
      console.log("Empty list");
      return false;
    }
    let temp = this.head.nextElement;
    while (temp != null){
      process.stdout.write(String(temp.data));
      process.stdout.write(" -> ");
      temp = temp.nextElement;
    }
    process.stdout.write('null');
    return true;
  }
}

let list = new LinkedinList();
console.log(list.isEmpty());

for (let i = 0; i < 10; i++) {
  list = list.insertAtHead(i);
}
list.printList();

console.log();

for (let i = 0; i < 5; i++) {
  list = list.insertAtTail(i);
}
list.printList();

console.log();

// searching
console.log(list.search(9));
console.log(list.search(100));

console.log();

// delete at head
list.deleteAtHead();
list.deleteAtHead();
list.printList();

console.log();

// delete by data
list.delete(1);
list.printList();
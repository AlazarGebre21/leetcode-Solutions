class Node:   
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.val,end='->')
            temp = temp.next
        print()

    def length(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count
        
    def get(self, index: int) -> int:
        pos = index
        temp = self.head
        if pos >= self.length():
            return -1
        while pos < self.length() and pos:
            temp = temp.next
            pos -= 1
        if temp:
            # print(f'get at {index} {temp.val}')
            return temp.val
        else:
            # print(f'get at {index} {-1}')
            return -1
        # self.display()            

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        # print(f'add at head {val}')
        # self.display()


    def addAtTail(self, val: int) -> None:
        if self.head == None:
            self.addAtHead(val)
        else:
            node = Node(val)
            temp = self.head
            while temp.next:
                temp = temp.next
            node.next = temp.next
            temp.next = node
            # print(f'add at tail {val}')
            # self.display()

    def addAtIndex(self, index: int, val: int) -> None:
        pos = index
        temp = self.head
        node = Node(val)
        if pos == 0:
            self.addAtHead(val)
        elif self.length() == pos:
            self.addAtTail(val)
        elif self.length()  < pos:
            return
        else:
            pos -= 1
            while temp.next and pos:
                temp = temp.next
                pos -= 1
            node.next = temp.next
            temp.next = node
            # print(f'add at index {index}{val}')
            # self.display()

    def deleteAtIndex(self, index: int) -> None:
        temp = self.head
        pos = index 
        if self.head == None:
            return
        elif pos == 0:
            self.head = self.head.next
        elif pos < self.length():
            pos -= 1
            while pos:
                temp = temp.next
                pos -= 1
            if temp.next:
                deleteNode = temp.next
                temp.next = deleteNode.next
                deleteNode.next = None
        else:
            return
        # print(f'delete at index {index}')
        # self.display()
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
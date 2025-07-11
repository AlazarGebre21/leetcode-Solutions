class MyCircularDeque:

    def __init__(self, k: int):
        self.que = [0] * k
        self.front = 0
        self.size = 0
    
    def _index(self, idx: int) -> int:
        return (idx % len(self.que))


    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = self._index(self.front - 1)
        self.que[self.front] = value
        self.size += 1
        return True
        

        
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        rear = self._index(self.front + self.size)
        self.que[rear] = value
        self.size += 1
        return True
        
        
        
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = self._index(self.front + 1)
        self.size -= 1
        return True

        
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.que[self.front]
        
        
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        rear = self._index(self.front + self.size - 1)
        return self.que[rear]
        
        
    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.size == len(self.que):
            return True
        return False
        

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(self.k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
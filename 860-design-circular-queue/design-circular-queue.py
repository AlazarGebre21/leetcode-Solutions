class MyCircularQueue:

    def __init__(self, k: int):
        self.cir_que = [0] * k
        self.front = 0
        self.size = 0
    
    def _index(self,idx:int) -> int:
        return (idx % len(self.cir_que))
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        rear = self._index(self.front + self.size)
        self.size += 1
        self.cir_que[rear] = value
        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = self._index(self.front + 1)
        self.size -= 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.cir_que[self.front]


    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        rear = self._index(self.front + self.size - 1)
        return self.cir_que[rear]


    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False


    def isFull(self) -> bool:
        if self.size == len(self.cir_que):
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj1 = MyCircularQueue(k)
# param_1 = obj1.enQueue(value)
# param_2 = obj1.deQueue()
# param_3 = obj1.Front()
# param_4 = obj1.Rear()
# param_5 = obj1.isEmpty()
# param_6 = obj1.isFull()


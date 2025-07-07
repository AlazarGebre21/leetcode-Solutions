class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.my_circular_que = deque([])

    def insertFront(self, value: int) -> bool:
        if len(self.my_circular_que) < self.k:
            self.my_circular_que.appendleft(value)
            return True
        else:
            return False
        

    def insertLast(self, value: int) -> bool:
        if len(self.my_circular_que) < self.k:
            self.my_circular_que.append(value)
            return True
        else:
            return False
        

    def deleteFront(self) -> bool:
        if len(self.my_circular_que) == 0:
            return False
        else:
            self.my_circular_que.popleft()
            return True
        

    def deleteLast(self) -> bool:
        if len(self.my_circular_que) == 0:
            return False
        else:
            self.my_circular_que.pop()
            return True
        

    def getFront(self) -> int:
        if len(self.my_circular_que) == 0:
            return -1
        else:
            return self.my_circular_que[0]

    def getRear(self) -> int:
        if len(self.my_circular_que) == 0:
            return -1
        else:
            return self.my_circular_que[-1]
        
    def isEmpty(self) -> bool:
        if len(self.my_circular_que) == 0:
            return True
        else:
            return False
            
    def isFull(self) -> bool:
        if len(self.my_circular_que) == self.k:
            return True
        else:
            return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
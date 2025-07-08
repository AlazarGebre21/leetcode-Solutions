class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.cir_que = deque([])

    def insertFront(self, value: int) -> bool:
        if len(self.cir_que) < self.k:
            self.cir_que.appendleft(value)
            return True
        else:
            return False
    def insertLast(self, value: int) -> bool:
        if len(self.cir_que) < self.k:
            self.cir_que.append(value)
            return True
        else:
            return False
        
    def deleteFront(self) -> bool:
        if len(self.cir_que) != 0:
            self.cir_que.popleft()
            return True
        else:
            return False
        

    def deleteLast(self) -> bool:
        if len(self.cir_que) != 0:
            self.cir_que.pop()
            return True
        else:
            return False
        
    def getFront(self) -> int:
        if len(self.cir_que) != 0:
            return self.cir_que[0]
            
        else:
            return -1
        
    def getRear(self) -> int:
        if len(self.cir_que) != 0:
            return self.cir_que[-1]
            
        else:
            return -1
        
    def isEmpty(self) -> bool:
        if len(self.cir_que) != 0:
            return False
            
        else:
            return True

    def isFull(self) -> bool:
        if len(self.cir_que) != self.k:
            return False
        else:
            return True
        


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
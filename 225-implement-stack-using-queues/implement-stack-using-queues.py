class MyStack:

    def __init__(self):
        self.que_stack = deque([])

    def push(self, x: int) -> None:
        self.que_stack.append(x)
        

    def pop(self) -> int:
        size = len(self.que_stack)

        for i in range(size-1):
            self.que_stack.append(self.que_stack.popleft())

        return self.que_stack.popleft()
        

    def top(self) -> int:
        size = len(self.que_stack)

        for i in range(size):
            tempo = self.que_stack.popleft()
            self.que_stack.append(tempo)

        return tempo
            
        

    def empty(self) -> bool:

        if len(self.que_stack) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
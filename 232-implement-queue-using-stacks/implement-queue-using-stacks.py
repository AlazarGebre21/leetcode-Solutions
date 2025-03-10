class MyQueue:

    def __init__(self):
        self.stack = []
        self.stack_head = 0

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        self.stack_head = self.stack_head + 1
        return self.stack[self.stack_head - 1]

    def peek(self) -> int:
        if self.stack_head < len(self.stack):
            return self.stack[self.stack_head]
        
    def empty(self) -> bool:
        if len(self.stack) - self.stack_head <= 0:
            return True
        else:
            return False

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
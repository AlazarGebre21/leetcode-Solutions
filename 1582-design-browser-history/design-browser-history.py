class BrowserHistory:

    def __init__(self, homepage: str):
        self.back_history = [homepage]
        self.forward_history = []

    def visit(self, url: str) -> None:
        self.forward_history.clear()
        self.back_history.append(url)

    def back(self, steps: int) -> str:
        x = steps
        while x > 0 and len(self.back_history) > 1:
            self.forward_history.append(self.back_history.pop())
            x-=1
        return self.back_history[-1]


    def forward(self, steps: int) -> str:
        x = steps
        while x > 0 and self.forward_history:
            self.back_history.append(self.forward_history.pop())
            x-=1
        
        return self.back_history[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

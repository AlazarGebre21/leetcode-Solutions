class RecentCounter:

    def __init__(self):
        self.counter = deque()
    def ping(self, t: int) -> int:
        self.counter.append(t)
        start = t - 3000
        end = t
        if start <= self.counter[0] <= end:
           return len(self.counter)
        else:
            while not start <= self.counter[0] <= end:
                self.counter.popleft()
            return len(self.counter)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

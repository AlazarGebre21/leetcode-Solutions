class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        if len(nums) < k:
            nums.append(float('-inf'))
        
        self.nums = nlargest(self.k, nums)
        heapify(self.nums)

    def add(self, val: int) -> int:

        if self.nums[0] > val:
            return self.nums[0]
        else:
            heappushpop(self.nums, val)
            return self.nums[0]
        



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
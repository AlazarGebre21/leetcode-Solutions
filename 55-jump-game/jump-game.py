class Solution:
    def canJump(self, nums: List[int]) -> bool:
        largest = 0
        
        for i in range(len(nums)):
            largest = max(largest, nums[i] + i)
            if largest == i and i != len(nums) - 1:
                return False
        return True
            
            
                
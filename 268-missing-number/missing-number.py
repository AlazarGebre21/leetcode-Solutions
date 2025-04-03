class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums.sort()

        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return n
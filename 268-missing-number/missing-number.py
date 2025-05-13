class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        xor_idx = 0
        xor_val = 0

        for idx, val in enumerate(nums):

            xor_idx = xor_idx ^ (idx + 1)

            xor_val = xor_val ^ val

        
        return xor_idx ^ xor_val
        

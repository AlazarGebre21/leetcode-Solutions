class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        i = 0
        j = 1
        ans = []

        while i < len(nums) and j < len(nums):
            ans.append(nums[j])
            ans.append(nums[i])
            j += 2
            i += 2
        
        return ans
            
        

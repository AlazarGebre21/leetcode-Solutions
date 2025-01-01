class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (2 * len(nums))
        i = 0
        j = 0
        while j < len(ans):
            if i != len(nums):
                ans[j] = nums[i]
                i+=1
                j+=1
            else:
                i = 0
        return ans
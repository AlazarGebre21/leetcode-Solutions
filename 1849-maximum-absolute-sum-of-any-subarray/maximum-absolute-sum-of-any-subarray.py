class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        cur_sum = max_sum = nums[0]

        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(cur_sum, max_sum)
        
        
        cur_sum = min_sum = nums[0]

        for num in nums[1:]:
            cur_sum = min(num, cur_sum + num)
            min_sum = min(cur_sum, min_sum)
        
        return max(abs(max_sum), abs(min_sum))
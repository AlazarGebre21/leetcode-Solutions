class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = 0
        max_sum = float('-inf')

        for i in range(len(nums)):
            if i == 0:
                prefix_sum = nums[0]
            else:
                if prefix_sum < 0:
                    prefix_sum = nums[i]
                else:
                    prefix_sum += nums[i]
            max_sum = max(max_sum,prefix_sum)
        return max_sum
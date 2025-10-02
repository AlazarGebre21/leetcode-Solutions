import sys
sys.setrecursionlimit(10**8)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1]*len(nums) for _ in range(len(nums))]

        def dp(prev, cur):
            if cur >= n:
                return 0 
            
            if memo[prev][cur] == -1:
                memo[prev][cur] = dp(prev, cur + 1)
                if nums[cur] > nums[prev] or prev == -1:
                    memo[prev][cur] = max(1 + dp(cur, cur+1), memo[prev][cur])
            return memo[prev][cur]
        
        return dp(-1, 0)
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums) - 1

        def robing(n):
            if n == 0:
                return nums[0]
            if n == 1:
                return max(nums[0], nums[1])
            
            if n in memo:
                return memo[n]

            
            memo[n] = max(robing(n-1), robing(n-2) + nums[n])
            return memo[n]

        
        return robing(n)
        
       
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        rem = sum(nums) // 2
        n = len(nums)
        memo = [[-1]*(rem+1) for _ in range(n)]

        def dp(i, rem):

            if rem == 0:
                return 1

            if i >= n:
                return 0
            
            if memo[i][rem] == -1:

                memo[i][rem] = dp(i+1, rem)

                if nums[i] <= rem:

                    memo[i][rem] = max(memo[i][rem], dp(i+1, rem-nums[i]))
                
            
            return memo[i][rem]

        
        res = dp(0,rem)

        if res ==  0:
            return False
        else:
            return True
            
            
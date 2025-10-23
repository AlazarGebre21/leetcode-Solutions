class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def helper(arr):

            memo = {}

            def dp(i):

                if i >= len(arr):
                    return 0
                
                if i == len(arr) - 1:
                    return arr[i]
                

                if i not in memo:

                    
                    memo[i] = max(dp(i+1), dp(i+2) + arr[i])
                    
                
                return memo[i]

            return dp(0)
            

        
        ans = max(helper(nums[1:]), helper(nums[0:len(nums)-1]))

        return ans
                



        



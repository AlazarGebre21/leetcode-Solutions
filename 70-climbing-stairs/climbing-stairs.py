class Solution:

    def __init__(self):
        self.dp = {}
        
    def climbStairs(self, n: int) -> int:
       
        if n == 1 or n == 2:
            return n
        elif n in self.dp:
            return self.dp[n]
        
        self.dp[n] = self.climbStairs(n-1)+ self.climbStairs(n-2)

        return self.dp[n]

        

        
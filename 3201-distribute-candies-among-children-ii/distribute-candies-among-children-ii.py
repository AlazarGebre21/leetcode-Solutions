class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:

        total = math.comb(n+2,2)
        illegal_1 = illegal_2 = illegal_3 = 0
        if n >= limit+1:
            illegal_1 = 3*math.comb(n-limit+1,2)
        if n >= 2*limit:
            illegal_2 = 3*math.comb(n-2*limit,2)
        if n >= (3*limit)-1:    
            illegal_3 = math.comb(n-((3*limit)-1),2)
        ans = total - illegal_1 + illegal_2 - illegal_3 
        return ans if ans >= 0 else 0
           


            

class Solution:
    def countBits(self, n: int) -> List[int]:


        current_base = 2
        future_base = current_base * 2

        ans = [0] * (n+1)
        ans[0] = 0

        for i in range(1, n+1):

            if i >= 3:

                if future_base == i:
                    ans[i] = 1
                    current_base = future_base
                    future_base = current_base * 2
                    
                else:
                    rem = i - current_base
                    ans[i] = ans[current_base] + ans[rem]
            
            else:
                ans[i] = 1
        
        return ans





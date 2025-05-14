class Solution:
    def countBits(self, n: int) -> List[int]:


        ans = [0] * (n+1)
        

        for i in range(n+1):

            pre = i // 2
            if i % 2 == 0:
                ans[i] = ans[pre]
            else:
                ans[i] = ans[pre] + 1
        
        return ans


            



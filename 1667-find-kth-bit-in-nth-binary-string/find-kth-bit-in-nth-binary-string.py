class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def rec(n):
            if n == 1:
                return ['0']
            
            temp = rec(n-1)
            temp2 = ['0' if temp[i] == '1' else '1' for i in range(len(temp))]

            res = temp + ['1'] + temp2[::-1]

            return res


        result = rec(n) 
               

        for i in range(len(result)):
            if i == k  - 1:
                return result[i]
        
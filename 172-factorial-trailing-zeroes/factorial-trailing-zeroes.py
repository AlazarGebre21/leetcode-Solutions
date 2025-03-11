class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        result = 0
        def countZeros(n):
            if n == 0:
                return 0
            k = n // 5

            return k + countZeros(k)
        

        return countZeros(n)
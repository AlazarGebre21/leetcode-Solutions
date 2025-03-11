class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        def countZeros(n,count):
            count += 1
            if n//pow(5,count) == 0:
                return 0

            k = n//pow(5,count)

            return k + countZeros(n,count)
        

        return countZeros(n,count)

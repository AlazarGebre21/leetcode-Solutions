class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n > 1 and n % 4 != 0:
            return False
        def pow_4(n):
            if n < 1:
                return False
            elif n == 1:
                return True
                
            return pow_4(n/4)


        return pow_4(n)




 
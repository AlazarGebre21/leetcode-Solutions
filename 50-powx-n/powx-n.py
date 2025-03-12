class Solution:
    def myPow(self, x: float, n: int) -> float:
        copy = n
        n = abs(n)

        def pow(n):
            if n == 1:
                return x
            elif n == 0:
                return 1

            half = pow(n // 2)

            result = half * half

            if n % 2 != 0:
                result *= x

            return result
        
        result = pow(n)
        return result if copy >= 0  else 1/result


        


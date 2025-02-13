class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(floor(math.sqrt(c)))
        while i <= j:
            squareNumbers = i ** 2 + j ** 2
            if squareNumbers == c:
                return True
            elif squareNumbers > c:
                j -= 1
            elif squareNumbers < c:
                i += 1
        return False
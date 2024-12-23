class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [0] * n
        i = 0

        for i in range(n):
            if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
                answer[i] = "FizzBuzz"
            elif (i + 1) % 3 == 0:
                answer[i] = "Fizz"
            elif (i + 1) % 5 == 0:
                answer[i] = "Buzz"
            else:
                res = i + 1
                answer[i] = str(res)
        return answer

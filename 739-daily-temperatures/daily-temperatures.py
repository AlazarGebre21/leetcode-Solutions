class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        # create a mono decreasing stack which holds both the index and the value

        for i in range(len(temperatures)):

                while stack and temperatures[i] > temperatures[stack[-1]]:
                    pop_i = stack.pop()
                    answer[pop_i] = i - pop_i

                stack.append(i)

                
        return answer
                


                     
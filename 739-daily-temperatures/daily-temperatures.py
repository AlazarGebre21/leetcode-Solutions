class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        # create a mono decreasing stack which holds both the index and the value

        for curr_index, curr_value in enumerate(temperatures):

                while stack and curr_value > stack[-1][1]:
                    poped_index, poped_value = stack.pop()
                    answer[poped_index] = curr_index - poped_index
                      
                stack.append((curr_index,curr_value))

                
        return answer
                


                     
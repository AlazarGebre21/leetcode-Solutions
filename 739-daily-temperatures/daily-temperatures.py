class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            temperatures[i] = (temperatures[i],i)


        for i in range(len(temperatures)):

            if stack:
                if stack[-1][0] >= temperatures[i][0]:
                    stack.append(temperatures[i])
                    
                else:
                    while stack and stack[-1][0] < temperatures[i][0]:
                        ans[stack[-1][1]] = temperatures[i][1] - stack[-1][1]
                        stack.pop()
                    else:
                        stack.append(temperatures[i])
                        continue
            else:
                stack.append(temperatures[i])

        

        return ans
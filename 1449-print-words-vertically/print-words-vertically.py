class Solution:
    def printVertically(self, s: str) -> List[str]:
        #spliting the string using spaces into a list of words
        result = s.split()
        answer = []
        #calculating the maximum length from the list of words
        max_length = len(max(result, key=len))

        #making all the string equal by adding space at the end of each string
        for i in range(len(result)):
            if len(result[i]) < max_length:
                diff = max_length - len(result[i])
                result[i] += (' ' * diff)
            else:
                continue
        
        #The logic for collecting the vertical word from the list of words in the result array and appending the final result to answers array.
        for j in range(max_length):
            temp = ''
            for i in range(len(result)):
                temp += result[i][j]
            answer.append(temp)
        
        #iterating through the answers array and deleting triming spaces
        for i in range(len(answer)):
            answer[i] = answer[i].rstrip()
        
        return answer
        

                
        
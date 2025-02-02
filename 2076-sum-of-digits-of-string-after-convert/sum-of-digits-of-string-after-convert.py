class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # changing the string into the integer string
        intString = ''
        for i in range(len(s)):
            intString += str(ord(s[i]) - ord('a') + 1)
        
        # Adding the digits in 'intString' k times
        result = 0
        while k > 0:
            result = 0
            for i in range(len(intString)):
                result += int(intString[i])
            intString = str(result)
            k -= 1
        return result
        

            

            
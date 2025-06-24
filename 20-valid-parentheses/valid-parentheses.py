class Solution:
    def isValid(self, s: str) -> bool:

        my_dict = {'(':')', '[':']','{':'}'}
        stack = []
        for bracket in s:
            if bracket in my_dict.keys():
                stack.append(bracket)      
            else:
                if len(stack) != 0:
                    if my_dict[stack[-1]] == bracket:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False

    

        
        
                
class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {'(':')','{':'}','[':']'}
        stack = []
        
        for parenthesis in s:
            if parenthesis in my_dict.keys():
                stack.append(parenthesis)
            elif parenthesis in my_dict.values():
                if stack:
                    closing = parenthesis
                    opening = stack.pop()
                    if my_dict[opening] != closing:
                        return False
                else:
                    return False
        
        return stack == []
                        
                        
                        
                        

        
        
                
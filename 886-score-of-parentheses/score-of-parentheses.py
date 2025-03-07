class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            
            else:
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    if stack[-1] == '(':
                        stack.pop()
                        stack.append(1)
                    else:
                        count = 0

                        while stack[-1] != '(':
                            count += stack[-1]
                            stack.pop()

                        stack.pop()
                        stack.append(2*count)
        return sum(stack)
                
                




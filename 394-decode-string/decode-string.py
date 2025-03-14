class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if  s[i] == '[' or s[i].isalnum():

                stack.append(s[i])
            
            else:
                alpha = ''
                num = ''

                while stack and stack[-1] != '[':
                    alpha = stack.pop() + alpha
                # pop [      
                stack.pop()

                while stack and stack[-1].isnumeric():
                    num += stack.pop()

                num = int(num[::-1])

                stack.append(num*alpha)
        return ''.join(stack)



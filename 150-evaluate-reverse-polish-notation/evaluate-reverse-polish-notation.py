class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        result = 0
        for tok in tokens:
            if tok == '+' or tok == '-' or tok == '*' or tok == '/':
                second_num = stack.pop()
                first_num = stack.pop()
                if tok == '+':
                    result = first_num + second_num
                    stack.append(result)
                elif tok == '-':
                    result = first_num - second_num
                    stack.append(result)
                elif tok == '*':
                    result = first_num * second_num
                    stack.append(result)
                elif tok == '/':
                    result = first_num / second_num
                    stack.append(int(result))
            else:
                stack.append(int(tok))
        
        return stack[0]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
my_sol = Solution()
print(my_sol.evalRPN(tokens))

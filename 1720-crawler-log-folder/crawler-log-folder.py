class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        # Iterate through the logs and when ever you got ../ pop the top if not empty if it is ./ just continue

        for log in logs:
            if log == '../':
                if stack:
                    stack.pop()
            elif log == './':
                continue
            else:
                stack.append(log)
        
        return len(stack)

                
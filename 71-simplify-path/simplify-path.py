class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        

        for p in path:
            if p == '..':
                if stack:
                    stack.pop()
            elif p == '.':
                continue
            else:
                if p != '':
                    stack.append(p)
        
        return '/' + '/'.join(stack)
            
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        queue = deque()
        queue.append(root)
        graph = defaultdict(list)
        _sum = 0
        arr = []
        
        while queue:
            node = queue.popleft()
            
            if node and node.left:
                left = node.left
                queue.append(left)
                graph[node].append(left)


            if node and node.right:
                right = node.right
                queue.append(right)
                graph[node].append(right)
        
            
            
        def dfs(node):
            nonlocal _sum
            
            arr.append(node.val)
            
            if node not in graph:
                _sum += int(''.join(map(str, arr)))
            else:
                for n in graph[node]:
                    dfs(n)
            arr.pop()            
            
            
        dfs(root)
        return _sum

            
        
        


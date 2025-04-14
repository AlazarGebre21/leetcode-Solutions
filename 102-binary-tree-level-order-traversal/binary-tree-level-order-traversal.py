# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        queue = deque()
        queue.appendleft(root)
        level_order = []

        if not root:
            return level_order

        while queue:
            temp = []
            
            for i in range(len(queue)):
                node = queue.popleft()
                
                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)
                temp.append(node.val)
            
            level_order.append(temp)
        
        return level_order
                

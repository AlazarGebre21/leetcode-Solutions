# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        p = root
        
        if p:
            stack = [p]
        else:
            stack = []

        while stack:

            if p and p.left:
                p = p.left
                if p:
                    stack.append(p)
            
            else:
                p = stack.pop()
                ans.append(p.val)
                if p:
                    p = p.right
                    if p:
                        stack.append(p)
            
        return ans


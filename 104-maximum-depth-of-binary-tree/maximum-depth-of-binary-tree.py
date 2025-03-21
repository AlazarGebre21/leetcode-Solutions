# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        maxim = 0

        def max_depth(root):

            nonlocal depth, maxim

            if not root:

                maxim  = max(maxim,depth)
                return depth

            depth += 1

            max_depth(root.left)

            max_depth(root.right)

            depth -= 1

            return
        

        max_depth(root)

        return maxim
            
            

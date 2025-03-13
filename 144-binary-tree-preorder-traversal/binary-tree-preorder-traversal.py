# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []
        def rec(root):

            if not root:
                return 
        
            result.append(root.val)
            rec(root.left)
            rec(root.right)

        rec(root)
        return result


        
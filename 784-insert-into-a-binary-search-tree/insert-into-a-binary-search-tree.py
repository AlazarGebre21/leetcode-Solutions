# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

      # REcursive approach

        current = root
        

        def insert(current, val):
        
            if not current:
                return TreeNode(val)

            if val > current.val:
                current.right = insert(current.right, val)

            else:
                current.left = insert(current.left, val)

            return current
    
        
        return insert(current,val)
        

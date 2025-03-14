# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def search(root,val):

            if root and root.val == val:
                return root
        
            
            if root and root.val > val:
                if root.left:
                    return search(root.left,val)
                
            elif root and root.val < val:
                if root.right:
                    return search(root.right,val)
            
            else:
                return None
        
        return search(root,val)


        
        
        
        

        
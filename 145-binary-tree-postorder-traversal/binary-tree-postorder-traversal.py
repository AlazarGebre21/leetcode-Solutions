# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        p = root
        stack = []
        visted = set()

        while p or stack:

            if p:

                stack.append(p)
                visted.add(p)
                stack.append(p.right)
                p = p.left
            
            else:
                
                p = stack.pop()

                if p and p in visted:
                    ans.append(p.val)
                    p = None
        return ans
                
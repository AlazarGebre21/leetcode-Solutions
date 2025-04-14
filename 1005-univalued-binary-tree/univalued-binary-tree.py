# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        que = deque()
        que.appendleft(root)
        value = root.val

        while que:

            for i in range(len(que)):

                node = que.popleft()

                if value != node.val:
                    return False

                if node.left:
                    que.appendleft(node.left)
                if node.right:
                    que.appendleft(node.right)
        return True


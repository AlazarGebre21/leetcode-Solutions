# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dq = deque([root])
        level = 0  # Start from level 0 (even), so odd levels will be 1,3,5...

        while dq:
            size = len(dq)
            nodes = list(dq)  # Store current level nodes for reversing
            
            if level % 2 == 1:  # Reverse values only on odd levels
                i, j = 0, len(nodes) - 1
                while i < j:
                    nodes[i].val, nodes[j].val = nodes[j].val, nodes[i].val
                    i += 1
                    j -= 1

            for _ in range(size):  # Process all nodes at this level
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

            level += 1  # Move to the next level
        
        return root

            





        
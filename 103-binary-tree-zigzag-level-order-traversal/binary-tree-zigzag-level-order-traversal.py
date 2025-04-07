# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        dq = deque()
        dq.append(root)
        left_to_right = True


        if not root:
            return []


        while dq: 

            temp_dq = deque()

            for i in range(len(dq)):

                node = dq.popleft()
                if left_to_right:
                    temp_dq.append(node.val)
                else:
                    temp_dq.appendleft(node.val)
        

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            
            
            left_to_right = not left_to_right
            result.append(list(temp_dq))
        
        return result



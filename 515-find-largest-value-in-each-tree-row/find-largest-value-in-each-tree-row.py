# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        my_dict = defaultdict(list)

        depth = 0

        def largest_row(root):

            nonlocal depth

            if not root:
                return

            
            depth += 1

            my_dict[depth].append(root.val)

            largest_row(root.left)

            largest_row(root.right)

            depth -= 1

        largest_row(root)

        ans = []

        for values in my_dict.values():
            ans.append(max(values))
        
        return ans
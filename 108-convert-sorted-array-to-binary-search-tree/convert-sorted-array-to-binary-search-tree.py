# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def sorted_array_to_bst(l,r):

            if l > r:
                return None
            
            mid = (l + r) // 2

            left_child = sorted_array_to_bst(l,mid-1)
            right_child = sorted_array_to_bst(mid+1,r)

            return TreeNode(nums[mid], left=left_child, right=right_child)
        

        return sorted_array_to_bst(0, len(nums)-1) 
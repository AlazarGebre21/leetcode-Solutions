# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        arr1 = []
        arr2 = []

        tree1 = root.left
        tree2 = root.right

        def pre_right_1(tree1):

            if not tree1:
                arr1.append('0')
                return
            
            arr1.append(tree1.val)
            pre_right_1(tree1.left)
            pre_right_1(tree1.right)
        
        

        def pre_right_2(tree2):

            if not tree2:
                arr2.append('0')
                return
            
            arr2.append(tree2.val)
            pre_right_2(tree2.right)
            pre_right_2(tree2.left)
        
        

        pre_right_1(tree1)
        pre_right_2(tree2)

        print(arr1)
        print(arr2)

        return arr1 == arr2

        
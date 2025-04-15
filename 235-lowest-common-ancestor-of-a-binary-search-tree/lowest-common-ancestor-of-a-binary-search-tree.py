# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        ancestors_of_p = []
        ancestors_of_q = []

        def binary_search(node):
            
            pointer = root
            result = []

            while True:

                if pointer.val == node.val:
                    result.append(pointer)
                    return result
                
                elif node.val > pointer.val:
                    result.append(pointer)
                    pointer = pointer.right
                
                else:
                    result.append(pointer)
                    pointer = pointer.left
        

        ancestors_of_p = binary_search(p)
        ancestors_of_q = binary_search(q)

        def father_child_checker():

            for i in range(len(ancestors_of_p)):
                if q.val  == ancestors_of_p[i]:
                    return q
            
            for i in range(len(ancestors_of_q)):
                if p.val == ancestors_of_q[i]:
                    return p
        i = 0
        j = 0
        LCA = root

        

        father_child_checker()

        while i < len(ancestors_of_p) and j < len(ancestors_of_q):

            if ancestors_of_p[i] == ancestors_of_q[j]:
                LCA = ancestors_of_p[i]
            i += 1
            j += 1
            
        
        return LCA

            





            
        

            
                   

            



        
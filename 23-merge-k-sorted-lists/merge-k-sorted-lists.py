# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy
        heap = []

        j = 0
     
        for i, node in enumerate(lists):

            if node:


                heappush(heap, (node.val, i, node))
                j = i
        

        j += 1
        
        while heap:

            val, i, node = heappop(heap)

            curr.next = node
            curr = node

            if node.next:

                heappush(heap, (node.next.val, j , node.next))
                j += 1
        
        return dummy.next


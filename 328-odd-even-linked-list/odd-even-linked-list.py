# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = head
        prevodd = head
        if head:
            even = head.next
            evenhead = even
        else:
            even = head
            evenhead = even

        while even and odd:
            
            odd.next = even.next
            odd = odd.next

            if odd:
                even.next = odd.next
                even = even.next
                prevodd = odd
        
        if prevodd:
            prevodd.next = evenhead
            
        return head
        
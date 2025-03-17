# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head
        lower_head = ListNode()
        higher_head = ListNode()
        lower = lower_head
        higher = higher_head

        while curr:
            
            if curr.val < x:
                lower.next = curr
                lower = curr
                
            
            else: 
                higher.next = curr
                higher = curr
                
            
            curr = curr.next
        
        higher.next = None
        
        lower.next = higher_head.next

        return lower_head.next
                

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fast = head
        slow = head
        has_cycle = False

        while slow and fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                has_cycle = True
                break
            
        
        if not has_cycle:
            return None
        
        elif has_cycle:
            slow = head

            while slow and fast:
                if slow == fast:
                    return slow
                
                slow = slow.next
                fast = fast.next
            
        
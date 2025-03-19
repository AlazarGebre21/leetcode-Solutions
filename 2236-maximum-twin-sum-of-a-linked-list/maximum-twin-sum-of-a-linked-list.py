# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        rev = head
        curr = head
        max_twin_sum = 0

        # Dividing the linked list into two one for the original and the other for the twin
        slow = head
        fast = head

        while slow and fast:
            if fast.next:
                fast = fast.next.next
            if fast:
                slow = slow.next
        
        rev = slow.next
        slow.next = None

        # After dividing the linked list into two here is the section to reverse the right hand side and to find the max_twin sum

        dummy = ListNode()
        dummy.next = rev
        prev = dummy

        while rev:
            store = rev.next
            rev.next = prev
            prev = rev
            rev = store
        
        while curr and prev.next:
            max_twin_sum = max((curr.val+prev.val),max_twin_sum)
            curr = curr.next
            prev = prev.next
        
        return max_twin_sum





        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        behind_pointer = dummy
        ahead_pointer = head
        while n > 0:
            ahead_pointer = ahead_pointer.next
            n -= 1
        
        while ahead_pointer:
            behind_pointer = behind_pointer.next
            ahead_pointer = ahead_pointer.next
        
        behind_pointer.next = behind_pointer.next.next

        return dummy.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # since the number is not reversed we need a function to reverse the linked list
        def reverse(head):
            prev = None
            curr = head
            while curr:
                store_dir = curr.next
                curr.next = prev
                prev = curr
                curr = store_dir
            return prev
        
        reverse_l1 = reverse(l1)
        reverse_l2 = reverse(l2)
        result = ListNode()

        temp = result
        rem = 0
        
        while reverse_l1 or reverse_l2:
            
            while reverse_l1 or reverse_l2:

                if reverse_l1 and reverse_l2:
                    sums = reverse_l1.val + reverse_l2.val + rem
                    rem = 0
                elif reverse_l1:
                    sums = reverse_l1.val + rem 
                    rem = 0
                elif reverse_l2:
                    sums = reverse_l2.val + rem
                    rem = 0

                if sums >= 10:
                    temp.val = sums - 10
                    rem = 1
                else:
                    temp.val = sums

                if reverse_l1 and reverse_l2:
                    reverse_l1 = reverse_l1.next
                    reverse_l2 = reverse_l2.next
                elif reverse_l1:
                    reverse_l1 = reverse_l1.next
                else:
                    reverse_l2 = reverse_l2.next
            
                if reverse_l1 or reverse_l2:
                    node = ListNode()
                    temp.next = node
                    temp = temp.next
        
        if rem != 0:
            node = ListNode()
            temp.next = node
            temp = temp.next
            temp.val = rem
            temp.next = None
            temp = temp.next

        return reverse(result)
